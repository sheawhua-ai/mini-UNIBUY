import sys

explore_content = """
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function Explore() {
  const navigate = useNavigate();
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 10);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div className="bg-[#F7F7F5] text-[#111111] font-sans antialiased min-h-screen pb-32">
      <header className={`fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 transition-colors duration-300 ${scrolled ? 'bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]' : 'bg-[#F7F7F5]'}`}>
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center justify-center p-2 -ml-2 text-[#111111] hover:opacity-80 transition-opacity" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <h1 className="font-serif text-[18px] text-[#111111] tracking-widest absolute left-1/2 -translate-x-1/2 pointer-events-none">EXPLORE</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-[#111111] hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
          </div>
        </div>
      </header>

      <main className="pt-16 pb-6 flex flex-col gap-6">
        <section className="px-4">
          <div className="flex items-center gap-4 mb-6 mt-2 border-b border-[#E4E3DE] pb-2">
            <button className="text-[14px] font-medium text-[#111111] border-b-2 border-[#111111] pb-2">分类浏览</button>
            <button className="text-[14px] text-[#666663] pb-2" onClick={() => navigate('/intent')}>意图找货</button>
          </div>
          
          <div className="grid grid-cols-2 gap-3">
            <div className="col-span-2 aspect-[21/9] rounded-sm relative group overflow-hidden bg-[#EFEFEB] cursor-pointer" onClick={() => navigate('/results')}>
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuDfVc20hhJWVxQ9Zjh_v_0zBZAsEedln_vNMHj7cZL4Y_gnL1TTk9NWfMcy47-aRhFr7CBI1vFLNXnSQIIcfIjMnUMY_soJ9CplOryBBIGsrB2AmhpXN0CAD7K5ZWqJy-s40LQDqQ82E8g-EZ936D1y8l8z-rcl8PEPjZBb-vxVal7cwW3xfsjGfrhMID4Bx3iSYt5UtheFUabrY6vRd-Fef53esvz2KlS7w6_RADP1qgTmeNN-QlVU')"}}></div>
              <div className="absolute inset-0 bg-black/20"></div>
              <div className="absolute bottom-4 left-4 z-10">
                <h3 className="font-serif text-[20px] text-white mb-1">时装与皮具</h3>
                <p className="text-[11px] text-white/90 tracking-widest uppercase">Fashion & Leather</p>
              </div>
            </div>
            
            <div className="aspect-[4/5] rounded-sm relative group overflow-hidden bg-[#EFEFEB] cursor-pointer">
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuDEu8Y7Q3mggUzbi1lfSzaf_Cvio0YgjG9-CHniOAk9sJ4jFykbZXegG4lw3sAJqcfV8NjX11U6gBrGKw4ll_cOXkhoOTVfMG6L7IwUkdH8lNNj7LUemnz8Im78f5vCeaaFnMvMOlrPBMNkLPgQwsl-kwru0MxNQ7dLRcmopmHUUE9qTsE4R6GSTSZM_GSVA8p5B9P_fQKAcp0fJghTW7bjuUI6K7IEpHNrQgnnO7gtXi_zChy7NEhf')"}}></div>
              <div className="absolute inset-0 bg-black/10"></div>
              <div className="absolute bottom-3 left-3 z-10">
                <h3 className="font-serif text-[16px] text-white">腕表与珠宝</h3>
              </div>
            </div>
            
            <div className="aspect-[4/5] rounded-sm relative group overflow-hidden bg-[#EFEFEB] cursor-pointer">
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuBRMauj5lZ76sk-DTEWjEvXkX0EZHfeM7XbaUoZsV3N5GgaNDTcMDEKsEPjob9ynmSz1962W0cEoOHV5hiCsmQr013vr_YrIYYgErH8SRSlnDwBjdLz1f6nTJU14tnBO_Y56mMRt9xyV6YUmrRdHOmylc5gBnZoWB3wX5KAb_enHH4nRFUdMbj07dmnygFM_ZGwbWYxCydXUmuDP7_fxd9k5LUGxCBM-_Ia4pLkqaAt-soro4N-wtCd')"}}></div>
              <div className="absolute inset-0 bg-black/10"></div>
              <div className="absolute bottom-3 left-3 z-10">
                <h3 className="font-serif text-[16px] text-white">美妆与香氛</h3>
              </div>
            </div>
          </div>
        </section>

        <section className="px-4 mt-4">
          <h2 className="font-serif text-[20px] text-[#111111] mb-4">为你精选</h2>
          <div className="grid grid-cols-2 gap-3">
            <div className="group cursor-pointer bg-[#FFFFFF] rounded-sm overflow-hidden pb-3" onClick={() => navigate('/product')}>
              <div className="aspect-[4/5] relative bg-[#EFEFEB] overflow-hidden mb-3">
                <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuCrE-noQEgrN3tzPv7mcJMdEx1LbcIaCgk_0asHWK7cpSLuE23HDZAu7f4Tab0YgR2D83xyJN1ELik_ifq0cCYaKU-2iz0jDFgOHJ_cWaS7yEJIgpO7IyK0MWDJOUYsQyMxvCUz20ZE45ydCp9uoBGc0j-RQdrDX_gT3VlvDSZa1z7cmcJb63PxdZZnhWEi28N71Y86ThAKpl2NWe9-Q9l8WE6JIK8Fog7wYf-NFdoDEL_xjwHBhLO7')"}}></div>
              </div>
              <div className="px-1 flex flex-col justify-between">
                <div>
                  <p className="font-medium text-[13px] text-[#111111] line-clamp-1 mb-0.5">The Row</p>
                  <p className="text-[11px] text-[#666663] truncate mb-2">Margaux 15 皮革手提包</p>
                </div>
                <p className="font-medium text-[14px] text-[#111111] font-mono">¥ 38,500</p>
              </div>
            </div>
            
            <div className="group cursor-pointer bg-[#FFFFFF] rounded-sm overflow-hidden pb-3" onClick={() => navigate('/product')}>
              <div className="aspect-[4/5] relative bg-[#EFEFEB] overflow-hidden mb-3">
                <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuBxn-3jlW6S_StmsyDGnaHRti2PJV5n1WQNkD6qniDJwK0pqF3B5W8TYEtvsAyMQGgRqG4qISTvbAPpjkcuXD_z2p1yS_1ejIYOgFwkQsUuQWsxqVdZI0hlqwJkUw8DMH_q08ln977s6xm_fEo01YnoQkxrhIGui2CmhSa_0SkU3e2I7qxQsDdILdg4JhJmUuerQ2-Ej_aecAWs5-BgfgA2DeHvEL-8PtTF9-_Tlfmp8D_IhxLELKe_')"}}></div>
              </div>
              <div className="px-1 flex flex-col justify-between">
                <div>
                  <p className="font-medium text-[13px] text-[#111111] line-clamp-1 mb-0.5">Bottega Veneta</p>
                  <p className="text-[11px] text-[#666663] truncate mb-2">编织皮革切尔西靴</p>
                </div>
                <p className="font-medium text-[14px] text-[#111111] font-mono">¥ 11,800</p>
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* Floating AI Intent Input Bar - Above Bottom Nav */}
      <div className="fixed bottom-[80px] left-1/2 -translate-x-1/2 max-w-[430px] w-full z-40 px-4 pointer-events-none pb-safe">
        <div 
          className="bg-[#FFFFFF]/95 backdrop-blur-xl border border-[#E4E3DE] h-[52px] shadow-[0_8px_32px_rgba(0,0,0,0.10)] flex items-center px-4 pointer-events-auto cursor-text rounded-sm"
          onClick={() => navigate('/intent')}
        >
          <span className="text-[12px] text-[#111111] font-bold mr-3 uppercase tracking-widest">AI</span>
          <div className="w-full bg-transparent text-[14px] text-[#666663] flex-1 overflow-hidden whitespace-nowrap text-ellipsis font-light">
            输入或描述您在寻找的...
          </div>
          <div className="flex items-center gap-3 text-[#111111] ml-2">
            <button className="hover:opacity-80 flex items-center"><span className="material-symbols-outlined text-[20px] font-light">mic</span></button>
            <div className="w-[1px] h-4 bg-[#E4E3DE]"></div>
            <button 
              className="hover:opacity-80 flex items-center" 
              onClick={(e) => { 
                e.stopPropagation(); 
                navigate('/visual-search'); 
              }}
            >
              <span className="material-symbols-outlined text-[20px] font-light">lens_camera</span>
            </button>
          </div>
        </div>
      </div>

      <BottomNav />
    </div>
  );
}
"""
with open('src/pages/Explore.tsx', 'w') as f:
    f.write(explore_content)

