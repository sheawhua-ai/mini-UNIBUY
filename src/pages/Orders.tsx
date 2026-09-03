import React, { useState, useEffect } from 'react';
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
