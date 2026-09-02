import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

export default function BottomNav() {
  const location = useLocation();
  const navigate = useNavigate();

  const tabs = [
    { id: 'explore', path: '/', label: '探索', icon: 'explore' },
    { id: 'member', path: '/member', label: '会员', icon: 'military_tech' },
    { id: 'profile', path: '/profile', label: '我的', icon: 'person' },
  ];

  return (
    <nav className="fixed bottom-0 left-0 w-full z-50 pb-safe bg-pure-white border-t border-hairline flex justify-around items-center h-[56px] px-4 shadow-[0_-4px_24px_rgba(0,0,0,0.02)]">
      {tabs.map(tab => {
        const isActive = location.pathname === tab.path;
        return (
          <button
            key={tab.id}
            onClick={() => navigate(tab.path)}
            className={`flex flex-col items-center justify-center w-16 transition-colors ${
              isActive ? 'text-primary font-bold translate-y-[-2px]' : 'text-on-surface-variant hover:text-primary'
            }`}
          >
            <span
              className="material-symbols-outlined mb-0.5 text-[22px]"
              style={{ fontVariationSettings: isActive ? "'FILL' 1" : "'FILL' 0" }}
            >
              {tab.icon}
            </span>
            <span className="font-label-ui text-[10px] uppercase tracking-wider">{tab.label}</span>
          </button>
        );
      })}
    </nav>
  );
}
