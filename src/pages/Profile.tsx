
import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function Profile() {
  const navigate = useNavigate();

  return (
    <div className="bg-[#F7F7F5] text-[#111111] font-sans antialiased min-h-screen pb-24">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#F7F7F5]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <div className="w-10"></div>
          <h1 className="font-serif text-[18px] text-[#111111] tracking-widest absolute left-1/2 -translate-x-1/2 pointer-events-none uppercase">Profile</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-[#111111] hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[24px]">settings</span>
            </button>
          </div>
        </div>
      </header>

      <main className="pt-14 w-full flex flex-col">
        <section className="px-5 py-8 bg-[#FFFFFF] flex items-center gap-5 border-b border-[#E4E3DE] mb-4">
          <div className="w-20 h-20 rounded-sm overflow-hidden">
             <img className="w-full h-full object-cover grayscale" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDNaeE-LiR7h5C_dDZP4Rma_H3UQZypRN2tkJncNemYb8j2JRV0-AC3MqwYxa_SftiX-SsTfhplEvJkF2rh7hNY4-sd8y0E5PP0tMte1bEFr6pinfnFjZf0ngqdTUz32S_qpcW5vF4J7wxePjqe0O-82NY3Bd55cjOHLiRmp6pPuVZN_XRqmTbpgv9QYxV2KIRC2fFKSinQu6y1hOZuWFRV3-vhLIMfykbe_MiO4Xdx68vA2kJoQvjr" alt="Avatar" />
          </div>
          <div>
            <h2 className="font-serif text-[24px] text-[#111111] mb-1">ALEX CHEN</h2>
            <div className="flex items-center gap-2 text-[12px] text-[#666663] uppercase tracking-widest">
              <span className="bg-[#242424] text-white px-2 py-0.5 rounded-sm">Noir</span>
              <span>PTS: 12,500</span>
            </div>
          </div>
        </section>

        <section className="px-5 py-6 bg-[#FFFFFF] mb-4 border-y border-[#E4E3DE]">
           <h3 className="font-serif text-[18px] text-[#111111] mb-6">我的订单</h3>
           <div className="flex justify-between items-center px-2">
              {[
                { icon: 'account_balance_wallet', label: '待付款' },
                { icon: 'inventory_2', label: '待发货' },
                { icon: 'local_shipping', label: '待收货' },
                { icon: 'rate_review', label: '评价' },
                { icon: 'headset_mic', label: '售后' },
              ].map((item, i) => (
                <div key={i} className="flex flex-col items-center gap-2 cursor-pointer text-[#111111] group">
                   <span className="material-symbols-outlined text-[24px] font-light group-hover:opacity-70 transition-opacity">{item.icon}</span>
                   <span className="text-[11px] font-medium">{item.label}</span>
                </div>
              ))}
           </div>
        </section>

        <section className="bg-[#FFFFFF] border-y border-[#E4E3DE] flex flex-col">
           {[
             { icon: 'favorite_border', label: '心愿单', value: '12' },
             { icon: 'history', label: '浏览记录', value: '128' },
             { icon: 'event', label: '我的预约', value: '1' },
             { icon: 'location_on', label: '收货地址' },
           ].map((item, i) => (
             <div key={i} className="flex items-center justify-between px-5 py-5 border-b border-[#E4E3DE] last:border-0 cursor-pointer hover:bg-[#F7F7F5] transition-colors">
                <div className="flex items-center gap-4 text-[#111111]">
                  <span className="material-symbols-outlined text-[24px] font-light">{item.icon}</span>
                  <span className="text-[14px] font-medium">{item.label}</span>
                </div>
                <div className="flex items-center gap-3 text-[#666663]">
                  {item.value && <span className="text-[13px] font-mono">{item.value}</span>}
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
