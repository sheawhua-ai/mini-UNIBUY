import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function VisualSearch() {
  const navigate = useNavigate();

  return (
    <div className="bg-surface text-on-surface font-body-main antialiased min-h-screen flex flex-col items-center pb-24">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full max-w-[1200px] mx-auto">
          <button aria-label="Close" className="relative z-10 text-primary hover:opacity-80 transition-opacity p-2 -ml-2" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">close</span>
          </button>
          <span className="font-label-ui text-[14px] text-on-surface-variant absolute left-1/2 -translate-x-1/2 pointer-events-none">视觉搜索</span>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="w-full max-w-[600px] mt-20 px-5 flex flex-col gap-8">
        <section className="relative w-full aspect-[4/5] bg-surface-container-highest flex items-center justify-center overflow-hidden">
          <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCK1r2hynCPyCQq9spEmeaKGffQN0Bj0F2sQorHjShShuWrdQSnCk5a1CXtWpl7U_l5vL7QpH2Vi4LRc8Sg6UXCgaXzx_vBRtmyHw92McNWEqJRX5YNMZNASekaMh38aziNL-FJI2vgntQhlHnh9V4jJXkjR9QBilqJ50uihZYta52a70uabfNFXFA6UQc1IZP4Dmq5ZtGI8XzpmzETE-TJIyjLR6imUGoI1rjpcI-GymrYsKR0_lB-" alt="Bag" />
          <div className="absolute inset-0 bg-black/40"></div>
          <div className="absolute top-1/4 left-[15%] w-[70%] h-1/2 border border-pure-white/80 shadow-[0_0_0_9999px_rgba(0,0,0,0.5)] bg-transparent z-10 cursor-move">
            <div className="w-3 h-3 bg-pure-white border border-primary absolute -top-1.5 -left-1.5 cursor-nwse-resize"></div>
            <div className="w-3 h-3 bg-pure-white border border-primary absolute -top-1.5 -right-1.5 cursor-nesw-resize"></div>
            <div className="w-3 h-3 bg-pure-white border border-primary absolute -bottom-1.5 -left-1.5 cursor-nesw-resize"></div>
            <div className="w-3 h-3 bg-pure-white border border-primary absolute -bottom-1.5 -right-1.5 cursor-nwse-resize"></div>
          </div>
          <div className="absolute bottom-4 right-4 flex gap-2 z-20">
            <button className="w-10 h-10 rounded-full bg-pure-white/90 backdrop-blur shadow-sm flex items-center justify-center text-primary">
              <span className="material-symbols-outlined text-[20px]">crop</span>
            </button>
          </div>
        </section>

        <section className="flex flex-col gap-4">
          <div className="flex items-center gap-2">
            <span className="material-symbols-outlined text-primary text-[18px] fill">auto_awesome</span>
            <span className="font-metadata text-[12px] text-on-surface-variant uppercase tracking-widest">已识别属性</span>
          </div>
          <div className="flex flex-wrap gap-2">
            <span className="px-4 py-2 border border-outline-variant bg-surface-container-lowest font-label-ui text-[14px] text-primary rounded-full flex items-center gap-1">
              手提包 <span className="material-symbols-outlined text-[14px] text-on-surface-variant">close</span>
            </span>
            <span className="px-4 py-2 border border-outline-variant bg-surface-container-lowest font-label-ui text-[14px] text-primary rounded-full flex items-center gap-1">
              皮革 <span className="material-symbols-outlined text-[14px] text-on-surface-variant">close</span>
            </span>
            <span className="px-4 py-2 border border-outline-variant bg-surface-container-lowest font-label-ui text-[14px] text-primary rounded-full flex items-center gap-1">
              米色 <span className="material-symbols-outlined text-[14px] text-on-surface-variant">close</span>
            </span>
            <button className="px-4 py-2 border border-dashed border-outline font-label-ui text-[14px] text-on-surface-variant rounded-full flex items-center gap-1">
              <span className="material-symbols-outlined text-[16px]">add</span> 添加标签
            </button>
          </div>
          <p className="font-metadata text-[12px] text-outline mt-2 flex items-center gap-1">
            <span className="material-symbols-outlined text-[14px]">info</span>
            视觉相似不代表同款，结果可能包含类似设计。
          </p>
        </section>
      </main>

      <div className="fixed bottom-0 w-full max-w-[600px] bg-surface/90 backdrop-blur-2xl border-t border-hairline px-5 py-4 pb-safe flex flex-col gap-4 z-40 absolute">
        <div className="relative w-full h-[52px] bg-pure-white border border-outline-variant rounded shadow-[0_4px_16px_rgba(0,0,0,0.04)] flex items-center px-4 focus-within:border-primary transition-colors">
          <span className="font-metadata text-[12px] text-primary font-bold mr-3">AI</span>
          <input className="w-full bg-transparent border-none p-0 focus:ring-0 font-body-main text-[16px] text-primary placeholder:text-outline outline-none" placeholder="添加描述以缩小范围..." type="text" defaultValue="像这个，但要黑色、不要链条、预算 2 万以内"/>
          <button className="ml-2 text-on-surface-variant hover:text-primary transition-colors">
            <span className="material-symbols-outlined">mic</span>
          </button>
        </div>
        <button onClick={() => navigate('/results')} className="w-full h-12 bg-primary text-pure-white font-label-ui text-[14px] rounded hover:bg-primary/90 transition-colors flex items-center justify-center gap-2">
          查看相似商品
          <span className="material-symbols-outlined text-[18px]">arrow_forward</span>
        </button>
      </div>
    </div>
  );
}
