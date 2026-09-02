import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="relative min-h-full pb-24 overflow-x-hidden bg-background text-on-surface">
      {/* TopAppBar */}
      <header className="fixed top-0 left-0 w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full max-w-7xl mx-auto">
          <button aria-label="Menu" className="relative z-10 text-primary hover:opacity-80 transition-transform active:scale-95 duration-200 p-2 -ml-2">
            <span className="material-symbols-outlined text-[24px]">menu</span>
          </button>
          <h1 className="font-display-hero text-[22px] tracking-tighter text-primary absolute left-1/2 -translate-x-1/2 pointer-events-none font-bold">UNIBUY</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button aria-label="Shopping Bag" className="text-primary hover:opacity-80 transition-transform active:scale-95 duration-200 p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section 
        className="relative h-[40vh] w-full flex items-end pb-20 bg-cover bg-center"
        style={{ backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuArjtrVE2lG4P8GVPHflyWb0Mo5SVTyYRhEKICWp9dXBZfgpnNrEjMm6dtbb5AIQEJulXtvOM2xsrCwwNtXTUGD-ijZT4Ysg_qC8E06uX1B8BvShZ3crQWafJlSTskDHLbYcvpzUhub0jJs9GzUV15SSZE3qvn2mQV6vrwfgxBhaFpM6nYybFKKT4dA7wbrIK7HlkPDWs23ehSoCcEl9zupcOvb1U6484cHAiBp62KwkzvTEDpq6g1U')" }}
      >
        <div className="absolute inset-0 bg-gradient-to-t from-surface via-transparent to-transparent opacity-90"></div>
        <div className="relative z-10 px-5 w-full max-w-7xl mx-auto">
          <h2 className="font-display-hero text-[38px] text-primary max-w-lg leading-tight mb-4 tracking-tighter">旅行，是另一种收藏。</h2>
          <p className="font-body-main text-[16px] text-on-surface-variant max-w-md">探索全球甄选的高级旅行方式，让每一次出发都成为不凡的印记。</p>
        </div>
      </section>

      {/* AI Intent Bar */}
      <div className="relative z-20 -mt-10 px-5 w-full max-w-2xl mx-auto">
        <div 
          className="bg-pure-white border border-hairline rounded flex items-center px-4 h-[52px] shadow-[0_8px_32px_rgba(0,0,0,0.08)] cursor-text"
          onClick={() => navigate('/intent')}
        >
          <span className="font-metadata text-[12px] text-on-surface-variant mr-3">AI</span>
          <div className="w-full bg-transparent font-body-main text-[16px] text-on-surface-variant flex-1 overflow-hidden whitespace-nowrap">
            帮我找适合商务差旅、低调又能装电脑的包
          </div>
          <button className="text-primary ml-2 hover:opacity-80 transition-opacity">
            <span className="material-symbols-outlined">arrow_forward</span>
          </button>
        </div>
      </div>

      <main className="w-full max-w-7xl mx-auto mt-12 px-4 flex flex-col gap-8">
        
        {/* Features Links */}
        <div className="flex flex-wrap gap-3 pt-2">
          <button onClick={() => navigate('/explore')} className="px-4 py-2 bg-mist rounded border border-hairline text-[14px] font-medium text-primary">随心逛</button>
          <button onClick={() => navigate('/private')} className="px-4 py-2 bg-mist rounded border border-hairline text-[14px] font-medium text-primary">私人精选</button>
          <button onClick={() => navigate('/visual-search')} className="px-4 py-2 bg-mist rounded border border-hairline text-[14px] font-medium text-primary">视觉搜索</button>
        </div>

        {/* 为你上新 */}
        <section>
          <div className="flex justify-between items-baseline mb-8">
            <h3 className="font-section-title text-[24px] text-primary tracking-tight">为你上新</h3>
            <span className="font-label-ui text-[14px] text-on-surface-variant hover:text-primary transition-colors cursor-pointer">查看全部</span>
          </div>
          <div className="grid grid-cols-2 gap-x-3 gap-y-8">
            <article className="flex flex-col group cursor-pointer" onClick={() => navigate('/product')}>
              <div className="w-full aspect-[4/5] bg-surface-container-lowest overflow-hidden mb-4 relative bg-cover bg-center" style={{ backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw')" }}>
                <div className="absolute top-2 left-2 bg-surface/80 backdrop-blur px-2 py-1">
                  <span className="font-metadata text-[12px] text-primary uppercase tracking-widest">上新</span>
                </div>
              </div>
              <h4 className="font-body-main text-[16px] text-primary mb-1">Noir Signature Tote</h4>
              <p className="font-metadata text-[12px] text-on-surface-variant mb-2 line-clamp-1">意大利全粒面牛皮</p>
              <p className="font-price-tabular text-[18px] text-primary">¥ 8,500</p>
            </article>

            <article className="flex flex-col group cursor-pointer" onClick={() => navigate('/product')}>
              <div className="w-full aspect-[4/5] bg-surface-container-lowest overflow-hidden mb-4 relative bg-cover bg-center" style={{ backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuALof-gjivI7JLbQxwFhG0FSCgL57IKvGoctb1bjLRjNyskfyOXxx2LwUwL65EttBmLlToJJyCmfdFB-0xdIvj2MQ0cA-YZqLB0TAiIbiBcnn9TuUrHtR3qWLMAa2K55d8ZpKnVvO7fki0iijcCiOGkAJWAnkhvz46UglO3JZ9IsgfdDHiKKQeGzjB7BI9NTt2uqI9JX55f4acEcI5bwju3mm5HLg6LOECdhukAeJWJLsxXMYr7kAu1')" }}>
                <div className="absolute top-2 left-2 bg-surface/80 backdrop-blur px-2 py-1">
                  <span className="font-metadata text-[12px] text-primary uppercase tracking-widest">独家</span>
                </div>
              </div>
              <h4 className="font-body-main text-[16px] text-primary mb-1">Voyageur Weekender</h4>
              <p className="font-metadata text-[12px] text-on-surface-variant mb-2 line-clamp-1">防水帆布</p>
              <p className="font-price-tabular text-[18px] text-primary">¥ 12,200</p>
            </article>
          </div>
        </section>

        <hr className="border-t border-hairline w-full" />

        {/* 顾问模块 (深炭黑) */}
        <section className="bg-charcoal text-pure-white p-8 relative overflow-hidden flex flex-col items-center justify-between">
          <div className="relative z-10 w-full mb-8">
            <h3 className="font-display-hero text-[38px] mb-4 tracking-tighter">私人顾问服务</h3>
            <p className="font-body-main text-[16px] text-surface-dim mb-8 max-w-sm">尊享一对一专属服务。我们的私人顾问随时为您解答差旅需求，提供低调且精准的推荐。</p>
            <button className="bg-pure-white text-primary font-label-ui text-[14px] px-6 py-3 rounded hover:bg-surface-dim transition-colors border border-[#E56A1D]">
              联系顾问
            </button>
          </div>
          <div className="relative z-10 w-full aspect-square bg-surface/10 rounded-sm overflow-hidden bg-cover bg-center" style={{ backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuAhM9LQsFBgXWPPE4J11BrRdLEApIux2PaZuy-1MiHeOh2Vohha9CfzE4Aofz2Za2B7rPXd_2LgxkpuZxuZoogOPhJhJe59uEPLKPNRvRgM04Sb_ZjyoHyXcR5h8E2A1oUgN1x6ZWU3iGsTGpKsHharFISf-oKM8X8shLH0kPmI4qd6xDA9EOFw7oOv9WfJDk_cO9fZBZheA6qBoCUbIH0CMjgpof2BPOtBF8_wIu2NU84y7wnLGMmv')" }}>
          </div>
        </section>
      </main>

      <BottomNav />
    </div>
  );
}
