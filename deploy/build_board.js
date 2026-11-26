const { chromium } = require('playwright');
const path = '/Users/ericmaosmac/WorkBuddy/个人网站/素材卡/_看板.html';
const out  = '/Users/ericmaosmac/WorkBuddy/个人网站/素材卡/_看板.pdf';

(async () => {
  const b = await chromium.launch();
  const p = await (await b.newContext()).newPage();
  await p.goto('file://' + encodeURI(path), { waitUntil: 'networkidle' });
  await p.emulateMedia({ media: 'print' });
  await p.waitForTimeout(300);
  const m = await p.evaluate(() => {
    const px2mm = 96 / 25.4;
    const doc = document.documentElement;
    const body = document.body;
    return {
      scrollH: +(Math.max(doc.scrollHeight, body.scrollHeight) / px2mm).toFixed(1),
      scrollW: +(Math.max(doc.scrollWidth, body.scrollWidth) / px2mm).toFixed(1)
    };
  });
  console.log('内容高度', m.scrollH, 'mm  宽度', m.scrollW, 'mm  （A4 可用 297 - 13*2 = 271mm）');
  await p.pdf({ path: out, printBackground: true, preferCSSPageSize: true });
  await b.close();
  console.log('PDF 已生成');
})();
