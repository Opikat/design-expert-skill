// Checks the six recipe skeletons in Chromium: motion allowed, reduced motion, no script.
// Engine: BROWSER=chromium|webkit|firefox; playwright-core from PLAYWRIGHT_CORE or the module path.
const engine = process.env.BROWSER || 'chromium'
const browserType = require(process.env.PLAYWRIGHT_CORE || 'playwright-core')[engine]
const path = require('path')
const url = 'file://' + path.resolve(process.argv[2])
const out = process.argv[3]
const results = []
const check = (ctx, name, ok, detail) => results.push({ ctx, name, ok: !!ok, detail })
const wait = ms => new Promise(r => setTimeout(r, ms))

const PAGE_HELPERS = () => {
  window.__runs = []
  for (const t of ['animationstart', 'transitionrun']) {
    document.addEventListener(t, e => {
      const c = e.target.className
      window.__runs.push([t, typeof c === 'string' ? c : c.baseVal, e.animationName || e.propertyName])
    }, true)
  }
  window.rect = el => el.getBoundingClientRect().toJSON()
  window.center = el => { const r = el.getBoundingClientRect(); return [r.left + r.width / 2, r.top + r.height / 2] }
  window.pathPoint = (path, frac) => {
    const p = path.getPointAtLength(path.getTotalLength() * frac)
    const m = path.getScreenCTM()
    return [m.a * p.x + m.c * p.y + m.e, m.b * p.x + m.d * p.y + m.f]
  }
  window.scaleY = el => { const t = getComputedStyle(el).transform; if (t === 'none') return 1; return new DOMMatrix(t).d }
  window.ty = el => { const t = getComputedStyle(el).transform; if (t === 'none') return 0; return new DOMMatrix(t).f }
}
const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1])

async function scrollTo(page, sel, offset = 0) {
  await page.evaluate(([s, o]) => {
    const el = document.querySelector(s); window.scrollTo(0, el.getBoundingClientRect().top + scrollY + o)
  }, [sel, offset])
  await wait(250)
}

