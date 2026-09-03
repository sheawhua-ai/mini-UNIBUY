import React from 'react';
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
        <div 
          className="mb-6 relative cursor-pointer group"
          onClick={() => navigate('/intent')}
        >
          <span className="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-[#111111] text-[20px] group-hover:scale-110 transition-transform">psychiatry</span>
          <div className="w-full h-11 pl-10 pr-10 bg-[#F7F7F5] rounded-sm flex items-center border border-transparent group-hover:border-[#E4E3DE] transition-colors">
            <span className="text-[14px] text-[#666663]">告诉 AI 您在寻找什么，或通过图片搜索...</span>
          </div>
          <span className="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 text-[#666663] text-[20px]">photo_camera</span>
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
