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
        {/* Black Card with Tiers and Points */}
        <section className="bg-[#242424] text-[#F7F7F5] rounded-sm p-6 relative overflow-hidden shadow-lg">
          <div className="absolute top-0 right-0 w-48 h-48 bg-white/5 rounded-full -translate-y-1/2 translate-x-1/4 blur-3xl"></div>
          
          <div className="relative z-10 flex justify-between items-start mb-8">
            <div>
              <div className="flex items-center gap-2 mb-1">
                <span className="w-1.5 h-1.5 bg-[#E56A1D] rounded-none"></span>
                <p className="font-medium text-[11px] text-[#E56A1D] uppercase tracking-widest">Noir 等级</p>
              </div>
              <h2 className="font-serif text-[24px] tracking-widest uppercase">ALEX CHEN</h2>
            </div>
            <div className="w-12 h-12 border border-[#E56A1D]/30 overflow-hidden rounded-sm">
              <img className="w-full h-full object-cover grayscale" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDNaeE-LiR7h5C_dDZP4Rma_H3UQZypRN2tkJncNemYb8j2JRV0-AC3MqwYxa_SftiX-SsTfhplEvJkF2rh7hNY4-sd8y0E5PP0tMte1bEFr6pinfnFjZf0ngqdTUz32S_qpcW5vF4J7wxePjqe0O-82NY3Bd55cjOHLiRmp6pPuVZN_XRqmTbpgv9QYxV2KIRC2fFKSinQu6y1hOZuWFRV3-vhLIMfykbe_MiO4Xdx68vA2kJoQvjr" alt="Avatar" />
            </div>
          </div>
          
          <div className="relative z-10 flex flex-col gap-2">
            <div className="flex justify-between items-end">
              <div>
                <p className="text-[10px] text-white/60 mb-0.5">可用积分余额</p>
                <p className="font-mono text-[22px] font-medium leading-none">12,500</p>
              </div>
              <button className="text-[11px] text-white/80 underline underline-offset-2 hover:text-white transition-colors">积分明细</button>
            </div>
            
            <div className="mt-4 pt-4 border-t border-white/10">
              <div className="flex justify-between text-[11px] text-[#F7F7F5]/80 font-mono mb-2">
                <span>升至顶级 Privé 需 2,500 积分</span>
              </div>
              <div className="w-full h-[2px] bg-white/20 overflow-hidden">
                <div className="h-full bg-[#E56A1D] w-[83%]"></div>
              </div>
            </div>
          </div>
        </section>

        {/* Services & Redemption */}
        <section>
          <div className="flex justify-between items-end mb-4 border-b border-[#E4E3DE] pb-2">
            <h3 className="font-serif text-[20px] text-[#111111]">积分兑换权益</h3>
            <button className="text-[11px] text-[#666663] underline underline-offset-2 hover:text-[#111111]">查看全部</button>
          </div>
          <div className="flex flex-col gap-4">
            {[
              { img: 'https://images.unsplash.com/photo-1584824486516-0555a07fc511?auto=format&fit=crop&q=80&w=200', title: '专柜深度皮具护理', points: '2,000 pts', desc: '包含名贵皮具深度清洁、专业补色及抛光服务。' },
              { img: 'https://images.unsplash.com/photo-1544148103-0773bf10d330?auto=format&fit=crop&q=80&w=200', title: '奢华酒店双人下午茶', points: '5,000 pts', desc: '全球指定合作五星级酒店或米其林餐厅双人套餐。' },
              { img: 'https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&q=80&w=200', title: '私人造型师上门', points: '10,000 pts', desc: '2小时专属衣橱整理、重要场合穿搭指导与改衣服务。' }
            ].map((item, i) => (
              <div key={i} className="bg-[#FFFFFF] border border-[#E4E3DE] rounded-sm p-3 flex items-center gap-4 shadow-sm cursor-pointer hover:border-[#111111] transition-colors group">
                <div className="w-16 h-20 bg-[#EFEFEB] rounded-sm overflow-hidden flex-shrink-0">
                  <img src={item.img} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Service" />
                </div>
                <div className="flex-1">
                  <h4 className="font-medium text-[14px] text-[#111111] mb-1">{item.title}</h4>
                  <p className="text-[11px] text-[#666663] leading-relaxed mb-2 line-clamp-2">{item.desc}</p>
                  <p className="text-[12px] font-mono font-medium text-[#E56A1D]">{item.points}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Regular Privileges */}
        <section className="mt-2">
          <div className="flex justify-between items-end mb-4 border-b border-[#E4E3DE] pb-2">
            <h3 className="font-serif text-[20px] text-[#111111]">常驻等级礼遇</h3>
          </div>
          <div className="grid grid-cols-2 gap-3">
            {[
              { icon: 'local_shipping', title: '全球免邮', desc: '尊享所有订单免费配送' },
              { icon: 'event_available', title: '优先抢购', desc: '提前24小时锁定限量品' }
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
      </main>
      <BottomNav />
    </div>
  );
}
