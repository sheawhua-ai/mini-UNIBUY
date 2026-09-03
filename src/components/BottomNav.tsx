import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { useCart } from '../context/CartContext';

export default function BottomNav() {
  const location = useLocation();
  const navigate = useNavigate();
  const { items } = useCart();
  const cartCount = items.reduce((acc, item) => acc + item.quantity, 0);

  const tabs = [
    { id: 'home', path: '/', label: '首页', icon: 'home' },
    { id: 'category', path: '/category', label: '分类', icon: 'search' },
    { id: 'cart', path: '/cart', label: '购物袋', icon: 'shopping_bag', badge: cartCount },
    { id: 'profile', path: '/profile', label: '我的', icon: 'person' },
  ];

  return (
    <nav className="fixed bottom-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-[100] pb-safe bg-[#FFFFFF] border-t border-[#E4E3DE] flex justify-around items-center h-[56px] px-4 shadow-[0_-4px_24px_rgba(0,0,0,0.02)]">
      {tabs.map(tab => {
        const isActive = location.pathname === tab.path || (tab.id === 'category' && location.pathname === '/explore');
        return (
          <button
            key={tab.id}
            onClick={() => navigate(tab.path)}
            className={`relative flex flex-col items-center justify-center w-16 transition-colors ${
              isActive ? 'text-[#111111] font-bold translate-y-[-2px]' : 'text-[#666663] hover:text-[#111111]'
            }`}
          >
            <span
              className="material-symbols-outlined mb-0.5 text-[22px]"
              style={{ fontVariationSettings: isActive ? "'FILL' 1" : "'FILL' 0" }}
            >
              {tab.icon}
            </span>
            <span className="font-sans text-[10px] uppercase tracking-wider">{tab.label}</span>
            {tab.badge && tab.badge > 0 ? (
              <span className="absolute top-0 right-2 bg-[#111111] text-[#FFFFFF] text-[9px] font-bold px-1 min-w-[16px] h-[16px] rounded-full flex items-center justify-center">
                {tab.badge}
              </span>
            ) : null}
          </button>
        );
      })}
    </nav>
  );
}
