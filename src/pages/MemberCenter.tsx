
import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function MemberCenter() {
  const navigate = useNavigate();

  return (
    <div className="bg-[#F7F7F5] text-[#111111] font-sans antialiased min-h-screen pb-24">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#F7F7F5]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center justify-center p-2 -ml-2 text-[#111111] hover:opacity-80 transition-opacity" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <h1 className="font-serif text-[18px] text-[#111111] tracking-widest absolute left-1/2 -translate-x-1/2 pointer-events-none uppercase">ATELIER</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-[#111111] hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
          </div>
        </div>
      </header>

      <main className="pt-20 pb-6 px-5 flex flex-col gap-8">
        {/* Black Card */}
        <section className="bg-[#242424] text-[#F7F7F5] rounded-sm p-6 relative overflow-hidden shadow-lg">
          <div className="absolute top-0 right-0 w-48 h-48 bg-white/5 rounded-full -translate-y-1/2 translate-x-1/4 blur-3xl"></div>
          
          <div className="relative z-10 flex justify-between items-start mb-10">
            <div>
              <p className="font-medium text-[11px] text-[#E56A1D] uppercase tracking-widest mb-1">Noir Member</p>
              <h2 className="font-serif text-[24px] tracking-widest uppercase">ALEX CHEN</h2>
            </div>
            <div className="w-12 h-12 border border-[#E56A1D]/30 overflow-hidden rounded-sm">
              <img className="w-full h-full object-cover grayscale" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDNaeE-LiR7h5C_dDZP4Rma_H3UQZypRN2tkJncNemYb8j2JRV0-AC3MqwYxa_SftiX-SsTfhplEvJkF2rh7hNY4-sd8y0E5PP0tMte1bEFr6pinfnFjZf0ngqdTUz32S_qpcW5vF4J7wxePjqe0O-82NY3Bd55cjOHLiRmp6pPuVZN_XRqmTbpgv9QYxV2KIRC2fFKSinQu6y1hOZuWFRV3-vhLIMfykbe_MiO4Xdx68vA2kJoQvjr" alt="Avatar" />
            </div>
          </div>
          
          <div className="relative z-10 flex flex-col gap-2">
            <div className="flex justify-between text-[11px] text-[#F7F7F5]/80 font-mono">
              <span>PTS: 12,500</span>
              <span>NEXT: 2,500</span>
            </div>
            <div className="w-full h-[2px] bg-white/20 overflow-hidden">
              <div className="h-full bg-[#E56A1D] w-[83%]"></div>
            </div>
          </div>
        </section>

        <section>
          <div className="flex justify-between items-end mb-4 border-b border-[#E4E3DE] pb-2">
            <h3 className="font-serif text-[20px] text-[#111111]">专属礼遇</h3>
          </div>
          <div className="grid grid-cols-2 gap-3">
            {[
              { icon: 'local_shipping', title: '全球免邮', desc: '尊享所有订单免费标准配送' },
              { icon: 'support_agent', title: '私人顾问', desc: '一对一专属造型与礼宾服务' },
              { icon: 'event_available', title: '优先抢购', desc: '提前24小时锁定限量单品' },
              { icon: 'cake', title: '生日礼遇', desc: '生日当月尊享双倍积分及好礼' }
            ].map((item, i) => (
              <div key={i} className="bg-[#FFFFFF] border border-[#E4E3DE] rounded-sm p-4 flex flex-col gap-3 shadow-sm cursor-pointer hover:border-[#111111] transition-colors">
                <span className="material-symbols-outlined text-[24px] text-[#111111] font-light">{item.icon}</span>
                <div>
                  <h4 className="font-medium text-[13px] text-[#111111] mb-1">{item.title}</h4>
                  <p className="text-[11px] text-[#666663] leading-relaxed">{item.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        <section className="mt-2">
          <div className="flex justify-between items-end mb-4 border-b border-[#E4E3DE] pb-2">
            <h3 className="font-serif text-[20px] text-[#111111]">近期活动</h3>
          </div>
          <div className="flex flex-col gap-4">
            <div className="relative h-[160px] rounded-sm overflow-hidden cursor-pointer group">
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuArjtrVE2lG4P8GVPHflyWb0Mo5SVTyYRhEKICWp9dXBZfgpnNrEjMm6dtbb5AIQEJulXtvOM2xsrCwwNtXTUGD-ijZT4Ysg_qC8E06uX1B8BvShZ3crQWafJlSTskDHLbYcvpzUhub0jJs9GzUV15SSZE3qvn2mQV6vrwfgxBhaFpM6nYybFKKT4dA7wbrIK7HlkPDWs23ehSoCcEl9zupcOvb1U6484cHAiBp62KwkzvTEDpq6g1U')"}}></div>
              <div className="absolute inset-0 bg-black/40"></div>
              <div className="absolute inset-0 p-5 flex flex-col justify-between">
                <span className="text-[10px] text-white/90 uppercase tracking-widest border border-white/50 w-fit px-2 py-1 backdrop-blur-sm rounded-sm">SHANGHAI</span>
                <div>
                  <h4 className="font-serif text-[20px] text-white leading-tight mb-2">2026 秋冬系列私享预览会</h4>
                  <button className="text-[12px] text-white underline underline-offset-4">立即预约</button>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
      <BottomNav />
    </div>
  );
}
