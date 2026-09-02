import os

home_content = """import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';
import AIFab from '../components/AIFab';

export default function Home() {
  const navigate = useNavigate();
  const [scrolled, setScrolled] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const products = [
    { 
      type: 'bag', 
      brand: 'THE ROW', 
      name: 'Margaux 15 皮革手提包', 
      price: '¥38,500', 
      img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw', 
      origin: '海外发货 (意大利)', 
      skus: { colors: ['黑色', '棕色', '大象灰'], sizes: ['15', '17'] },
      desc: '经典倒梯形托特包，采用细腻光泽的全粒面小牛皮制成。顶部搭扣开合，侧边束带设计。宽敞的内部空间足够收纳您的日常所需。'
    },
    { 
      type: 'shoe', 
      brand: 'LORO PIANA', 
      name: 'Summer Walk 麂皮乐福鞋', 
      price: '¥8,200', 
      img: 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&q=80&w=400', 
      origin: '中国大陆发货 (上海)', 
      skus: { colors: ['珍珠灰', '海军蓝', '沙色'], sizes: ['39', '40', '41', '42', '43'] },
      desc: '标志性无衬里乐福鞋，采用经过防水抗污处理的翻毛皮制成。浅色橡胶鞋底，穿着轻盈舒适。'
    },
    { 
      type: 'apparel', 
      brand: 'JIL SANDER', 
      name: '极简无领羊毛大衣', 
      price: '¥22,800', 
      img: 'https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&q=80&w=400', 
      origin: '海外发货 (德国)', 
      skus: { colors: ['黑色', '米白'], sizes: ['S', 'M', 'L', 'XL'] },
      desc: '挺括的混纺羊毛面料，极简无领设计，暗门襟纽扣，展现纯粹的建筑感剪裁。'
    },
    { 
      type: 'belt', 
      brand: 'BOTTEGA VENETA', 
      name: 'Intrecciato 编织皮革腰带', 
      price: '¥4,600', 
      img: 'https://images.unsplash.com/photo-1626497764746-6dc36546b388?auto=format&fit=crop&q=80&w=400', 
      origin: '中国大陆发货 (上海)', 
      skus: { colors: ['黑色', '深棕', '酒红'], sizes: ['75', '80', '85', '90', '95'] },
      desc: '采用品牌标志性 Intrecciato 编织工艺制成的窄版皮革腰带，配以几何形针扣。'
    }
  ];

  return (
    <div className="relative min-h-screen pb-24 overflow-x-hidden bg-[#F7F7F5] text-[#111111] font-sans">
      <header className={`fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 transition-colors duration-300 ${scrolled ? 'bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]' : 'bg-transparent'}`}>
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button onClick={() => setIsMenuOpen(true)} aria-label="Menu" className={`relative z-10 hover:opacity-80 transition-transform active:scale-95 duration-200 p-2 -ml-2 ${scrolled ? 'text-[#111111]' : 'text-white'}`}>
            <span className="material-symbols-outlined text-[24px]">menu</span>
          </button>
          <h1 className={`font-serif text-[20px] tracking-widest absolute left-1/2 -translate-x-1/2 pointer-events-none font-bold ${scrolled ? 'text-[#111111]' : 'text-white'}`}>UNIBUY</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button aria-label="Shopping Bag" className={`hover:opacity-80 transition-transform active:scale-95 duration-200 p-2 ${scrolled ? 'text-[#111111]' : 'text-white'}`}>
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
          </div>
        </div>
      </header>

      {/* Slide-out Menu Drawer */}
      {isMenuOpen && (
        <div className="fixed inset-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full h-full z-[60]">
          <div className="absolute inset-0 bg-black/40 backdrop-blur-sm transition-opacity" onClick={() => setIsMenuOpen(false)}></div>
          <div className="absolute top-0 left-0 bottom-0 w-[280px] bg-[#F7F7F5] z-[70] shadow-2xl flex flex-col animate-in slide-in-from-left duration-300">
            <div className="h-14 flex items-center px-4 border-b border-[#E4E3DE]">
              <button onClick={() => setIsMenuOpen(false)} className="p-2 -ml-2 text-[#111111] hover:opacity-80 transition-opacity">
                <span className="material-symbols-outlined">close</span>
              </button>
              <span className="font-serif text-[16px] tracking-widest ml-2">UNIBUY</span>
            </div>
            <div className="flex-1 overflow-y-auto px-6 py-8 flex flex-col gap-10">
              <div>
                <h3 className="text-[11px] text-[#666663] font-mono tracking-widest uppercase mb-4">按分类探索</h3>
                <ul className="flex flex-col gap-5 text-[15px] font-medium text-[#111111]">
                  <li className="cursor-pointer hover:opacity-70 flex items-center justify-between" onClick={() => { setIsMenuOpen(false); navigate('/explore'); }}>包袋 Bags <span className="material-symbols-outlined text-[16px] text-[#666663]">chevron_right</span></li>
                  <li className="cursor-pointer hover:opacity-70 flex items-center justify-between" onClick={() => { setIsMenuOpen(false); navigate('/explore'); }}>鞋履 Shoes <span className="material-symbols-outlined text-[16px] text-[#666663]">chevron_right</span></li>
                  <li className="cursor-pointer hover:opacity-70 flex items-center justify-between" onClick={() => { setIsMenuOpen(false); navigate('/explore'); }}>成衣 Ready-to-Wear <span className="material-symbols-outlined text-[16px] text-[#666663]">chevron_right</span></li>
                  <li className="cursor-pointer hover:opacity-70 flex items-center justify-between" onClick={() => { setIsMenuOpen(false); navigate('/explore'); }}>配饰 Accessories <span className="material-symbols-outlined text-[16px] text-[#666663]">chevron_right</span></li>
                </ul>
              </div>
              <div>
                <h3 className="text-[11px] text-[#666663] font-mono tracking-widest uppercase mb-4">品牌目录</h3>
                <ul className="flex flex-col gap-5 text-[14px] text-[#111111]">
                  <li className="cursor-pointer hover:opacity-70">The Row</li>
                  <li className="cursor-pointer hover:opacity-70">Loro Piana</li>
                  <li className="cursor-pointer hover:opacity-70">Bottega Veneta</li>
                  <li className="cursor-pointer hover:opacity-70">Jil Sander</li>
                  <li className="cursor-pointer hover:opacity-70 text-[#666663] mt-2 underline underline-offset-2">查看全部 A-Z</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      )}

      <main className="w-full flex flex-col">
        {/* Cinematic Hero (75vh) */}
        <section className="relative w-full h-[75vh]">
          <img 
            src="https://lh3.googleusercontent.com/aida-public/AB6AXuArjtrVE2lG4P8GVPHflyWb0Mo5SVTyYRhEKICWp9dXBZfgpnNrEjMm6dtbb5AIQEJulXtvOM2xsrCwwNtXTUGD-ijZT4Ysg_qC8E06uX1B8BvShZ3crQWafJlSTskDHLbYcvpzUhub0jJs9GzUV15SSZE3qvn2mQV6vrwfgxBhaFpM6nYybFKKT4dA7wbrIK7HlkPDWs23ehSoCcEl9zupcOvb1U6484cHAiBp62KwkzvTEDpq6g1U" 
            alt="Hero" 
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-black/20"></div>
          <div className="absolute bottom-[20%] left-6 right-6 text-white flex flex-col items-start">
            <span className="text-[11px] uppercase tracking-widest mb-3 opacity-90">Autumn / Winter 2026</span>
            <h2 className="font-serif text-[30px] leading-[36px] mb-6 max-w-[280px]">重塑都会行囊<br/>秋季旅行指南</h2>
            <button className="px-6 py-3 bg-white text-[#111111] font-medium text-[14px] rounded-sm hover:bg-white/90 transition-colors">
              探索系列
            </button>
          </div>
        </section>

        {/* Editorial Topics */}
        <section className="px-5 py-8 bg-[#FFFFFF] border-b border-[#E4E3DE]">
          <div className="flex gap-3 overflow-x-auto hide-scrollbar pb-2">
            {[
              { label: '新季成衣', img: 'https://images.unsplash.com/photo-1539109136881-3be0616acf4b?auto=format&fit=crop&q=80&w=300' },
              { label: '极简手袋', img: 'https://images.unsplash.com/photo-1591561954557-26941169b49e?auto=format&fit=crop&q=80&w=300' },
              { label: '私享珠宝', img: 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&q=80&w=300' }
            ].map((topic, i) => (
              <div key={i} className="flex-none w-32 group cursor-pointer" onClick={() => navigate('/explore')}>
                <div className="aspect-[4/5] overflow-hidden rounded-sm mb-2">
                  <img src={topic.img} alt={topic.label} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                </div>
                <p className="text-[12px] font-medium text-[#111111] tracking-widest">{topic.label}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Curated Editorial Product Grid */}
        <section className="px-5 py-10 bg-[#F7F7F5]">
          <div className="flex justify-between items-end mb-6">
            <div>
              <h3 className="font-serif text-[24px] text-[#111111]">为你推荐</h3>
            </div>
          </div>
          
          <div className="grid grid-cols-2 gap-3">
            {products.map((prod, i) => (
              <article key={i} className="flex flex-col group cursor-pointer bg-[#FFFFFF] pb-3 shadow-[0_2px_8px_rgba(0,0,0,0.02)] rounded-sm overflow-hidden border border-[#E4E3DE]" onClick={() => navigate('/product', { state: prod })}>
                <div className="w-full aspect-square bg-[#EFEFEB] overflow-hidden relative mb-3">
                  <img src={prod.img} alt={prod.name} className="w-full h-full object-cover mix-blend-multiply" />
                </div>
                <div className="px-2 flex flex-col">
                  <h4 className="font-bold text-[12px] text-[#111111] mb-0.5 line-clamp-1 uppercase tracking-wide">{prod.brand}</h4>
                  <p className="text-[11px] text-[#666663] mb-1.5 truncate">{prod.name}</p>
                  <p className="font-medium text-[13px] text-[#111111] font-mono">{prod.price}</p>
                </div>
              </article>
            ))}
          </div>
        </section>
      </main>

      <AIFab />
      <BottomNav />
    </div>
  );
}
"""