private_content = """
import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function PrivateCuration() {
  const navigate = useNavigate();

  return (
    <div className="font-sans antialiased pb-10 pt-14 bg-[#F7F7F5] text-[#111111] min-h-screen">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#F7F7F5]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center text-[#111111] hover:opacity-80 transition-opacity cursor-pointer p-2 -ml-2" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <div className="font-serif text-[18px] tracking-widest text-[#111111] absolute left-1/2 -translate-x-1/2 pointer-events-none uppercase">Private</div>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="flex items-center text-[#111111] hover:opacity-80 transition-opacity cursor-pointer p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
          </div>
        </div>
      </header>

      <main className="w-full mx-auto px-4 mt-6">
        <div className="mb-10">
          <h1 className="font-serif text-[28px] text-[#111111] mb-2">私人精选</h1>
          <p className="text-[13px] text-[#666663]">
            基于您的风格偏好为您生成的专属推荐
          </p>
        </div>

        <section className="mb-10">
          <div className="flex justify-between items-end mb-4 border-b border-[#E4E3DE] pb-2">
            <h2 className="font-serif text-[20px] text-[#111111]">需要关注</h2>
            <span className="text-[11px] text-[#666663] uppercase tracking-widest">2 Items</span>
          </div>
          
          <div className="grid grid-cols-1 gap-3">
            <div className="bg-[#FFFFFF] p-4 rounded-sm relative group border border-[#E4E3DE] shadow-sm">
              <div className="absolute top-0 right-0 p-3">
                <span className="bg-[#111111] text-[#FFFFFF] text-[10px] px-2 py-1 uppercase tracking-widest rounded-sm">Restock / 补货</span>
              </div>
              <div className="flex items-center mb-4 mt-2">
                <div className="w-16 h-20 mr-4 bg-[#EFEFEB] rounded-sm overflow-hidden">
                  <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAYlN6lKjDkSkgpox5C6K4wTG7J7VkP_56-6EEM6QlC8vUdE_eM8V_q7TIZ1-E1ZwOS7vM2yNTqqT-Lsdta6WnzOjDm79xqhUY0UhATTVYH0V18ILrl2HS1xndkT_eIRFYxWl1CgzNOME7zvciMiHprw2wh6MqNKMyQyGYQIWzwftqLCLTezXcmv3dxSMV560Q3bh0X2sRCDbmKusXzfRG10lZ9RgOzUvm8-PZGKD713IJ3So0LNJx9" alt="Tote" />
                </div>
                <div>
                  <h3 className="font-medium text-[14px] text-[#111111] mb-1">经典皮革托特包</h3>
                  <p className="text-[12px] text-[#666663]">您收藏的颜色已补货</p>
                </div>
              </div>
              <button className="w-full border border-[#111111] bg-[#111111] text-white rounded-sm text-[13px] py-2.5 hover:bg-[#111111]/90 transition-colors">立即购买</button>
            </div>
          </div>
        </section>

        <section className="mb-6">
          <div className="flex justify-between items-end mb-4 border-b border-[#E4E3DE] pb-2">
            <h2 className="font-serif text-[20px] text-[#111111]">为您上新</h2>
          </div>
          
          <div className="grid grid-cols-1 gap-6">
            <div className="flex flex-col group cursor-pointer bg-[#FFFFFF] rounded-sm overflow-hidden border border-[#E4E3DE] pb-4" onClick={() => navigate('/product')}>
              <div className="aspect-[4/5] overflow-hidden mb-4 bg-[#EFEFEB] relative">
                <div className="absolute top-3 left-3 z-20 bg-white/90 backdrop-blur px-2 py-0.5 rounded-sm border border-[#E56A1D]">
                  <p className="text-[10px] text-[#E56A1D] uppercase font-bold tracking-widest">会员优先购</p>
                </div>
                <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBvnjeXrTvdYdonVeWiBW2XxNehwXQK9uPnKt9guDDZ-yk9krbCF8FcYd-WWKD3BKwer-6XhpgLl84wjh3v7JvQ_cc9ntccBLss0iY528pIKCwNOspqzUWfi98TB5xn7OHwa11B-OWzAgYBvGSddpB8_7a4JfdwDeSYqFF1weToskJXdVtP_upiP9YKtTotLxQ0Q_DzoqT8uIrxHtUjr_z4I_52OF6ArsLBrPm2auc6lMZPQE0Qr4Vy" alt="Model" />
                <div className="absolute bottom-3 left-3 right-3 z-20 bg-white/95 backdrop-blur px-3 py-2 rounded-sm border border-[#E4E3DE]">
                  <p className="text-[12px] text-[#111111] flex items-start">
                    <span className="material-symbols-outlined text-[16px] mr-1 mt-0.5">auto_awesome</span> 
                    <span><strong className="font-medium">推荐理由：</strong>符合您偏好的大地色系，且轮廓与您收藏过的多款风衣高度一致。</span>
                  </p>
                </div>
              </div>
              <div className="flex justify-between items-start px-4">
                <div>
                  <h3 className="font-medium text-[15px] text-[#111111]">定制羊毛大衣</h3>
                  <p className="text-[12px] text-[#666663] mt-1 uppercase tracking-widest">AW26 秋冬系列</p>
                </div>
                <span className="font-mono text-[15px] text-[#111111] font-medium">¥ 8,500</span>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
"""
with open('src/pages/PrivateCuration.tsx', 'w') as f:
    f.write(private_content)
    
member_content = """
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
"""
with open('src/pages/MemberCenter.tsx', 'w') as f:
    f.write(member_content)
    
profile_content = """
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
"""
with open('src/pages/Profile.tsx', 'w') as f:
    f.write(profile_content)
