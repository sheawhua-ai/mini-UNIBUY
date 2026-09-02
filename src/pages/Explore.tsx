import React, { useState, useEffect } from 'react';
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