with open('src/pages/Home.tsx', 'w') as f:
    f.write(home_content)

product_detail_content = """import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

export default function ProductDetail() {
  const navigate = useNavigate();
  const location = useLocation();
  const [isFavorite, setIsFavorite] = useState(false);
  
  // Accept product from state, or fallback to default Bag
  const product = location.state || { 
    type: 'bag', 
    brand: 'THE ROW', 
    name: 'Margaux 15 皮革手提包', 
    price: '¥38,500', 
    img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw', 
    origin: '海外发货 (意大利)', 
    skus: { colors: ['黑色', '棕色', '大象灰'], sizes: ['15', '17'] },
    desc: '经典倒梯形托特包，采用细腻光泽的全粒面小牛皮制成。顶部搭扣开合，侧边束带设计。宽敞的内部空间足够收纳您的日常所需。'
  };

  const [selectedColor, setSelectedColor] = useState(product.skus.colors[0]);
  const [selectedSize, setSelectedSize] = useState(product.skus.sizes[0]);
  const isOverseas = product.origin.includes('海外');

  return (
    <div className="bg-[#FFFFFF] text-[#111111] font-sans antialiased min-h-screen pb-[100px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button onClick={() => navigate(-1)} className="relative z-10 text-[#111111] hover:opacity-80 transition-opacity p-2 -ml-2">
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-[#111111] hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">share</span>
            </button>
            <button className="text-[#111111] hover:opacity-80 transition-opacity p-2 -mr-2" onClick={() => setIsFavorite(!isFavorite)}>
              <span className={`material-symbols-outlined text-[22px] ${isFavorite ? 'fill text-[#E56A1D]' : ''}`}>favorite</span>
            </button>
          </div>
        </div>
      </header>

      <main className="pt-14 flex flex-col w-full">
        {/* Product Image Gallery */}
        <section className="w-full aspect-[4/5] bg-[#EFEFEB] relative overflow-hidden">
          <img className="w-full h-full object-cover" src={product.img} alt={product.name} />
          <div className="absolute bottom-4 right-4 bg-[#FFFFFF]/90 backdrop-blur px-2 py-1 text-[11px] font-mono rounded-sm shadow-sm">
            1 / 5
          </div>
        </section>

        {/* Product Meta */}
        <section className="px-5 py-6 flex flex-col">
          <h1 className="font-bold text-[18px] text-[#111111] uppercase tracking-wide mb-1">{product.brand}</h1>
          <p className="text-[14px] text-[#666663] mb-4">{product.name}</p>
          <p className="font-mono text-[22px] font-medium text-[#111111]">{product.price}</p>
          
          {/* Shipping Origin Module */}
          <div className="flex items-center gap-2 mt-5 py-3 border-y border-[#E4E3DE]">
            <span className="material-symbols-outlined text-[18px] text-[#111111]">
              {isOverseas ? 'flight_takeoff' : 'local_shipping'}
            </span>
            <span className="text-[13px] font-medium text-[#111111]">{product.origin}</span>
            {isOverseas && (
              <span className="text-[11px] text-[#666663] ml-auto bg-[#F7F7F5] px-2 py-1 rounded-sm border border-[#E4E3DE]">预计 7-14 工作日</span>
            )}
          </div>
        </section>

        {/* SKU Selector: Colors */}
        <section className="px-5 pb-6 border-b border-[#E4E3DE]">
          <div className="flex justify-between items-end mb-3">
            <span className="text-[13px] font-medium text-[#111111]">颜色: <span className="text-[#666663] font-normal">{selectedColor}</span></span>
          </div>
          <div className="flex flex-wrap gap-2.5">
            {product.skus.colors.map((c, i) => (
              <button 
                key={i} 
                onClick={() => setSelectedColor(c)}
                className={`px-4 py-2.5 text-[12px] rounded-sm border transition-colors ${selectedColor === c ? 'border-[#111111] bg-[#111111] text-[#FFFFFF]' : 'border-[#E4E3DE] bg-[#FFFFFF] text-[#111111] hover:border-[#111111]'}`}
              >
                {c}
              </button>
            ))}
          </div>
        </section>

        {/* SKU Selector: Sizes */}
        <section className="px-5 py-6 border-b border-[#E4E3DE]">
          <div className="flex justify-between items-end mb-3">
            <span className="text-[13px] font-medium text-[#111111]">尺码</span>
            <button className="text-[11px] text-[#666663] underline underline-offset-2">尺码指南</button>
          </div>
          <div className="flex flex-wrap gap-2">
            {product.skus.sizes.map((s, i) => (
              <button 
                key={i} 
                onClick={() => setSelectedSize(s)}
                className={`min-w-[56px] h-[40px] flex items-center justify-center text-[13px] font-mono rounded-sm border transition-colors ${selectedSize === s ? 'border-[#111111] bg-[#111111] text-[#FFFFFF]' : 'border-[#E4E3DE] bg-[#FFFFFF] text-[#111111] hover:border-[#111111]'}`}
              >
                {s}
              </button>
            ))}
          </div>
        </section>

        {/* Details & Accordions */}
        <section className="px-5 py-6">
          <h3 className="font-medium text-[14px] text-[#111111] mb-3">商品详情</h3>
          <p className="text-[13px] text-[#666663] leading-relaxed mb-6">
            {product.desc}
          </p>

          <div className="flex flex-col border-t border-[#E4E3DE]">
            <details className="group cursor-pointer">
              <summary className="flex justify-between items-center py-4 text-[14px] font-medium text-[#111111] list-none outline-none">
                材质与保养
                <span className="material-symbols-outlined text-[#666663] group-open:rotate-180 transition-transform">expand_more</span>
              </summary>
              <div className="pb-4 text-[13px] text-[#666663] leading-relaxed">
                主体采用 100% 顶级小牛皮。建议由专业皮具护理机构进行清洁与保养，避免长时间接触水或阳光直射。
              </div>
            </details>
            <details className="group cursor-pointer border-t border-[#E4E3DE]">
              <summary className="flex justify-between items-center py-4 text-[14px] font-medium text-[#111111] list-none outline-none">
                配送与退货
                <span className="material-symbols-outlined text-[#666663] group-open:rotate-180 transition-transform">expand_more</span>
              </summary>
              <div className="pb-4 text-[13px] text-[#666663] leading-relaxed">
                全球免费标准配送。您可在收到商品后 14 天内申请无理由退换货（需保证商品全新且标签完整）。
              </div>
            </details>
          </div>
        </section>

        {/* Personal Advisor */}
        <section className="px-5 py-8 bg-[#F7F7F5] mt-4">
           <div className="flex items-center gap-4">
             <div className="w-12 h-12 rounded-full overflow-hidden bg-[#E4E3DE] shrink-0 border border-[#E4E3DE]">
               <img className="w-full h-full object-cover" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=150" alt="Advisor" />
             </div>
             <div className="flex-1">
               <h4 className="text-[14px] font-medium text-[#111111]">需要搭配建议？</h4>
               <p className="text-[11px] text-[#666663] mt-0.5">您的私人顾问 Sarah 随时为您解答。</p>
             </div>
             <button className="w-10 h-10 border border-[#111111] rounded-sm flex items-center justify-center text-[#111111] hover:bg-[#111111] hover:text-[#FFFFFF] transition-colors">
               <span className="material-symbols-outlined text-[18px]">chat_bubble</span>
             </button>
           </div>
        </section>
      </main>

      {/* Fixed Bottom Action Bar */}
      <div className="fixed bottom-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF] border-t border-[#E4E3DE] px-4 py-3 flex items-center gap-3 pb-safe shadow-[0_-4px_16px_rgba(0,0,0,0.04)]">
        <button className="flex-1 h-[48px] border border-[#111111] text-[#111111] font-medium text-[14px] rounded-sm flex items-center justify-center hover:bg-[#F7F7F5] transition-colors">
          加入购物袋
        </button>
        <button className="flex-1 h-[48px] bg-[#111111] text-[#FFFFFF] font-medium text-[14px] rounded-sm flex items-center justify-center hover:opacity-90 transition-opacity">
          立即购买
        </button>
      </div>
    </div>
  );
}
"""

with open('src/pages/ProductDetail.tsx', 'w') as f:
    f.write(product_detail_content)
