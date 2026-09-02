import sys

content = """
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function ProductDetail() {
  const navigate = useNavigate();
  const [activeTab, setActiveTab] = useState('details');

  return (
    <div className="bg-[#F7F7F5] text-[#111111] antialiased min-h-screen pb-[120px] font-sans">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="flex justify-between items-center px-4 h-14">
          <button onClick={() => navigate(-1)} className="text-[#111111] hover:opacity-80 transition-opacity p-2 -ml-2">
            <span className="material-symbols-outlined text-[24px]">arrow_back</span>
          </button>
          <div className="flex items-center gap-2">
            <button className="text-[#111111] hover:opacity-80 transition-opacity p-2">
              <span className="material-symbols-outlined text-[24px]">ios_share</span>
            </button>
          </div>
        </div>
      </header>

      <main className="w-full flex flex-col mt-14">
        {/* Gallery */}
        <section className="w-full aspect-[4/5] bg-[#EFEFEB] relative">
          <img className="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDky0km-Mff6UbX7pS3nRRlvZ-WCm8QtYE5jEwt6tk_m0_-KqtkINhD5Xvbhff0HxO1fYTJSXxhCnY11wtOf-7TMiiAD7pvI-2oXzAIVWTTVlh4GNF0drfE0VIjcRTZsJuvXHb_KgTMAy3q2oQBxNEIM-0XsIbp9pPvaFYZ_khYyg1VykTUibem34dsPc1x4GTcsragr9ZnGdvu-2emHV0dOBBW3wcbRiJ8zk2_u60WQW5EqNj3VByw" alt="Product" />
          <div className="absolute bottom-4 right-4 bg-white/90 backdrop-blur-sm px-2 py-1 text-[11px] font-medium tracking-widest uppercase">1 / 6</div>
        </section>

        {/* Core Info */}
        <section className="px-5 py-6 bg-[#FFFFFF]">
          <div className="flex justify-between items-start mb-2">
            <div>
              <p className="text-[11px] text-[#666663] uppercase tracking-widest mb-1">Maison Signature</p>
              <h1 className="font-serif text-[24px] text-[#111111] leading-tight">Noir Signature Tote</h1>
            </div>
            <button className="p-2 -mr-2 text-[#111111]">
              <span className="material-symbols-outlined">favorite_border</span>
            </button>
          </div>
          <p className="font-mono text-[20px] font-medium text-[#111111] mb-4">¥ 8,500</p>
          <div className="flex items-center gap-2 text-[12px] text-[#666663]">
            <span className="w-2 h-2 bg-[#E56A1D] rounded-none"></span>
            <span>仅余 2 件 · 预计 2-3 天达</span>
          </div>
        </section>

        {/* Selection */}
        <section className="px-5 py-6 bg-[#FFFFFF] border-t border-[#E4E3DE]">
          <div className="mb-6">
            <h3 className="text-[13px] font-medium text-[#111111] mb-3">颜色：经典黑</h3>
            <div className="flex gap-3">
              <div className="w-10 h-10 border border-[#111111] p-0.5 cursor-pointer rounded-sm">
                <div className="w-full h-full bg-[#111111] rounded-sm"></div>
              </div>
              <div className="w-10 h-10 border border-[#E4E3DE] p-0.5 cursor-pointer rounded-sm">
                <div className="w-full h-full bg-[#5D4037] rounded-sm"></div>
              </div>
            </div>
          </div>
          <div>
            <div className="flex justify-between items-center mb-3">
              <h3 className="text-[13px] font-medium text-[#111111]">尺寸：大号</h3>
              <button className="text-[12px] text-[#666663] underline">尺寸指南</button>
            </div>
            <div className="flex gap-2">
              <button className="flex-1 py-3 border border-[#E4E3DE] text-[13px] text-[#111111] rounded-sm hover:border-[#111111] transition-colors">标准</button>
              <button className="flex-1 py-3 border border-[#111111] text-[13px] font-medium text-[#111111] bg-[#F7F7F5] rounded-sm">大号</button>
            </div>
          </div>
        </section>

        {/* AI Intent Match (from search) */}
        <section className="px-5 py-6 mt-2 bg-[#FFFFFF]">
          <div className="flex items-center gap-2 mb-4">
            <span className="text-[12px] text-[#111111] font-bold uppercase tracking-widest">AI 匹配分析</span>
          </div>
          <div className="bg-[#F7F7F5] p-4 rounded-sm border border-[#E4E3DE]">
            <p className="text-[13px] text-[#666663] leading-relaxed">
              <strong className="text-[#111111] font-medium">为何适合：</strong>这款手袋完全符合您的“商务差旅”与“低调无Logo”需求。内置加厚电脑隔层，全粒面小牛皮确保耐用且不失质感。
            </p>
          </div>
        </section>

        {/* Details Accordion */}
        <section className="mt-2 bg-[#FFFFFF] flex flex-col">
          <div className="px-5 py-4 border-b border-[#E4E3DE] flex justify-between items-center cursor-pointer" onClick={() => setActiveTab('details')}>
            <h3 className="text-[14px] font-medium text-[#111111]">材质与工艺</h3>
            <span className="material-symbols-outlined text-[#666663]">{activeTab === 'details' ? 'remove' : 'add'}</span>
          </div>
          {activeTab === 'details' && (
            <div className="px-5 py-4 text-[13px] text-[#666663] leading-relaxed">
              采用法国头层小牛皮，经自然鞣制工艺处理。内部衬里为超细纤维，金属件采用复古做旧镀层。
              <ul className="list-disc pl-4 mt-2 space-y-1">
                <li>尺寸: 38 x 28 x 15 cm</li>
                <li>手柄高度: 22 cm</li>
                <li>产地: 意大利</li>
              </ul>
            </div>
          )}
          <div className="px-5 py-4 border-b border-[#E4E3DE] flex justify-between items-center cursor-pointer">
            <h3 className="text-[14px] font-medium text-[#111111]">配送与退换</h3>
            <span className="material-symbols-outlined text-[#666663]">add</span>
          </div>
        </section>
      </main>

      {/* Fixed Bottom Action Bar */}
      <div className="fixed bottom-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF] border-t border-[#E4E3DE] px-4 py-3 flex items-center gap-3 pb-safe shadow-[0_-4px_16px_rgba(0,0,0,0.04)]">
        <div className="flex gap-4 px-2">
          <button className="flex flex-col items-center justify-center text-[#666663] hover:text-[#111111] transition-colors" onClick={() => navigate('/compare')}>
            <span className="material-symbols-outlined text-[20px] font-light">compare_arrows</span>
            <span className="text-[10px] mt-0.5">对比</span>
          </button>
          <button className="flex flex-col items-center justify-center text-[#666663] hover:text-[#111111] transition-colors">
            <span className="material-symbols-outlined text-[20px] font-light">support_agent</span>
            <span className="text-[10px] mt-0.5">咨询</span>
          </button>
        </div>
        <button className="flex-1 bg-[#111111] text-[#FFFFFF] font-medium text-[14px] rounded-sm hover:bg-[#111111]/90 transition-colors h-11">
          加入购物袋
        </button>
      </div>
    </div>
  );
}
"""
with open('src/pages/ProductDetail.tsx', 'w') as f:
    f.write(content)
