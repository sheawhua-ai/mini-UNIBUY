import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function Compare() {
  const navigate = useNavigate();

  return (
    <div className="antialiased pb-[120px] font-body-main text-[16px] bg-surface text-on-surface min-h-screen">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline transition-transform duration-200">
        <div className="relative flex justify-between items-center px-4 h-14 w-full max-w-7xl mx-auto">
          <button className="relative z-10 text-primary hover:opacity-80 transition-opacity flex items-center justify-center p-2 -ml-2" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <div className="font-display-hero text-[22px] tracking-tighter text-primary font-bold absolute left-1/2 -translate-x-1/2 pointer-events-none">UNIBUY</div>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto pt-24">
        <section className="px-5 mb-8">
          <div className="flex items-center gap-2 mb-4">
            <span className="font-metadata text-[12px] text-primary border border-primary px-2 py-1 rounded-sm uppercase tracking-widest">AI Analysis</span>
            <div className="h-[1px] bg-hairline flex-grow"></div>
          </div>
          <h1 className="font-section-title text-[24px] text-primary mb-2">商务差旅、低 Logo 对比</h1>
          <p className="text-on-surface-variant text-[16px]">基于您的偏好，AI 已提取 3 款符合“低调、高容量、适合短期商务出行”的高级皮具进行深度维度对比。</p>
        </section>

        <div className="w-full overflow-x-auto hide-scrollbar border-y border-hairline bg-surface-container-lowest">
          <div className="min-w-[800px]">
            <div className="grid grid-cols-4 gap-4 px-5 py-6 border-b border-hairline items-end">
              <div className="col-span-1 pb-4">
                <span className="font-metadata text-[12px] text-on-surface-variant uppercase tracking-wider">对比维度</span>
              </div>
              
              <div className="col-span-1 flex flex-col gap-3" onClick={() => navigate('/product')}>
                <div className="relative w-full aspect-[4/5] bg-surface-container flex items-center justify-center overflow-hidden rounded-sm group cursor-pointer">
                  <img className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-500" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDWHyGl7M9C0hMl9-3YQNOLtKD1eavYxpJXxt6mVuFcJr1LABS_jkna6-RLrch8zH1ouVZizrkgqsqzvPbaEJ-YVa92Eyb82YJAeScsQmqMRtcDE8U2afGU0y99uDWWRoj2m3AjV_d9VVy0s7QyN7zg95egHmbFmskLVNnKA-7MOLu7yq8xCMGujtr9evGM3pC2q920kaPAT15oOFJXShjpOViwpw30eHuKgSSIcJkuQm4OxEwDzLAs" alt="Bag 1" />
                  <div className="absolute top-2 left-2 bg-primary text-pure-white font-metadata text-[12px] px-2 py-0.5 rounded-sm">AI 首选</div>
                </div>
                <div>
                  <h3 className="font-label-ui text-[14px] text-primary line-clamp-1">The Minimalist Brief</h3>
                  <p className="font-price-tabular text-[18px] text-on-surface-variant mt-1">¥ 18,500</p>
                  <div className="flex items-center gap-1 mt-1 text-on-surface-variant">
                    <span className="material-symbols-outlined text-[14px]">check_circle</span>
                    <span className="font-metadata text-[12px]">现货</span>
                  </div>
                </div>
              </div>

              <div className="col-span-1 flex flex-col gap-3" onClick={() => navigate('/product')}>
                <div className="relative w-full aspect-[4/5] bg-surface-container flex items-center justify-center overflow-hidden rounded-sm group cursor-pointer">
                  <img className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-500" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDZC7X3M0GOFrAC73vu6q1hqeYE2GjcYoKbOZLMOTsOY8VaU9XWdzAUP5BZd95qr_X1OE_odzQNAP4wliqj9jzCGmYyEXYeT7y5eDaEmc3YhKVLW-WD8mtHAvX-NmIpPAZCMeluJdFIZNIKrWxsXBczefVct0CZhaUew9-apnkZfZUCOG1ACvJOIdWUfVqa__ZYAic5zZC9SfAD1N4O8SS6NWrwhyGuth8VNvrckiI2Lz5zIpIx3fkv" alt="Bag 2" />
                </div>
                <div>
                  <h3 className="font-label-ui text-[14px] text-primary line-clamp-1">Classic Overnighter</h3>
                  <p className="font-price-tabular text-[18px] text-on-surface-variant mt-1">¥ 22,300</p>
                  <div className="flex items-center gap-1 mt-1 text-[#E56A1D]">
                    <span className="material-symbols-outlined text-[14px]">warning</span>
                    <span className="font-metadata text-[12px]">仅剩 2 件</span>
                  </div>
                </div>
              </div>

              <div className="col-span-1 flex flex-col gap-3" onClick={() => navigate('/product')}>
                <div className="relative w-full aspect-[4/5] bg-surface-container flex items-center justify-center overflow-hidden rounded-sm group cursor-pointer">
                  <img className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-500" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCMFuE4u2EjLy_BjdXpi5vRqfEOIWa5-17xhGhIJVOs54jp1oWgtsdtC-fU0PJAhjNPXwwYSKvjRUbZ8Dld9WDPktO9WbmeaRSzr6lqNAwCUDBhtfcC5Hx3AYxYgGieyyHwsrdB2ds28ZXHzF9IOyLdQ0EOmbj8OZda5XV2X2jzg8NJKi722-BhPSA0KJvFyw7lWByfIPRHpGoPe6fvifVqUCq37o1rXvSoJunI13C2BNT3Ol_Z02tl" alt="Bag 3" />
                </div>
                <div>
                  <h3 className="font-label-ui text-[14px] text-primary line-clamp-1">Architect Tote</h3>
                  <p className="font-price-tabular text-[18px] text-on-surface-variant mt-1">¥ 16,800</p>
                  <div className="flex items-center gap-1 mt-1 text-on-surface-variant">
                    <span className="material-symbols-outlined text-[14px]">local_shipping</span>
                    <span className="font-metadata text-[12px]">3天内发货</span>
                  </div>
                </div>
              </div>
            </div>

            <div className="grid grid-cols-4 gap-4 px-5 py-4 border-b border-hairline items-center hover:bg-surface-container-low transition-colors">
              <div className="col-span-1 font-label-ui text-[14px] text-on-surface-variant">重量</div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">0.9 kg <span className="text-on-surface-variant text-sm ml-1">(最轻)</span></div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">1.4 kg</div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">1.1 kg</div>
            </div>

            <div className="grid grid-cols-4 gap-4 px-5 py-4 border-b border-hairline items-center hover:bg-surface-container-low transition-colors">
              <div className="col-span-1 font-label-ui text-[14px] text-on-surface-variant">容量</div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">13寸笔电 + 文件</div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">衣物(1天) + 15寸笔电</div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">15寸笔电 + 杂物</div>
            </div>

            <div className="grid grid-cols-4 gap-4 px-5 py-4 border-b border-hairline items-center hover:bg-surface-container-low transition-colors">
              <div className="col-span-1 font-label-ui text-[14px] text-on-surface-variant">材质</div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">Epi 压纹牛皮</div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">Taurillon 颗粒牛皮</div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">光滑小牛皮</div>
            </div>

            <div className="grid grid-cols-4 gap-4 px-5 py-4 items-center hover:bg-surface-container-low transition-colors">
              <div className="col-span-1 font-label-ui text-[14px] text-on-surface-variant">交付期</div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">现货闪送 (同城)</div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">门店自提 / 顺丰</div>
              <div className="col-span-1 font-body-main text-[16px] text-primary">预定 (3-5工作日)</div>
            </div>
          </div>
        </div>

        <section className="px-5 mt-12 mb-20">
          <h2 className="font-headline-lg-mobile text-[26px] text-primary mb-6">AI 深度洞察</h2>
          <div className="grid grid-cols-1 gap-4">
            <div className="p-6 border border-hairline bg-pure-white rounded-sm">
              <div className="flex items-center gap-2 mb-3 text-primary">
                <span className="material-symbols-outlined fill">star</span>
                <h3 className="font-label-ui text-[14px] font-bold">最符合预期</h3>
              </div>
              <p className="text-on-surface-variant text-[16px]"><strong>The Minimalist Brief</strong> 完全摒弃外部 Logo，Epi 压纹防刮耐磨，0.9kg 极致轻量化，完美契合高频差旅的实用需求与低调审美。</p>
            </div>
            <div className="p-6 border border-hairline bg-pure-white rounded-sm">
              <div className="flex items-center gap-2 mb-3 text-primary">
                <span className="material-symbols-outlined">flight_takeoff</span>
                <h3 className="font-label-ui text-[14px] font-bold">更具功能性</h3>
              </div>
              <p className="text-on-surface-variant text-[16px]">若有偶发的过夜需求，<strong>Classic Overnighter</strong> 虽自重略大（1.4kg），但其颗粒牛皮质感更为奢华，且足以容纳一套换洗衣物。</p>
            </div>
            <div className="p-6 border border-hairline bg-pure-white rounded-sm">
              <div className="flex items-center gap-2 mb-3 text-primary">
                <span className="material-symbols-outlined">diamond</span>
                <h3 className="font-label-ui text-[14px] font-bold">更具收藏性</h3>
              </div>
              <p className="text-on-surface-variant text-[16px]"><strong>Architect Tote</strong> 的结构感最强，采用稀有工坊的光滑小牛皮，随着使用岁月会呈现独特光泽，适合追求极致材质工艺的藏家。</p>
            </div>
          </div>
          <div className="mt-8 flex items-center justify-end text-on-surface-variant">
            <span className="material-symbols-outlined text-[16px] mr-1">update</span>
            <span className="font-metadata text-[12px]">数据更新于: 2024-05-20 14:32</span>
          </div>
        </section>
      </main>

      <div className="fixed bottom-0 w-full z-40 bg-surface/90 backdrop-blur-2xl border-t border-hairline pb-safe absolute">
        <div className="flex justify-between items-center h-20 w-full px-5 max-w-7xl mx-auto gap-4">
          <button className="flex-1 h-12 flex items-center justify-center gap-2 border border-primary text-primary font-label-ui text-[14px] rounded-sm hover:bg-surface-container-low transition-colors">
            <span className="material-symbols-outlined text-[18px]">support_agent</span>
            咨询私人顾问
          </button>
          <button onClick={() => navigate('/product')} className="flex-1 h-12 flex items-center justify-center gap-2 bg-primary text-pure-white font-label-ui text-[14px] rounded-sm hover:bg-charcoal transition-colors">
            查看最匹配单品
            <span className="material-symbols-outlined text-[18px]">arrow_forward</span>
          </button>
        </div>
      </div>
    </div>
  );
}
