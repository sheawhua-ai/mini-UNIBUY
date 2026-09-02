import React, { useState, useEffect } from 'react';
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

  return (
    <div className="relative min-h-screen pb-24 overflow-x-hidden bg-[#F7F7F5] text-[#111111] font-sans">
      <header className={`fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 transition-colors duration-300 ${scrolled ? 'bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]' : 'bg-transparent'}`}>
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button aria-label="Menu" className={`relative z-10 hover:opacity-80 transition-transform active:scale-95 duration-200 p-2 -ml-2 ${scrolled ? 'text-[#111111]' : 'text-white'}`}>
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

        {/* Editorial Topics (Replaces redundant 4-icon grid) */}
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
              <span className="text-[11px] text-[#666663] uppercase tracking-widest mb-1 block">Curated For You</span>
              <h3 className="font-serif text-[24px] text-[#111111]">为你推荐</h3>
            </div>
          </div>
          
          <div className="grid grid-cols-2 gap-3">
            {[
              { title: 'Noir Signature Tote', material: '全粒面牛皮', price: '¥8,500', img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw', tag: '上新' },
              { title: 'Voyageur Weekender', material: '防水帆布', price: '¥12,200', img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuALof-gjivI7JLbQxwFhG0FSCgL57IKvGoctb1bjLRjNyskfyOXxx2LwUwL65EttBmLlToJJyCmfdFB-0xdIvj2MQ0cA-YZqLB0TAiIbiBcnn9TuUrHtR3qWLMAa2K55d8ZpKnVvO7fki0iijcCiOGkAJWAnkhvz46UglO3JZ9IsgfdDHiKKQeGzjB7BI9NTt2uqI9JX55f4acEcI5bwju3mm5HLg6LOECdhukAeJWJLsxXMYr7kAu1', tag: '' },
              { title: 'Leather Briefcase', material: '头层牛皮', price: '¥6,800', img: 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&q=80&w=400', tag: '推荐' },
              { title: 'Urban Backpack', material: '尼龙拼接', price: '¥4,500', img: 'https://images.unsplash.com/photo-1622560480605-d83c853bc5c3?auto=format&fit=crop&q=80&w=400', tag: '' }
            ].map((prod, i) => (
              <article key={i} className="flex flex-col group cursor-pointer bg-[#FFFFFF] pb-3" onClick={() => navigate('/product')}>
                <div className="w-full aspect-[4/5] bg-[#EFEFEB] overflow-hidden relative mb-3">
                  <img src={prod.img} alt={prod.title} className="w-full h-full object-cover" />
                  {prod.tag && (
                    <div className="absolute top-2 left-2 bg-white/90 backdrop-blur px-2 py-0.5 text-[10px] font-medium text-[#111111]">
                      {prod.tag}
                    </div>
                  )}
                </div>
                <div className="px-1 flex flex-col">
                  <h4 className="font-medium text-[13px] text-[#111111] mb-0.5 line-clamp-1">{prod.title}</h4>
                  <p className="text-[11px] text-[#666663] mb-1.5">{prod.material}</p>
                  <p className="font-medium text-[14px] text-[#111111] font-mono">{prod.price}</p>
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
