import sys

content = """
import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function DynamicResults() {
  const navigate = useNavigate();

  return (
    <div className="bg-surface text-on-surface antialiased font-body-main min-h-screen pb-[120px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="flex flex-col px-4 pt-2 pb-1 w-full">
          <div className="relative flex justify-between items-center mb-2 h-10">
            <button onClick={() => navigate(-1)} className="relative z-10 text-primary hover:opacity-80 transition-opacity p-2 -ml-2">
              <span className="material-symbols-outlined text-[24px]">arrow_back</span>
            </button>
            <div className="font-bold text-[18px] tracking-tight text-primary absolute left-1/2 -translate-x-1/2 pointer-events-none">意图找货结果</div>
            <div className="relative z-10 flex items-center shrink-0">
              <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
            </div>
          </div>
          <div className="flex items-center gap-2 overflow-x-auto hide-scrollbar pb-1">
            <span className="px-3 py-1 bg-surface-container-lowest rounded-full border border-hairline text-[11px] text-primary whitespace-nowrap shadow-sm">商务差旅</span>
            <span className="px-3 py-1 bg-surface-container-lowest rounded-full border border-hairline text-[11px] text-primary whitespace-nowrap shadow-sm">低调</span>
            <span className="px-3 py-1 bg-surface-container-lowest rounded-full border border-hairline text-[11px] text-primary whitespace-nowrap shadow-sm">能装电脑</span>
          </div>
        </div>
      </header>

      <main className="pt-24 px-4 w-full">
        <div className="mb-6 px-1">
          <h1 className="font-bold text-[20px] text-primary mb-1">最符合您的 2 件单品</h1>
          <p className="text-[13px] text-on-surface-variant">基于您的差旅需求及偏好为您挑选。</p>
        </div>

        <div className="grid grid-cols-1 gap-5">
          <div className="group flex flex-col gap-3 bg-pure-white rounded-xl p-3 shadow-sm border border-hairline cursor-pointer" onClick={() => navigate('/product')}>
            <div className="aspect-[4/3] relative overflow-hidden bg-surface-container-lowest rounded-lg">
              <img className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw" alt="Tote" />
              <div className="absolute top-2 left-2 px-2 py-1 bg-white/90 backdrop-blur-sm border border-hairline rounded font-bold text-[10px] text-primary uppercase">极高匹配度</div>
            </div>
            
            <div className="flex flex-col gap-1 px-1">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="font-bold text-[16px] text-primary">Noir Signature Tote</h3>
                  <p className="text-[11px] text-on-surface-variant mt-0.5">全粒面小牛皮</p>
                </div>
                <span className="font-semibold text-[16px] text-primary">¥8,500</span>
              </div>
              <div className="mt-2 p-3 bg-surface-container-lowest rounded-lg border border-hairline">
                <p className="text-[12px] text-on-surface-variant leading-relaxed">
                  <strong className="text-primary font-bold">为何推荐：</strong>无 Logo 设计符合您的低调要求；内部结构自带加厚电脑隔层，是商务通勤的完美选择。
                </p>
              </div>
            </div>
          </div>

          <div className="group flex flex-col gap-3 bg-pure-white rounded-xl p-3 shadow-sm border border-hairline cursor-pointer" onClick={() => navigate('/product')}>
            <div className="aspect-[4/3] relative overflow-hidden bg-surface-container-lowest rounded-lg">
              <img className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuALof-gjivI7JLbQxwFhG0FSCgL57IKvGoctb1bjLRjNyskfyOXxx2LwUwL65EttBmLlToJJyCmfdFB-0xdIvj2MQ0cA-YZqLB0TAiIbiBcnn9TuUrHtR3qWLMAa2K55d8ZpKnVvO7fki0iijcCiOGkAJWAnkhvz46UglO3JZ9IsgfdDHiKKQeGzjB7BI9NTt2uqI9JX55f4acEcI5bwju3mm5HLg6LOECdhukAeJWJLsxXMYr7kAu1" alt="Weekender" />
            </div>
            
            <div className="flex flex-col gap-1 px-1">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="font-bold text-[16px] text-primary">Voyageur Weekender</h3>
                  <p className="text-[11px] text-on-surface-variant mt-0.5">防水涂层帆布</p>
                </div>
                <span className="font-semibold text-[16px] text-primary">¥12,200</span>
              </div>
              <div className="mt-2 p-3 bg-surface-container-lowest rounded-lg border border-hairline">
                <p className="text-[12px] text-on-surface-variant leading-relaxed">
                  <strong className="text-primary font-bold">为何推荐：</strong>若差旅包含短途过夜，此款包不仅能装下电脑，还能轻松收纳一到两天的换洗衣物，外层防泼水。
                </p>
              </div>
            </div>
          </div>
        </div>
        
        <div className="mt-8 flex justify-center mb-4">
            <button onClick={() => navigate('/compare')} className="px-6 py-2 border border-outline-variant text-primary font-bold text-[13px] hover:bg-surface-container-lowest transition-colors rounded-full shadow-sm">对比这两件单品</button>
        </div>
      </main>

      <div className="fixed bottom-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-40 bg-pure-white border-t border-hairline pb-safe px-4 py-3 shadow-[0_-4px_16px_rgba(0,0,0,0.04)]">
        <div className="relative flex items-center bg-surface-container-lowest border border-hairline h-[44px] rounded-full shadow-inner px-4 focus-within:border-primary transition-colors">
          <span className="text-[12px] text-primary font-bold mr-2">AI</span>
          <input className="flex-1 bg-transparent border-none focus:ring-0 text-[13px] text-primary placeholder:text-outline-variant p-0 h-full outline-none" placeholder="继续说：第二个太大..." type="text" />
          <button className="text-on-surface-variant hover:text-primary transition-colors ml-2">
            <span className="material-symbols-outlined text-[18px]">arrow_upward</span>
          </button>
        </div>
      </div>
    </div>
  );
}
"""
with open('src/pages/DynamicResults.tsx', 'w') as f:
    f.write(content)
