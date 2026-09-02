
import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function PrivateCuration() {
  const navigate = useNavigate();

  return (
    <div className="font-sans antialiased pb-10 pt-14 bg-[#F7F7F5] text-[#111111] min-h-screen">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#F7F7F5]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center text-[#111111] hover:opacity-80 transition-opacity cursor-pointer p-2 -ml-2" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <div className="font-serif text-[18px] tracking-widest text-[#111111] absolute left-1/2 -translate-x-1/2 pointer-events-none uppercase">Private</div>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="flex items-center text-[#111111] hover:opacity-80 transition-opacity cursor-pointer p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
          </div>
        </div>
      </header>

      <main className="w-full mx-auto px-4 mt-6">
        <div className="mb-10">
          <h1 className="font-serif text-[28px] text-[#111111] mb-2">私人精选</h1>
          <p className="text-[13px] text-[#666663]">
            基于您的风格偏好为您生成的专属推荐
          </p>
        </div>

        <section className="mb-10">
          <div className="flex justify-between items-end mb-4 border-b border-[#E4E3DE] pb-2">
            <h2 className="font-serif text-[20px] text-[#111111]">需要关注</h2>
            <span className="text-[11px] text-[#666663] uppercase tracking-widest">2 Items</span>
          </div>
          
          <div className="grid grid-cols-1 gap-3">
            <div className="bg-[#FFFFFF] p-4 rounded-sm relative group border border-[#E4E3DE] shadow-sm">
              <div className="absolute top-0 right-0 p-3">
                <span className="bg-[#111111] text-[#FFFFFF] text-[10px] px-2 py-1 uppercase tracking-widest rounded-sm">Restock / 补货</span>
              </div>
              <div className="flex items-center mb-4 mt-2">
                <div className="w-16 h-20 mr-4 bg-[#EFEFEB] rounded-sm overflow-hidden">
                  <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAYlN6lKjDkSkgpox5C6K4wTG7J7VkP_56-6EEM6QlC8vUdE_eM8V_q7TIZ1-E1ZwOS7vM2yNTqqT-Lsdta6WnzOjDm79xqhUY0UhATTVYH0V18ILrl2HS1xndkT_eIRFYxWl1CgzNOME7zvciMiHprw2wh6MqNKMyQyGYQIWzwftqLCLTezXcmv3dxSMV560Q3bh0X2sRCDbmKusXzfRG10lZ9RgOzUvm8-PZGKD713IJ3So0LNJx9" alt="Tote" />
                </div>
                <div>
                  <h3 className="font-medium text-[14px] text-[#111111] mb-1">经典皮革托特包</h3>
                  <p className="text-[12px] text-[#666663]">您收藏的颜色已补货</p>
                </div>
              </div>
              <button className="w-full border border-[#111111] bg-[#111111] text-white rounded-sm text-[13px] py-2.5 hover:bg-[#111111]/90 transition-colors">立即购买</button>
            </div>
          </div>
        </section>

        <section className="mb-6">
          <div className="flex justify-between items-end mb-4 border-b border-[#E4E3DE] pb-2">
            <h2 className="font-serif text-[20px] text-[#111111]">为您上新</h2>
          </div>
          
          <div className="grid grid-cols-1 gap-6">
            <div className="flex flex-col group cursor-pointer bg-[#FFFFFF] rounded-sm overflow-hidden border border-[#E4E3DE] pb-4" onClick={() => navigate('/product')}>
              <div className="aspect-[4/5] overflow-hidden mb-4 bg-[#EFEFEB] relative">
                <div className="absolute top-3 left-3 z-20 bg-white/90 backdrop-blur px-2 py-0.5 rounded-sm border border-[#E56A1D]">
                  <p className="text-[10px] text-[#E56A1D] uppercase font-bold tracking-widest">会员优先购</p>
                </div>
                <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBvnjeXrTvdYdonVeWiBW2XxNehwXQK9uPnKt9guDDZ-yk9krbCF8FcYd-WWKD3BKwer-6XhpgLl84wjh3v7JvQ_cc9ntccBLss0iY528pIKCwNOspqzUWfi98TB5xn7OHwa11B-OWzAgYBvGSddpB8_7a4JfdwDeSYqFF1weToskJXdVtP_upiP9YKtTotLxQ0Q_DzoqT8uIrxHtUjr_z4I_52OF6ArsLBrPm2auc6lMZPQE0Qr4Vy" alt="Model" />
                <div className="absolute bottom-3 left-3 right-3 z-20 bg-white/95 backdrop-blur px-3 py-2 rounded-sm border border-[#E4E3DE]">
                  <p className="text-[12px] text-[#111111] flex items-start">
                    <span className="material-symbols-outlined text-[16px] mr-1 mt-0.5">auto_awesome</span> 
                    <span><strong className="font-medium">推荐理由：</strong>符合您偏好的大地色系，且轮廓与您收藏过的多款风衣高度一致。</span>
                  </p>
                </div>
              </div>
              <div className="flex justify-between items-start px-4">
                <div>
                  <h3 className="font-medium text-[15px] text-[#111111]">定制羊毛大衣</h3>
                  <p className="text-[12px] text-[#666663] mt-1 uppercase tracking-widest">AW26 秋冬系列</p>
                </div>
                <span className="font-mono text-[15px] text-[#111111] font-medium">¥ 8,500</span>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
