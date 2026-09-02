import React, { useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function IntentCanvas() {
  const navigate = useNavigate();
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Scroll to bottom on mount to simulate active chat
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, []);

  return (
    <div className="bg-[#F7F7F5] text-[#111111] font-sans antialiased h-screen flex flex-col overflow-hidden">
      {/* Header */}
      <header className="shrink-0 w-full z-50 bg-[#F7F7F5]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="max-w-[430px] mx-auto relative flex justify-between items-center px-4 h-14">
          <button onClick={() => navigate(-1)} className="relative z-10 text-[#111111] hover:opacity-80 transition-opacity p-2 -ml-2">
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <div className="font-serif text-[16px] text-[#111111] flex items-center gap-1.5 absolute left-1/2 -translate-x-1/2 pointer-events-none uppercase tracking-widest">
            <span className="material-symbols-outlined text-[18px]">psychiatry</span> AI
          </div>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-[#111111] hover:opacity-80 transition-opacity p-2 -mr-2">
              <span className="material-symbols-outlined text-[22px]">more_horiz</span>
            </button>
          </div>
        </div>
      </header>

      {/* Chat Area */}
      <main className="flex-1 overflow-y-auto w-full hide-scrollbar scroll-smooth relative">
        <div className="max-w-[430px] mx-auto px-4 pt-6 pb-40 flex flex-col gap-6">
          
          <div className="text-center text-[11px] text-[#666663] font-mono mb-2 mt-2">
            TODAY 09:41 AM
          </div>

          {/* User Message */}
          <div className="flex justify-end w-full animate-in fade-in slide-in-from-bottom-2 duration-500">
            <div className="max-w-[85%] bg-[#111111] text-[#FFFFFF] p-3.5 rounded-sm text-[14px] leading-relaxed shadow-sm">
              下周去东京，找一个能装 13 英寸电脑、没有明显 Logo、预算 3 万以内的黑色包
            </div>
          </div>

          {/* AI Message */}
          <div className="flex flex-col items-start w-full animate-in fade-in slide-in-from-bottom-2 duration-500 delay-150 fill-mode-both">
            <div className="w-7 h-7 rounded-none bg-[#FFFFFF] border border-[#E4E3DE] flex items-center justify-center shrink-0 shadow-sm mb-2">
              <span className="material-symbols-outlined text-[16px] text-[#111111]">psychiatry</span>
            </div>
            
            <div className="bg-[#FFFFFF] border border-[#E4E3DE] py-4 rounded-sm shadow-sm w-full overflow-hidden">
              <p className="px-4 text-[14px] leading-relaxed mb-4 text-[#111111]">
                已为您筛选出 12 件符合要求的单品。提取属性：<br/>
                <span className="inline-flex items-center gap-1 text-[11px] font-mono bg-[#F7F7F5] px-1.5 py-0.5 mt-2 mr-2 border border-[#E4E3DE] rounded-sm">东京差旅</span>
                <span className="inline-flex items-center gap-1 text-[11px] font-mono bg-[#F7F7F5] px-1.5 py-0.5 mt-2 mr-2 border border-[#E4E3DE] rounded-sm">13英寸电脑</span>
                <span className="inline-flex items-center gap-1 text-[11px] font-mono bg-[#F7F7F5] px-1.5 py-0.5 mt-2 mr-2 border border-[#E4E3DE] rounded-sm">低Logo</span>
                <span className="inline-flex items-center gap-1 text-[11px] font-mono bg-[#F7F7F5] px-1.5 py-0.5 mt-2 mr-2 border border-[#E4E3DE] rounded-sm">黑色</span>
                <span className="inline-flex items-center gap-1 text-[11px] font-mono bg-[#F7F7F5] px-1.5 py-0.5 mt-2 border border-[#E4E3DE] rounded-sm">≤¥30,000</span>
              </p>

              {/* Rich Component: Product Carousel */}
              <div className="flex gap-3 overflow-x-auto hide-scrollbar pb-4 mb-2 px-4 snap-x">
                <div className="w-[140px] shrink-0 snap-center cursor-pointer group" onClick={() => navigate('/product')}>
                  <div className="w-full aspect-[4/5] bg-[#EFEFEB] rounded-sm overflow-hidden mb-2 relative">
                    <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Noir Tote" />
                    <div className="absolute top-1.5 left-1.5 bg-white/90 backdrop-blur px-1.5 py-0.5 text-[9px] font-medium text-[#111111] border border-[#E4E3DE] rounded-sm">极高匹配</div>
                  </div>
                  <h4 className="font-medium text-[12px] text-[#111111] truncate">Noir Signature Tote</h4>
                  <p className="text-[11px] text-[#666663] truncate">全粒面小牛皮</p>
                  <p className="font-mono text-[12px] text-[#111111] mt-0.5">¥8,500</p>
                </div>
                
                <div className="w-[140px] shrink-0 snap-center cursor-pointer group" onClick={() => navigate('/product')}>
                  <div className="w-full aspect-[4/5] bg-[#EFEFEB] rounded-sm overflow-hidden mb-2">
                    <img src="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&q=80&w=400" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Briefcase" />
                  </div>
                  <h4 className="font-medium text-[12px] text-[#111111] truncate">Leather Briefcase</h4>
                  <p className="text-[11px] text-[#666663] truncate">极简公文包</p>
                  <p className="font-mono text-[12px] text-[#111111] mt-0.5">¥6,800</p>
                </div>

                <div className="w-[140px] shrink-0 snap-center cursor-pointer group" onClick={() => navigate('/product')}>
                  <div className="w-full aspect-[4/5] bg-[#EFEFEB] rounded-sm overflow-hidden mb-2">
                    <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuALof-gjivI7JLbQxwFhG0FSCgL57IKvGoctb1bjLRjNyskfyOXxx2LwUwL65EttBmLlToJJyCmfdFB-0xdIvj2MQ0cA-YZqLB0TAiIbiBcnn9TuUrHtR3qWLMAa2K55d8ZpKnVvO7fki0iijcCiOGkAJWAnkhvz46UglO3JZ9IsgfdDHiKKQeGzjB7BI9NTt2uqI9JX55f4acEcI5bwju3mm5HLg6LOECdhukAeJWJLsxXMYr7kAu1" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Weekender" />
                  </div>
                  <h4 className="font-medium text-[12px] text-[#111111] truncate">Canvas Weekender</h4>
                  <p className="text-[11px] text-[#666663] truncate">防水涂层帆布</p>
                  <p className="font-mono text-[12px] text-[#111111] mt-0.5">¥12,200</p>
                </div>
              </div>

              <div className="w-full h-[1px] bg-[#E4E3DE] mb-4"></div>

              {/* Follow up actions */}
              <p className="px-4 text-[13px] text-[#111111] mb-3">为进一步缩小范围，您更看重：</p>
              <div className="px-4 flex flex-col gap-2">
                <button onClick={() => navigate('/results')} className="py-2.5 px-3 border border-[#E4E3DE] rounded-sm hover:bg-[#F7F7F5] transition-colors text-left flex justify-between items-center group">
                  <span className="text-[13px] text-[#111111]">极致轻便 (尼龙/帆布)</span>
                  <span className="material-symbols-outlined text-[16px] text-[#666663] group-hover:text-[#111111]">arrow_forward</span>
                </button>
                <button onClick={() => navigate('/results')} className="py-2.5 px-3 border border-[#E4E3DE] rounded-sm hover:bg-[#F7F7F5] transition-colors text-left flex justify-between items-center group">
                  <span className="text-[13px] text-[#111111]">商务正式 (全皮质)</span>
                  <span className="material-symbols-outlined text-[16px] text-[#666663] group-hover:text-[#111111]">arrow_forward</span>
                </button>
              </div>
            </div>
          </div>
          
          <div ref={messagesEndRef} />
        </div>
      </main>

      {/* Input Area (Bottom Fixed) */}
      <div className="absolute bottom-0 left-0 right-0 z-50 bg-[#F7F7F5]/90 backdrop-blur-xl border-t border-[#E4E3DE]">
        <div className="max-w-[430px] mx-auto px-4 py-3 pb-safe">
          <div className="flex items-end gap-1.5 bg-[#FFFFFF] border border-[#E4E3DE] rounded-sm p-1.5 shadow-sm focus-within:border-[#111111] transition-colors">
            <button className="p-1.5 pb-2 pl-2 text-[#666663] hover:text-[#111111] transition-colors shrink-0 flex items-center justify-center" onClick={() => navigate('/visual-search')}>
              <span className="material-symbols-outlined text-[18px] font-light">add_photo_alternate</span>
            </button>
            <textarea 
              className="flex-1 bg-transparent border-none p-0 py-2 focus:ring-0 resize-none font-sans text-[14px] leading-relaxed text-[#111111] placeholder:text-[#666663] outline-none max-h-[100px] min-h-[36px]"
              placeholder="回复 AI..."
              rows={1}
            />
            <div className="flex items-center shrink-0 pb-0.5 pr-0.5">
              <button onClick={() => navigate('/results')} className="w-8 h-8 rounded-sm bg-[#111111] text-[#FFFFFF] flex items-center justify-center hover:opacity-90 transition-opacity">
                <span className="material-symbols-outlined text-[18px]">arrow_upward</span>
              </button>
            </div>
          </div>
          <div className="text-center mt-2">
            <p className="text-[10px] text-[#666663]">AI 助手可能会犯错，请核实重要信息。</p>
          </div>
        </div>
      </div>
    </div>
  );
}
