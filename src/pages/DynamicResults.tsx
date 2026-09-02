import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function DynamicResults() {
  const navigate = useNavigate();

  return (
    <div className="bg-surface text-on-surface antialiased font-body-main min-h-screen pb-24">
      <header className="fixed top-0 left-0 w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="flex flex-col px-4 pt-3 pb-2 w-full max-w-7xl mx-auto">
          <div className="relative flex justify-between items-center mb-3 h-10">
            <button onClick={() => navigate(-1)} className="relative z-10 text-primary hover:opacity-80 transition-opacity p-2 -ml-2">
              <span className="material-symbols-outlined text-[24px]">arrow_back</span>
            </button>
            <div className="font-display-hero text-[22px] tracking-tighter text-primary absolute left-1/2 -translate-x-1/2 pointer-events-none font-bold">UNIBUY</div>
            <div className="relative z-10 flex items-center shrink-0">
              <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
            </div>
          </div>
          <div className="flex items-center gap-2 overflow-x-auto hide-scrollbar pb-2">
            <span className="px-4 py-1.5 bg-mist rounded-full border border-hairline font-label-ui text-[14px] text-on-surface-variant whitespace-nowrap">周末晚宴</span>
            <span className="px-4 py-1.5 bg-mist rounded-full border border-hairline font-label-ui text-[14px] text-on-surface-variant whitespace-nowrap">偏向松弛感</span>
            <span className="px-4 py-1.5 bg-mist rounded-full border border-hairline font-label-ui text-[14px] text-on-surface-variant whitespace-nowrap">预算 5000 左右</span>
          </div>
        </div>
      </header>

      <main className="pt-40 px-5 pb-24 max-w-7xl mx-auto">
        <div className="mb-16">
          <h1 className="font-headline-lg-mobile text-[26px] text-primary mb-2">最符合你的 4 件单品</h1>
          <p className="font-body-main text-[16px] text-on-surface-variant">基于周末晚宴场景及预算为您精心挑选。</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-x-3 gap-y-16">
          <div className="group flex flex-col gap-4" onClick={() => navigate('/product')}>
            <div className="aspect-[4/5] relative overflow-hidden bg-mist">
              <img className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCb5GX1NgebA1BEN4TvMqvO_ATmXWwggjzGHa6DIOebRa3nabx-ptiDZwYvVXBjAACN2fIbp9lSHJ9di0VXDuHq4hDPjDtkg5WjQuNTs3i7Urz2MRdZRY46ttSD0DtmAQEzXk5ajRp1V5N2oC4CBpCjrSH0jS9gISsWW1oY-QQgv5a3IlOd48OA0KSkqRhQgDRrB6v3-cRDCP7LEPCf9mzBHbk-DJWgrkbZm7rZd_6UL6gkgTSHRJZ5" alt="Dress" />
              <div className="absolute top-2 left-2 px-2 py-1 bg-surface/90 backdrop-blur-sm border border-hairline rounded font-metadata text-[12px] text-primary uppercase tracking-widest">高匹配</div>
            </div>
            <div className="flex flex-col gap-1">
              <div className="flex justify-between items-start">
                <h3 className="font-section-title text-[24px] text-primary">真丝垂坠吊带裙</h3>
                <span className="font-price-tabular text-[18px] text-primary">¥3,200</span>
              </div>
              <p className="font-metadata text-[12px] text-on-surface-variant uppercase tracking-widest">AURALEE</p>
              <div className="mt-4 p-4 bg-mist/50 border-l border-primary">
                <p className="font-body-main text-[16px] text-on-surface-variant"><strong className="text-primary font-medium">为何适合：</strong>极简剪裁带来毫不费力的松弛感，真丝光泽在晚宴灯光下质感出众。</p>
              </div>
            </div>
          </div>

          <div className="group flex flex-col gap-4" onClick={() => navigate('/product')}>
            <div className="aspect-[4/5] relative overflow-hidden bg-mist">
              <img className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBuEA5GbSvq0FUczZPnBUcC6b0xW2_Q2M3rrYuctNRk6CW5EYLWUCv_LFcw-ZTkrKjTqVVoh3eWycp1gWuZdlxG_X7gk_EcoHGZxj9WUBSYw2XjZyqLqsD4AbHiJQTrrtDTn7uMCGuyaYhkmE-SzVteILWSJQEgspWY8RTSmgtK_inoIQ29QEH5nUKM1IEYbLVFFiX1eYD0pVj_UPTB56KqyFs2JvyMaqYIiOVSryhjkmRrO64KgH_m" alt="Blazer" />
            </div>
            <div className="flex flex-col gap-1">
              <div className="flex justify-between items-start">
                <h3 className="font-section-title text-[24px] text-primary">结构感羊毛混纺西装</h3>
                <span className="font-price-tabular text-[18px] text-primary">¥4,500</span>
              </div>
              <p className="font-metadata text-[12px] text-on-surface-variant uppercase tracking-widest">LEMAIRE</p>
              <div className="mt-4 p-4 bg-mist/50 border-l border-primary">
                <p className="font-body-main text-[16px] text-on-surface-variant"><strong className="text-primary font-medium">为何适合：</strong>可披在肩上增加层次，既能应对夜间微凉，又能中和过度的隆重感。</p>
              </div>
            </div>
          </div>
        </div>
        
        <div className="mt-12 flex justify-center">
            <button onClick={() => navigate('/compare')} className="px-6 py-3 border border-primary text-primary font-label-ui text-[14px] hover:bg-mist transition-colors rounded">对比这些单品</button>
        </div>
      </main>

      <div className="fixed bottom-0 w-full z-40 bg-surface/90 backdrop-blur-2xl border-t border-hairline pb-safe absolute">
        <div className="px-5 py-4 max-w-7xl mx-auto">
          <div className="relative flex items-center bg-pure-white border border-hairline h-[52px] rounded shadow-[0_8px_32px_rgba(0,0,0,0.08)] px-4">
            <span className="font-metadata text-[12px] text-on-surface-variant uppercase tracking-widest mr-3">AI</span>
            <input className="flex-1 bg-transparent border-none focus:ring-0 font-body-main text-[16px] text-primary placeholder-outline p-0 h-full outline-none" placeholder="继续说：第二个太正式..." type="text" />
            <button className="text-primary hover:opacity-80 transition-opacity ml-2">
              <span className="material-symbols-outlined fill">arrow_upward</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
