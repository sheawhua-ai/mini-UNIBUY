import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# 1. Update CartContext to include clearCart
with open('src/context/CartContext.tsx', 'r') as f:
    cart_context = f.read()

if 'clearCart: () => void' not in cart_context:
    cart_context = cart_context.replace(
        "updateQuantity: (id: string, qty: number) => void;",
        "updateQuantity: (id: string, qty: number) => void;\n  clearCart: () => void;"
    )
    cart_context = cart_context.replace(
        "const updateQuantity = (id: string, qty: number) => {",
        "const clearCart = () => setItems([]);\n\n  const updateQuantity = (id: string, qty: number) => {"
    )
    cart_context = cart_context.replace(
        "value={{ items, addToCart, removeFromCart, updateQuantity, totalPrice }}",
        "value={{ items, addToCart, removeFromCart, updateQuantity, clearCart, totalPrice }}"
    )
    write_file('src/context/CartContext.tsx', cart_context)

# 2. Checkout.tsx
write_file('src/pages/Checkout.tsx', """import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useCart } from '../context/CartContext';

export default function Checkout() {
  const navigate = useNavigate();
  const { items, totalPrice, clearCart } = useCart();
  const [isProcessing, setIsProcessing] = useState(false);

  // If accessed without items, redirect back
  if (items.length === 0 && !isProcessing) {
    setTimeout(() => navigate('/cart'), 0);
    return null;
  }

  const domItems = items.filter(item => item.fulfillment.id === 'dom');
  const ovsItems = items.filter(item => item.fulfillment.id === 'ovs');
  
  // Calculate mock tax for overseas items
  const ovsTotal = ovsItems.reduce((sum, item) => {
    const priceStr = item.fulfillment.price.replace(/[^0-9]/g, '');
    return sum + (parseInt(priceStr) * item.quantity);
  }, 0);
  const importTax = Math.floor(ovsTotal * 0.1); // 10% tax for overseas
  const finalTotal = totalPrice + importTax;

  const handlePay = () => {
    setIsProcessing(true);
    setTimeout(() => {
      clearCart();
      navigate('/orders', { state: { showSuccess: true } });
    }, 1500);
  };

  return (
    <div className="bg-[#F7F7F5] text-[#111111] font-sans antialiased min-h-screen pb-[100px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center justify-center p-2 -ml-2 text-[#111111] hover:opacity-80" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <h1 className="font-serif text-[18px] tracking-widest absolute left-1/2 -translate-x-1/2 font-bold pointer-events-none">确认订单</h1>
          <div className="w-10"></div>
        </div>
      </header>
      
      <main className="pt-20 px-4 flex flex-col gap-4">
        {/* Address Card */}
        <div className="bg-[#FFFFFF] p-5 rounded-sm border border-[#E4E3DE] shadow-sm flex items-center justify-between cursor-pointer">
          <div className="flex flex-col gap-1.5">
            <div className="flex items-center gap-3">
              <span className="font-medium text-[15px]">S. Wang</span>
              <span className="text-[14px] text-[#666663] font-mono">138****8849</span>
            </div>
            <p className="text-[13px] text-[#666663] leading-relaxed">
              上海市 静安区 南京西路 1266 号<br/>恒隆广场 66 楼
            </p>
          </div>
          <span className="material-symbols-outlined text-[#666663]">chevron_right</span>
        </div>

        {/* Order Summary */}
        <div className="bg-[#FFFFFF] rounded-sm border border-[#E4E3DE] shadow-sm overflow-hidden">
          <div className="px-5 py-4 border-b border-[#E4E3DE]">
            <h3 className="font-medium text-[14px]">商品明细 ({items.length}件)</h3>
          </div>
          <div className="px-5 py-2 flex flex-col">
            {domItems.length > 0 && (
              <div className="py-2">
                <div className="flex items-center gap-2 mb-3 text-[#666663]">
                  <span className="material-symbols-outlined text-[16px]">local_shipping</span>
                  <span className="text-[12px]">大陆现货发货</span>
                </div>
                <div className="flex overflow-x-auto hide-scrollbar gap-3 pb-2">
                  {domItems.map(item => (
                    <div key={item.id} className="w-[60px] h-[75px] bg-[#F7F7F5] shrink-0 rounded-sm overflow-hidden relative">
                      <img src={item.product.img} alt={item.product.name} className="w-full h-full object-cover mix-blend-multiply" />
                      <span className="absolute bottom-0 right-0 bg-[#111111]/80 text-white text-[10px] font-mono px-1.5 rounded-tl-sm">x{item.quantity}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
            
            {ovsItems.length > 0 && (
              <div className="py-2 border-t border-[#E4E3DE] mt-2">
                <div className="flex items-center gap-2 mb-3 text-[#666663]">
                  <span className="material-symbols-outlined text-[16px]">flight_takeoff</span>
                  <span className="text-[12px]">海外直邮发货 (含清关)</span>
                </div>
                <div className="flex overflow-x-auto hide-scrollbar gap-3 pb-2">
                  {ovsItems.map(item => (
                    <div key={item.id} className="w-[60px] h-[75px] bg-[#F7F7F5] shrink-0 rounded-sm overflow-hidden relative">
                      <img src={item.product.img} alt={item.product.name} className="w-full h-full object-cover mix-blend-multiply" />
                      <span className="absolute bottom-0 right-0 bg-[#111111]/80 text-white text-[10px] font-mono px-1.5 rounded-tl-sm">x{item.quantity}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Payment Methods */}
        <div className="bg-[#FFFFFF] rounded-sm border border-[#E4E3DE] shadow-sm overflow-hidden">
          <div className="px-5 py-4 border-b border-[#E4E3DE]">
            <h3 className="font-medium text-[14px]">支付方式</h3>
          </div>
          <div className="flex flex-col">
            <label className="flex items-center justify-between px-5 py-4 border-b border-[#E4E3DE] cursor-pointer">
              <div className="flex items-center gap-3">
                <span className="material-symbols-outlined text-[24px]">contactless</span>
                <span className="text-[14px] text-[#111111]">Apple Pay</span>
              </div>
              <div className="w-4 h-4 rounded-full border border-[#111111] flex items-center justify-center">
                <div className="w-2 h-2 bg-[#111111] rounded-full" />
              </div>
            </label>
            <label className="flex items-center justify-between px-5 py-4 cursor-pointer">
              <div className="flex items-center gap-3">
                <span className="material-symbols-outlined text-[24px]">credit_card</span>
                <span className="text-[14px] text-[#111111]">信用卡 / 借记卡</span>
              </div>
              <div className="w-4 h-4 rounded-full border border-[#E4E3DE]" />
            </label>
          </div>
        </div>

        {/* Price Breakdown */}
        <div className="bg-[#FFFFFF] p-5 rounded-sm border border-[#E4E3DE] shadow-sm flex flex-col gap-3">
          <div className="flex justify-between items-center text-[13px] text-[#666663]">
            <span>商品合计</span>
            <span className="font-mono">¥{totalPrice.toLocaleString()}</span>
          </div>
          <div className="flex justify-between items-center text-[13px] text-[#666663]">
            <span>运费</span>
            <span className="font-mono">¥0</span>
          </div>
          {importTax > 0 && (
            <div className="flex justify-between items-center text-[13px] text-[#666663]">
              <span>预估进口税费</span>
              <span className="font-mono">¥{importTax.toLocaleString()}</span>
            </div>
          )}
          <div className="h-px bg-[#E4E3DE] my-1" />
          <div className="flex justify-between items-end">
            <span className="font-medium text-[14px]">应付总额</span>
            <span className="font-mono text-[20px] font-bold">¥{finalTotal.toLocaleString()}</span>
          </div>
        </div>
      </main>

      {/* Checkout Bar */}
      <div className="fixed bottom-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-40 bg-[#FFFFFF] border-t border-[#E4E3DE] px-4 py-3 pb-safe shadow-[0_-10px_20px_rgba(0,0,0,0.02)] flex items-center justify-between">
        <div className="flex flex-col">
          <span className="text-[11px] text-[#666663]">实付款</span>
          <span className="font-mono text-[18px] font-bold text-[#111111]">¥{finalTotal.toLocaleString()}</span>
        </div>
        <button 
          onClick={handlePay}
          disabled={isProcessing}
          className="w-[160px] h-[48px] bg-[#111111] text-[#FFFFFF] font-medium text-[14px] rounded-sm flex items-center justify-center hover:opacity-90 transition-opacity disabled:opacity-50"
        >
          {isProcessing ? '处理中...' : '确认支付'}
        </button>
      </div>
      
      {/* Processing Overlay */}
      {isProcessing && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-[#FFFFFF]/80 backdrop-blur-sm">
           <div className="flex flex-col items-center">
             <div className="w-8 h-8 border-2 border-[#111111] border-t-transparent rounded-full animate-spin mb-4" />
             <span className="text-[13px] font-medium tracking-widest uppercase">Processing</span>
           </div>
        </div>
      )}
    </div>
  );
}
""")

