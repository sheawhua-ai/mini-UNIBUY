import sys

content = """
import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function Profile() {
  const navigate = useNavigate();

  return (
    <div className="bg-surface text-on-surface font-body-main antialiased min-h-screen pb-24">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <div className="w-[87px]"></div>
          <h1 className="font-bold text-[18px] text-primary tracking-tight absolute left-1/2 -translate-x-1/2 pointer-events-none">我的</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-primary hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[24px]">settings</span>
            </button>
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="pt-14 w-full flex flex-col">
        <section className="px-5 py-6 bg-pure-white flex items-center gap-4 border-b border-hairline mb-2">
          <div className="w-16 h-16 rounded-full border border-hairline overflow-hidden">
             <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDNaeE-LiR7h5C_dDZP4Rma_H3UQZypRN2tkJncNemYb8j2JRV0-AC3MqwYxa_SftiX-SsTfhplEvJkF2rh7hNY4-sd8y0E5PP0tMte1bEFr6pinfnFjZf0ngqdTUz32S_qpcW5vF4J7wxePjqe0O-82NY3Bd55cjOHLiRmp6pPuVZN_XRqmTbpgv9QYxV2KIRC2fFKSinQu6y1hOZuWFRV3-vhLIMfykbe_MiO4Xdx68vA2kJoQvjr" alt="Avatar" />
          </div>
          <div>
            <h2 className="font-bold text-[18px] text-primary mb-1">ALEX CHEN</h2>
            <p className="text-[12px] text-on-surface-variant">黑金会员 | 积分: 12,500</p>
          </div>
        </section>

        <section className="px-4 py-4 bg-pure-white mb-2">
           <h3 className="font-bold text-[15px] text-primary mb-4 px-1">我的订单</h3>
           <div className="flex justify-between items-center px-2">
              {[
                { icon: 'account_balance_wallet', label: '待付款' },
                { icon: 'inventory_2', label: '待发货' },
                { icon: 'local_shipping', label: '待收货' },
                { icon: 'rate_review', label: '评价' },
                { icon: 'headset_mic', label: '售后' },
              ].map((item, i) => (
                <div key={i} className="flex flex-col items-center gap-1.5 cursor-pointer text-on-surface-variant hover:text-primary">
                   <span className="material-symbols-outlined text-[24px]">{item.icon}</span>
                   <span className="text-[11px]">{item.label}</span>
                </div>
              ))}
           </div>
        </section>

        <section className="bg-pure-white mb-2 flex flex-col">
           {[
             { icon: 'favorite_border', label: '心愿单', value: '12' },
             { icon: 'history', label: '浏览记录', value: '128' },
             { icon: 'confirmation_number', label: '优惠券', value: '3' },
             { icon: 'location_on', label: '收货地址' },
           ].map((item, i) => (
             <div key={i} className="flex items-center justify-between px-5 py-4 border-b border-hairline last:border-0 cursor-pointer hover:bg-surface-container-lowest">
                <div className="flex items-center gap-3 text-primary">
                  <span className="material-symbols-outlined text-[22px]">{item.icon}</span>
                  <span className="text-[14px] font-medium">{item.label}</span>
                </div>
                <div className="flex items-center gap-2 text-on-surface-variant">
                  {item.value && <span className="text-[13px]">{item.value}</span>}
                  <span className="material-symbols-outlined text-[20px]">chevron_right</span>
                </div>
             </div>
           ))}
        </section>
      </main>
      <BottomNav />
    </div>
  );
}
"""
with open('src/pages/Profile.tsx', 'w') as f:
    f.write(content)
