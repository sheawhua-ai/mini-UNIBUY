const fs = require('fs');

let homeContent = `
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="relative min-h-screen pb-20 overflow-x-hidden bg-background text-on-surface">
      {/* TopAppBar */}
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-surface/90 backdrop-blur-xl border-b border-hairline">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button aria-label="Menu" className="relative z-10 text-primary hover:opacity-80 transition-transform active:scale-95 duration-200 p-2 -ml-2">
            <span className="material-symbols-outlined text-[24px]">menu</span>
          </button>
          <h1 className="font-display-hero text-[20px] tracking-tighter text-primary absolute left-1/2 -translate-x-1/2 pointer-events-none font-bold">UNIBUY</h1>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button aria-label="Shopping Bag" className="text-primary hover:opacity-80 transition-transform active:scale-95 duration-200 p-2">
              <span className="material-symbols-outlined text-[22px]">shopping_bag</span>
            </button>
            <div className="w-[87px] h-[32px] shrink-0 rounded-full border border-outline-variant flex items-center justify-between px-3 bg-surface-container-lowest/50 backdrop-blur-md"><span className="material-symbols-outlined text-[18px] text-primary">more_horiz</span><div className="w-[1px] h-4 bg-outline-variant"></div><span className="material-symbols-outlined text-[16px] text-primary">radio_button_unchecked</span></div>
          </div>
        </div>
      </header>

      <main className="w-full mt-14 flex flex-col">
        {/* Search / AI Bar */}
        <div className="px-4 py-3 bg-surface z-20 sticky top-14 shadow-sm">
          <div 
            className="bg-surface-container-lowest border border-hairline rounded-full flex items-center px-4 h-10 cursor-text"
            onClick={() => navigate('/intent')}
          >
            <span className="material-symbols-outlined text-[18px] text-on-surface-variant mr-2">search</span>
            <div className="w-full bg-transparent font-body-main text-[13px] text-on-surface-variant flex-1 overflow-hidden whitespace-nowrap text-ellipsis">
              帮我找适合商务差旅的电脑包...
            </div>
            <span className="material-symbols-outlined text-[18px] text-primary ml-2">psychiatry</span>
          </div>
        </div>

        {/* Hero Banner */}
        <section className="px-4 py-2">
          <div 
            className="w-full aspect-[21/9] rounded-xl bg-cover bg-center overflow-hidden relative flex items-center px-6"
            style={{ backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuArjtrVE2lG4P8GVPHflyWb0Mo5SVTyYRhEKICWp9dXBZfgpnNrEjMm6dtbb5AIQEJulXtvOM2xsrCwwNtXTUGD-ijZT4Ysg_qC8E06uX1B8BvShZ3crQWafJlSTskDHLbYcvpzUhub0jJs9GzUV15SSZE3qvn2mQV6vrwfgxBhaFpM6nYybFKKT4dA7wbrIK7HlkPDWs23ehSoCcEl9zupcOvb1U6484cHAiBp62KwkzvTEDpq6g1U')" }}
          >
             <div className="absolute inset-0 bg-black/20"></div>
             <div className="relative z-10 text-white">
                <h2 className="font-bold text-[20px] mb-1">秋季旅行指南</h2>
                <p className="text-[12px] opacity-90">探索甄选出行装备</p>
             </div>
          </div>
        </section>

        {/* Quick Links / Categories */}
        <section className="px-4 py-4 grid grid-cols-4 gap-4">
           {[
             { name: '随心逛', icon: 'explore', path: '/explore' },
             { name: '私人精选', icon: 'diamond', path: '/private' },
             { name: '视觉搜索', icon: 'image_search', path: '/visual-search' },
             { name: '会员中心', icon: 'workspace_premium', path: '/member' }
           ].map((item, i) => (
             <div key={i} className="flex flex-col items-center gap-1 cursor-pointer" onClick={() => navigate(item.path)}>
                <div className="w-12 h-12 rounded-full bg-mist flex items-center justify-center text-primary mb-1">
                  <span className="material-symbols-outlined">{item.icon}</span>
                </div>
                <span className="text-[11px] font-medium text-on-surface">{item.name}</span>
             </div>
           ))}
        </section>

        {/* Product Grid */}
        <section className="px-4 py-4 bg-surface-container-lowest mt-2 rounded-t-2xl">
          <div className="flex justify-between items-center mb-4">
            <h3 className="font-bold text-[16px] text-primary">为你推荐</h3>
          </div>
          
          <div className="grid grid-cols-2 gap-3">
            {[
              { title: 'Noir Signature Tote', material: '全粒面牛皮', price: '¥ 8,500', img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw', tag: '上新' },
              { title: 'Voyageur Weekender', material: '防水帆布', price: '¥ 12,200', img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuALof-gjivI7JLbQxwFhG0FSCgL57IKvGoctb1bjLRjNyskfyOXxx2LwUwL65EttBmLlToJJyCmfdFB-0xdIvj2MQ0cA-YZqLB0TAiIbiBcnn9TuUrHtR3qWLMAa2K55d8ZpKnVvO7fki0iijcCiOGkAJWAnkhvz46UglO3JZ9IsgfdDHiKKQeGzjB7BI9NTt2uqI9JX55f4acEcI5bwju3mm5HLg6LOECdhukAeJWJLsxXMYr7kAu1', tag: '独家' },
              { title: 'Classic Leather Briefcase', material: '头层牛皮', price: '¥ 6,800', img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuB2yK2D_eL8v88K_l2M7v4L_H-uY_o98Y9L_45_E_93L_Q_M_25V_o_8-9V-v7C_3Z5274_H11G1C2_11V4T5X_G-Y2v27N8P5G3M-3O2Y72382_J0-T1I2A039U_R1S8W_1', tag: '热销' },
              { title: 'Urban Backpack', material: '尼龙拼接', price: '¥ 4,500', img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuC1P1T8G9x2T3v1Z3w9F_M-M2Z72236P4I-M3U7T_2_N_V3_6234M_N-L55Z_7_9P2O3X-N7I03_G5_V3Q_K4X_W4E_S1L5X3_K_M-Q3Q933_T3T7P-X4W2R_R2N4U1V-5', tag: '推荐' }
            ].map((prod, i) => (
              <article key={i} className="flex flex-col group cursor-pointer bg-pure-white rounded-lg overflow-hidden shadow-sm border border-hairline" onClick={() => navigate('/product')}>
                <div className="w-full aspect-square bg-surface-container-lowest overflow-hidden relative bg-cover bg-center" style={{ backgroundImage: `url('${prod.img}')` }}>
                  <div className="absolute top-2 left-2 bg-white/90 backdrop-blur px-2 py-0.5 rounded text-[10px] font-medium text-primary">
                    {prod.tag}
                  </div>
                </div>
                <div className="p-3 flex flex-col">
                  <h4 className="font-bold text-[13px] text-primary mb-1 line-clamp-1">{prod.title}</h4>
                  <p className="text-[11px] text-on-surface-variant mb-2">{prod.material}</p>
                  <p className="font-semibold text-[14px] text-primary">{prod.price}</p>
                </div>
              </article>
            ))}
          </div>
        </section>
      </main>
      <BottomNav />
    </div>
  );
}
`

fs.writeFileSync('src/pages/Home.tsx', homeContent);
console.log("Done Home");