# 3. Orders.tsx
write_file('src/pages/Orders.tsx', """import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function Orders() {
  const navigate = useNavigate();
  const location = useLocation();
  const [activeTab, setActiveTab] = useState('ALL');
  const [showSuccess, setShowSuccess] = useState(false);

  useEffect(() => {
    if (location.state?.showSuccess) {
      setShowSuccess(true);
      setTimeout(() => setShowSuccess(false), 3000);
      window.history.replaceState({}, document.title)
    }
  }, [location]);

  const tabs = [
    { id: 'ALL', label: '全部' },
    { id: 'UNPAID', label: '待付款' },
    { id: 'SHIPPING', label: '待发货' },
    { id: 'RECEIVED', label: '待收货' }
  ];

  const mockOrders = [
    {
      id: 'UB984392011',
      status: 'SHIPPING',
      statusLabel: '待发货',
      date: '2026-09-02',
      items: [
        {
          brand: 'THE ROW',
          name: 'Margaux 15 皮革手提包',
          img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw',
          color: '黑色',
          size: '15',
          price: '¥38,500',
          qty: 1
        }
      ],
      total: '¥38,500'
    },
    {
      id: 'UB773499210',
      status: 'RECEIVED',
      statusLabel: '已完成',
      date: '2026-08-15',
      items: [
        {
          brand: 'LORO PIANA',
          name: 'Summer Walk 麂皮乐福鞋',
          img: 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&q=80&w=400',
          color: '珍珠灰',
          size: '41',
          price: '¥8,200',
          qty: 1
        },
        {
          brand: 'BOTTEGA VENETA',
          name: 'Intrecciato 编织皮革腰带',
          img: 'https://images.unsplash.com/photo-1626497764746-6dc36546b388?auto=format&fit=crop&q=80&w=400',
          color: '黑色',
          size: '85',
          price: '¥4,600',
          qty: 1
        }
      ],
      total: '¥12,800'
    }
  ];

  const filteredOrders = activeTab === 'ALL' 
    ? mockOrders 
    : mockOrders.filter(o => o.status === activeTab);

  return (
    <div className="bg-[#F7F7F5] text-[#111111] font-sans antialiased min-h-screen pb-[100px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-between items-center px-4 h-14 w-full">
          <button className="relative z-10 flex items-center justify-center p-2 -ml-2 text-[#111111] hover:opacity-80 transition-opacity" onClick={() => navigate(-1)}>
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <h1 className="font-serif text-[18px] tracking-widest absolute left-1/2 -translate-x-1/2 font-bold pointer-events-none">我的订单</h1>
          <div className="w-10"></div>
        </div>
        
        {/* Tabs */}
        <div className="flex px-4 pt-1 pb-3 overflow-x-auto hide-scrollbar gap-6">
          {tabs.map(tab => (
            <button 
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`text-[13px] whitespace-nowrap pb-1 border-b-2 transition-colors ${activeTab === tab.id ? 'border-[#111111] text-[#111111] font-medium' : 'border-transparent text-[#666663] hover:text-[#111111]'}`}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </header>

      <main className="pt-28 px-4 flex flex-col gap-4">
        {showSuccess && (
          <div className="bg-[#111111] text-[#FFFFFF] px-4 py-3 rounded-sm flex items-center gap-3 animate-in slide-in-from-top-4 fade-in duration-300 shadow-xl mb-2">
            <span className="material-symbols-outlined text-[20px] text-green-400">check_circle</span>
            <span className="text-[13px] font-medium">支付成功，您的订单已确认</span>
          </div>
        )}

        {filteredOrders.length === 0 ? (
          <div className="flex flex-col items-center justify-center py-20 text-center">
             <span className="material-symbols-outlined text-[48px] text-[#E4E3DE] mb-4">receipt_long</span>
             <h3 className="text-[14px] font-medium text-[#111111] mb-2">暂无相关订单</h3>
             <p className="text-[12px] text-[#666663]">您可以去探索更多精选好物</p>
          </div>
        ) : (
          filteredOrders.map(order => (
            <div key={order.id} className="bg-[#FFFFFF] rounded-sm border border-[#E4E3DE] shadow-sm overflow-hidden flex flex-col cursor-pointer hover:shadow-md transition-shadow">
               <div className="px-4 py-3 border-b border-[#E4E3DE] flex justify-between items-center bg-[#FAFAFA]">
                 <span className="text-[11px] font-mono text-[#666663]">Order No. {order.id}</span>
                 <span className={`text-[12px] font-medium ${order.status === 'SHIPPING' ? 'text-[#D08B2D]' : 'text-[#666663]'}`}>{order.statusLabel}</span>
               </div>
               <div className="flex flex-col px-4 py-2">
                 {order.items.map((item, idx) => (
                   <div key={idx} className="flex gap-4 py-4 border-b border-[#E4E3DE] last:border-0">
                     <div className="w-[70px] h-[90px] bg-[#F7F7F5] rounded-sm overflow-hidden shrink-0">
                       <img src={item.img} alt={item.name} className="w-full h-full object-cover mix-blend-multiply" />
                     </div>
                     <div className="flex-1 flex flex-col justify-between py-0.5">
                       <div>
                         <div className="flex justify-between items-start mb-1">
                           <h4 className="font-bold text-[11px] uppercase tracking-wide">{item.brand}</h4>
                           <span className="font-mono text-[13px] text-[#111111]">{item.price}</span>
                         </div>
                         <p className="text-[12px] text-[#666663] mb-1 line-clamp-1">{item.name}</p>
                         <p className="text-[10px] text-[#666663]">颜色: {item.color} | 尺码: {item.size}</p>
                       </div>
                       <span className="text-[11px] text-[#666663] font-mono self-end">x{item.qty}</span>
                     </div>
                   </div>
                 ))}
               </div>
               <div className="px-4 py-3 border-t border-[#E4E3DE] flex justify-between items-center">
                 <span className="text-[11px] text-[#666663]">{order.date}</span>
                 <div className="flex items-center gap-2">
                   <span className="text-[12px] text-[#111111]">共 {order.items.reduce((a,b)=>a+b.qty, 0)} 件商品</span>
                   <span className="font-medium text-[14px]">总计: <span className="font-mono">{order.total}</span></span>
                 </div>
               </div>
            </div>
          ))
        )}
      </main>

      <BottomNav />
    </div>
  );
}
""")