async function motionAllowed(browser) {
  const C = 'motion'
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 }, reducedMotion: 'no-preference' })
  const page = await ctx.newPage()
  const errors = []
  page.on('pageerror', e => errors.push(String(e)))
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()) })
  await page.addInitScript(PAGE_HELPERS)
  await page.goto(url)
  const t5start = await page.evaluate(() => {
    const dot = document.querySelector('#r5 .dot'), a = dot.getAnimations()[0]
    return { state: a.playState, t: a.currentTime, d: Math.hypot(...center(dot).map((v, i) => v - pathPoint(document.querySelector('#r5 .track'), 0)[i])) }
  })
  check(C, '5 dot: paused at the path start until in view', t5start.state === 'paused' && t5start.t === 0 && t5start.d < 1, JSON.stringify(t5start))
  const t5fold = await page.evaluate(() => document.querySelector('#flow-nofold .dot').getAnimations()[0]?.playState)
  check(C, '5 dot without data-inview (above the fold) runs on load', t5fold === 'running', String(t5fold))
  await wait(1600)

  // 1. Text reveal
  const t1 = await page.evaluate(() => {
    const h = document.querySelector('#r1 h2[data-split]'), ctl = document.querySelector('#r1 h2.control')
    const spans = [...h.querySelectorAll('.split-word > span')]
    const hr = h.getBoundingClientRect(), cr = ctl.getBoundingClientRect()
    const tn = ctl.firstChild, words = tn.textContent.split(' ')
    let pos = 0, deltas = []
    words.forEach((w, i) => {
      const r = document.createRange(); r.setStart(tn, pos); r.setEnd(tn, pos + w.length); pos += w.length + 1
      const r2 = document.createRange(); r2.selectNodeContents(spans[i])
      const a = r.getBoundingClientRect(), b = r2.getBoundingClientRect()
      deltas.push([+(b.left - hr.left - (a.left - cr.left)).toFixed(2), +(b.top - hr.top - (a.top - cr.top)).toFixed(2)])
    })
    const visibleInMask = spans.every(s => { const m = s.parentElement.getBoundingClientRect(), r = s.getBoundingClientRect(); return r.top >= m.top - 0.5 && r.bottom <= m.bottom + 0.5 })
    return {
      split: h.classList.contains('is-split'), label: h.getAttribute('aria-label'), words: spans.length,
      ariaHidden: [...h.querySelectorAll('.split-word')].every(w => w.getAttribute('aria-hidden') === 'true'),
      transforms: spans.map(s => getComputedStyle(s).transform), lastDelay: getComputedStyle(spans.at(-1)).transitionDelay,
      lastDone: parseFloat(getComputedStyle(spans.at(-1)).transitionDelay) + parseFloat(getComputedStyle(spans.at(-1)).transitionDuration),
      visibleInMask, deltas, runs: window.__runs.filter(r => r[1] === '' && r[2] === 'transform').length,
      heightSplit: hr.height, heightControl: cr.height,
    }
  })
  check(C, '1 split: aria-label, 6 aria-hidden words', t1.split && t1.label === 'Every invoice finds its way home' && t1.words === 6 && t1.ariaHidden, t1.label)
  check(C, '1 split: words end at rest inside their masks', t1.transforms.every(t => t === 'none') && t1.visibleInMask, t1.transforms.join(' '))
  check(C, '1 split: six transform transitions ran, last delay 250ms', t1.runs === 6 && t1.lastDelay === '0.25s', `runs ${t1.runs}, last delay ${t1.lastDelay}`)
  check(C, '1 split: last word in place within 900 ms of the trigger', t1.lastDone <= 0.9, `${t1.lastDone}s`)
  check(C, '1 split: word positions match the unsplit heading (≤1px)', t1.deltas.every(([x, y]) => Math.abs(x) <= 1 && Math.abs(y) <= 1) && Math.abs(t1.heightSplit - t1.heightControl) <= 1, JSON.stringify(t1.deltas) + ` h ${t1.heightSplit}/${t1.heightControl}`)

  // 2. Flip
  await scrollTo(page, '#r2', -20)
  const before2 = await page.evaluate(() => {
    const [x, y] = center(document.getElementById('card-1'))
    return { hit: document.elementFromPoint(x, y).closest('.face')?.className, backInert: document.querySelector('#card-1 .back').inert }
  })
  for (const id of ['card-1', 'card-2', 'card-3']) await page.click(`button[aria-controls="${id}"]`)
  await wait(700)
  const t2 = await page.evaluate(() => {
    const card = document.getElementById('card-1'), [x, y] = center(card)
    return {
      flipped: card.hasAttribute('data-flipped'), m: getComputedStyle(card).transform,
      frontInert: card.querySelector('.front').inert, backInert: card.querySelector('.back').inert,
      label: document.querySelector('button[aria-controls="card-1"]').textContent,
      hit: document.elementFromPoint(x, y).closest('.face')?.className,
    }
  })
  check(C, '2 flip: front hit-tested before the flip, back inert', before2.hit === 'face front' && before2.backInert, JSON.stringify(before2))
  check(C, '2 flip: rotated 180°, inert swapped, label updated, back is hit', t2.flipped && /matrix3d\(-1/.test(t2.m) && t2.frontInert && !t2.backInert && t2.label === 'Show front' && t2.hit === 'face back', JSON.stringify(t2))
  await page.locator('#r2').screenshot({ path: `${out}/a-flip.png` })

  // 3. Tilt
  await scrollTo(page, '#r3', -20)
  const box = await page.locator('.tilt').boundingBox()
  await page.mouse.move(box.x + 1, box.y + 1)
  await wait(500)
  const t3 = await page.evaluate(() => {
    const el = document.querySelector('.tilt')
    return { rx: el.style.getPropertyValue('--rx'), ry: el.style.getPropertyValue('--ry'), m: getComputedStyle(el.querySelector('.tilt-face')).transform,
      gate: matchMedia('(hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference)').matches }
  })
  await page.mouse.move(5, 5)
  await wait(500)
  const t3b = await page.evaluate(() => document.querySelector('.tilt').style.cssText)
  const rx = parseFloat(t3.rx), ry = parseFloat(t3.ry)
  check(C, '3 tilt: ±8° at the corner, reset on leave', t3.gate && rx > 7.5 && rx <= 8 && ry < -7.5 && ry >= -8 && t3.m.startsWith('matrix3d') && t3b === '', `rx ${t3.rx}, ry ${t3.ry}, after leave "${t3b}"`)

  // 4. Ring and tilt-in
  await scrollTo(page, '#r4', -20)
  const ringGeo = () => page.evaluate(() => {
    const cells = [...document.querySelectorAll('#ring-1 > *')].map(c => c.getBoundingClientRect())
    const ring = document.querySelector('#r4 .carousel').getBoundingClientRect()
    return { cells: cells.map(r => [+r.left.toFixed(1), +r.right.toFixed(1), +r.width.toFixed(1)]), ringCenter: ring.left + ring.width / 2,
      display: getComputedStyle(document.getElementById('ring-1')).display, front: document.elementFromPoint(ring.left + ring.width / 2, ring.top + ring.height / 2)?.textContent }
  })
  const g0 = await ringGeo()
  const [c0, c1, , , , c5] = g0.cells
  check(C, '4 ring: front face at true size, neighbours share its edges (radius formula)',
    g0.display === 'block' && Math.abs(c0[2] - 220) < 1 && Math.abs(c1[0] - c0[1]) < 1 && Math.abs(c5[1] - c0[0]) < 1, JSON.stringify(g0))
  for (let k = 0; k < 2; k++) await page.click('[data-ring-step="1"]')
  await wait(900)
  const g2 = await ringGeo()
  const front2 = g2.cells[2]
  check(C, '4 ring: two Next clicks bring face 3 to the front', Math.abs(front2[2] - 220) < 1 && Math.abs((front2[0] + front2[1]) / 2 - g2.ringCenter) < 1 && g2.front === '3', JSON.stringify({ front2, center: g2.ringCenter, hit: g2.front }))
  const tiltIn = []
  for (const off of [-900, -600, -300, 0]) {
    await scrollTo(page, '.tilt-in', off)
    tiltIn.push(await page.evaluate(() => {
      const el = document.querySelector('.tilt-in'), a = el.getAnimations()[0]
      return [a?.timeline?.constructor.name, getComputedStyle(el).transform.slice(0, 40)]
    }))
  }
  check(C, '4 tilt-in: view timeline, tilts while entering, flat once inside', tiltIn[0][0] === 'ViewTimeline' && tiltIn[0][1] !== tiltIn[1][1] && ['none', 'matrix(1, 0, 0, 1, 0, 0)'].includes(tiltIn[3][1]), JSON.stringify(tiltIn))

  // 5. Path dot
  await scrollTo(page, '#r5', -40)
  await wait(300)
  const t5 = await page.evaluate(() => {
    const svg = document.querySelector('#r5 .flow'), dot = svg.querySelector('.dot'), path = svg.querySelector('.track')
    const a = dot.getAnimations()[0], timing = a.effect.getComputedTiming(), running = a.playState
    a.pause(); const res = {}
    for (const f of [0.25, 0.5, 1]) { a.currentTime = 3500 * f; res[f] = Math.hypot(...center(dot).map((v, i) => v - pathPoint(path, f)[i])) }
    a.play()
    const stops = [...svg.querySelectorAll('stop')].map(s => getComputedStyle(s).stopColor)
    return { running, iterations: timing.iterations, duration: timing.duration, scale: svg.getBoundingClientRect().width / 400, res, stops,
      attrVar: getComputedStyle(document.getElementById('attr-var')).stopColor, inView: svg.classList.contains('is-in') }
  })
  check(C, '5 dot: one finite 3.5 s run, starts on entering view', t5.inView && t5.running === 'running' && t5.iterations === 1 && t5.duration === 3500, JSON.stringify(t5))
  check(C, '5 dot: on the path at 25/50/100% with the SVG scaled ×2 (≤1px)', t5.scale === 2 && Object.values(t5.res).every(d => d < 1), JSON.stringify(t5.res))
  check(C, '5 dot: themed gradient stops come from CSS', t5.stops[1] === 'rgb(63, 182, 255)', t5.stops.join(' | '))
  check(C, '5 probe: var() in a presentation attribute resolves in Chromium (no gotcha to document)', t5.attrVar === 'rgb(63, 182, 255)', `stop-color="var(--glow)" computes to ${t5.attrVar}`)
  await page.evaluate(() => { const a = document.querySelector('#r5 .dot').getAnimations()[0]; a.pause(); a.currentTime = 1750 })
  await page.locator('#r5 .flow').first().screenshot({ path: `${out}/a-dot-50.png` })

  // 6. Rail
  const samples = []
  const offsets = [-900, -700, -500, -300, -100, 100, 300, 500, 700, 900, 1100]
  for (const off of [...offsets, ...offsets.slice(0, -1).reverse()]) {
    await scrollTo(page, '#r6 .steps', off)
    samples.push(await page.evaluate(() => {
      const fill = document.querySelector('.rail-fill'), marker = document.querySelector('.rail-marker'), rail = document.querySelector('.rail')
      const rr = rail.getBoundingClientRect(), dot = getComputedStyle(marker, '::after')
      const markerCenter = marker.getBoundingClientRect().bottom - rr.top
      return { s: +scaleY(fill).toFixed(3), m: +(markerCenter / rr.height).toFixed(3), y: +(rr.top + markerCenter).toFixed(1), vh: innerHeight, tl: fill.getAnimations()[0]?.timeline?.constructor.name }
    }))
  }
  const mids = samples.filter(x => x.s > 0 && x.s < 1)
  check(C, '6 rail: for a tall sequence the fill edge stays on the middle line (≤2px)', mids.length > 3 && mids.every(x => Math.abs(x.y - x.vh / 2) <= 2), mids.map(x => x.y).join(' '))
  const down = samples.slice(0, offsets.length), up = samples.slice(offsets.length)
  const mono = down.every((x, i) => i === 0 || x.s >= down[i - 1].s)
  const unwinds = up.every((x, i) => Math.abs(x.s - down[offsets.length - 2 - i].s) < 0.002)
  const markerMatches = samples.every(x => Math.abs(x.s - x.m) < 0.01)
  check(C, '6 rail: view timeline; fill grows 0→1 with scroll', down[0].tl === 'ViewTimeline' && mono && down[0].s === 0 && down.at(-1).s === 1, down.map(x => x.s).join(' '))
  check(C, '6 rail: unwinds on scroll-up', unwinds, up.map(x => x.s).join(' '))
  check(C, '6 rail: marker dot sits at the fill edge', markerMatches, samples.map(x => `${x.s}/${x.m}`).join(' '))
  await scrollTo(page, '#r6 .steps', 100)
  await page.screenshot({ path: `${out}/a-rail.png` })

  // 6b. The same rail when the sequence ends the page
  const endFill = async extraCss => {
    await page.evaluate(css => {
      document.getElementById('after')?.remove()
      if (css) document.head.insertAdjacentHTML('beforeend', `<style>${css}</style>`)
      window.scrollTo(0, document.documentElement.scrollHeight)
    }, extraCss)
    await wait(300)
    return page.evaluate(() => +scaleY(document.querySelector('.rail-fill')).toFixed(3))
  }
  const atEnd = await endFill('')
  const atEndContain = await endFill('.rail-fill, .rail-marker { animation-range: entry 50% contain 100% !important; }')
  check(C, '6 rail at page end: exit 50% stops part-filled, contain 100% completes', atEnd < 1 && atEndContain === 1, `exit 50%: ${atEnd}, contain 100%: ${atEndContain}`)

  check(C, 'no page errors', errors.length === 0, errors.join(' | '))
  await ctx.close()
}

