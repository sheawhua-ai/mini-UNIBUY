import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# 1. Cart Context
write_file('src/context/CartContext.tsx', """import React, { createContext, useContext, useState, ReactNode } from 'react';

export interface CartItem {
  id: string;
  product: any;
  color: string;
  size: string;
  fulfillment: any;
  quantity: number;
}

interface CartContextType {
  items: CartItem[];
  addToCart: (item: Omit<CartItem, 'id'>) => void;
  removeFromCart: (id: string) => void;
  updateQuantity: (id: string, qty: number) => void;
  totalPrice: number;
}

const CartContext = createContext<CartContextType | undefined>(undefined);

export function CartProvider({ children }: { children: ReactNode }) {
  const [items, setItems] = useState<CartItem[]>([]);

  const addToCart = (newItem: Omit<CartItem, 'id'>) => {
    setItems(prev => {
      const existing = prev.find(i => 
        i.product.name === newItem.product.name && 
        i.color === newItem.color && 
        i.size === newItem.size && 
        i.fulfillment.id === newItem.fulfillment.id
      );
      if (existing) {
        return prev.map(i => i.id === existing.id ? { ...i, quantity: i.quantity + newItem.quantity } : i);
      }
      return [...prev, { ...newItem, id: Math.random().toString(36).substr(2, 9) }];
    });
  };

  const removeFromCart = (id: string) => setItems(prev => prev.filter(i => i.id !== id));
  
  const updateQuantity = (id: string, qty: number) => {
    if (qty < 1) return;
    setItems(prev => prev.map(i => i.id === id ? { ...i, quantity: qty } : i));
  };

  const totalPrice = items.reduce((sum, item) => {
    const priceStr = item.fulfillment.price.replace(/[^0-9]/g, '');
    return sum + (parseInt(priceStr) * item.quantity);
  }, 0);

  return (
    <CartContext.Provider value={{ items, addToCart, removeFromCart, updateQuantity, totalPrice }}>
      {children}
    </CartContext.Provider>
  );
}

export const useCart = () => {
  const context = useContext(CartContext);
  if (!context) throw new Error('useCart must be used within CartProvider');
  return context;
};
""")

# 2. App.tsx
with open('src/App.tsx', 'r') as f:
    app_code = f.read()
    
# Remove MobileFrame import if it exists, add Context, Category, Cart
app_code = app_code.replace("import MemberCenter from './pages/MemberCenter';", "import Category from './pages/Category';\\nimport Cart from './pages/Cart';")
app_code = app_code.replace("import { BrowserRouter, Routes, Route } from 'react-router-dom';", "import { BrowserRouter, Routes, Route } from 'react-router-dom';\\nimport { CartProvider } from './context/CartContext';")
app_code = app_code.replace("<Route path=\"/member\" element={<MemberCenter />} />", "<Route path=\"/category\" element={<Category />} />\\n        <Route path=\"/cart\" element={<Cart />} />")
app_code = app_code.replace("<BrowserRouter>", "<CartProvider>\\n      <BrowserRouter>")
app_code = app_code.replace("</BrowserRouter>", "</BrowserRouter>\\n    </CartProvider>")

write_file('src/App.tsx', app_code)

# 3. BottomNav.tsx
write_file('src/components/BottomNav.tsx', """import React from 'react';
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
""")

