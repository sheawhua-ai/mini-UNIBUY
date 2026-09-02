import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function PrivateCuration() {
  const navigate = useNavigate();

  return (
    <div className="font-body-main antialiased pb-[100px] pt-[80px] bg-background text-on-surface min-h-screen">
      <header className="fixed top-0 left-0 w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full max-w-7xl mx-auto">
          <button className="relative z-10 flex items-center text-primary hover:opacity-80 transition-opacity cursor-pointer p-2 -ml-2" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <div className="font-display-hero text-[22px] tracking-tighter text-primary font-bold absolute left-1/2 -translate-x-1/2 pointer-events-none">UNIBUY</div>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="flex items-center text-primary hover:opacity-80 transition-opacity cursor-pointer p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="max-w-[1200px] mx-auto px-5 mt-6">
        <div className="mb-16">
          <h1 className="font-headline-lg-mobile text-[26px] text-primary mb-2">私人精选</h1>
          <p className="font-metadata text-[12px] text-on-surface-variant flex items-center">
            <span className="material-symbols-outlined text-[16px] mr-1">bolt</span> AI curated for you
          </p>
        </div>

        <section className="mb-[24px]">
          <div className="flex justify-between items-end mb-6 border-b border-hairline pb-2">
            <h2 className="font-section-title text-[24px] text-primary">需要关注</h2>
            <span className="font-metadata text-[12px] text-on-surface-variant">2 items</span>
          </div>
          <div className="grid grid-cols-1 gap-3">
            <div className="bg-surface-container-low p-6 rounded relative overflow-hidden group border border-hairline">
              <div className="absolute top-0 right-0 p-4">
                <span className="bg-primary text-pure-white font-metadata text-[12px] px-2 py-1 uppercase tracking-wider">补货</span>
              </div>
              <div className="flex items-center mb-4">
                <div className="w-16 h-20 mr-4 bg-mist rounded overflow-hidden">
                  <img className="w-full h-full object-cover grayscale opacity-80" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAYlN6lKjDkSkgpox5C6K4wTG7J7VkP_56-6EEM6QlC8vUdE_eM8V_q7TIZ1-E1ZwOS7vM2yNTqqT-Lsdta6WnzOjDm79xqhUY0UhATTVYH0V18ILrl2HS1xndkT_eIRFYxWl1CgzNOME7zvciMiHprw2wh6MqNKMyQyGYQIWzwftqLCLTezXcmv3dxSMV560Q3bh0X2sRCDbmKusXzfRG10lZ9RgOzUvm8-PZGKD713IJ3So0LNJx9" alt="Tote" />
                </div>
                <div>
                  <h3 className="font-body-main text-[16px] text-primary mb-1">经典皮革托特包</h3>
                  <p className="font-metadata text-[12px] text-on-surface-variant">您收藏的颜色已补货。</p>
                </div>
              </div>
              <button className="w-full border border-hairline text-primary font-label-ui text-[14px] py-3 hover:bg-mist transition-colors">立即购买</button>
            </div>
          </div>
        </section>

        <section className="mb-[24px]">
          <div className="flex justify-between items-end mb-6 border-b border-hairline pb-2">
            <h2 className="font-section-title text-[24px] text-primary">为你上新</h2>
          </div>
          <div className="grid grid-cols-1 gap-4">
            <div className="flex flex-col group cursor-pointer" onClick={() => navigate('/product')}>
              <div className="aspect-[4/5] overflow-hidden mb-4 bg-mist relative">
                <div className="absolute top-4 right-4 z-20 bg-surface/90 backdrop-blur px-2 py-1 border border-[#E56A1D]">
                  <p className="font-metadata text-[12px] text-[#E56A1D] uppercase tracking-wider">会员优先购</p>
                </div>
                <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBvnjeXrTvdYdonVeWiBW2XxNehwXQK9uPnKt9guDDZ-yk9krbCF8FcYd-WWKD3BKwer-6XhpgLl84wjh3v7JvQ_cc9ntccBLss0iY528pIKCwNOspqzUWfi98TB5xn7OHwa11B-OWzAgYBvGSddpB8_7a4JfdwDeSYqFF1weToskJXdVtP_upiP9YKtTotLxQ0Q_DzoqT8uIrxHtUjr_z4I_52OF6ArsLBrPm2auc6lMZPQE0Qr4Vy" alt="Model" />
                <div className="absolute bottom-4 left-4 z-20 bg-surface/90 backdrop-blur px-3 py-2 border border-hairline">
                  <p className="font-metadata text-[12px] text-primary flex items-center">
                    <span className="material-symbols-outlined text-[14px] mr-1">auto_awesome</span> 符合你收藏过的轮廓
                  </p>
                </div>
              </div>
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="font-body-main text-[16px] text-primary">定制羊毛大衣</h3>
                  <p className="font-metadata text-[12px] text-on-surface-variant mt-1">秋冬系列</p>
                </div>
                <span className="font-price-tabular text-[18px] text-primary">¥ 8,500</span>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
