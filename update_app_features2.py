import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# 4. Category.tsx
write_file('src/pages/Category.tsx', """import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function Category() {
  const navigate = useNavigate();

  return (
    <div className="bg-[#FFFFFF] text-[#111111] font-sans antialiased min-h-screen pb-[100px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-center items-center px-4 h-14 w-full">
          <h1 className="font-serif text-[18px] tracking-widest font-bold">分类</h1>
        </div>
      </header>
      
      <main className="pt-20 px-6">
        <div className="mb-6 relative">
          <span className="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-[#666663] text-[20px]">search</span>
          <input type="text" placeholder="搜索品牌、单品..." className="w-full h-11 pl-10 pr-4 bg-[#F7F7F5] rounded-sm text-[14px] outline-none placeholder:text-[#666663]" />
        </div>

        <div className="mb-10">
          <h3 className="text-[11px] text-[#666663] font-mono tracking-widest uppercase mb-5">按分类探索</h3>
          <ul className="flex flex-col gap-6 text-[16px] font-medium text-[#111111]">
            <li className="cursor-pointer hover:opacity-70 flex items-center justify-between" onClick={() => navigate('/explore')}>包袋 Bags <span className="material-symbols-outlined text-[20px] text-[#666663]">chevron_right</span></li>
            <li className="cursor-pointer hover:opacity-70 flex items-center justify-between" onClick={() => navigate('/explore')}>鞋履 Shoes <span className="material-symbols-outlined text-[20px] text-[#666663]">chevron_right</span></li>
            <li className="cursor-pointer hover:opacity-70 flex items-center justify-between" onClick={() => navigate('/explore')}>成衣 Ready-to-Wear <span className="material-symbols-outlined text-[20px] text-[#666663]">chevron_right</span></li>
            <li className="cursor-pointer hover:opacity-70 flex items-center justify-between" onClick={() => navigate('/explore')}>配饰 Accessories <span className="material-symbols-outlined text-[20px] text-[#666663]">chevron_right</span></li>
          </ul>
        </div>
        
        <div>
          <h3 className="text-[11px] text-[#666663] font-mono tracking-widest uppercase mb-5">品牌目录</h3>
          <ul className="flex flex-col gap-5 text-[15px] text-[#111111]">
            <li className="cursor-pointer hover:opacity-70" onClick={() => navigate('/explore')}>The Row</li>
            <li className="cursor-pointer hover:opacity-70" onClick={() => navigate('/explore')}>Loro Piana</li>
            <li className="cursor-pointer hover:opacity-70" onClick={() => navigate('/explore')}>Bottega Veneta</li>
            <li className="cursor-pointer hover:opacity-70" onClick={() => navigate('/explore')}>Jil Sander</li>
            <li className="cursor-pointer hover:opacity-70 text-[#666663] mt-2 underline underline-offset-4">查看全部 A-Z</li>
          </ul>
        </div>
      </main>

      <BottomNav />
    </div>
  );
}
""")

# 5. Cart.tsx
write_file('src/pages/Cart.tsx', """import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';
import { useCart } from '../context/CartContext';

export default function Cart() {
  const navigate = useNavigate();
  const { items, updateQuantity, removeFromCart, totalPrice } = useCart();

  return (
    <div className="bg-[#FFFFFF] text-[#111111] font-sans antialiased min-h-screen pb-[120px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-center items-center px-4 h-14 w-full">
          <h1 className="font-serif text-[18px] tracking-widest font-bold">购物袋</h1>
        </div>
      </header>
      
      <main className="pt-14 flex flex-col w-full h-full">
        {items.length === 0 ? (
          <div className="flex-1 flex flex-col items-center justify-center mt-32 px-5 text-center">
            <span className="material-symbols-outlined text-[48px] text-[#E4E3DE] mb-4">shopping_bag</span>
            <h2 className="text-[16px] font-medium text-[#111111] mb-2">您的购物袋是空的</h2>
            <p className="text-[13px] text-[#666663] mb-8">探索我们为您精选的最新单品。</p>
            <button onClick={() => navigate('/explore')} className="w-[180px] h-[44px] bg-[#111111] text-[#FFFFFF] font-medium text-[13px] rounded-sm hover:opacity-90 transition-opacity">
              去逛逛
            </button>
          </div>
        ) : (
          <div className="px-5 py-6 flex flex-col gap-6">
            {items.map((item) => (
              <div key={item.id} className="flex gap-4 border-b border-[#E4E3DE] pb-6 last:border-0">
                <div className="w-[100px] h-[120px] bg-[#F7F7F5] rounded-sm overflow-hidden shrink-0 cursor-pointer" onClick={() => navigate('/product', { state: item.product })}>
                  <img src={item.product.img} alt={item.product.name} className="w-full h-full object-cover mix-blend-multiply" />
                </div>
                <div className="flex-1 flex flex-col justify-between">
                  <div>
                    <div className="flex justify-between items-start mb-1">
                      <h3 className="font-bold text-[12px] uppercase tracking-wide">{item.product.brand}</h3>
                      <button onClick={() => removeFromCart(item.id)} className="text-[#666663] hover:text-[#111111]">
                        <span className="material-symbols-outlined text-[18px]">close</span>
                      </button>
                    </div>
                    <p className="text-[12px] text-[#666663] mb-2 line-clamp-1">{item.product.name}</p>
                    <p className="text-[11px] text-[#666663] mb-1">颜色: {item.color}</p>
                    <p className="text-[11px] text-[#666663] mb-1">尺码: {item.size}</p>
                    <div className="flex items-center gap-1.5 mt-2">
                      <span className="material-symbols-outlined text-[14px] text-[#666663]">{item.fulfillment.icon}</span>
                      <span className="text-[10px] text-[#666663]">{item.fulfillment.label}</span>
                    </div>
                  </div>
                  
                  <div className="flex justify-between items-end mt-4">
                    <div className="flex items-center border border-[#E4E3DE] rounded-sm">
                      <button onClick={() => updateQuantity(item.id, item.quantity - 1)} className="w-8 h-8 flex items-center justify-center text-[#666663] hover:bg-[#F7F7F5] disabled:opacity-30" disabled={item.quantity <= 1}>
                        <span className="material-symbols-outlined text-[16px]">remove</span>
                      </button>
                      <span className="w-8 text-center text-[13px] font-mono">{item.quantity}</span>
                      <button onClick={() => updateQuantity(item.id, item.quantity + 1)} className="w-8 h-8 flex items-center justify-center text-[#666663] hover:bg-[#F7F7F5]">
                        <span className="material-symbols-outlined text-[16px]">add</span>
                      </button>
                    </div>
                    <p className="font-mono text-[15px] font-medium">{item.fulfillment.price}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>

      {items.length > 0 && (
        <div className="fixed bottom-[56px] left-1/2 -translate-x-1/2 max-w-[430px] w-full z-40 bg-[#FFFFFF] border-t border-[#E4E3DE] p-5 shadow-[0_-10px_20px_rgba(0,0,0,0.02)]">
          <div className="flex justify-between items-center mb-4">
            <span className="text-[13px] font-medium text-[#111111]">小计</span>
            <span className="font-mono text-[18px] font-medium text-[#111111]">¥{totalPrice.toLocaleString()}</span>
          </div>
          <button className="w-full h-[48px] bg-[#111111] text-[#FFFFFF] font-medium text-[14px] rounded-sm flex items-center justify-center hover:opacity-90 transition-opacity">
            结算
          </button>
        </div>
      )}

      <BottomNav />
    </div>
  );
}
""")

