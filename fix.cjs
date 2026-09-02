const fs = require('fs');
const path = require('path');
const pagesDir = path.join(process.cwd(), 'src', 'pages');
const files = fs.readdirSync(pagesDir).filter(f => f.endsWith('.tsx'));
const capsule = `<div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>`;

files.forEach(file => {
  const filePath = path.join(pagesDir, file);
  let content = fs.readFileSync(filePath, 'utf8');

  content = content.replace(/<div className="w-\[72px\] h-\[32px\] shrink-0 pointer-events-none"><\/div>/g, capsule);
  content = content.replace(/<div className="w-\[72px\] h-\[32px\] pointer-events-none shrink-0"><\/div>/g, capsule);
  
  content = content.replace(/gap-\[96px\]/g, 'gap-[40px]');
  content = content.replace(/gap-\[64px\]/g, 'gap-[32px]');
  content = content.replace(/gap-\[40px\]/g, 'gap-[24px]');
  content = content.replace(/mb-\[96px\]/g, 'mb-[40px]');
  content = content.replace(/mb-\[64px\]/g, 'mb-[32px]');
  content = content.replace(/mb-\[40px\]/g, 'mb-[24px]');
  content = content.replace(/pb-32/g, 'pb-24');

  if (file === 'Home.tsx') {
    content = content.replace(/h-\[45vh\]/g, 'h-[40vh]');
    content = content.replace(/h-\[65vh\]/g, 'h-[40vh]');
    content = content.replace(/gap-12/g, 'gap-8');
    content = content.replace(/随心逛 \(Explore\)/g, '随心逛');
    content = content.replace(/私人精选 \(Private\)/g, '私人精选');
    content = content.replace(/视觉搜索 \(Visual\)/g, '视觉搜索');
    content = content.replace(/>New</g, '>上新<');
    content = content.replace(/>Exclusive</g, '>独家<');
    content = content.replace(/Italian Full-Grain Leather/g, '意大利全粒面牛皮');
    content = content.replace(/Water-Resistant Canvas/g, '防水帆布');
  }

  if (file === 'PrivateCuration.tsx') {
    content = content.replace(/>Restock</g, '>补货<');
    content = content.replace(/Classic Leather Tote/g, '经典皮革托特包');
    content = content.replace(/Back in stock in your saved color\./g, '您收藏的颜色已补货。');
    content = content.replace(/Tailored Wool Overcoat/g, '定制羊毛大衣');
    content = content.replace(/Autumn\/Winter Collection/g, '秋冬系列');
  }

  if (file === 'DynamicResults.tsx') {
    content = content.replace(/>Match</g, '>高匹配<');
  }

  if (file === 'MemberCenter.tsx') {
    content = content.replace(/>Status</g, '>当前等级<');
    content = content.replace(/>Noir</g, '>黑卡<');
    content = content.replace(/>Next Tier: Elite</g, '>下一等级：精英<');
    content = content.replace(/>Travel</g, '>出行<');
    content = content.replace(/>Experience</g, '>体验<');
  }

  if (file === 'ProductDetail.tsx') {
    content = content.replace(/>ATELIER</g, '>工坊系列<');
    content = content.replace(/>Member</g, '>会员专享<');
  }

  if (file === 'Profile.tsx') {
    content = content.replace(/w-24 h-24/g, 'w-16 h-16');
    content = content.replace(/>Elena R\.</g, '>林女士<');
    content = content.replace(/>Noir Member</g, '>黑卡会员<');
    content = content.replace(/尺码 \(Size\)/g, '尺码');
    content = content.replace(/材质偏好 \(Materials\)/g, '材质偏好');
    content = content.replace(/避免 \(Avoid\)/g, '避免');
    content = content.replace(/Cashmere \(羊绒\)/g, '羊绒');
    content = content.replace(/Silk \(真丝\)/g, '真丝');
    content = content.replace(/Togo Leather/g, 'Togo牛皮');
  }

  if (file === 'Compare.tsx') {
    content = content.replace(/>Dimension</g, '>对比维度<');
    content = content.replace(/>AI Top Pick</g, '>AI 首选<');
    content = content.replace(/>In Stock</g, '>现货<');
    content = content.replace(/>Low Stock \(2\)</g, '>仅剩 2 件<');
    content = content.replace(/>Ships in 3 Days</g, '>3天内发货<');
  }

  fs.writeFileSync(filePath, content);
});
console.log("Done");
