import os

# 1. Create AIFab.tsx
os.makedirs('src/components', exist_ok=True)
with open('src/components/AIFab.tsx', 'w') as f:
    f.write("""import React, { useState, useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function AIFab() {
  const [expanded, setExpanded] = useState(false);
  const navigate = useNavigate();
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (expanded && inputRef.current) {
      inputRef.current.focus();
    }
  }, [expanded]);

  return (
    <div className="fixed bottom-[80px] right-4 z-50 flex items-center justify-end h-[52px]">
      {expanded ? (
        <div className="bg-[#FFFFFF]/95 backdrop-blur-xl border border-[#E4E3DE] h-full shadow-[0_8px_32px_rgba(0,0,0,0.12)] flex items-center px-4 rounded-sm w-[calc(100vw-32px)] max-w-[398px] animate-in slide-in-from-right-8 fade-in duration-300">
          <span className="text-[12px] text-[#111111] font-bold mr-3 uppercase tracking-widest">AI</span>
          <input
            ref={inputRef}
            className="flex-1 bg-transparent border-none p-0 focus:ring-0 text-[14px] text-[#111111] placeholder:text-[#666663] outline-none font-light"
            placeholder="帮我找..."
            onKeyDown={(e) => {
              if (e.key === 'Enter') navigate('/intent');
            }}
          />
          <div className="flex items-center gap-3 text-[#111111] ml-2 shrink-0">
            <button className="hover:opacity-80 flex items-center" onClick={() => navigate('/intent')}><span className="material-symbols-outlined text-[20px] font-light">mic</span></button>
            <div className="w-[1px] h-4 bg-[#E4E3DE]"></div>
            <button className="hover:opacity-80 flex items-center" onClick={() => navigate('/visual-search')}>
              <span className="material-symbols-outlined text-[20px] font-light">lens_camera</span>
            </button>
            <button className="hover:opacity-80 flex items-center ml-1 text-[#666663]" onClick={() => setExpanded(false)}>
              <span className="material-symbols-outlined text-[20px] font-light">close</span>
            </button>
          </div>
        </div>
      ) : (
        <button
          onClick={() => setExpanded(true)}
          className="w-[52px] h-[52px] bg-[#111111] text-[#FFFFFF] rounded-sm shadow-[0_4px_16px_rgba(0,0,0,0.2)] flex items-center justify-center hover:scale-105 transition-transform active:scale-95 animate-in zoom-in duration-300"
        >
          <span className="material-symbols-outlined text-[24px]">psychiatry</span>
        </button>
      )}
    </div>
  );
}
""")

# 2. Update Home.tsx
with open('src/pages/Home.tsx', 'w') as f:
    f.write("""import React, { useState, useEffect } from 'react';
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
""")

