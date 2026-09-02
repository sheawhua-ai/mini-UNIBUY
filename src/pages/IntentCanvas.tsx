import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function IntentCanvas() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex flex-col canvas-bg text-primary">
      <header className="fixed top-0 left-0 w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full max-w-7xl mx-auto">
          <button onClick={() => navigate(-1)} className="relative z-10 text-primary hover:opacity-80 transition-opacity p-2 -ml-2">
            <span className="material-symbols-outlined text-[24px]">close</span>
          </button>
          <div className="font-label-ui text-[14px] text-on-surface-variant flex items-center gap-2 absolute left-1/2 -translate-x-1/2 pointer-events-none">
            <span className="material-symbols-outlined text-[16px]">psychiatry</span> AI
          </div>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="flex-1 flex flex-col px-5 pt-24 pb-safe mx-auto w-full">
        <div className="mb-12 animate-[fadeInUp_0.6s_ease-out]">
          <h1 className="font-display-hero text-[38px] tracking-tighter">帮我找</h1>
        </div>

        <div className="relative w-full mb-[32px] animate-[fadeInUp_0.6s_ease-out_100ms] fill-mode-forwards opacity-0" style={{animationFillMode: 'forwards'}}>
          <textarea 
            className="w-full bg-transparent border-0 border-b border-outline-variant focus:border-primary focus:ring-0 resize-none font-headline-lg-mobile text-[26px] placeholder:text-surface-tint pb-4 transition-colors duration-300 outline-none" 
            placeholder="描述您需要的商品、场景或要求..." 
            rows={4}
            defaultValue="下周去东京，找一个能装 13 英寸电脑、没有明显 Logo、预算 3 万以内的黑色包"
          />
          <div className="absolute bottom-4 right-0 flex gap-4">
            <button className="text-on-surface-variant hover:text-primary transition-colors">
              <span className="material-symbols-outlined">mic</span>
            </button>
            <button className="text-on-surface-variant hover:text-primary transition-colors">
              <span className="material-symbols-outlined">image</span>
            </button>
          </div>
        </div>

        <div className="mb-12 animate-[fadeInUp_0.6s_ease-out_200ms] opacity-0" style={{animationFillMode: 'forwards'}}>
          <div className="flex flex-wrap gap-3">
            <button className="px-4 py-2 border border-hairline rounded font-label-ui text-[14px] hover:bg-mist transition-colors flex items-center gap-2">
              东京差旅 <span className="material-symbols-outlined text-[14px] text-outline">edit</span>
            </button>
            <button className="px-4 py-2 border border-hairline rounded font-label-ui text-[14px] hover:bg-mist transition-colors flex items-center gap-2">
              13 英寸电脑 <span className="material-symbols-outlined text-[14px] text-outline">edit</span>
            </button>
            <button className="px-4 py-2 border border-hairline rounded font-label-ui text-[14px] hover:bg-mist transition-colors flex items-center gap-2">
              低 Logo <span className="material-symbols-outlined text-[14px] text-outline">edit</span>
            </button>
            <button className="px-4 py-2 border border-hairline rounded font-label-ui text-[14px] bg-mist flex items-center gap-2">
              <div className="w-3 h-3 rounded-full bg-primary border border-hairline"></div>
              黑色 <span className="material-symbols-outlined text-[14px] text-outline">close</span>
            </button>
            <button className="px-4 py-2 border border-hairline rounded font-label-ui text-[14px] hover:bg-mist transition-colors flex items-center gap-2">
              ≤ ¥30,000 <span className="material-symbols-outlined text-[14px] text-outline">edit</span>
            </button>
          </div>
        </div>

        <div className="mt-auto border-t border-hairline pt-8 pb-12 animate-[fadeInUp_0.6s_ease-out_300ms] opacity-0" style={{animationFillMode: 'forwards'}}>
          <div className="flex items-start gap-4">
            <div className="w-8 h-8 rounded-full bg-mist flex items-center justify-center shrink-0">
              <span className="material-symbols-outlined text-[16px]">psychiatry</span>
            </div>
            <div className="flex-1">
              <p className="font-section-title text-[24px] mb-6">更看重轻便，还是正式感？</p>
              <div className="flex flex-col gap-4 mb-6">
                <button onClick={() => navigate('/results')} className="py-4 px-6 border border-hairline rounded hover:bg-mist transition-colors text-left flex justify-between items-center group">
                  <span className="font-body-main text-[16px]">极致轻便 (尼龙/帆布)</span>
                  <span className="material-symbols-outlined text-outline">arrow_forward</span>
                </button>
                <button onClick={() => navigate('/results')} className="py-4 px-6 border border-hairline rounded hover:bg-mist transition-colors text-left flex justify-between items-center group">
                  <span className="font-body-main text-[16px]">商务正式 (全皮质)</span>
                  <span className="material-symbols-outlined text-outline">arrow_forward</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>
      
      <style>{`
        @keyframes fadeInUp {
          to { opacity: 1; transform: translateY(0); }
        }
        .animate-\\[fadeInUp_0\\.6s_ease-out\\] { transform: translateY(20px); }
        .animate-\\[fadeInUp_0\\.6s_ease-out_100ms\\] { transform: translateY(20px); }
        .animate-\\[fadeInUp_0\\.6s_ease-out_200ms\\] { transform: translateY(20px); }
        .animate-\\[fadeInUp_0\\.6s_ease-out_300ms\\] { transform: translateY(20px); }
      `}</style>
    </div>
  );
}
