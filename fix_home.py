import os
import re

with open('src/pages/Home.tsx', 'r') as f:
    home_content = f.read()

# Just recreate Home.tsx cleanly.
new_home = """import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';
import AIFab from '../components/AIFab';

export default function Home() {
  const navigate = useNavigate();
  const [scrolled, setScrolled] = useState(false);

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
    }
  ];

  return (
    <div className="relative min-h-screen pb-24 overflow-x-hidden bg-[#F7F7F5] text-[#111111] font-sans">
      <header className={`fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 transition-colors duration-300 ${scrolled ? 'bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]' : 'bg-transparent'}`}>
        <div className="relative flex justify-center items-center px-4 h-14 w-full">
          <h1 className={`font-serif text-[20px] tracking-widest pointer-events-none font-bold ${scrolled ? 'text-[#111111]' : 'text-white'}`}>UNIBUY</h1>
        </div>
      </header>

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
    f.write(new_home)
