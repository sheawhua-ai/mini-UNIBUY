import React from 'react';
import BottomNav from '../components/BottomNav';

export default function Profile() {
  return (
    <div className="bg-background text-on-surface font-body-main antialiased pb-24 min-h-screen">
      <header className="fixed top-0 left-0 w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full max-w-7xl mx-auto">
          <button className="relative z-10 hover:opacity-80 transition-opacity flex items-center justify-center p-2 -ml-2">
            <span className="material-symbols-outlined text-primary text-[24px]">menu</span>
          </button>
          <h1 className="font-display-hero text-[22px] tracking-tighter text-primary font-bold absolute left-1/2 -translate-x-1/2 pointer-events-none">UNIBUY</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-primary hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="pt-20 px-4 max-w-[1200px] mx-auto pb-24">
        <section className="mb-[24px] flex items-center space-x-6">
          <div className="relative">
            <img className="w-16 h-16 rounded-full object-cover border border-hairline shadow-sm" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCfOZspri41H5IB5p-ksqybt0UwbGrpLbIbKXxg09N_78OpqXG_ZQZ5p_0Z5GuK8xYIrpps0o1ZQ-LH_DzAFGO5_14rQ737no5loSTACV--y5NiIr7H8SsBZCZt8_C5Awcmxzjk-be4ooacTRieN6zh8jDDYXfcDCIqEjM46ALAjM4UOx1sGoBSCeReQuVKf5R3GhwdCqpgRSrlfFub8hJLew967EgGJ5OtvHqnH9ug34Byl7KqWJ2d" alt="Profile" />
          </div>
          <div>
            <h2 className="font-headline-lg-mobile text-[26px] text-on-surface">林女士</h2>
            <div className="mt-2 flex items-center space-x-2">
              <span className="bg-charcoal text-pure-white px-2 py-1 font-metadata text-[12px] tracking-widest uppercase">黑卡会员</span>
            </div>
          </div>
        </section>

        <section className="mb-[32px]">
          <div className="flex justify-between items-end mb-6">
            <h3 className="font-section-title text-[24px] text-on-surface">我的订单</h3>
            <span className="font-label-ui text-[14px] text-on-surface-variant hover:text-primary transition-colors flex items-center cursor-pointer">
              全部 <span className="material-symbols-outlined text-[16px] ml-1">chevron_right</span>
            </span>
          </div>
          <div className="grid grid-cols-4 gap-4 mb-6">
            <div className="flex flex-col items-center justify-center space-y-2 cursor-pointer hover:opacity-80 transition-opacity">
              <span className="material-symbols-outlined text-[28px] text-primary">account_balance_wallet</span>
              <span className="font-metadata text-[12px] text-on-surface">待支付</span>
            </div>
            <div className="flex flex-col items-center justify-center space-y-2 cursor-pointer hover:opacity-80 transition-opacity">
              <span className="material-symbols-outlined text-[28px] text-primary">pending_actions</span>
              <span className="font-metadata text-[12px] text-on-surface">处理中</span>
            </div>
            <div className="flex flex-col items-center justify-center space-y-2 cursor-pointer hover:opacity-80 transition-opacity relative">
              <span className="material-symbols-outlined text-[28px] text-primary">local_shipping</span>
              <span className="font-metadata text-[12px] text-on-surface">配送中</span>
              <div className="absolute top-0 right-2 w-2 h-2 bg-[#E56A1D] rounded-full"></div>
            </div>
            <div className="flex flex-col items-center justify-center space-y-2 cursor-pointer hover:opacity-80 transition-opacity">
              <span className="material-symbols-outlined text-[28px] text-primary">support_agent</span>
              <span className="font-metadata text-[12px] text-on-surface">售后</span>
            </div>
          </div>
          <div className="border border-hairline p-4 flex items-center space-x-4 bg-pure-white">
            <img className="w-16 h-20 object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDF0oT5FqU47yKPTpFSCxXPkRsX_mH61CgIHxjhZbUKHrjEqV_cSPfV6e4e2hi7PrXv4ulW7p_E92AZvBwkG9WJxDmdfvRelFVxp5k1aKZWPQsuLHNllMg1bWy1jW8Aebu69vdUPagx77DQdwNoF4j9zn7D3ckpL-IutSo1AQP6bax7JKu4JMXdImMXbA4txPFq6RXjdAC9U3MrDWeQ7BA-FZc4u1ZaCGd2FOO4k_zsaNO1bSlWeaoJ" alt="Order" />
            <div className="flex-1">
              <p className="font-metadata text-[12px] text-[#E56A1D] mb-1">正在派送中</p>
              <p className="font-body-main text-[16px] text-on-surface line-clamp-1">Hermès Birkin 25 Togo 黑银</p>
              <p className="font-metadata text-[12px] text-on-surface-variant mt-1">预计今日 14:00 - 16:00 送达</p>
            </div>
            <span className="material-symbols-outlined text-on-surface-variant">chevron_right</span>
          </div>
        </section>

        <hr className="border-hairline mb-[32px] w-full" />

        <section className="mb-[32px]">
          <div className="grid grid-cols-2 gap-3">
            <div className="border border-hairline p-6 bg-pure-white flex flex-col items-start hover:shadow-sm transition-shadow cursor-pointer">
              <span className="material-symbols-outlined text-[24px] text-primary mb-4">favorite</span>
              <h4 className="font-label-ui text-[14px] text-on-surface">收藏</h4>
              <p className="font-metadata text-[12px] text-on-surface-variant mt-1">12 件单品</p>
            </div>
            <div className="border border-hairline p-6 bg-pure-white flex flex-col items-start hover:shadow-sm transition-shadow cursor-pointer">
              <span className="material-symbols-outlined text-[24px] text-primary mb-4">calendar_today</span>
              <h4 className="font-label-ui text-[14px] text-on-surface">预约</h4>
              <p className="font-metadata text-[12px] text-on-surface-variant mt-1">私人预览 & 门店</p>
            </div>
            <div className="border border-hairline p-6 bg-pure-white flex flex-col items-start hover:shadow-sm transition-shadow cursor-pointer">
              <span className="material-symbols-outlined text-[24px] text-primary mb-4">verified</span>
              <h4 className="font-label-ui text-[14px] text-on-surface">鉴定</h4>
              <p className="font-metadata text-[12px] text-on-surface-variant mt-1">数字证书</p>
            </div>
            <div className="border border-hairline p-6 bg-pure-white flex flex-col items-start hover:shadow-sm transition-shadow cursor-pointer">
              <span className="material-symbols-outlined text-[24px] text-primary mb-4">tune</span>
              <h4 className="font-label-ui text-[14px] text-on-surface">偏好</h4>
              <p className="font-metadata text-[12px] text-on-surface-variant mt-1">AI 个性化设置</p>
            </div>
          </div>
        </section>

        <hr className="border-hairline mb-[32px] w-full" />

        <section className="mb-[32px] pb-12">
          <h3 className="font-section-title text-[24px] text-on-surface mb-6">AI 记住的偏好</h3>
          <div className="space-y-6">
            <div>
              <h4 className="font-label-ui text-[14px] text-on-surface-variant uppercase tracking-widest mb-3">尺码</h4>
              <div className="flex flex-wrap gap-2">
                <span className="border-b border-[#E56A1D] px-4 py-2 font-metadata text-[12px] text-primary">上装: M (38)</span>
                <span className="border-b border-[#E56A1D] px-4 py-2 font-metadata text-[12px] text-primary">鞋履: 39 IT</span>
                <span className="border-b border-[#E56A1D] px-4 py-2 font-metadata text-[12px] text-primary">戒指: 52</span>
              </div>
            </div>
            <div>
              <h4 className="font-label-ui text-[14px] text-on-surface-variant uppercase tracking-widest mb-3">材质偏好</h4>
              <div className="flex flex-wrap gap-2">
                <span className="border border-hairline px-4 py-2 font-metadata text-[12px] text-on-surface bg-surface-container">羊绒</span>
                <span className="border border-hairline px-4 py-2 font-metadata text-[12px] text-on-surface bg-surface-container">真丝</span>
                <span className="border border-hairline px-4 py-2 font-metadata text-[12px] text-on-surface bg-surface-container">Togo牛皮</span>
              </div>
            </div>
            <div>
              <h4 className="font-label-ui text-[14px] text-on-surface-variant uppercase tracking-widest mb-3">避免</h4>
              <div className="flex flex-wrap gap-2">
                <span className="border border-hairline px-4 py-2 font-metadata text-[12px] text-on-surface-variant line-through opacity-70">大面积 Logo</span>
                <span className="border border-hairline px-4 py-2 font-metadata text-[12px] text-on-surface-variant line-through opacity-70">荧光色</span>
                <span className="border border-hairline px-4 py-2 font-metadata text-[12px] text-on-surface-variant line-through opacity-70">粗花呢</span>
              </div>
            </div>
          </div>
        </section>
      </main>

      <BottomNav />
    </div>
  );
}
