import React, { useState } from 'react';
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