# 3. Update Explore.tsx
with open('src/pages/Explore.tsx', 'w') as f:
    f.write("""import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';
import AIFab from '../components/AIFab';

export default function Explore() {
  const navigate = useNavigate();
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 10);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div className="bg-[#F7F7F5] text-[#111111] font-sans antialiased min-h-screen pb-24">
      <header className={`fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 transition-colors duration-300 ${scrolled ? 'bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]' : 'bg-[#F7F7F5]'}`}>
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center justify-center p-2 -ml-2 text-[#111111] hover:opacity-80 transition-opacity" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <h1 className="font-serif text-[18px] text-[#111111] tracking-widest absolute left-1/2 -translate-x-1/2 pointer-events-none">EXPLORE</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-[#111111] hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
          </div>
        </div>
      </header>

      <main className="pt-16 pb-6 flex flex-col gap-6">
        <section className="px-4">
          <div className="flex items-center gap-4 mb-6 mt-2 border-b border-[#E4E3DE] pb-2">
            <button className="text-[14px] font-medium text-[#111111] border-b-2 border-[#111111] pb-2">分类浏览</button>
            <button className="text-[14px] text-[#666663] pb-2" onClick={() => navigate('/private')}>私人精选</button>
          </div>
          
          <div className="grid grid-cols-2 gap-3">
            <div className="col-span-2 aspect-[21/9] rounded-sm relative group overflow-hidden bg-[#EFEFEB] cursor-pointer" onClick={() => navigate('/results')}>
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuDfVc20hhJWVxQ9Zjh_v_0zBZAsEedln_vNMHj7cZL4Y_gnL1TTk9NWfMcy47-aRhFr7CBI1vFLNXnSQIIcfIjMnUMY_soJ9CplOryBBIGsrB2AmhpXN0CAD7K5ZWqJy-s40LQDqQ82E8g-EZ936D1y8l8z-rcl8PEPjZBb-vxVal7cwW3xfsjGfrhMID4Bx3iSYt5UtheFUabrY6vRd-Fef53esvz2KlS7w6_RADP1qgTmeNN-QlVU')"}}></div>
              <div className="absolute inset-0 bg-black/20"></div>
              <div className="absolute bottom-4 left-4 z-10">
                <h3 className="font-serif text-[20px] text-white mb-1">时装与皮具</h3>
                <p className="text-[11px] text-white/90 tracking-widest uppercase">Fashion & Leather</p>
              </div>
            </div>
            
            <div className="aspect-[4/5] rounded-sm relative group overflow-hidden bg-[#EFEFEB] cursor-pointer">
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuDEu8Y7Q3mggUzbi1lfSzaf_Cvio0YgjG9-CHniOAk9sJ4jFykbZXegG4lw3sAJqcfV8NjX11U6gBrGKw4ll_cOXkhoOTVfMG6L7IwUkdH8lNNj7LUemnz8Im78f5vCeaaFnMvMOlrPBMNkLPgQwsl-kwru0MxNQ7dLRcmopmHUUE9qTsE4R6GSTSZM_GSVA8p5B9P_fQKAcp0fJghTW7bjuUI6K7IEpHNrQgnnO7gtXi_zChy7NEhf')"}}></div>
              <div className="absolute inset-0 bg-black/10"></div>
              <div className="absolute bottom-3 left-3 z-10">
                <h3 className="font-serif text-[16px] text-white">腕表与珠宝</h3>
              </div>
            </div>
            
            <div className="aspect-[4/5] rounded-sm relative group overflow-hidden bg-[#EFEFEB] cursor-pointer">
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuBRMauj5lZ76sk-DTEWjEvXkX0EZHfeM7XbaUoZsV3N5GgaNDTcMDEKsEPjob9ynmSz1962W0cEoOHV5hiCsmQr013vr_YrIYYgErH8SRSlnDwBjdLz1f6nTJU14tnBO_Y56mMRt9xyV6YUmrRdHOmylc5gBnZoWB3wX5KAb_enHH4nRFUdMbj07dmnygFM_ZGwbWYxCydXUmuDP7_fxd9k5LUGxCBM-_Ia4pLkqaAt-soro4N-wtCd')"}}></div>
              <div className="absolute inset-0 bg-black/10"></div>
              <div className="absolute bottom-3 left-3 z-10">
                <h3 className="font-serif text-[16px] text-white">美妆与香氛</h3>
              </div>
            </div>
          </div>
        </section>

        <section className="px-4 mt-4">
          <h2 className="font-serif text-[20px] text-[#111111] mb-4">为你精选</h2>
          <div className="grid grid-cols-2 gap-3">
            <div className="group cursor-pointer bg-[#FFFFFF] rounded-sm overflow-hidden pb-3" onClick={() => navigate('/product')}>
              <div className="aspect-[4/5] relative bg-[#EFEFEB] overflow-hidden mb-3">
                <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuCrE-noQEgrN3tzPv7mcJMdEx1LbcIaCgk_0asHWK7cpSLuE23HDZAu7f4Tab0YgR2D83xyJN1ELik_ifq0cCYaKU-2iz0jDFgOHJ_cWaS7yEJIgpO7IyK0MWDJOUYsQyMxvCUz20ZE45ydCp9uoBGc0j-RQdrDX_gT3VlvDSZa1z7cmcJb63PxdZZnhWEi28N71Y86ThAKpl2NWe9-Q9l8WE6JIK8Fog7wYf-NFdoDEL_xjwHBhLO7')"}}></div>
              </div>
              <div className="px-1 flex flex-col justify-between">
                <div>
                  <p className="font-medium text-[13px] text-[#111111] line-clamp-1 mb-0.5">The Row</p>
                  <p className="text-[11px] text-[#666663] truncate mb-2">Margaux 15 皮革手提包</p>
                </div>
                <p className="font-medium text-[14px] text-[#111111] font-mono">¥ 38,500</p>
              </div>
            </div>
            
            <div className="group cursor-pointer bg-[#FFFFFF] rounded-sm overflow-hidden pb-3" onClick={() => navigate('/product')}>
              <div className="aspect-[4/5] relative bg-[#EFEFEB] overflow-hidden mb-3">
                <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuBxn-3jlW6S_StmsyDGnaHRti2PJV5n1WQNkD6qniDJwK0pqF3B5W8TYEtvsAyMQGgRqG4qISTvbAPpjkcuXD_z2p1yS_1ejIYOgFwkQsUuQWsxqVdZI0hlqwJkUw8DMH_q08ln977s6xm_fEo01YnoQkxrhIGui2CmhSa_0SkU3e2I7qxQsDdILdg4JhJmUuerQ2-Ej_aecAWs5-BgfgA2DeHvEL-8PtTF9-_Tlfmp8D_IhxLELKe_')"}}></div>
              </div>
              <div className="px-1 flex flex-col justify-between">
                <div>
                  <p className="font-medium text-[13px] text-[#111111] line-clamp-1 mb-0.5">Bottega Veneta</p>
                  <p className="text-[11px] text-[#666663] truncate mb-2">编织皮革切尔西靴</p>
                </div>
                <p className="font-medium text-[14px] text-[#111111] font-mono">¥ 11,800</p>
              </div>
            </div>
          </div>
        </section>
      </main>

      <AIFab />
      <BottomNav />
    </div>
  );
}
""")

