
import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function VisualSearch() {
  const navigate = useNavigate();

  return (
    <div className="bg-[#111111] text-[#F7F7F5] font-sans antialiased min-h-screen flex flex-col items-center pb-[140px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#111111]/90 backdrop-blur-xl border-b border-white/10">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button aria-label="Close" className="relative z-10 text-[#F7F7F5] hover:opacity-80 transition-opacity p-2 -ml-2" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">close</span>
          </button>
          <span className="font-serif text-[16px] text-[#F7F7F5] absolute left-1/2 -translate-x-1/2 pointer-events-none tracking-widest uppercase">Visual Search</span>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <div className="w-[87px] h-[32px] shrink-0 rounded-none border border-white/20 flex items-center justify-between px-3 bg-white/5 backdrop-blur-md">
              <span className="material-symbols-outlined text-[18px] text-[#F7F7F5]">more_horiz</span>
              <div className="w-[1px] h-4 bg-white/20"></div>
              <span className="material-symbols-outlined text-[16px] text-[#F7F7F5]">radio_button_unchecked</span>
            </div>
          </div>
        </div>
      </header>

      <main className="w-full mt-14 flex flex-col">
        <section className="relative w-full aspect-square bg-[#242424] flex items-center justify-center overflow-hidden">
          <img className="w-full h-full object-cover opacity-90" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCK1r2hynCPyCQq9spEmeaKGffQN0Bj0F2sQorHjShShuWrdQSnCk5a1CXtWpl7U_l5vL7QpH2Vi4LRc8Sg6UXCgaXzx_vBRtmyHw92McNWEqJRX5YNMZNASekaMh38aziNL-FJI2vgntQhlHnh9V4jJXkjR9QBilqJ50uihZYta52a70uabfNFXFA6UQc1IZP4Dmq5ZtGI8XzpmzETE-TJIyjLR6imUGoI1rjpcI-GymrYsKR0_lB-" alt="Bag" />
          <div className="absolute inset-0 bg-black/40"></div>
          <div className="absolute top-[15%] left-[20%] w-[60%] h-[70%] border border-[#F7F7F5]/80 shadow-[0_0_0_9999px_rgba(0,0,0,0.7)] bg-transparent z-10 cursor-move rounded-sm">
            <div className="w-3 h-3 bg-[#F7F7F5] border border-[#111111] absolute -top-1.5 -left-1.5 cursor-nwse-resize shadow-sm rounded-sm"></div>
            <div className="w-3 h-3 bg-[#F7F7F5] border border-[#111111] absolute -top-1.5 -right-1.5 cursor-nesw-resize shadow-sm rounded-sm"></div>
            <div className="w-3 h-3 bg-[#F7F7F5] border border-[#111111] absolute -bottom-1.5 -left-1.5 cursor-nesw-resize shadow-sm rounded-sm"></div>
            <div className="w-3 h-3 bg-[#F7F7F5] border border-[#111111] absolute -bottom-1.5 -right-1.5 cursor-nwse-resize shadow-sm rounded-sm"></div>
          </div>
          <div className="absolute bottom-4 right-4 flex gap-2 z-20">
            <button className="w-10 h-10 rounded-sm bg-[#FFFFFF]/10 border border-white/20 backdrop-blur shadow-sm flex items-center justify-center text-[#F7F7F5] hover:bg-[#FFFFFF]/20 transition-colors">
              <span className="material-symbols-outlined text-[20px] font-light">crop</span>
            </button>
          </div>
        </section>

        <section className="px-5 py-6 flex flex-col gap-4 bg-[#111111] border-t border-white/10">
          <div className="flex items-center gap-2">
            <span className="material-symbols-outlined text-[#F7F7F5] text-[18px]">auto_awesome</span>
            <span className="font-medium text-[13px] text-[#F7F7F5]">已识别属性</span>
          </div>
          <div className="flex flex-wrap gap-2">
            <span className="px-3 py-1.5 border border-white/20 bg-white/5 text-[13px] text-[#F7F7F5] rounded-sm flex items-center gap-1">
              手提包 <span className="material-symbols-outlined text-[14px] text-white/60">close</span>
            </span>
            <span className="px-3 py-1.5 border border-white/20 bg-white/5 text-[13px] text-[#F7F7F5] rounded-sm flex items-center gap-1">
              皮革 <span className="material-symbols-outlined text-[14px] text-white/60">close</span>
            </span>
            <span className="px-3 py-1.5 border border-white/20 bg-white/5 text-[13px] text-[#F7F7F5] rounded-sm flex items-center gap-1">
              米色 <span className="material-symbols-outlined text-[14px] text-white/60">close</span>
            </span>
            <button className="px-3 py-1.5 border border-dashed border-white/30 text-[13px] text-white/60 rounded-sm flex items-center gap-1 hover:bg-white/5">
              <span className="material-symbols-outlined text-[16px]">add</span> 添加标签
            </button>
          </div>
          <p className="text-[11px] text-white/50 mt-2 flex items-center gap-1">
            <span className="material-symbols-outlined text-[14px]">info</span>
            视觉相似不代表同款，结果可能包含类似设计。
          </p>
        </section>
      </main>

      <div className="fixed bottom-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#111111]/95 backdrop-blur-xl border-t border-white/10 px-4 py-4 flex flex-col gap-3 pb-safe">
        <div className="relative w-full h-[48px] bg-white/5 border border-white/20 rounded-sm flex items-center px-4 focus-within:border-white/40 transition-colors">
          <span className="text-[12px] text-[#F7F7F5] font-bold mr-3 uppercase tracking-widest">AI</span>
          <input className="w-full bg-transparent border-none p-0 pr-2 focus:ring-0 text-[14px] text-[#F7F7F5] placeholder:text-white/40 outline-none font-light" placeholder="添加描述以缩小范围..." type="text" defaultValue="像这个，但要黑色、预算 2 万以内"/>
        </div>
        <button onClick={() => navigate('/results')} className="w-full h-[48px] bg-[#F7F7F5] text-[#111111] font-medium text-[14px] rounded-sm hover:bg-[#F7F7F5]/90 transition-colors flex items-center justify-center gap-2">
          查看相似商品
          <span className="material-symbols-outlined text-[18px]">arrow_forward</span>
        </button>
      </div>
    </div>
  );
}
