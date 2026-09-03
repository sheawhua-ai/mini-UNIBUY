/** 
 * @license 
 * SPDX-License-Identifier: Apache-2.0 
 */
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { CartProvider } from './context/CartContext';
import Home from './pages/Home';
import PrivateCuration from './pages/PrivateCuration';
import IntentCanvas from './pages/IntentCanvas';
import DynamicResults from './pages/DynamicResults';
import Explore from './pages/Explore';
import VisualSearch from './pages/VisualSearch';
import Category from './pages/Category';
import Cart from './pages/Cart';
import Checkout from './pages/Checkout';
import Orders from './pages/Orders';
import ProductDetail from './pages/ProductDetail';
import Profile from './pages/Profile';
import Compare from './pages/Compare';

export default function App() {
  return (
    <CartProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/private" element={<PrivateCuration />} />
          <Route path="/intent" element={<IntentCanvas />} />
          <Route path="/results" element={<DynamicResults />} />
          <Route path="/explore" element={<Explore />} />
          <Route path="/visual-search" element={<VisualSearch />} />
          <Route path="/category" element={<Category />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/checkout" element={<Checkout />} />
          <Route path="/orders" element={<Orders />} />
          <Route path="/product" element={<ProductDetail />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/compare" element={<Compare />} />
        </Routes>
      </BrowserRouter>
    </CartProvider>
  );
}
