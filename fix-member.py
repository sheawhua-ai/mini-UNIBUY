import sys

content = """
import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function MemberCenter() {
  const navigate = useNavigate();

  return (
    <div className="bg-surface text-on-surface font-body-main antialiased min-h-screen pb-24">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center justify-center p-2 -ml-2 text-primary hover:opacity-80 transition-opacity" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <h1 className="font-bold text-[18px] text-primary tracking-tight absolute left-1/2 -translate-x-1/2 pointer-events-none">会员中心</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-primary hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="pt-16 pb-6 px-4 flex flex-col gap-5">
        <section className="bg-charcoal text-pure-white rounded-2xl p-6 relative overflow-hidden shadow-md">
          <div className="absolute top-0 right-0 w-32 h-32 bg-pure-white/5 rounded-full -translate-y-1/2 translate-x-1/4 blur-2xl"></div>
          <div className="absolute bottom-0 left-0 w-24 h-24 bg-pure-white/5 rounded-full translate-y-1/3 -translate-x-1/3 blur-xl"></div>
          
          <div className="relative z-10 flex justify-between items-start mb-6">
            <div>
              <p className="font-bold text-[12px] text-pure-white/70 uppercase tracking-widest mb-1">黑金会员</p>
              <h2 className="font-bold text-[22px] tracking-tight">ALEX CHEN</h2>
            </div>
            <div className="w-12 h-12 rounded-full border border-pure-white/20 overflow-hidden">
              <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDNaeE-LiR7h5C_dDZP4Rma_H3UQZypRN2tkJncNemYb8j2JRV0-AC3MqwYxa_SftiX-SsTfhplEvJkF2rh7hNY4-sd8y0E5PP0tMte1bEFr6pinfnFjZf0ngqdTUz32S_qpcW5vF4J7wxePjqe0O-82NY3Bd55cjOHLiRmp6pPuVZN_XRqmTbpgv9QYxV2KIRC2fFKSinQu6y1hOZuWFRV3-vhLIMfykbe_MiO4Xdx68vA2kJoQvjr" alt="Avatar" />
            </div>
          </div>
          
          <div className="relative z-10 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] text-pure-white/80">
              <span>当前积分: 12,500</span>
              <span>距离升级: 2,500</span>
            </div>
            <div className="w-full h-1 bg-pure-white/20 rounded-full overflow-hidden">
              <div className="h-full bg-pure-white w-[83%]"></div>
            </div>
          </div>
        </section>

        <section>
          <h3 className="font-bold text-[16px] text-primary mb-3">专属权益</h3>
          <div className="grid grid-cols-2 gap-3">
            <div className="bg-pure-white border border-hairline rounded-xl p-4 flex flex-col gap-2 shadow-sm">
              <span className="material-symbols-outlined text-[24px] text-primary">local_shipping</span>
              <div>
                <h4 className="font-bold text-[13px] text-primary">全球免邮</h4>
                <p className="text-[11px] text-on-surface-variant mt-0.5">尊享所有订单免费标准配送</p>
              </div>
            </div>
            <div className="bg-pure-white border border-hairline rounded-xl p-4 flex flex-col gap-2 shadow-sm">
              <span className="material-symbols-outlined text-[24px] text-primary">support_agent</span>
              <div>
                <h4 className="font-bold text-[13px] text-primary">私人顾问</h4>
                <p className="text-[11px] text-on-surface-variant mt-0.5">一对一专属造型与礼宾服务</p>
              </div>
            </div>
            <div className="bg-pure-white border border-hairline rounded-xl p-4 flex flex-col gap-2 shadow-sm">
              <span className="material-symbols-outlined text-[24px] text-primary">event_available</span>
              <div>
                <h4 className="font-bold text-[13px] text-primary">优先抢购</h4>
                <p className="text-[11px] text-on-surface-variant mt-0.5">提前24小时锁定限量单品</p>
              </div>
            </div>
            <div className="bg-pure-white border border-hairline rounded-xl p-4 flex flex-col gap-2 shadow-sm">
              <span className="material-symbols-outlined text-[24px] text-primary">cake</span>
              <div>
                <h4 className="font-bold text-[13px] text-primary">生日礼遇</h4>
                <p className="text-[11px] text-on-surface-variant mt-0.5">生日当月尊享双倍积分及好礼</p>
              </div>
            </div>
          </div>
        </section>

        <section className="mt-2">
          <h3 className="font-bold text-[16px] text-primary mb-3">近期活动</h3>
          <div className="flex flex-col gap-3">
            <div className="relative h-[120px] rounded-xl overflow-hidden cursor-pointer">
              <div className="absolute inset-0 bg-cover bg-center" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuArjtrVE2lG4P8GVPHflyWb0Mo5SVTyYRhEKICWp9dXBZfgpnNrEjMm6dtbb5AIQEJulXtvOM2xsrCwwNtXTUGD-ijZT4Ysg_qC8E06uX1B8BvShZ3crQWafJlSTskDHLbYcvpzUhub0jJs9GzUV15SSZE3qvn2mQV6vrwfgxBhaFpM6nYybFKKT4dA7wbrIK7HlkPDWs23ehSoCcEl9zupcOvb1U6484cHAiBp62KwkzvTEDpq6g1U')"}}></div>
              <div className="absolute inset-0 bg-black/40"></div>
              <div className="absolute inset-0 p-4 flex flex-col justify-end">
                <span className="text-[10px] text-pure-white/80 uppercase tracking-widest mb-1">上海</span>
                <h4 className="font-bold text-[15px] text-pure-white leading-tight">2026 秋冬系列私享预览会</h4>
              </div>
            </div>
          </div>
        </section>
      </main>
      <BottomNav />
    </div>
  );
}
"""
with open('src/pages/MemberCenter.tsx', 'w') as f:
    f.write(content)
