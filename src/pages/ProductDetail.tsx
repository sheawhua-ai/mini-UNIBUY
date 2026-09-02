import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

export default function ProductDetail() {
  const navigate = useNavigate();
  const location = useLocation();
  const [isFavorite, setIsFavorite] = useState(false);
  
  // Accept product from state, or fallback to default Bag
  const product = location.state || { 
    type: 'bag', 
    brand: 'THE ROW', 
    name: 'Margaux 15 皮革手提包', 
    price: '¥35,500 起', 
    img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw', 
    skus: { colors: ['黑色', '棕色', '大象灰'], sizes: ['15', '17'] },
    fulfillments: [
      { id: 'ovs', label: '海外发货 (意大利)', price: '¥35,500', eta: '预计 7-14 工作日', icon: 'flight_takeoff' },
      { id: 'dom', label: '中国大陆发货 (上海)', price: '¥38,500', eta: '预计 1-3 工作日', icon: 'local_shipping' }
    ],
    desc: '经典倒梯形托特包，采用细腻光泽的全粒面小牛皮制成。顶部搭扣开合，侧边束带设计。宽敞的内部空间足够收纳您的日常所需。'
  };

  const [selectedColor, setSelectedColor] = useState(product.skus.colors[0]);
  const [selectedSize, setSelectedSize] = useState(product.skus.sizes[0]);
  const [selectedFulfillment, setSelectedFulfillment] = useState(product.fulfillments[0]);

  return (
    <div className="bg-[#FFFFFF] text-[#111111] font-sans antialiased min-h-screen pb-[100px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button onClick={() => navigate(-1)} className="relative z-10 text-[#111111] hover:opacity-80 transition-opacity p-2 -ml-2">
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <div className="relative z-10 flex items-center gap-2 shrink-0">
            <button className="text-[#111111] hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[22px]">share</span>
            </button>
            <button className="text-[#111111] hover:opacity-80 transition-opacity p-2 -mr-2" onClick={() => setIsFavorite(!isFavorite)}>
              <span className={`material-symbols-outlined text-[22px] ${isFavorite ? 'fill text-[#E56A1D]' : ''}`}>favorite</span>
            </button>
          </div>
        </div>
      </header>

      <main className="pt-14 flex flex-col w-full">
        {/* Product Image Gallery */}
        <section className="w-full aspect-[4/5] bg-[#EFEFEB] relative overflow-hidden">
          <img className="w-full h-full object-cover" src={product.img} alt={product.name} />
          <div className="absolute bottom-4 right-4 bg-[#FFFFFF]/90 backdrop-blur px-2 py-1 text-[11px] font-mono rounded-sm shadow-sm">
            1 / 5
          </div>
        </section>

        {/* Product Meta */}
        <section className="px-5 pt-6 pb-4 flex flex-col">
          <h1 className="font-bold text-[18px] text-[#111111] uppercase tracking-wide mb-1">{product.brand}</h1>
          <p className="text-[14px] text-[#666663] mb-4">{product.name}</p>
          {/* Dynamic price based on selected fulfillment */}
          <p className="font-mono text-[22px] font-medium text-[#111111] transition-all">{selectedFulfillment.price}</p>
        </section>

        {/* SKU Selector: Fulfillment Origin (Dynamic Price Driver) */}
        <section className="px-5 py-4 border-t border-[#E4E3DE]">
          <div className="flex justify-between items-end mb-3">
            <span className="text-[13px] font-medium text-[#111111]">发货版本 <span className="text-[#666663] font-normal ml-1">不同产地价格可能浮动</span></span>
          </div>
          <div className="flex flex-col gap-2.5">
            {product.fulfillments.map((f: any, i: number) => (
              <button 
                key={i} 
                onClick={() => setSelectedFulfillment(f)}
                className={`flex items-center justify-between p-3.5 border transition-all rounded-sm text-left ${selectedFulfillment.id === f.id ? 'border-[#111111] bg-[#F7F7F5] shadow-sm' : 'border-[#E4E3DE] bg-[#FFFFFF] hover:border-[#111111]/40'}`}
              >
                <div className="flex items-center gap-3">
                  <span className={`material-symbols-outlined text-[20px] ${selectedFulfillment.id === f.id ? 'text-[#111111]' : 'text-[#666663]'}`}>
                    {f.icon}
                  </span>
                  <div className="flex flex-col">
                    <span className={`text-[13px] font-medium ${selectedFulfillment.id === f.id ? 'text-[#111111]' : 'text-[#666663]'}`}>{f.label}</span>
                    <span className="text-[11px] text-[#666663] mt-0.5">{f.eta}</span>
                  </div>
                </div>
                <span className={`font-mono text-[14px] font-medium ${selectedFulfillment.id === f.id ? 'text-[#111111]' : 'text-[#666663]'}`}>{f.price}</span>
              </button>
            ))}
          </div>
        </section>

        {/* SKU Selector: Colors */}
        <section className="px-5 py-6 border-t border-[#E4E3DE]">
          <div className="flex justify-between items-end mb-3">
            <span className="text-[13px] font-medium text-[#111111]">颜色: <span className="text-[#666663] font-normal">{selectedColor}</span></span>
          </div>
          <div className="flex flex-wrap gap-2.5">
            {product.skus.colors.map((c: string, i: number) => (
              <button 
                key={i} 
                onClick={() => setSelectedColor(c)}
                className={`px-4 py-2.5 text-[12px] rounded-sm border transition-colors ${selectedColor === c ? 'border-[#111111] bg-[#111111] text-[#FFFFFF]' : 'border-[#E4E3DE] bg-[#FFFFFF] text-[#111111] hover:border-[#111111]'}`}
              >
                {c}
              </button>
            ))}
          </div>
        </section>

        {/* SKU Selector: Sizes */}
        <section className="px-5 py-6 border-t border-b border-[#E4E3DE]">
          <div className="flex justify-between items-end mb-3">
            <span className="text-[13px] font-medium text-[#111111]">尺码</span>
            <button className="text-[11px] text-[#666663] underline underline-offset-2">尺码指南</button>
          </div>
          <div className="flex flex-wrap gap-2">
            {product.skus.sizes.map((s: string, i: number) => (
              <button 
                key={i} 
                onClick={() => setSelectedSize(s)}
                className={`min-w-[56px] h-[40px] flex items-center justify-center text-[13px] font-mono rounded-sm border transition-colors ${selectedSize === s ? 'border-[#111111] bg-[#111111] text-[#FFFFFF]' : 'border-[#E4E3DE] bg-[#FFFFFF] text-[#111111] hover:border-[#111111]'}`}
              >
                {s}
              </button>
            ))}
          </div>
        </section>

        {/* Details & Accordions */}
        <section className="px-5 py-6">
          <h3 className="font-medium text-[14px] text-[#111111] mb-3">商品详情</h3>
          <p className="text-[13px] text-[#666663] leading-relaxed mb-6">
            {product.desc}
          </p>

          <div className="flex flex-col border-t border-[#E4E3DE]">
            <details className="group cursor-pointer">
              <summary className="flex justify-between items-center py-4 text-[14px] font-medium text-[#111111] list-none outline-none">
                材质与保养
                <span className="material-symbols-outlined text-[#666663] group-open:rotate-180 transition-transform">expand_more</span>
              </summary>
              <div className="pb-4 text-[13px] text-[#666663] leading-relaxed">
                主体采用顶级材质。建议由专业机构进行清洁与保养，避免长时间接触水或阳光直射。
              </div>
            </details>
            <details className="group cursor-pointer border-t border-[#E4E3DE]">
              <summary className="flex justify-between items-center py-4 text-[14px] font-medium text-[#111111] list-none outline-none">
                配送与退货
                <span className="material-symbols-outlined text-[#666663] group-open:rotate-180 transition-transform">expand_more</span>
              </summary>
              <div className="pb-4 text-[13px] text-[#666663] leading-relaxed">
                全球免费标准配送。您可在收到商品后 14 天内申请无理由退换货（需保证商品全新且标签完整）。
              </div>
            </details>
          </div>
        </section>

        {/* Personal Advisor */}
        <section className="px-5 py-8 bg-[#F7F7F5] mt-4">
           <div className="flex items-center gap-4">
             <div className="w-12 h-12 rounded-full overflow-hidden bg-[#E4E3DE] shrink-0 border border-[#E4E3DE]">
               <img className="w-full h-full object-cover" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=150" alt="Advisor" />
             </div>
             <div className="flex-1">
               <h4 className="text-[14px] font-medium text-[#111111]">需要搭配建议？</h4>
               <p className="text-[11px] text-[#666663] mt-0.5">您的私人顾问 Sarah 随时为您解答。</p>
             </div>
             <button className="w-10 h-10 border border-[#111111] rounded-sm flex items-center justify-center text-[#111111] hover:bg-[#111111] hover:text-[#FFFFFF] transition-colors">
               <span className="material-symbols-outlined text-[18px]">chat_bubble</span>
             </button>
           </div>
        </section>
      </main>

      {/* Fixed Bottom Action Bar */}
      <div className="fixed bottom-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF] border-t border-[#E4E3DE] px-4 py-3 flex items-center gap-3 pb-safe shadow-[0_-4px_16px_rgba(0,0,0,0.04)]">
        <button className="flex-1 h-[48px] border border-[#111111] text-[#111111] font-medium text-[14px] rounded-sm flex items-center justify-center hover:bg-[#F7F7F5] transition-colors">
          加入购物袋
        </button>
        <button className="flex-1 h-[48px] bg-[#111111] text-[#FFFFFF] font-medium text-[14px] rounded-sm flex items-center justify-center hover:opacity-90 transition-opacity">
          立即购买
        </button>
      </div>
    </div>
  );
}
