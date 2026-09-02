import sys

content = """
import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function Explore() {
  const navigate = useNavigate();

  return (
    <div className="bg-surface text-on-surface font-body-main antialiased min-h-screen pb-24">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center justify-center p-2 -ml-2 text-primary hover:opacity-80 transition-opacity" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <h1 className="font-bold text-[18px] text-primary tracking-tight absolute left-1/2 -translate-x-1/2 pointer-events-none">分类浏览</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-primary hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="pt-16 pb-6 flex flex-col gap-6">
        <section className="px-4 pt-2">
          <div className="flex items-center bg-surface-container-lowest rounded-full p-1 border border-hairline w-full max-w-[280px] mx-auto mb-6 shadow-sm">
            <button onClick={() => navigate('/intent')} className="flex-1 py-1.5 rounded-full text-on-surface-variant text-[13px] hover:bg-surface transition-colors">意图找货</button>
            <button className="flex-1 py-1.5 rounded-full bg-surface text-primary font-bold text-[13px] shadow-[0_2px_8px_rgba(0,0,0,0.06)] transition-colors">分类浏览</button>
          </div>
          
          <div className="grid grid-cols-2 gap-3">
            <div className="col-span-2 aspect-[21/9] rounded-xl relative group overflow-hidden bg-surface-container-low cursor-pointer" onClick={() => navigate('/results')}>
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuDfVc20hhJWVxQ9Zjh_v_0zBZAsEedln_vNMHj7cZL4Y_gnL1TTk9NWfMcy47-aRhFr7CBI1vFLNXnSQIIcfIjMnUMY_soJ9CplOryBBIGsrB2AmhpXN0CAD7K5ZWqJy-s40LQDqQ82E8g-EZ936D1y8l8z-rcl8PEPjZBb-vxVal7cwW3xfsjGfrhMID4Bx3iSYt5UtheFUabrY6vRd-Fef53esvz2KlS7w6_RADP1qgTmeNN-QlVU')"}}></div>
              <div className="absolute inset-0 bg-black/20"></div>
              <div className="absolute bottom-3 left-4 z-10">
                <h3 className="font-bold text-[18px] text-pure-white mb-0.5">时装皮具</h3>
                <p className="text-[11px] text-pure-white/90">探索本季成衣与经典手袋</p>
              </div>
            </div>
            
            <div className="aspect-[4/5] rounded-xl relative group overflow-hidden bg-surface-container-low cursor-pointer">
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuDEu8Y7Q3mggUzbi1lfSzaf_Cvio0YgjG9-CHniOAk9sJ4jFykbZXegG4lw3sAJqcfV8NjX11U6gBrGKw4ll_cOXkhoOTVfMG6L7IwUkdH8lNNj7LUemnz8Im78f5vCeaaFnMvMOlrPBMNkLPgQwsl-kwru0MxNQ7dLRcmopmHUUE9qTsE4R6GSTSZM_GSVA8p5B9P_fQKAcp0fJghTW7bjuUI6K7IEpHNrQgnnO7gtXi_zChy7NEhf')"}}></div>
              <div className="absolute inset-0 bg-black/10"></div>
              <div className="absolute bottom-3 left-3 z-10">
                <h3 className="font-bold text-[14px] text-pure-white shadow-sm">腕表珠宝</h3>
              </div>
            </div>
            
            <div className="aspect-[4/5] rounded-xl relative group overflow-hidden bg-surface-container-low cursor-pointer">
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuBRMauj5lZ76sk-DTEWjEvXkX0EZHfeM7XbaUoZsV3N5GgaNDTcMDEKsEPjob9ynmSz1962W0cEoOHV5hiCsmQr013vr_YrIYYgErH8SRSlnDwBjdLz1f6nTJU14tnBO_Y56mMRt9xyV6YUmrRdHOmylc5gBnZoWB3wX5KAb_enHH4nRFUdMbj07dmnygFM_ZGwbWYxCydXUmuDP7_fxd9k5LUGxCBM-_Ia4pLkqaAt-soro4N-wtCd')"}}></div>
              <div className="absolute inset-0 bg-black/10"></div>
              <div className="absolute bottom-3 left-3 z-10">
                <h3 className="font-bold text-[14px] text-pure-white shadow-sm">美妆香氛</h3>
              </div>
            </div>
          </div>
        </section>

        <section className="px-4">
          <h2 className="font-bold text-[16px] text-primary tracking-tight mb-4 px-1">为你精选</h2>
          <div className="grid grid-cols-2 gap-3">
            <div className="group cursor-pointer bg-pure-white rounded-xl overflow-hidden shadow-[0_2px_8px_rgba(0,0,0,0.04)] border border-hairline pb-2" onClick={() => navigate('/product')}>
              <div className="aspect-square relative bg-surface-container-lowest overflow-hidden">
                <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuCrE-noQEgrN3tzPv7mcJMdEx1LbcIaCgk_0asHWK7cpSLuE23HDZAu7f4Tab0YgR2D83xyJN1ELik_ifq0cCYaKU-2iz0jDFgOHJ_cWaS7yEJIgpO7IyK0MWDJOUYsQyMxvCUz20ZE45ydCp9uoBGc0j-RQdrDX_gT3VlvDSZa1z7cmcJb63PxdZZnhWEi28N71Y86ThAKpl2NWe9-Q9l8WE6JIK8Fog7wYf-NFdoDEL_xjwHBhLO7')"}}></div>
              </div>
              <div className="p-3 flex flex-col justify-between">
                <div>
                  <p className="font-bold text-[13px] text-primary line-clamp-1">The Row</p>
                  <p className="text-[11px] text-on-surface-variant truncate mb-2">Margaux 15 皮革手提包</p>
                </div>
                <p className="font-semibold text-[14px] text-primary">¥ 38,500</p>
              </div>
            </div>
            
            <div className="group cursor-pointer bg-pure-white rounded-xl overflow-hidden shadow-[0_2px_8px_rgba(0,0,0,0.04)] border border-hairline pb-2" onClick={() => navigate('/product')}>
              <div className="aspect-square relative bg-surface-container-lowest overflow-hidden">
                <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuBxn-3jlW6S_StmsyDGnaHRti2PJV5n1WQNkD6qniDJwK0pqF3B5W8TYEtvsAyMQGgRqG4qISTvbAPpjkcuXD_z2p1yS_1ejIYOgFwkQsUuQWsxqVdZI0hlqwJkUw8DMH_q08ln977s6xm_fEo01YnoQkxrhIGui2CmhSa_0SkU3e2I7qxQsDdILdg4JhJmUuerQ2-Ej_aecAWs5-BgfgA2DeHvEL-8PtTF9-_Tlfmp8D_IhxLELKe_')"}}></div>
              </div>
              <div className="p-3 flex flex-col justify-between">
                <div>
                  <p className="font-bold text-[13px] text-primary line-clamp-1">Bottega Veneta</p>
                  <p className="text-[11px] text-on-surface-variant truncate mb-2">编织皮革切尔西靴</p>
                </div>
                <p className="font-semibold text-[14px] text-primary">¥ 11,800</p>
              </div>
            </div>
          </div>
        </section>
      </main>
      <BottomNav />
    </div>
  );
}
"""
with open('src/pages/Explore.tsx', 'w') as f:
    f.write(content)