# 4. Update App.tsx
with open('src/App.tsx', 'r') as f:
    app_content = f.read()

if 'Checkout' not in app_content:
    app_content = app_content.replace(
        "import Cart from './pages/Cart';",
        "import Cart from './pages/Cart';\nimport Checkout from './pages/Checkout';\nimport Orders from './pages/Orders';"
    )
    app_content = app_content.replace(
        '<Route path="/cart" element={<Cart />} />',
        '<Route path="/cart" element={<Cart />} />\n          <Route path="/checkout" element={<Checkout />} />\n          <Route path="/orders" element={<Orders />} />'
    )
    write_file('src/App.tsx', app_content)

# 5. Update Cart.tsx to navigate to checkout
with open('src/pages/Cart.tsx', 'r') as f:
    cart_content = f.read()

cart_content = cart_content.replace(
    '<button className="flex-1 h-[44px] bg-[#111111] text-[#FFFFFF] font-medium text-[13px] rounded-sm flex items-center justify-center hover:opacity-90 transition-opacity">',
    '<button onClick={() => navigate(\'/checkout\')} className="flex-1 h-[44px] bg-[#111111] text-[#FFFFFF] font-medium text-[13px] rounded-sm flex items-center justify-center hover:opacity-90 transition-opacity">'
)
write_file('src/pages/Cart.tsx', cart_content)

# 6. Update Profile.tsx to navigate to orders
with open('src/pages/Profile.tsx', 'r') as f:
    profile_content = f.read()

profile_content = profile_content.replace(
    '<span className="text-[12px] text-[#666663] cursor-pointer hover:text-[#111111]">查看全部</span>',
    '<span onClick={() => navigate(\'/orders\')} className="text-[12px] text-[#666663] cursor-pointer hover:text-[#111111]">查看全部</span>'
)
profile_content = profile_content.replace(
    'className="flex flex-col items-center gap-1.5 cursor-pointer hover:opacity-70"',
    'className="flex flex-col items-center gap-1.5 cursor-pointer hover:opacity-70" onClick={() => navigate(\'/orders\')}'
)
write_file('src/pages/Profile.tsx', profile_content)

