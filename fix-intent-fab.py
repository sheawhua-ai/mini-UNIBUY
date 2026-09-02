import os

# 1. Update AIFab.tsx
with open('src/components/AIFab.tsx', 'w') as f:
    f.write("""import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function AIFab() {
  const navigate = useNavigate();

  return (
    <div className="fixed bottom-[80px] right-4 z-50 flex items-center justify-end h-[52px]">
      <button
        onClick={() => navigate('/intent')}
        className="w-[52px] h-[52px] bg-[#111111] text-[#FFFFFF] rounded-sm shadow-[0_4px_16px_rgba(0,0,0,0.2)] flex items-center justify-center hover:scale-105 transition-transform active:scale-95 animate-in zoom-in duration-300"
      >
        <span className="material-symbols-outlined text-[24px] font-light">psychiatry</span>
      </button>
    </div>
  );
}
""")

# 2. Update IntentCanvas.tsx
with open('src/pages/IntentCanvas.tsx', 'w') as f:
    f.write("""import React, { useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function IntentCanvas() {
  const navigate = useNavigate();
  const inputRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, []);

  return (
    <div className="bg-[#F7F7F5] text-[#111111] font-sans antialiased min-h-screen flex flex-col">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#F7F7F5]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button onClick={() => navigate(-1)} className="relative z-10 text-[#111111] hover:opacity-80 transition-opacity p-2 -ml-2">
            <span className="material-symbols-outlined text-[24px]">close</span>
          </button>
          <div className="font-serif text-[16px] text-[#111111] flex items-center gap-1.5 absolute left-1/2 -translate-x-1/2 pointer-events-none uppercase tracking-widest">
            <span className="material-symbols-outlined text-[18px]">psychiatry</span> AI
          </div>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <div className="w-[87px] h-[32px] shrink-0 rounded-none border border-[#E4E3DE] flex items-center justify-between px-3 bg-[#FFFFFF]/50 backdrop-blur-md">
              <span className="material-symbols-outlined text-[18px] text-[#111111]">more_horiz</span>
              <div className="w-[1px] h-4 bg-[#E4E3DE]"></div>
              <span className="material-symbols-outlined text-[16px] text-[#111111]">radio_button_unchecked</span>
            </div>
          </div>
        </div>
      </header>

      <main className="flex-1 flex flex-col px-4 pt-16 pb-safe w-full">
        <div className="bg-[#FFFFFF] border border-[#E4E3DE] rounded-sm p-3 mt-4 flex flex-col shadow-sm">
          <textarea 
            ref={inputRef}
            className="w-full bg-transparent border-none p-0 focus:ring-0 resize-none font-sans text-[15px] leading-relaxed text-[#111111] placeholder:text-[#666663] outline-none"
            placeholder="描述您需要的商品、场景或要求..."
            rows={3}
            defaultValue="下周去东京，找一个能装 13 英寸电脑、没有明显 Logo、预算 3 万以内的黑色包"
          />
          <div className="flex justify-between items-center mt-2 pt-2 border-t border-[#E4E3DE]">
            <div className="flex gap-3">
              <button className="text-[#666663] hover:text-[#111111] transition-colors flex items-center justify-center">
                <span className="material-symbols-outlined text-[20px] font-light">mic</span>
              </button>
              <button className="text-[#666663] hover:text-[#111111] transition-colors flex items-center justify-center" onClick={() => navigate('/visual-search')}>
                <span className="material-symbols-outlined text-[20px] font-light">image</span>
              </button>
            </div>
            <button onClick={() => navigate('/results')} className="w-8 h-8 rounded-sm bg-[#111111] text-[#FFFFFF] flex items-center justify-center hover:opacity-90 transition-opacity">
              <span className="material-symbols-outlined text-[18px]">arrow_upward</span>
            </button>
          </div>
        </div>

        <div className="mt-4">
          <div className="flex flex-wrap gap-2">
            <span className="px-3 py-1.5 border border-[#E4E3DE] bg-[#FFFFFF] rounded-sm text-[12px] text-[#111111] flex items-center gap-1 shadow-sm">
              东京差旅 <span className="material-symbols-outlined text-[14px] text-[#666663]">edit</span>
            </span>
            <span className="px-3 py-1.5 border border-[#E4E3DE] bg-[#FFFFFF] rounded-sm text-[12px] text-[#111111] flex items-center gap-1 shadow-sm">
              13 英寸电脑 <span className="material-symbols-outlined text-[14px] text-[#666663]">edit</span>
            </span>
            <span className="px-3 py-1.5 border border-[#E4E3DE] bg-[#FFFFFF] rounded-sm text-[12px] text-[#111111] flex items-center gap-1 shadow-sm">
              低 Logo <span className="material-symbols-outlined text-[14px] text-[#666663]">edit</span>
            </span>
            <span className="px-3 py-1.5 border border-[#E4E3DE] bg-[#FFFFFF] rounded-sm text-[12px] text-[#111111] flex items-center gap-1 shadow-sm">
              <div className="w-2.5 h-2.5 rounded-none bg-[#111111] border border-[#E4E3DE] mr-0.5"></div>
              黑色 <span className="material-symbols-outlined text-[14px] text-[#666663]">close</span>
            </span>
            <span className="px-3 py-1.5 border border-[#E4E3DE] bg-[#FFFFFF] rounded-sm text-[12px] font-mono text-[#111111] flex items-center gap-1 shadow-sm">
              ≤ ¥30,000 <span className="material-symbols-outlined text-[14px] text-[#666663]">edit</span>
            </span>
          </div>
        </div>

        <div className="mt-8">
          <div className="flex items-start gap-3">
            <div className="w-7 h-7 rounded-none bg-[#FFFFFF] border border-[#E4E3DE] flex items-center justify-center shrink-0 shadow-sm mt-0.5">
              <span className="material-symbols-outlined text-[16px] text-[#111111]">psychiatry</span>
            </div>
            <div className="flex-1 bg-[#FFFFFF] border border-[#E4E3DE] rounded-sm p-4 shadow-sm">
              <p className="font-serif text-[15px] text-[#111111] mb-4">为您找到 12 件符合预期的单品。您更看重材质的轻便，还是正式感？</p>
              <div className="flex flex-col gap-2">
                <button onClick={() => navigate('/results')} className="py-2.5 px-4 border border-[#E4E3DE] rounded-sm hover:bg-[#F7F7F5] transition-colors text-left flex justify-between items-center group bg-[#FFFFFF]">
                  <span className="text-[13px] text-[#111111]">极致轻便 (尼龙/帆布)</span>
                  <span className="material-symbols-outlined text-[18px] text-[#666663]">arrow_forward</span>
                </button>
                <button onClick={() => navigate('/results')} className="py-2.5 px-4 border border-[#E4E3DE] rounded-sm hover:bg-[#F7F7F5] transition-colors text-left flex justify-between items-center group bg-[#FFFFFF]">
                  <span className="text-[13px] text-[#111111]">商务正式 (全皮质)</span>
                  <span className="material-symbols-outlined text-[18px] text-[#666663]">arrow_forward</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
""")
