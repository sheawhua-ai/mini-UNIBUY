import os

explore_content = """import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';
import AIFab from '../components/AIFab';

export default function Explore() {
  const navigate = useNavigate();
  const [scrolled, setScrolled] = useState(false);
  const [activeTab, setActiveTab] = useState('ALL');
  const [isFilterOpen, setIsFilterOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 10);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Shared mock products structure, identical to Home
  const products = [
    { 
      type: 'bag', 
      brand: 'THE ROW', 
      name: 'Margaux 15 皮革手提包', 
      price: '¥35,500 起', 
      img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw', 
      skus: { colors: ['黑色', '棕色', '大象灰'], sizes: ['15', '17'] },
      fulfillments: [
        { id: 'ovs', label: '海外发货 (意大利)', price: '¥35,500', eta: '预计 7-14 工作日', icon: 'flight_takeoff' },
        { id: 'dom', label: '中国大陆发货 (上海)', price: '¥38,500', eta: '预计 1-3 工作日', icon: 'local_shipping' }
      ],
      desc: '经典倒梯形托特包，采用细腻光泽的全粒面小牛皮制成。顶部搭扣开合，侧边束带设计。宽敞的内部空间足够收纳您的日常所需。'
    },
    { 
      type: 'shoe', 
      brand: 'LORO PIANA', 
      name: 'Summer Walk 麂皮乐福鞋', 
      price: '¥8,200', 
      img: 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&q=80&w=400', 
      skus: { colors: ['珍珠灰', '海军蓝', '沙色'], sizes: ['39', '40', '41', '42', '43'] },
      fulfillments: [
        { id: 'dom', label: '中国大陆发货 (上海)', price: '¥8,200', eta: '预计 1-3 工作日', icon: 'local_shipping' }
      ],
      desc: '标志性无衬里乐福鞋，采用经过防水抗污处理的翻毛皮制成。浅色橡胶鞋底，穿着轻盈舒适。'
    },
    { 
      type: 'apparel', 
      brand: 'JIL SANDER', 
      name: '极简无领羊毛大衣', 
      price: '¥22,800', 
      img: 'https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&q=80&w=400', 
      skus: { colors: ['黑色', '米白'], sizes: ['S', 'M', 'L', 'XL'] },
      fulfillments: [
        { id: 'ovs', label: '海外发货 (德国)', price: '¥22,800', eta: '预计 7-14 工作日', icon: 'flight_takeoff' }
      ],
      desc: '挺括的混纺羊毛面料，极简无领设计，暗门襟纽扣，展现纯粹的建筑感剪裁。'
    },
    { 
      type: 'belt', 
      brand: 'BOTTEGA VENETA', 
      name: 'Intrecciato 编织皮革腰带', 
      price: '¥4,600 起', 
      img: 'https://images.unsplash.com/photo-1626497764746-6dc36546b388?auto=format&fit=crop&q=80&w=400', 
      skus: { colors: ['黑色', '深棕', '酒红'], sizes: ['75', '80', '85', '90', '95'] },
      fulfillments: [
        { id: 'ovs', label: '海外发货 (意大利)', price: '¥4,600', eta: '预计 7-14 工作日', icon: 'flight_takeoff' },
        { id: 'dom', label: '中国大陆发货 (上海)', price: '¥4,900', eta: '预计 1-3 工作日', icon: 'local_shipping' }
      ],
      desc: '采用品牌标志性 Intrecciato 编织工艺制成的窄版皮革腰带，配以几何形针扣。'
    },
    { 
      type: 'shoe', 
      brand: 'BOTTEGA VENETA', 
      name: 'Lug 厚底切尔西靴', 
      price: '¥11,800', 
      img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuBxn-3jlW6S_StmsyDGnaHRti2PJV5n1WQNkD6qniDJwK0pqF3B5W8TYEtvsAyMQGgRqG4qISTvbAPpjkcuXD_z2p1yS_1ejIYOgFwkQsUuQWsxqVdZI0hlqwJkUw8DMH_q08ln977s6xm_fEo01YnoQkxrhIGui2CmhSa_0SkU3e2I7qxQsDdILdg4JhJmUuerQ2-Ej_aecAWs5-BgfgA2DeHvEL-8PtTF9-_Tlfmp8D_IhxLELKe_', 
      skus: { colors: ['黑色', '海盐色'], sizes: ['39', '40', '41'] },
      fulfillments: [
        { id: 'dom', label: '中国大陆发货 (上海)', price: '¥11,800', eta: '预计 1-3 工作日', icon: 'local_shipping' }
      ],
      desc: '小牛皮切尔西靴，标志性厚底设计。'
    },
    { 
      type: 'apparel', 
      brand: 'THE ROW', 
      name: 'Cenda 羊绒混纺大衣', 
      price: '¥42,000', 
      img: 'https://images.unsplash.com/photo-1544022613-e87ca75a784a?auto=format&fit=crop&q=80&w=400', 
      skus: { colors: ['深灰', '驼色'], sizes: ['XS', 'S', 'M'] },
      fulfillments: [
        { id: 'ovs', label: '海外发货 (法国)', price: '¥42,000', eta: '预计 7-14 工作日', icon: 'flight_takeoff' }
      ],
      desc: '柔软触感的羊绒混纺大衣，配有同材质腰带。'
    }
  ];

  return (
    <div className="bg-[#F7F7F5] text-[#111111] font-sans antialiased min-h-screen pb-24">
      <header className={`fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 transition-colors duration-300 ${scrolled ? 'bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]' : 'bg-[#F7F7F5]'}`}>
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center justify-center p-2 -ml-2 text-[#111111] hover:opacity-80 transition-opacity" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <h1 className="font-serif text-[18px] tracking-widest absolute left-1/2 -translate-x-1/2 font-bold pointer-events-none">EXPLORE</h1>
          <div className="relative z-10 flex items-center gap-2">
            <button className="flex flex-col items-center justify-center p-2 text-[#111111] hover:opacity-80 transition-opacity" onClick={() => navigate('/visual-search')}>
              <span className="material-symbols-outlined text-[20px]">center_focus_strong</span>
            </button>
          </div>
        </div>
        
        {/* Categories / Tabs */}
        <div className="px-4 pb-3 flex gap-6 overflow-x-auto hide-scrollbar whitespace-nowrap mt-1">
          {['ALL', 'BAGS', 'SHOES', 'READY TO WEAR', 'ACCESSORIES'].map((tab) => (
            <button 
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`text-[11px] font-mono tracking-widest pb-1 border-b-2 transition-colors ${activeTab === tab ? 'border-[#111111] text-[#111111]' : 'border-transparent text-[#666663] hover:text-[#111111]'}`}
            >
              {tab}
            </button>
          ))}
        </div>
      </header>

      <main className="pt-28 flex flex-col w-full">
        {/* Utilities Bar */}
        <div className="px-5 py-4 flex justify-between items-center">
          <span className="text-[12px] text-[#666663] font-mono tracking-wider">{products.length} RESULTS</span>
          <div className="flex gap-4">
            <button className="flex items-center gap-1.5 text-[12px] font-medium text-[#111111] hover:opacity-70">
              <span className="material-symbols-outlined text-[16px]">swap_vert</span>
              排序
            </button>
            <button onClick={() => setIsFilterOpen(true)} className="flex items-center gap-1.5 text-[12px] font-medium text-[#111111] hover:opacity-70">
              <span className="material-symbols-outlined text-[16px]">tune</span>
              筛选
            </button>
          </div>
        </div>

        {/* Product Grid (Matching Home.tsx format) */}
        <section className="px-5 pb-10">
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

      {/* Advanced Filter Drawer */}
      {isFilterOpen && (
        <div className="fixed inset-0 z-[110] left-1/2 -translate-x-1/2 max-w-[430px] w-full h-full flex justify-end">
          <div className="absolute inset-0 bg-black/40 backdrop-blur-sm transition-opacity" onClick={() => setIsFilterOpen(false)} />
          <div className="relative w-[85%] bg-[#FFFFFF] h-full shadow-2xl flex flex-col animate-in slide-in-from-right duration-300">
             
             <div className="h-14 border-b border-[#E4E3DE] flex justify-between items-center px-5">
               <span className="font-medium text-[15px] text-[#111111]">筛选与排序</span>
               <button onClick={() => setIsFilterOpen(false)} className="text-[#666663] hover:text-[#111111] -mr-2 p-2">
                 <span className="material-symbols-outlined text-[20px]">close</span>
               </button>
             </div>
             
             <div className="flex-1 overflow-y-auto px-5 py-6 flex flex-col gap-8">
               {/* Sort Section */}
               <section>
                 <h4 className="text-[12px] font-medium text-[#111111] mb-4">排序方式</h4>
                 <div className="flex flex-col gap-3">
                   {['最新上架', '价格从低到高', '价格从高到低', '热销单品'].map((opt, i) => (
                     <label key={i} className="flex items-center justify-between cursor-pointer group">
                       <span className={`text-[13px] ${i === 0 ? 'text-[#111111] font-medium' : 'text-[#666663] group-hover:text-[#111111]'}`}>{opt}</span>
                       <div className={`w-4 h-4 rounded-full border flex items-center justify-center ${i === 0 ? 'border-[#111111]' : 'border-[#E4E3DE]'}`}>
                         {i === 0 && <div className="w-2 h-2 bg-[#111111] rounded-full" />}
                       </div>
                     </label>
                   ))}
                 </div>
               </section>

               <div className="h-px bg-[#E4E3DE] w-full" />

               {/* Origin Section */}
               <section>
                 <h4 className="text-[12px] font-medium text-[#111111] mb-4">发货地版本</h4>
                 <div className="flex gap-2">
                   <button className="flex-1 py-2.5 border border-[#111111] bg-[#111111] text-[#FFFFFF] text-[12px] rounded-sm">不限</button>
                   <button className="flex-1 py-2.5 border border-[#E4E3DE] bg-[#FFFFFF] text-[#111111] text-[12px] rounded-sm hover:border-[#111111] transition-colors">海外直发</button>
                   <button className="flex-1 py-2.5 border border-[#E4E3DE] bg-[#FFFFFF] text-[#111111] text-[12px] rounded-sm hover:border-[#111111] transition-colors">大陆现货</button>
                 </div>
               </section>

               <div className="h-px bg-[#E4E3DE] w-full" />

               {/* Brand Section */}
               <section>
                 <div className="flex justify-between items-center mb-4">
                   <h4 className="text-[12px] font-medium text-[#111111]">品牌</h4>
                   <span className="text-[11px] text-[#666663] underline underline-offset-2">展开全部</span>
                 </div>
                 <div className="flex flex-col gap-4">
                   {['The Row', 'Loro Piana', 'Bottega Veneta', 'Jil Sander'].map((brand, i) => (
                     <label key={i} className="flex items-center gap-3 cursor-pointer group">
                       <div className={`w-4 h-4 border rounded-sm flex items-center justify-center ${i === 0 ? 'border-[#111111] bg-[#111111]' : 'border-[#E4E3DE] bg-[#FFFFFF]'}`}>
                         {i === 0 && <span className="material-symbols-outlined text-[12px] text-[#FFFFFF]">check</span>}
                       </div>
                       <span className={`text-[13px] ${i === 0 ? 'text-[#111111] font-medium' : 'text-[#666663] group-hover:text-[#111111]'}`}>{brand}</span>
                     </label>
                   ))}
                 </div>
               </section>
               
               <div className="h-px bg-[#E4E3DE] w-full" />
               
               {/* Price Section */}
               <section>
                 <h4 className="text-[12px] font-medium text-[#111111] mb-4">价格区间 (¥)</h4>
                 <div className="flex items-center gap-3">
                   <input type="number" placeholder="最低" className="w-full h-10 border border-[#E4E3DE] rounded-sm px-3 text-[13px] outline-none focus:border-[#111111] bg-[#F7F7F5]" />
                   <span className="text-[#666663]">-</span>
                   <input type="number" placeholder="最高" className="w-full h-10 border border-[#E4E3DE] rounded-sm px-3 text-[13px] outline-none focus:border-[#111111] bg-[#F7F7F5]" />
                 </div>
               </section>

             </div>
             
             {/* Bottom Action */}
             <div className="p-4 border-t border-[#E4E3DE] flex gap-3 pb-safe bg-[#FFFFFF]">
                <button className="flex-1 h-11 border border-[#111111] text-[#111111] text-[13px] font-medium rounded-sm hover:bg-[#F7F7F5] transition-colors">重置</button>
                <button onClick={() => setIsFilterOpen(false)} className="flex-[2] h-11 bg-[#111111] text-[#FFFFFF] text-[13px] font-medium rounded-sm hover:opacity-90 transition-opacity">
                  查看 {products.length} 件商品
                </button>
             </div>
          </div>
        </div>
      )}

      <AIFab />
      <BottomNav />
    </div>
  );
}
"""

with open('src/pages/Explore.tsx', 'w') as f:
    f.write(explore_content)
