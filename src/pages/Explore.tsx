import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function Explore() {
  const navigate = useNavigate();

  return (
    <div className="bg-surface text-on-surface font-body-main antialiased min-h-screen pb-24">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full max-w-7xl mx-auto">
          <button className="relative z-10 flex items-center justify-center p-2 -ml-2 text-primary hover:opacity-80 transition-opacity" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <h1 className="font-headline-lg-mobile text-[20px] text-primary tracking-tight absolute left-1/2 -translate-x-1/2 pointer-events-none">随心逛</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-primary hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="pt-20 pb-24 flex flex-col gap-[24px] max-w-7xl mx-auto">
        <section className="px-4">
          <div className="flex items-center bg-surface-container rounded-full p-1 border border-hairline w-fit mx-auto mb-6">
            <button onClick={() => navigate('/intent')} className="px-6 py-2 rounded-full text-on-surface-variant font-label-ui text-[14px] hover:bg-surface-variant transition-colors">意图找货</button>
            <button className="px-6 py-2 rounded-full bg-pure-white text-primary font-label-ui text-[14px] shadow-sm transition-colors">分类浏览</button>
          </div>
          
          <div className="grid grid-cols-2 gap-4">
            <div className="col-span-2 aspect-[21/9] relative group overflow-hidden bg-surface-container-low cursor-pointer" onClick={() => navigate('/results')}>
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuDfVc20hhJWVxQ9Zjh_v_0zBZAsEedln_vNMHj7cZL4Y_gnL1TTk9NWfMcy47-aRhFr7CBI1vFLNXnSQIIcfIjMnUMY_soJ9CplOryBBIGsrB2AmhpXN0CAD7K5ZWqJy-s40LQDqQ82E8g-EZ936D1y8l8z-rcl8PEPjZBb-vxVal7cwW3xfsjGfrhMID4Bx3iSYt5UtheFUabrY6vRd-Fef53esvz2KlS7w6_RADP1qgTmeNN-QlVU')"}}></div>
              <div className="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent"></div>
              <div className="absolute bottom-4 left-4 z-10">
                <h3 className="font-section-title text-[24px] text-pure-white mb-1">时装皮具</h3>
                <p className="font-metadata text-[12px] text-pure-white/80">探索本季成衣与经典手袋</p>
              </div>
            </div>
            <div className="aspect-[4/5] relative group overflow-hidden bg-surface-container-low cursor-pointer">
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuDEu8Y7Q3mggUzbi1lfSzaf_Cvio0YgjG9-CHniOAk9sJ4jFykbZXegG4lw3sAJqcfV8NjX11U6gBrGKw4ll_cOXkhoOTVfMG6L7IwUkdH8lNNj7LUemnz8Im78f5vCeaaFnMvMOlrPBMNkLPgQwsl-kwru0MxNQ7dLRcmopmHUUE9qTsE4R6GSTSZM_GSVA8p5B9P_fQKAcp0fJghTW7bjuUI6K7IEpHNrQgnnO7gtXi_zChy7NEhf')"}}></div>
              <div className="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent"></div>
              <div className="absolute bottom-4 left-4 z-10">
                <h3 className="font-label-ui text-[14px] text-pure-white mb-0.5">腕表珠宝</h3>
              </div>
            </div>
            <div className="aspect-[4/5] relative group overflow-hidden bg-surface-container-low cursor-pointer">
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuBRMauj5lZ76sk-DTEWjEvXkX0EZHfeM7XbaUoZsV3N5GgaNDTcMDEKsEPjob9ynmSz1962W0cEoOHV5hiCsmQr013vr_YrIYYgErH8SRSlnDwBjdLz1f6nTJU14tnBO_Y56mMRt9xyV6YUmrRdHOmylc5gBnZoWB3wX5KAb_enHH4nRFUdMbj07dmnygFM_ZGwbWYxCydXUmuDP7_fxd9k5LUGxCBM-_Ia4pLkqaAt-soro4N-wtCd')"}}></div>
              <div className="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent"></div>
              <div className="absolute bottom-4 left-4 z-10">
                <h3 className="font-label-ui text-[14px] text-pure-white mb-0.5">美妆香氛</h3>
              </div>
            </div>
          </div>
        </section>

        <section className="px-5">
          <h2 className="font-section-title text-[24px] text-primary tracking-tight mb-6">为你精选</h2>
          <div className="grid grid-cols-2 gap-x-3 gap-y-10">
            <div className="group cursor-pointer" onClick={() => navigate('/product')}>
              <div className="aspect-[4/5] relative bg-surface-container-low mb-4 overflow-hidden">
                <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuCrE-noQEgrN3tzPv7mcJMdEx1LbcIaCgk_0asHWK7cpSLuE23HDZAu7f4Tab0YgR2D83xyJN1ELik_ifq0cCYaKU-2iz0jDFgOHJ_cWaS7yEJIgpO7IyK0MWDJOUYsQyMxvCUz20ZE45ydCp9uoBGc0j-RQdrDX_gT3VlvDSZa1z7cmcJb63PxdZZnhWEi28N71Y86ThAKpl2NWe9-Q9l8WE6JIK8Fog7wYf-NFdoDEL_xjwHBhLO7')"}}></div>
              </div>
              <p className="font-label-ui text-[14px] text-primary">The Row</p>
              <p className="font-body-main text-[16px] text-on-surface-variant truncate mt-0.5">Margaux 15 皮革手提包</p>
              <p className="font-price-tabular text-[18px] text-primary mt-2">¥ 38,500</p>
            </div>
            
            <div className="group cursor-pointer" onClick={() => navigate('/product')}>
              <div className="aspect-[4/5] relative bg-surface-container-low mb-4 overflow-hidden">
                <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuBxn-3jlW6S_StmsyDGnaHRti2PJV5n1WQNkD6qniDJwK0pqF3B5W8TYEtvsAyMQGgRqG4qISTvbAPpjkcuXD_z2p1yS_1ejIYOgFwkQsUuQWsxqVdZI0hlqwJkUw8DMH_q08ln977s6xm_fEo01YnoQkxrhIGui2CmhSa_0SkU3e2I7qxQsDdILdg4JhJmUuerQ2-Ej_aecAWs5-BgfgA2DeHvEL-8PtTF9-_Tlfmp8D_IhxLELKe_')"}}></div>
              </div>
              <p className="font-label-ui text-[14px] text-primary">Bottega Veneta</p>
              <p className="font-body-main text-[16px] text-on-surface-variant truncate mt-0.5">编织皮革切尔西靴</p>
              <p className="font-price-tabular text-[18px] text-primary mt-2">¥ 11,800</p>
            </div>
          </div>
        </section>
      </main>

      <BottomNav />
    </div>
  );
}
