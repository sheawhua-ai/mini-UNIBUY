import os

with open('src/pages/Cart.tsx', 'r') as f:
    content = f.read()

new_content = """import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';
import { useCart, CartItem } from '../context/CartContext';

export default function Cart() {
  const navigate = useNavigate();
  const { items, updateQuantity, removeFromCart, totalPrice } = useCart();

  const domItems = items.filter(item => item.fulfillment.id === 'dom');
  const ovsItems = items.filter(item => item.fulfillment.id === 'ovs');
  
  // Get other items if any
  const otherItems = items.filter(item => item.fulfillment.id !== 'dom' && item.fulfillment.id !== 'ovs');

  const renderOrderGroup = (title: string, groupItems: CartItem[], icon: string) => {
    if (groupItems.length === 0) return null;
    
    const groupTotal = groupItems.reduce((sum, item) => {
      const priceStr = item.fulfillment.price.replace(/[^0-9]/g, '');
      return sum + (parseInt(priceStr) * item.quantity);
    }, 0);

    return (
      <div className="mb-6 bg-[#FFFFFF] rounded-sm border border-[#E4E3DE] shadow-sm overflow-hidden">
        <div className="bg-[#F7F7F5] px-4 py-3 flex items-center justify-between border-b border-[#E4E3DE]">
          <div className="flex items-center gap-2 text-[#111111]">
            <span className="material-symbols-outlined text-[18px]">{icon}</span>
            <h3 className="font-medium text-[13px]">{title}</h3>
          </div>
        </div>
        <div className="px-4 py-2 flex flex-col">
          {groupItems.map((item) => (
            <div key={item.id} className="flex gap-4 border-b border-[#E4E3DE] py-5 last:border-0">
              <div className="w-[80px] h-[100px] bg-[#F7F7F5] rounded-sm overflow-hidden shrink-0 cursor-pointer" onClick={() => navigate('/product', { state: item.product })}>
                <img src={item.product.img} alt={item.product.name} className="w-full h-full object-cover mix-blend-multiply" />
              </div>
              <div className="flex-1 flex flex-col justify-between">
                <div>
                  <div className="flex justify-between items-start mb-1">
                    <h3 className="font-bold text-[11px] uppercase tracking-wide">{item.product.brand}</h3>
                    <button onClick={() => removeFromCart(item.id)} className="text-[#666663] hover:text-[#111111]">
                      <span className="material-symbols-outlined text-[16px]">close</span>
                    </button>
                  </div>
                  <p className="text-[12px] text-[#666663] mb-2 line-clamp-1">{item.product.name}</p>
                  <p className="text-[11px] text-[#666663] mb-0.5">颜色: {item.color}</p>
                  <p className="text-[11px] text-[#666663] mb-0.5">尺码: {item.size}</p>
                  <p className="text-[10px] text-[#666663] mt-1 line-clamp-1">{item.fulfillment.label}</p>
                </div>
                
                <div className="flex justify-between items-end mt-4">
                  <div className="flex items-center border border-[#E4E3DE] rounded-sm">
                    <button onClick={() => updateQuantity(item.id, item.quantity - 1)} className="w-7 h-7 flex items-center justify-center text-[#666663] hover:bg-[#F7F7F5] disabled:opacity-30" disabled={item.quantity <= 1}>
                      <span className="material-symbols-outlined text-[14px]">remove</span>
                    </button>
                    <span className="w-7 text-center text-[12px] font-mono">{item.quantity}</span>
                    <button onClick={() => updateQuantity(item.id, item.quantity + 1)} className="w-7 h-7 flex items-center justify-center text-[#666663] hover:bg-[#F7F7F5]">
                      <span className="material-symbols-outlined text-[14px]">add</span>
                    </button>
                  </div>
                  <p className="font-mono text-[14px] font-medium">{item.fulfillment.price}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
        <div className="px-4 py-3 bg-[#FAFAFA] border-t border-[#E4E3DE] flex justify-between items-center">
          <span className="text-[12px] text-[#666663]">本单小计</span>
          <span className="font-mono text-[15px] font-medium text-[#111111]">¥{groupTotal.toLocaleString()}</span>
        </div>
      </div>
    );
  };

  return (
    <div className="bg-[#FAFAFA] text-[#111111] font-sans antialiased min-h-screen pb-[120px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-center items-center px-4 h-14 w-full">
          <h1 className="font-serif text-[18px] tracking-widest font-bold">购物袋</h1>
        </div>
      </header>
      
      <main className="pt-20 flex flex-col w-full h-full px-4">
        {items.length === 0 ? (
          <div className="flex-1 flex flex-col items-center justify-center mt-24 px-5 text-center">
            <span className="material-symbols-outlined text-[48px] text-[#E4E3DE] mb-4">shopping_bag</span>
            <h2 className="text-[16px] font-medium text-[#111111] mb-2">您的购物袋是空的</h2>
            <p className="text-[13px] text-[#666663] mb-8">探索我们为您精选的最新单品。</p>
            <button onClick={() => navigate('/explore')} className="w-[180px] h-[44px] bg-[#111111] text-[#FFFFFF] font-medium text-[13px] rounded-sm hover:opacity-90 transition-opacity">
              去逛逛
            </button>
          </div>
        ) : (
          <div className="flex flex-col pb-6">
            {renderOrderGroup('大陆现货订单', domItems, 'local_shipping')}
            {renderOrderGroup('海外直邮订单', ovsItems, 'flight_takeoff')}
            {renderOrderGroup('其他订单', otherItems, 'inventory_2')}
          </div>
        )}
      </main>

      {items.length > 0 && (
        <div className="fixed bottom-[56px] left-1/2 -translate-x-1/2 max-w-[430px] w-full z-40 bg-[#FFFFFF] border-t border-[#E4E3DE] p-4 shadow-[0_-10px_20px_rgba(0,0,0,0.02)]">
          <div className="flex justify-between items-center mb-3">
            <span className="text-[12px] font-medium text-[#111111]">总计 ({items.length} 件商品)</span>
            <span className="font-mono text-[18px] font-medium text-[#111111]">¥{totalPrice.toLocaleString()}</span>
          </div>
          <div className="flex gap-2">
             <button className="flex-1 h-[44px] bg-[#111111] text-[#FFFFFF] font-medium text-[13px] rounded-sm flex items-center justify-center hover:opacity-90 transition-opacity">
               合并结算
             </button>
          </div>
        </div>
      )}

      <BottomNav />
    </div>
  );
}
"""

with open('src/pages/Cart.tsx', 'w') as f:
    f.write(new_content)