# 4. Update MemberCenter.tsx
with open('src/pages/MemberCenter.tsx', 'w') as f:
    f.write("""import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function MemberCenter() {
  const navigate = useNavigate();

  return (
    <div className="bg-[#F7F7F5] text-[#111111] font-sans antialiased min-h-screen pb-24">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#F7F7F5]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center justify-center p-2 -ml-2 text-[#111111] hover:opacity-80 transition-opacity" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <h1 className="font-serif text-[18px] text-[#111111] tracking-widest absolute left-1/2 -translate-x-1/2 pointer-events-none uppercase">ATELIER</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-[#111111] hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
          </div>
        </div>
      </header>

      <main className="pt-20 pb-6 px-5 flex flex-col gap-8">
        {/* Black Card with Tiers and Points */}
        <section className="bg-[#242424] text-[#F7F7F5] rounded-sm p-6 relative overflow-hidden shadow-lg">
          <div className="absolute top-0 right-0 w-48 h-48 bg-white/5 rounded-full -translate-y-1/2 translate-x-1/4 blur-3xl"></div>
          
          <div className="relative z-10 flex justify-between items-start mb-8">
            <div>
              <div className="flex items-center gap-2 mb-1">
                <span className="w-1.5 h-1.5 bg-[#E56A1D] rounded-none"></span>
                <p className="font-medium text-[11px] text-[#E56A1D] uppercase tracking-widest">Noir 等级</p>
              </div>
              <h2 className="font-serif text-[24px] tracking-widest uppercase">ALEX CHEN</h2>
            </div>
            <div className="w-12 h-12 border border-[#E56A1D]/30 overflow-hidden rounded-sm">
              <img className="w-full h-full object-cover grayscale" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDNaeE-LiR7h5C_dDZP4Rma_H3UQZypRN2tkJncNemYb8j2JRV0-AC3MqwYxa_SftiX-SsTfhplEvJkF2rh7hNY4-sd8y0E5PP0tMte1bEFr6pinfnFjZf0ngqdTUz32S_qpcW5vF4J7wxePjqe0O-82NY3Bd55cjOHLiRmp6pPuVZN_XRqmTbpgv9QYxV2KIRC2fFKSinQu6y1hOZuWFRV3-vhLIMfykbe_MiO4Xdx68vA2kJoQvjr" alt="Avatar" />
            </div>
          </div>
          
          <div className="relative z-10 flex flex-col gap-2">
            <div className="flex justify-between items-end">
              <div>
                <p className="text-[10px] text-white/60 mb-0.5">可用积分余额</p>
                <p className="font-mono text-[22px] font-medium leading-none">12,500</p>
              </div>
              <button className="text-[11px] text-white/80 underline underline-offset-2 hover:text-white transition-colors">积分明细</button>
            </div>
            
            <div className="mt-4 pt-4 border-t border-white/10">
              <div className="flex justify-between text-[11px] text-[#F7F7F5]/80 font-mono mb-2">
                <span>升至顶级 Privé 需 2,500 积分</span>
              </div>
              <div className="w-full h-[2px] bg-white/20 overflow-hidden">
                <div className="h-full bg-[#E56A1D] w-[83%]"></div>
              </div>
            </div>
          </div>
        </section>

        {/* Services & Redemption */}
        <section>
          <div className="flex justify-between items-end mb-4 border-b border-[#E4E3DE] pb-2">
            <h3 className="font-serif text-[20px] text-[#111111]">积分兑换权益</h3>
            <button className="text-[11px] text-[#666663] underline underline-offset-2 hover:text-[#111111]">查看全部</button>
          </div>
          <div className="flex flex-col gap-4">
            {[
              { img: 'https://images.unsplash.com/photo-1584824486516-0555a07fc511?auto=format&fit=crop&q=80&w=200', title: '专柜深度皮具护理', points: '2,000 pts', desc: '包含名贵皮具深度清洁、专业补色及抛光服务。' },
              { img: 'https://images.unsplash.com/photo-1544148103-0773bf10d330?auto=format&fit=crop&q=80&w=200', title: '奢华酒店双人下午茶', points: '5,000 pts', desc: '全球指定合作五星级酒店或米其林餐厅双人套餐。' },
              { img: 'https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&q=80&w=200', title: '私人造型师上门', points: '10,000 pts', desc: '2小时专属衣橱整理、重要场合穿搭指导与改衣服务。' }
            ].map((item, i) => (
              <div key={i} className="bg-[#FFFFFF] border border-[#E4E3DE] rounded-sm p-3 flex items-center gap-4 shadow-sm cursor-pointer hover:border-[#111111] transition-colors group">
                <div className="w-16 h-20 bg-[#EFEFEB] rounded-sm overflow-hidden flex-shrink-0">
                  <img src={item.img} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Service" />
                </div>
                <div className="flex-1">
                  <h4 className="font-medium text-[14px] text-[#111111] mb-1">{item.title}</h4>
                  <p className="text-[11px] text-[#666663] leading-relaxed mb-2 line-clamp-2">{item.desc}</p>
                  <p className="text-[12px] font-mono font-medium text-[#E56A1D]">{item.points}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Regular Privileges */}
        <section className="mt-2">
          <div className="flex justify-between items-end mb-4 border-b border-[#E4E3DE] pb-2">
            <h3 className="font-serif text-[20px] text-[#111111]">常驻等级礼遇</h3>
          </div>
          <div className="grid grid-cols-2 gap-3">
            {[
              { icon: 'local_shipping', title: '全球免邮', desc: '尊享所有订单免费配送' },
              { icon: 'event_available', title: '优先抢购', desc: '提前24小时锁定限量品' }
            ].map((item, i) => (
              <div key={i} className="bg-[#FFFFFF] border border-[#E4E3DE] rounded-sm p-4 flex flex-col gap-3 shadow-sm cursor-pointer hover:border-[#111111] transition-colors">
                <span className="material-symbols-outlined text-[24px] text-[#111111] font-light">{item.icon}</span>
                <div>
                  <h4 className="font-medium text-[13px] text-[#111111] mb-1">{item.title}</h4>
                  <p className="text-[11px] text-[#666663] leading-relaxed">{item.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
      </main>
      <BottomNav />
    </div>
  );
}
""")
