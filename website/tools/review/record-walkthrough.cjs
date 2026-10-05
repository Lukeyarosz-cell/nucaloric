// Record the real site, including its normal animations, without changing it.
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const base = process.env.REVIEW_BASE_URL || 'http://127.0.0.1:8080';
const output = process.env.REVIEW_OUTPUT || path.resolve(__dirname, '../../../nucaloric-walkthrough');
const pages = [
  ['index', 'Home'], ['explorer', 'Explorer'], ['launchpad', 'Launchpad'],
  ['registry', 'Registry'], ['studio', 'Studio'], ['hosting', 'Hosting'],
  ['dashboard', 'Dashboard'], ['rewards', 'Rewards'], ['coin', 'Coin'],
  ['optimizer', 'Optimizer'], ['ecosystem', 'Ecosystem'],
  ['status', 'Service status'], ['roadmap', 'Implementation roadmap'],
];
(async () => {
  fs.mkdirSync(path.join(output, 'raw'), { recursive: true });
  fs.mkdirSync(path.join(output, 'stills'), { recursive: true });
  const browser = await chromium.launch({ executablePath: chromium.executablePath(), headless: true });
  const results = [];
  try {
    for (const [index, [slug, title]] of pages.entries()) {
      const context = await browser.newContext({
        viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1,
        reducedMotion: 'no-preference',
        recordVideo: { dir: path.join(output, 'raw'), size: { width: 1440, height: 900 } },
      });
      const page = await context.newPage();
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      await page.goto(`${base}/${slug}.html`, { waitUntil: 'load' });
      await page.evaluate(() => document.fonts.ready);
      if (slug === 'status') await page.locator('.service-row').first().waitFor();
      await page.evaluate(({ number, title, count }) => {
        const label = document.createElement('div');
        label.textContent = `${String(number).padStart(2, '0')} / ${count}  ·  ${title}`;
        label.setAttribute('aria-hidden', 'true');
        Object.assign(label.style, {
          position: 'fixed', bottom: '20px', left: '20px', zIndex: '2147483647',
          background: 'rgba(8,8,9,.9)', color: '#f4f1ec', border: '1px solid #e7b5c4',
          borderRadius: '6px', padding: '10px 15px', font: '600 12px/1.3 system-ui',
          letterSpacing: '.06em', pointerEvents: 'none',
        });
        document.body.append(label);
        window.scrollTo({ top: 0, behavior: 'instant' });
      }, { number: index + 1, title, count: pages.length });
      await page.waitForTimeout(2200);
      await page.screenshot({ path: path.join(output, 'stills', `${slug}-top.jpg`), type: 'jpeg', quality: 85 });
      const coverage = await page.evaluate(async () => {
        const startHeight = document.documentElement.scrollHeight;
        const pixelsPerSecond = 500;
        await new Promise(resolve => {
          let previous;
          let position = 0;
          const step = now => {
            if (previous !== undefined) position += Math.min(now - previous, 100) * pixelsPerSecond / 1000;
            previous = now;
            const bottom = document.documentElement.scrollHeight - innerHeight;
            window.scrollTo({ top: Math.min(position, bottom), behavior: 'instant' });
            if (position >= bottom) resolve();
            else requestAnimationFrame(step);
          };
          requestAnimationFrame(step);
        });
        return {
          startHeight, finalHeight: document.documentElement.scrollHeight,
          finalScroll: scrollY, viewportHeight: innerHeight,
          reachedBottom: Math.abs(document.documentElement.scrollHeight - innerHeight - scrollY) <= 2,
        };
      });
      await page.waitForTimeout(1800);
      await page.screenshot({ path: path.join(output, 'stills', `${slug}-bottom.jpg`), type: 'jpeg', quality: 85 });
      assert.ok(coverage.reachedBottom, `${title}: did not reach the footer`);
      assert.equal(errors.length, 0, `${title}: browser errors`);
      const video = page.video();
      const source = await video.path();
      await context.close();
      const filename = `${String(index + 1).padStart(2, '0')}-${slug}.webm`;
      fs.renameSync(source, path.join(output, 'raw', filename));
      results.push({ page: slug, title, file: filename, ...coverage, errors });
      fs.writeFileSync(path.join(output, 'recording-coverage.json'), JSON.stringify(results, null, 2));
      console.log(`RECORDED ${index + 1}/${pages.length}: ${title}, ${coverage.finalHeight}px, footer reached`);
    }
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error.stack); process.exitCode = 1; });
