import sys

content = """
import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function PrivateCuration() {
  const navigate = useNavigate();

  return (
    <div className="font-body-main antialiased pb-10 pt-16 bg-background text-on-surface min-h-screen">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center text-primary hover:opacity-80 transition-opacity cursor-pointer p-2 -ml-2" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <div className="font-bold text-[18px] tracking-tight text-primary absolute left-1/2 -translate-x-1/2 pointer-events-none">私人精选</div>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="flex items-center text-primary hover:opacity-80 transition-opacity cursor-pointer p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="w-full mx-auto px-4 mt-6">
        <div className="mb-8">
          <p className="font-bold text-[12px] text-primary flex items-center mb-1">
            <span className="material-symbols-outlined text-[14px] mr-1">auto_awesome</span> AI Curated For You
          </p>
          <p className="text-[13px] text-on-surface-variant">
            基于您的风格偏好为您生成的专属推荐
          </p>
        </div>

        <section className="mb-6">
          <div className="flex justify-between items-end mb-4 border-b border-hairline pb-2">
            <h2 className="font-bold text-[16px] text-primary">需要关注</h2>
            <span className="text-[12px] text-on-surface-variant">2 件商品</span>
          </div>
          
          <div className="grid grid-cols-1 gap-3">
            <div className="bg-pure-white p-4 rounded-xl relative overflow-hidden group border border-hairline shadow-sm">
              <div className="absolute top-0 right-0 p-3">
                <span className="bg-primary text-pure-white text-[10px] px-2 py-1 uppercase rounded-sm">补货</span>
              </div>
              <div className="flex items-center mb-4">
                <div className="w-16 h-20 mr-4 bg-surface-container-lowest rounded-lg overflow-hidden">
                  <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAYlN6lKjDkSkgpox5C6K4wTG7J7VkP_56-6EEM6QlC8vUdE_eM8V_q7TIZ1-E1ZwOS7vM2yNTqqT-Lsdta6WnzOjDm79xqhUY0UhATTVYH0V18ILrl2HS1xndkT_eIRFYxWl1CgzNOME7zvciMiHprw2wh6MqNKMyQyGYQIWzwftqLCLTezXcmv3dxSMV560Q3bh0X2sRCDbmKusXzfRG10lZ9RgOzUvm8-PZGKD713IJ3So0LNJx9" alt="Tote" />
                </div>
                <div>
                  <h3 className="font-bold text-[14px] text-primary mb-1">经典皮革托特包</h3>
                  <p className="text-[12px] text-on-surface-variant">您收藏的颜色已补货</p>
                </div>
              </div>
              <button className="w-full border border-hairline rounded-lg text-primary font-bold text-[13px] py-2.5 hover:bg-surface transition-colors">立即购买</button>
            </div>
          </div>
        </section>

        <section className="mb-6">
          <div className="flex justify-between items-end mb-4 border-b border-hairline pb-2">
            <h2 className="font-bold text-[16px] text-primary">为您推荐</h2>
          </div>
          
          <div className="grid grid-cols-1 gap-4">
            <div className="flex flex-col group cursor-pointer bg-pure-white rounded-xl overflow-hidden shadow-sm border border-hairline pb-3" onClick={() => navigate('/product')}>
              <div className="aspect-[4/3] overflow-hidden mb-3 bg-surface-container-lowest relative">
                <div className="absolute top-3 left-3 z-20 bg-white/90 backdrop-blur px-2 py-0.5 rounded border border-[#E56A1D]">
                  <p className="text-[10px] text-[#E56A1D] uppercase font-bold">会员优先购</p>
                </div>
                <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBvnjeXrTvdYdonVeWiBW2XxNehwXQK9uPnKt9guDDZ-yk9krbCF8FcYd-WWKD3BKwer-6XhpgLl84wjh3v7JvQ_cc9ntccBLss0iY528pIKCwNOspqzUWfi98TB5xn7OHwa11B-OWzAgYBvGSddpB8_7a4JfdwDeSYqFF1weToskJXdVtP_upiP9YKtTotLxQ0Q_DzoqT8uIrxHtUjr_z4I_52OF6ArsLBrPm2auc6lMZPQE0Qr4Vy" alt="Model" />
                <div className="absolute bottom-3 left-3 z-20 bg-white/90 backdrop-blur px-2.5 py-1.5 rounded-md border border-hairline">
                  <p className="text-[11px] text-primary flex items-center font-medium">
                    <span className="material-symbols-outlined text-[13px] mr-1">auto_awesome</span> 符合你的偏好
                  </p>
                </div>
              </div>
              <div className="flex justify-between items-start px-3">
                <div>
                  <h3 className="font-bold text-[15px] text-primary">定制羊毛大衣</h3>
                  <p className="text-[12px] text-on-surface-variant mt-0.5">秋冬系列</p>
                </div>
                <span className="font-semibold text-[15px] text-primary">¥ 8,500</span>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
"""
with open('src/pages/PrivateCuration.tsx', 'w') as f:
    f.write(content)