async function reducedMotion(browser) {
  const C = 'reduced'
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 }, reducedMotion: 'reduce' })
  const page = await ctx.newPage()
  const errors = []
  page.on('pageerror', e => errors.push(String(e)))
  await page.addInitScript(PAGE_HELPERS)
  await page.goto(url)
  await wait(300)
  const t1 = await page.evaluate(() => {
    const h = document.querySelector('#r1 h2[data-split]')
    return { spans: h.querySelectorAll('.split-word').length, split: h.classList.contains('is-split'), vis: getComputedStyle(h).visibility, label: h.getAttribute('aria-label') }
  })
  check(C, '1 split: not split, visible at load', t1.spans === 0 && t1.split && t1.vis === 'visible' && t1.label === null, JSON.stringify(t1))

  await scrollTo(page, '#r2', -20)
  const hitBefore = await page.evaluate(() => { const [x, y] = center(document.getElementById('card-1')); return document.elementFromPoint(x, y).closest('.face')?.className })
  await page.click('button[aria-controls="card-1"]')
  await wait(60)
  const mid = await page.evaluate(() => +getComputedStyle(document.querySelector('#card-1 .back')).opacity)
  await wait(300)
  const t2 = await page.evaluate(() => {
    const card = document.getElementById('card-1'), [x, y] = center(card)
    return { m: getComputedStyle(card).transform, back: getComputedStyle(card.querySelector('.back')).opacity, front: getComputedStyle(card.querySelector('.front')).opacity,
      hit: document.elementFromPoint(x, y).closest('.face')?.className, label: document.querySelector('button[aria-controls="card-1"]').textContent }
  })
  check(C, '2 flip: inert back face lets the front take the hit', hitBefore === 'face front', hitBefore)
  check(C, '2 flip: no 3D, crossfade to the back (mid-fade seen)', t2.m === 'none' && t2.back === '1' && t2.front === '0' && mid > 0 && mid < 1 && t2.hit === 'face back' && t2.label === 'Show front', JSON.stringify({ ...t2, mid }))
  await page.locator('#r2').screenshot({ path: `${out}/b-flip.png` })

  await scrollTo(page, '#r3', -20)
  const box = await page.locator('.tilt').boundingBox()
  await page.mouse.move(box.x + 1, box.y + 1)
  await wait(200)
  const t3 = await page.evaluate(() => ({ css: document.querySelector('.tilt').style.cssText, m: getComputedStyle(document.querySelector('.tilt-face')).transform }))
  check(C, '3 tilt: no properties written, no transform', t3.css === '' && t3.m === 'none', JSON.stringify(t3))

  await scrollTo(page, '#r4', -20)
  const r0 = await page.evaluate(() => { const r = document.getElementById('ring-1'); return { d: getComputedStyle(r).display, m: getComputedStyle(r).transform, sl: r.scrollLeft } })
  for (let k = 0; k < 3; k++) await page.click('[data-ring-step="1"]')
  await wait(200)
  const r1 = await page.evaluate(() => { const r = document.getElementById('ring-1'); return { sl: r.scrollLeft, i: r.dataset.i, v: r.style.getPropertyValue('--i') } })
  check(C, '4 ring: plain row, Next scrolls the row', r0.d === 'flex' && r0.m === 'none' && r1.sl > 0 && r1.v === '', JSON.stringify({ r0, r1 }))

  await scrollTo(page, '#r5', -40)
  const t5 = await page.evaluate(() => {
    const dot = document.querySelector('#r5 .dot')
    return { anims: dot.getAnimations().length, d: Math.hypot(...center(dot).map((v, i) => v - pathPoint(document.querySelector('#r5 .track'), 1)[i])) }
  })
  check(C, '5 dot: no animation, rests at the path end', t5.anims === 0 && t5.d < 1, JSON.stringify(t5))

  await scrollTo(page, '#r6 .steps', 100)
  const t6 = await page.evaluate(() => ({ anims: document.querySelector('.rail-fill').getAnimations().length + document.querySelector('.rail-marker').getAnimations().length, s: scaleY(document.querySelector('.rail-fill')), tilt: document.querySelector('.tilt-in').getAnimations().length }))
  check(C, '6 rail and 4 tilt-in: no scroll animations, rail fully drawn', t6.anims === 0 && t6.s === 1 && t6.tilt === 0, JSON.stringify(t6))
  const moving = await page.evaluate(() => window.__runs.filter(r => r[0] === 'animationstart' || r[2] !== 'opacity'))
  check(C, 'only opacity transitions ran on the whole page', moving.length === 0, JSON.stringify(moving))
  check(C, 'no page errors', errors.length === 0, errors.join(' | '))
  await ctx.close()
}

