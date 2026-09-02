import sys

results_content = """
import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function DynamicResults() {
  const navigate = useNavigate();

  return (
    <div className="bg-[#F7F7F5] text-[#111111] antialiased font-sans min-h-screen pb-[120px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#F7F7F5]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="flex flex-col px-4 pt-2 pb-1 w-full">
          <div className="relative flex justify-between items-center mb-2 h-10">
            <button onClick={() => navigate(-1)} className="relative z-10 text-[#111111] hover:opacity-80 transition-opacity p-2 -ml-2">
              <span className="material-symbols-outlined text-[24px]">arrow_back</span>
            </button>
            <div className="font-serif text-[18px] tracking-widest text-[#111111] absolute left-1/2 -translate-x-1/2 pointer-events-none uppercase">RESULTS</div>
            <div className="relative z-10 flex items-center shrink-0">
              <div className="w-[87px] h-[32px] shrink-0 rounded-none border border-[#E4E3DE] flex items-center justify-between px-3 bg-[#FFFFFF]/50 backdrop-blur-md">
                <span className="material-symbols-outlined text-[18px] text-[#111111]">more_horiz</span>
                <div className="w-[1px] h-4 bg-[#E4E3DE]"></div>
                <span className="material-symbols-outlined text-[16px] text-[#111111]">radio_button_unchecked</span>
              </div>
            </div>
          </div>
          <div className="flex items-center gap-2 overflow-x-auto hide-scrollbar pb-1">
            <span className="px-3 py-1 bg-[#FFFFFF] rounded-sm border border-[#E4E3DE] text-[11px] text-[#111111] whitespace-nowrap shadow-sm">商务差旅</span>
            <span className="px-3 py-1 bg-[#FFFFFF] rounded-sm border border-[#E4E3DE] text-[11px] text-[#111111] whitespace-nowrap shadow-sm">低调</span>
            <span className="px-3 py-1 bg-[#FFFFFF] rounded-sm border border-[#E4E3DE] text-[11px] text-[#111111] whitespace-nowrap shadow-sm">能装电脑</span>
          </div>
        </div>
      </header>

      <main className="pt-24 px-4 w-full">
        <div className="mb-6 px-1">
          <h1 className="font-serif text-[20px] text-[#111111] mb-1">最符合您的 2 件单品</h1>
          <p className="text-[13px] text-[#666663]">基于您的差旅需求及偏好为您挑选。</p>
        </div>

        <div className="grid grid-cols-1 gap-5">
          <div className="group flex flex-col gap-3 bg-[#FFFFFF] rounded-sm p-3 shadow-[0_2px_8px_rgba(0,0,0,0.04)] border border-[#E4E3DE] cursor-pointer" onClick={() => navigate('/product')}>
            <div className="aspect-[4/3] relative overflow-hidden bg-[#EFEFEB] rounded-sm">
              <img className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw" alt="Tote" />
              <div className="absolute top-2 left-2 px-2 py-1 bg-white/90 backdrop-blur-sm border border-[#E4E3DE] rounded-sm font-medium text-[10px] text-[#111111] uppercase tracking-widest">极高匹配度</div>
            </div>
            
            <div className="flex flex-col gap-1 px-1">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="font-medium text-[15px] text-[#111111]">Noir Signature Tote</h3>
                  <p className="text-[11px] text-[#666663] mt-0.5">全粒面小牛皮</p>
                </div>
                <span className="font-mono text-[16px] font-medium text-[#111111]">¥8,500</span>
              </div>
              <div className="mt-2 p-3 bg-[#F7F7F5] rounded-sm border border-[#E4E3DE]">
                <p className="text-[12px] text-[#666663] leading-relaxed">
                  <strong className="text-[#111111] font-medium">为何推荐：</strong>无 Logo 设计符合您的低调要求；内部结构自带加厚电脑隔层，是商务通勤的完美选择。
                </p>
              </div>
            </div>
          </div>

          <div className="group flex flex-col gap-3 bg-[#FFFFFF] rounded-sm p-3 shadow-[0_2px_8px_rgba(0,0,0,0.04)] border border-[#E4E3DE] cursor-pointer" onClick={() => navigate('/product')}>
            <div className="aspect-[4/3] relative overflow-hidden bg-[#EFEFEB] rounded-sm">
              <img className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuALof-gjivI7JLbQxwFhG0FSCgL57IKvGoctb1bjLRjNyskfyOXxx2LwUwL65EttBmLlToJJyCmfdFB-0xdIvj2MQ0cA-YZqLB0TAiIbiBcnn9TuUrHtR3qWLMAa2K55d8ZpKnVvO7fki0iijcCiOGkAJWAnkhvz46UglO3JZ9IsgfdDHiKKQeGzjB7BI9NTt2uqI9JX55f4acEcI5bwju3mm5HLg6LOECdhukAeJWJLsxXMYr7kAu1" alt="Weekender" />
            </div>
            
            <div className="flex flex-col gap-1 px-1">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="font-medium text-[15px] text-[#111111]">Voyageur Weekender</h3>
                  <p className="text-[11px] text-[#666663] mt-0.5">防水涂层帆布</p>
                </div>
                <span className="font-mono text-[16px] font-medium text-[#111111]">¥12,200</span>
              </div>
              <div className="mt-2 p-3 bg-[#F7F7F5] rounded-sm border border-[#E4E3DE]">
                <p className="text-[12px] text-[#666663] leading-relaxed">
                  <strong className="text-[#111111] font-medium">为何推荐：</strong>若差旅包含短途过夜，此款包不仅能装下电脑，还能轻松收纳一到两天的换洗衣物，外层防泼水。
                </p>
              </div>
            </div>
          </div>
        </div>
        
        <div className="mt-8 flex justify-center mb-4">
            <button onClick={() => navigate('/compare')} className="px-6 py-2 border border-[#E4E3DE] text-[#111111] font-medium text-[13px] hover:bg-[#EFEFEB] transition-colors rounded-sm shadow-sm">对比这两件单品</button>
        </div>
      </main>

      <div className="fixed bottom-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-40 bg-[#F7F7F5]/95 backdrop-blur-xl border-t border-[#E4E3DE] pb-safe px-4 py-3 shadow-[0_-4px_16px_rgba(0,0,0,0.04)]">
        <div className="relative flex items-center bg-[#FFFFFF] border border-[#E4E3DE] h-[48px] rounded-sm px-4 focus-within:border-[#111111] transition-colors shadow-sm">
          <span className="text-[12px] text-[#111111] font-bold mr-3 uppercase tracking-widest">AI</span>
          <input className="flex-1 bg-transparent border-none focus:ring-0 text-[14px] text-[#111111] placeholder:text-[#666663] p-0 h-full outline-none font-light" placeholder="继续说：第二个太大..." type="text" />
          <button className="text-[#666663] hover:text-[#111111] transition-colors ml-2">
            <span className="material-symbols-outlined text-[20px] font-light">arrow_upward</span>
          </button>
        </div>
      </div>
    </div>
  );
}
"""
with open('src/pages/DynamicResults.tsx', 'w') as f:
    f.write(results_content)
    
visual_content = """
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
          <input className="w-full bg-transparent border-none p-0 focus:ring-0 text-[14px] text-[#F7F7F5] placeholder:text-white/40 outline-none font-light" placeholder="添加描述以缩小范围..." type="text" defaultValue="像这个，但要黑色、预算 2 万以内"/>
          <button className="ml-2 text-white/60 hover:text-[#F7F7F5] transition-colors">
            <span className="material-symbols-outlined text-[20px] font-light">mic</span>
          </button>
        </div>
        <button onClick={() => navigate('/results')} className="w-full h-[48px] bg-[#F7F7F5] text-[#111111] font-medium text-[14px] rounded-sm hover:bg-[#F7F7F5]/90 transition-colors flex items-center justify-center gap-2">
          查看相似商品
          <span className="material-symbols-outlined text-[18px]">arrow_forward</span>
        </button>
      </div>
    </div>
  );
}
"""
with open('src/pages/VisualSearch.tsx', 'w') as f:
    f.write(visual_content)
