import sys

content = """
import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function VisualSearch() {
  const navigate = useNavigate();

  return (
    <div className="bg-surface text-on-surface font-body-main antialiased min-h-screen flex flex-col items-center pb-[140px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button aria-label="Close" className="relative z-10 text-primary hover:opacity-80 transition-opacity p-2 -ml-2" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">close</span>
          </button>
          <span className="font-bold text-[16px] text-primary absolute left-1/2 -translate-x-1/2 pointer-events-none">视觉搜索</span>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="w-full mt-14 flex flex-col">
        <section className="relative w-full aspect-square bg-surface-container-highest flex items-center justify-center overflow-hidden">
          <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCK1r2hynCPyCQq9spEmeaKGffQN0Bj0F2sQorHjShShuWrdQSnCk5a1CXtWpl7U_l5vL7QpH2Vi4LRc8Sg6UXCgaXzx_vBRtmyHw92McNWEqJRX5YNMZNASekaMh38aziNL-FJI2vgntQhlHnh9V4jJXkjR9QBilqJ50uihZYta52a70uabfNFXFA6UQc1IZP4Dmq5ZtGI8XzpmzETE-TJIyjLR6imUGoI1rjpcI-GymrYsKR0_lB-" alt="Bag" />
          <div className="absolute inset-0 bg-black/40"></div>
          <div className="absolute top-[15%] left-[20%] w-[60%] h-[70%] border-2 border-pure-white/90 shadow-[0_0_0_9999px_rgba(0,0,0,0.6)] bg-transparent z-10 cursor-move rounded-lg">
            <div className="w-4 h-4 bg-pure-white rounded-full border border-primary absolute -top-2 -left-2 cursor-nwse-resize shadow-sm"></div>
            <div className="w-4 h-4 bg-pure-white rounded-full border border-primary absolute -top-2 -right-2 cursor-nesw-resize shadow-sm"></div>
            <div className="w-4 h-4 bg-pure-white rounded-full border border-primary absolute -bottom-2 -left-2 cursor-nesw-resize shadow-sm"></div>
            <div className="w-4 h-4 bg-pure-white rounded-full border border-primary absolute -bottom-2 -right-2 cursor-nwse-resize shadow-sm"></div>
          </div>
          <div className="absolute bottom-4 right-4 flex gap-2 z-20">
            <button className="w-10 h-10 rounded-full bg-pure-white/90 backdrop-blur shadow-sm flex items-center justify-center text-primary active:bg-pure-white">
              <span className="material-symbols-outlined text-[20px]">crop</span>
            </button>
          </div>
        </section>

        <section className="px-5 py-6 flex flex-col gap-4 bg-pure-white">
          <div className="flex items-center gap-2">
            <span className="material-symbols-outlined text-primary text-[18px]">auto_awesome</span>
            <span className="font-bold text-[13px] text-primary">已识别属性</span>
          </div>
          <div className="flex flex-wrap gap-2">
            <span className="px-3 py-1.5 border border-hairline bg-surface-container-lowest text-[13px] text-primary rounded-full flex items-center gap-1 shadow-sm">
              手提包 <span className="material-symbols-outlined text-[14px] text-on-surface-variant">close</span>
            </span>
            <span className="px-3 py-1.5 border border-hairline bg-surface-container-lowest text-[13px] text-primary rounded-full flex items-center gap-1 shadow-sm">
              皮革 <span className="material-symbols-outlined text-[14px] text-on-surface-variant">close</span>
            </span>
            <span className="px-3 py-1.5 border border-hairline bg-surface-container-lowest text-[13px] text-primary rounded-full flex items-center gap-1 shadow-sm">
              米色 <span className="material-symbols-outlined text-[14px] text-on-surface-variant">close</span>
            </span>
            <button className="px-3 py-1.5 border border-dashed border-outline-variant text-[13px] text-on-surface-variant rounded-full flex items-center gap-1 hover:bg-surface-container-lowest">
              <span className="material-symbols-outlined text-[16px]">add</span> 添加标签
            </button>
          </div>
          <p className="text-[11px] text-on-surface-variant mt-2 flex items-center gap-1">
            <span className="material-symbols-outlined text-[14px]">info</span>
            视觉相似不代表同款，结果可能包含类似设计。
          </p>
        </section>
      </main>

      <div className="fixed bottom-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-pure-white border-t border-hairline px-4 py-3 flex flex-col gap-3 pb-safe shadow-[0_-4px_16px_rgba(0,0,0,0.04)]">
        <div className="relative w-full h-[44px] bg-surface-container-lowest border border-hairline rounded-full flex items-center px-4 focus-within:border-primary transition-colors shadow-inner">
          <span className="text-[12px] text-primary font-bold mr-2">AI</span>
          <input className="w-full bg-transparent border-none p-0 focus:ring-0 text-[13px] text-primary placeholder:text-outline-variant outline-none" placeholder="添加描述以缩小范围..." type="text" defaultValue="像这个，但要黑色、预算 2 万以内"/>
          <button className="ml-2 text-on-surface-variant hover:text-primary transition-colors">
            <span className="material-symbols-outlined text-[18px]">mic</span>
          </button>
        </div>
        <button onClick={() => navigate('/results')} className="w-full h-[44px] bg-charcoal text-pure-white font-bold text-[14px] rounded-full hover:bg-charcoal/90 transition-colors flex items-center justify-center gap-2 shadow-sm">
          查看相似商品
          <span className="material-symbols-outlined text-[18px]">arrow_forward</span>
        </button>
      </div>
    </div>
  );
}
"""
with open('src/pages/VisualSearch.tsx', 'w') as f:
    f.write(content)
