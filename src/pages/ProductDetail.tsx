import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function ProductDetail() {
  const navigate = useNavigate();
  const [openSection, setOpenSection] = useState<string | null>(null);

  const toggleSection = (id: string) => {
    setOpenSection(openSection === id ? null : id);
  };

  return (
    <div className="bg-background text-on-surface font-body-main antialiased pb-24 min-h-screen">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full max-w-7xl mx-auto">
          <button onClick={() => navigate(-1)} className="relative z-10 text-primary hover:opacity-80 transition-opacity p-2 -ml-2">
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <h1 className="font-display-hero text-[22px] text-primary tracking-tighter absolute left-1/2 -translate-x-1/2 pointer-events-none">UNIBUY</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-primary hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="pt-14 max-w-7xl mx-auto">
        <section className="w-full relative aspect-[4/5] bg-surface-container overflow-hidden">
          <div className="flex w-full h-full snap-x snap-mandatory overflow-x-auto hide-scrollbar">
            <div className="snap-center w-full h-full flex-shrink-0 relative">
              <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBPKGS7xf9zk70TpBqZRRqzPTO-3sMdu0MmdycHstpbuyXM3QkbF6R0wHPAPAzu4b1RiYmYUNhgxKC-cHEHAFf-bB20TSGB8gbhqFduIQ5hnQlTHf1xQawPdn7qLFLXRhFccXOr1QpRj2x9LQayZ0b_dxiCyfZQMly-6DMFB_RK-AUYqPFl4XEtsuUxf-ZgYww2odM6wHRPMmtR4iauslUT9m-FprvVtHIEMcBGLTT3dFB0TzDOc_ge" alt="Bag" />
            </div>
          </div>
          <div className="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2">
            <div className="w-1.5 h-1.5 rounded-full bg-pure-white"></div>
            <div className="w-1.5 h-1.5 rounded-full bg-pure-white/40"></div>
          </div>
        </section>

        <section className="px-5 pt-6 pb-8 border-b border-hairline">
          <div className="flex justify-between items-start mb-2">
            <div>
              <h2 className="font-label-ui text-[14px] text-on-surface-variant uppercase tracking-widest mb-1">工坊系列</h2>
              <h3 className="font-section-title text-[24px] text-primary font-medium leading-tight">The Executive Tote</h3>
            </div>
            <span className="inline-block border border-[#E56A1D] text-[#E56A1D] font-metadata text-[12px] px-2 py-0.5 uppercase rounded">会员专享</span>
          </div>
          <div className="flex justify-between items-center mt-6">
            <p className="font-price-tabular text-[18px] text-primary">¥ 12,500</p>
            <div className="flex items-center text-on-surface-variant gap-1">
              <span className="material-symbols-outlined text-[16px]">local_shipping</span>
              <span className="font-metadata text-[12px]">预计 2-3 个工作日送达</span>
            </div>
          </div>
        </section>

        <section className="px-5 py-8 border-b border-hairline">
          <div className="flex items-center gap-2 mb-4">
            <span className="material-symbols-outlined text-on-surface-variant">auto_awesome</span>
            <h4 className="font-label-ui text-[14px] text-primary uppercase">为何适合你</h4>
          </div>
          <div className="bg-surface-container-low p-4 rounded-lg">
            <p className="font-body-main text-[16px] text-on-surface mb-4 leading-relaxed">基于您的偏好分析，此款手袋完美契合您的需求：</p>
            <ul className="space-y-3">
              <li className="flex items-start gap-3">
                <span className="material-symbols-outlined text-primary text-[20px] mt-0.5">check</span>
                <div>
                  <p className="font-label-ui text-[14px] text-primary">低调无 Logo 设计</p>
                  <p className="font-metadata text-[12px] text-on-surface-variant mt-0.5">符合您一贯的极简主义美学追求，避免过度张扬。</p>
                </div>
              </li>
              <li className="flex items-start gap-3">
                <span className="material-symbols-outlined text-primary text-[20px] mt-0.5">check</span>
                <div>
                  <p className="font-label-ui text-[14px] text-primary">可容纳 15 英寸笔记本电脑</p>
                  <p className="font-metadata text-[12px] text-on-surface-variant mt-0.5">内置专属加厚隔层，满足您日常通勤的实用需求。</p>
                </div>
              </li>
            </ul>
          </div>
        </section>

        <section className="px-5 py-4">
          <div className="border-b border-hairline">
            <button className="w-full py-4 flex justify-between items-center text-left" onClick={() => toggleSection('story')}>
              <span className="font-label-ui text-[14px] text-primary uppercase">设计故事</span>
              <span className="material-symbols-outlined text-on-surface-variant transition-transform duration-300">
                {openSection === 'story' ? 'remove' : 'add'}
              </span>
            </button>
            {openSection === 'story' && (
              <div className="pb-4">
                <p className="font-body-main text-[16px] text-on-surface-variant leading-relaxed">灵感源自现代都会建筑的利落线条，The Executive Tote 旨在为当代专业人士提供一个既能承载日常重任，又能保持优雅身姿的完美容器。每一个切角都经过精确计算。</p>
              </div>
            )}
          </div>
          
          <div className="border-b border-hairline">
            <button className="w-full py-4 flex justify-between items-center text-left" onClick={() => toggleSection('craft')}>
              <span className="font-label-ui text-[14px] text-primary uppercase">材质工艺</span>
              <span className="material-symbols-outlined text-on-surface-variant transition-transform duration-300">
                {openSection === 'craft' ? 'remove' : 'add'}
              </span>
            </button>
            {openSection === 'craft' && (
              <div className="pb-4">
                <p className="font-body-main text-[16px] text-on-surface-variant leading-relaxed">甄选顶级全粒面小牛皮，经由意大利工坊传统鞣制工艺处理。内部采用超细纤维内衬，金属配件均经过哑光抗氧化处理，确保历久弥新。</p>
              </div>
            )}
          </div>
        </section>

        <section className="px-5 py-8 mt-4">
          <button className="w-full flex items-center justify-between p-4 border border-hairline rounded hover:bg-surface-container-low transition-colors">
            <div className="flex items-center gap-4">
              <div className="w-10 h-10 rounded-full bg-surface-dim flex items-center justify-center overflow-hidden">
                <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDNaeE-LiR7h5C_dDZP4Rma_H3UQZypRN2tkJncNemYb8j2JRV0-AC3MqwYxa_SftiX-SsTfhplEvJkF2rh7hNY4-sd8y0E5PP0tMte1bEFr6pinfnFjZf0ngqdTUz32S_qpcW5vF4J7wxePjqe0O-82NY3Bd55cjOHLiRmp6pPuVZN_XRqmTbpgv9QYxV2KIRC2fFKSinQu6y1hOZuWFRV3-vhLIMfykbe_MiO4Xdx68vA2kJoQvjr" alt="Advisor" />
              </div>
              <div className="text-left">
                <p className="font-label-ui text-[14px] text-primary">专属顾问 Elara</p>
                <p className="font-metadata text-[12px] text-on-surface-variant">在线为您解答搭配疑问</p>
              </div>
            </div>
            <span className="material-symbols-outlined text-primary">chat_bubble_outline</span>
          </button>
        </section>
      </main>

      <div className="fixed bottom-0 w-full z-50 bg-surface/90 backdrop-blur-2xl border-t border-hairline px-5 py-4 pb-safe flex items-center gap-4 absolute">
        <div className="flex gap-4">
          <button className="flex flex-col items-center justify-center text-primary hover:opacity-70 transition-opacity">
            <span className="material-symbols-outlined">favorite_border</span>
            <span className="font-metadata text-[10px] mt-1">收藏</span>
          </button>
          <button className="flex flex-col items-center justify-center text-primary hover:opacity-70 transition-opacity" onClick={() => navigate('/compare')}>
            <span className="material-symbols-outlined">compare_arrows</span>
            <span className="font-metadata text-[10px] mt-1">对比</span>
          </button>
        </div>
        <button className="flex-1 bg-primary text-pure-white font-label-ui text-[14px] rounded uppercase tracking-wider hover:bg-primary/90 transition-colors h-12">
          加入购物袋
        </button>
      </div>
    </div>
  );
}
