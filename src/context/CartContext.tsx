import React, { createContext, useContext, useState, ReactNode } from 'react';

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
  clearCart: () => void;
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
  
  const clearCart = () => setItems([]);

  const updateQuantity = (id: string, qty: number) => {
    if (qty < 1) return;
    setItems(prev => prev.map(i => i.id === id ? { ...i, quantity: qty } : i));
  };

  const totalPrice = items.reduce((sum, item) => {
    const priceStr = item.fulfillment.price.replace(/[^0-9]/g, '');
    return sum + (parseInt(priceStr) * item.quantity);
  }, 0);

  return (
    <CartContext.Provider value={{ items, addToCart, removeFromCart, updateQuantity, clearCart, totalPrice }}>
      {children}
    </CartContext.Provider>
  );
}

export const useCart = () => {
  const context = useContext(CartContext);
  if (!context) throw new Error('useCart must be used within CartProvider');
  return context;
};