async function noScript(browser) {
  const C = 'no script'
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 }, javaScriptEnabled: false })
  const page = await ctx.newPage()
  await page.goto(url)
  await wait(200)
  const t1 = await page.evaluate(() => {
    const h = document.querySelector('#r1 h2[data-split]')
    return { vis: getComputedStyle(h).visibility, spans: h.querySelectorAll('.split-word').length }
  }).catch(e => ({ error: String(e) }))
  check(C, '1 split: heading visible, untouched', t1.vis === 'visible' && t1.spans === 0, JSON.stringify(t1))
  const t2 = await page.evaluate(() => {
    const f = document.querySelector('#card-1 .front').getBoundingClientRect(), b = document.querySelector('#card-1 .back').getBoundingClientRect()
    return { btn: getComputedStyle(document.querySelector('.flip')).display, stacked: b.top >= f.bottom - 0.5, backH: b.height }
  }).catch(e => ({ error: String(e) }))
  check(C, '2 flip: button hidden, both faces readable in flow', t2.btn === 'none' && t2.stacked && t2.backH > 0, JSON.stringify(t2))
  const t4 = await page.evaluate(() => ({ d: getComputedStyle(document.getElementById('ring-1')).display, btn: getComputedStyle(document.querySelector('[data-ring-step]')).display }))
    .catch(e => ({ error: String(e) }))
  check(C, '4 ring: scrollable row, buttons hidden', t4.d === 'flex' && t4.btn === 'none', JSON.stringify(t4))
  await page.evaluate(() => { const el = document.querySelector('#r5'); window.scrollTo(0, el.getBoundingClientRect().top + scrollY - 40) }).catch(() => {})
  await wait(3900)
  const t5 = await page.evaluate(() => {
    const dot = document.querySelector('#r5 .dot'), path = document.querySelector('#r5 .track')
    const p = path.getPointAtLength(path.getTotalLength()), m = path.getScreenCTM(), r = dot.getBoundingClientRect()
    return Math.hypot(r.left + r.width / 2 - (m.a * p.x + m.c * p.y + m.e), r.top + r.height / 2 - (m.b * p.x + m.d * p.y + m.f))
  }).catch(e => String(e))
  check(C, '5 dot: plays on load and ends at the path end', typeof t5 === 'number' && t5 < 1, String(t5))
  await page.evaluate(() => { const el = document.querySelector('#r6 .steps'); window.scrollTo(0, el.getBoundingClientRect().top + scrollY + 200) })
  await wait(300)
  const t6 = await page.evaluate(() => { const t = getComputedStyle(document.querySelector('.rail-fill')).transform; return t === 'none' ? 1 : new DOMMatrix(t).d })
  check(C, '6 rail: scroll-driven fill works without script', t6 > 0 && t6 < 1, String(t6))
  await page.screenshot({ path: `${out}/c-noscript-top.png` })
  await ctx.close()
}

async function touchPhone(browser) {
  const C = 'touch phone'
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true })
  const page = await ctx.newPage()
  await page.goto(url)
  await scrollTo(page, '#r3', -20)
  await page.tap('.tilt')
  await wait(300)
  const t3 = await page.evaluate(() => ({
    gate: matchMedia('(hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference)').matches,
    css: document.querySelector('.tilt').style.cssText, m: getComputedStyle(document.querySelector('.tilt-face')).transform }))
  check(C, '3 tilt: gate closed on touch, tap writes nothing', !t3.gate && t3.css === '' && t3.m === 'none', JSON.stringify(t3))
  await ctx.close()
}

;(async () => {
  const browser = await browserType.launch()
  console.log(engine, browser.version())
  await motionAllowed(browser)
  await reducedMotion(browser)
  await noScript(browser)
  await touchPhone(browser)
  await browser.close()
  for (const r of results) console.log(`${r.ok ? 'PASS' : 'FAIL'} [${r.ctx}] ${r.name}${r.ok ? '' : '\n      ' + r.detail}`)
  console.log(`${results.filter(r => r.ok).length}/${results.length} passed`)
  require('fs').writeFileSync(`${out}/results.json`, JSON.stringify(results, null, 2))
})()
