import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function AIFab() {
  const navigate = useNavigate();

  return (
    <div className="fixed bottom-[80px] right-4 z-50 flex items-center justify-end h-[52px]">
      <button
        onClick={() => navigate('/intent')}
        className="w-[52px] h-[52px] bg-[#111111] text-[#FFFFFF] rounded-sm shadow-[0_4px_16px_rgba(0,0,0,0.2)] flex items-center justify-center hover:scale-105 transition-transform active:scale-95 animate-in zoom-in duration-300"
      >
        <span className="material-symbols-outlined text-[24px] font-light">psychiatry</span>
      </button>
    </div>
  );
}
