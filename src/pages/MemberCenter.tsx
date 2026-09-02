import React from 'react';
import BottomNav from '../components/BottomNav';

export default function MemberCenter() {
  return (
    <div className="bg-surface text-on-surface flex flex-col min-h-screen">
      <header className="fixed top-0 left-0 w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full max-w-7xl mx-auto">
          <button className="relative z-10 text-primary hover:opacity-80 transition-opacity flex items-center justify-center p-2 -ml-2">
            <span className="material-symbols-outlined text-[24px]">menu</span>
          </button>
          <div className="font-display-hero text-[22px] tracking-tighter text-primary font-bold absolute left-1/2 -translate-x-1/2 pointer-events-none">UNIBUY</div>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-primary hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="flex-1 w-full max-w-[1200px] mx-auto pt-20 pb-24 px-4 flex flex-col gap-[24px]">
        <section className="flex flex-col gap-6">
          <h1 className="font-headline-lg-mobile text-[26px] md:font-headline-lg md:text-[30px] text-primary tracking-tight">会员中心</h1>
          <div className="relative bg-charcoal rounded-lg p-8 md:p-10 text-pure-white overflow-hidden shadow-2xl shadow-charcoal/10 flex flex-col justify-between min-h-[220px]">
            <div className="absolute top-0 left-0 w-full h-[1px] bg-[#E56A1D]"></div>
            <div className="flex justify-between items-start w-full relative z-10">
              <div className="flex flex-col gap-1">
                <span className="font-metadata text-[12px] text-secondary-fixed-dim uppercase tracking-widest">当前等级</span>
                <h2 className="font-display-hero text-[38px] tracking-tighter text-pure-white">黑卡</h2>
              </div>
              <span className="material-symbols-outlined text-[#E56A1D] fill text-[32px]">diamond</span>
            </div>
            <div className="flex flex-col gap-3 relative z-10 mt-12">
              <div className="flex justify-between items-end">
                <span className="font-metadata text-[12px] text-secondary-fixed-dim">下一等级：精英</span>
                <span className="font-price-tabular text-[18px]">68%</span>
              </div>
              <div className="w-full h-[2px] bg-white/20 relative">
                <div className="absolute top-0 left-0 h-full bg-[#E56A1D] w-[68%]"></div>
                <div className="absolute top-1/2 -translate-y-1/2 w-2 h-2 rounded-full bg-[#E56A1D] shadow-[0_0_8px_rgba(229,106,29,0.6)] left-[68%]"></div>
              </div>
            </div>
          </div>
        </section>

        <section className="flex flex-col gap-6">
          <div className="flex justify-between items-end border-b border-hairline pb-4">
            <h3 className="font-section-title text-[24px] text-primary">专享权益</h3>
            <span className="font-label-ui text-[14px] text-on-surface-variant hover:text-primary transition-colors cursor-pointer">全部权益</span>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div className="group relative overflow-hidden rounded-lg aspect-[4/3] md:aspect-auto md:h-64 cursor-pointer">
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuAbw5zqgCNeG8fokukhHPUHDxDXc-VX7vFZKIns9EPdLHeH1rL-G31Ujy3gsISxUrUwU8ocQxMQM8fbgyoMyEM1aRzC-brQL03N1MraHcgfbF4na1KtpqhGDkDQSRlbvSEkwdulPfJvcvqAaIqeQXxbewr64vOXmza6Mivv-54I6bv1el4iqtPuCTJH-GbWnuUossgT6CWyHRZRQrO-TmMHMhHIx-J0ElcSlMP_PUEjDpWj9x1KLctd')"}}></div>
              <div className="absolute inset-0 bg-gradient-to-t from-charcoal/80 via-charcoal/20 to-transparent"></div>
              <div className="absolute bottom-0 left-0 w-full p-6 flex flex-col gap-2">
                <div className="flex items-center gap-2">
                  <span className="material-symbols-outlined text-pure-white text-sm fill">flight_takeoff</span>
                  <span className="font-metadata text-[12px] text-pure-white uppercase tracking-widest">出行</span>
                </div>
                <h4 className="font-body-main text-[16px] text-pure-white font-medium">全球机场贵宾厅</h4>
              </div>
            </div>
            
            <div className="group relative overflow-hidden rounded-lg aspect-[4/3] md:aspect-auto md:h-64 cursor-pointer">
              <div className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105" style={{backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuDLfr0_J-RhpEmODx8FHEkg8O6CvxRGemQnnJk8o2xTcAItSmlb5D-SCL0shJPbWTCh7xN5YW62JiIBm__mK2LNme3PDHAIjJkd4l-E-PPZUZSmbPQFQQ7KQHipCRHnxpEvBJa9ckKgeu89XZWGDXd2uPjUENNdjMMEDo-6gbHw5MecBEkrIVmNr1r5G-9PqJvoJaACvBE98sJfABQVM3C8u2VSaVlA8goVAUzhy_WAMrYlwYTV6yYs')"}}></div>
              <div className="absolute inset-0 bg-gradient-to-t from-charcoal/80 via-charcoal/20 to-transparent"></div>
              <div className="absolute bottom-0 left-0 w-full p-6 flex flex-col gap-2">
                <div className="flex items-center gap-2">
                  <span className="material-symbols-outlined text-pure-white text-sm fill">theater_comedy</span>
                  <span className="font-metadata text-[12px] text-pure-white uppercase tracking-widest">体验</span>
                </div>
                <h4 className="font-body-main text-[16px] text-pure-white font-medium">私人预展邀请</h4>
              </div>
            </div>
          </div>
        </section>

        <section className="grid grid-cols-1 md:grid-cols-3 gap-3">
          <div className="md:col-span-2 border border-hairline rounded-lg p-6 flex flex-col gap-6 bg-pure-white">
            <div className="flex justify-between items-center">
              <h3 className="font-section-title text-[24px] text-primary">私人日程</h3>
              <button className="font-label-ui text-[14px] text-primary border border-hairline px-4 py-2 hover:bg-surface transition-colors rounded">查看完整日历</button>
            </div>
            <div className="flex flex-col gap-4">
              <div className="flex gap-4 p-4 border-l-2 border-[#E56A1D] bg-surface-container-low hover:bg-surface-container transition-colors cursor-pointer">
                <div className="flex flex-col justify-center items-center min-w-[48px]">
                  <span className="font-metadata text-[12px] text-on-surface-variant">OCT</span>
                  <span className="font-headline-lg-mobile text-[26px] text-primary">12</span>
                </div>
                <div className="flex flex-col justify-center gap-1">
                  <h4 className="font-body-main text-[16px] font-medium text-primary">2024 秋季高定私享会</h4>
                  <div className="flex items-center gap-2 font-metadata text-[12px] text-on-surface-variant">
                    <span className="material-symbols-outlined text-[14px]">schedule</span>
                    <span>14:00 - 17:00</span>
                    <span className="mx-1">·</span>
                    <span className="material-symbols-outlined text-[14px]">location_on</span>
                    <span>Shanghai, The Peninsula</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="border border-hairline rounded-lg p-6 flex flex-col justify-between gap-6 bg-pure-white relative overflow-hidden">
            <div className="flex flex-col gap-1">
              <span className="font-metadata text-[12px] text-on-surface-variant uppercase tracking-widest">专属顾问</span>
              <h3 className="font-section-title text-[24px] text-primary">Eleanor</h3>
            </div>
            <div className="flex items-center gap-4">
              <img className="w-16 h-16 rounded-full object-cover border border-hairline" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBuWsNMqM4gAo4c2tVkdXX2SAuN4v2kjYxLI-pR83bCnPniEFMbILmDVsHpgpqrQI96uVOkEsL7ynDdmQo9jpX3qdZvHPwkY7CxGqx2bi4ozcscac3GRdyL0En5G-7i-Umg6wdsONfoHd3UcW8lDE2ODvhMa3ENpXvYrTB2Of8CKKOEjXZ8IW9RayQGLPXtKDEVKOcMiZnqLOMJCq3ze2M7bO5JyXKSsCxcdnvu6jjGoDdRXLR4YRPY" alt="Advisor" />
              <div className="flex flex-col">
                <span className="font-label-ui text-[14px] text-primary">高级生活管家</span>
                <span className="font-metadata text-[12px] text-on-surface-variant">为您提供全天候定制服务</span>
              </div>
            </div>
            <button className="w-full py-3 bg-[#E56A1D] text-primary font-label-ui text-[14px] rounded hover:opacity-90 transition-opacity flex justify-center items-center gap-2">
              <span className="material-symbols-outlined text-[18px]">chat_bubble</span>
              联系顾问
            </button>
          </div>
        </section>
      </main>

      <BottomNav />
    </div>
  );
}
