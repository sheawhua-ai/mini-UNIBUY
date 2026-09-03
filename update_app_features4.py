import os
import re

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# 8. Update ProductDetail.tsx
with open('src/pages/ProductDetail.tsx', 'r') as f:
    pd_content = f.read()

# Add useCart import
if "import { useCart }" not in pd_content:
    pd_content = pd_content.replace("import { useNavigate, useLocation } from 'react-router-dom';", "import { useNavigate, useLocation } from 'react-router-dom';\nimport { useCart } from '../context/CartContext';")

# Add useCart hook logic
if "const { addToCart } = useCart();" not in pd_content:
    pd_content = pd_content.replace("const [selectedFulfillment, setSelectedFulfillment] = useState(productFulfillments[0]);", 
    """const [selectedFulfillment, setSelectedFulfillment] = useState(productFulfillments[0]);
  
  const { addToCart } = useCart();
  const [showToast, setShowToast] = useState(false);

  const handleAddToCart = () => {
    addToCart({
      product,
      color: selectedColor,
      size: selectedSize,
      fulfillment: selectedFulfillment,
      quantity: 1
    });
    setShowToast(true);
    setTimeout(() => setShowToast(false), 2000);
  };""")

# Update the Bottom Action Bar
old_bottom_bar = """<div className="fixed bottom-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF] border-t border-[#E4E3DE] px-4 py-3 flex items-center gap-3 pb-safe shadow-[0_-4px_16px_rgba(0,0,0,0.04)]">
        <button className="flex-1 h-[48px] border border-[#111111] text-[#111111] font-medium text-[14px] rounded-sm flex items-center justify-center hover:bg-[#F7F7F5] transition-colors">
          加入购物袋
        </button>
        <button className="flex-1 h-[48px] bg-[#111111] text-[#FFFFFF] font-medium text-[14px] rounded-sm flex items-center justify-center hover:opacity-90 transition-opacity">
          立即购买
        </button>
      </div>"""

new_bottom_bar = """<div className="fixed bottom-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF] border-t border-[#E4E3DE] px-4 py-3 flex items-center gap-3 pb-safe shadow-[0_-4px_16px_rgba(0,0,0,0.04)]">
        <button onClick={handleAddToCart} className="flex-1 h-[48px] border border-[#111111] text-[#111111] font-medium text-[14px] rounded-sm flex items-center justify-center hover:bg-[#F7F7F5] transition-colors">
          加入购物袋
        </button>
        <button onClick={() => { handleAddToCart(); navigate('/cart'); }} className="flex-1 h-[48px] bg-[#111111] text-[#FFFFFF] font-medium text-[14px] rounded-sm flex items-center justify-center hover:opacity-90 transition-opacity">
          立即购买
        </button>
      </div>

      {showToast && (
        <div className="fixed top-20 left-1/2 -translate-x-1/2 z-[60] bg-[#111111] text-[#FFFFFF] px-6 py-3 rounded-sm shadow-xl text-[13px] font-medium animate-in slide-in-from-top-4 fade-in duration-300">
          商品已成功加入购物袋
        </div>
      )}"""

pd_content = pd_content.replace(old_bottom_bar, new_bottom_bar)
write_file('src/pages/ProductDetail.tsx', pd_content)

# 9. Update Explore.tsx
with open('src/pages/Explore.tsx', 'r') as f:
    ex_content = f.read()

# Add isFilterOpen state
if "const [isFilterOpen, setIsFilterOpen] = useState(false);" not in ex_content:
    ex_content = ex_content.replace("const [activeTab, setActiveTab] = useState('ALL');", "const [activeTab, setActiveTab] = useState('ALL');\n  const [isFilterOpen, setIsFilterOpen] = useState(false);")

# Update "Filter" button to open the drawer
ex_content = ex_content.replace(
    '<button className="flex items-center gap-1.5 text-[12px] font-medium text-[#111111] hover:opacity-70">',
    '<button onClick={() => setIsFilterOpen(true)} className="flex items-center gap-1.5 text-[12px] font-medium text-[#111111] hover:opacity-70">'
)

# Add Filter Drawer before closing main tag
filter_drawer = """
      {/* Advanced Filter Drawer */}
      {isFilterOpen && (
        <div className="fixed inset-0 z-[110] left-1/2 -translate-x-1/2 max-w-[430px] w-full h-full flex justify-end">
          <div className="absolute inset-0 bg-black/40 backdrop-blur-sm transition-opacity" onClick={() => setIsFilterOpen(false)} />
          <div className="relative w-[85%] bg-[#FFFFFF] h-full shadow-2xl flex flex-col animate-in slide-in-from-right duration-300">
             
             <div className="h-14 border-b border-[#E4E3DE] flex justify-between items-center px-5">
               <span className="font-medium text-[15px] text-[#111111]">筛选与排序</span>
               <button onClick={() => setIsFilterOpen(false)} className="text-[#666663] hover:text-[#111111] -mr-2 p-2">
                 <span className="material-symbols-outlined text-[20px]">close</span>
               </button>
             </div>
             
             <div className="flex-1 overflow-y-auto px-5 py-6 flex flex-col gap-8">
               {/* Sort Section */}
               <section>
                 <h4 className="text-[12px] font-medium text-[#111111] mb-4">排序方式</h4>
                 <div className="flex flex-col gap-3">
                   {['最新上架', '价格从低到高', '价格从高到低', '热销单品'].map((opt, i) => (
                     <label key={i} className="flex items-center justify-between cursor-pointer group">
                       <span className={`text-[13px] ${i === 0 ? 'text-[#111111] font-medium' : 'text-[#666663] group-hover:text-[#111111]'}`}>{opt}</span>
                       <div className={`w-4 h-4 rounded-full border flex items-center justify-center ${i === 0 ? 'border-[#111111]' : 'border-[#E4E3DE]'}`}>
                         {i === 0 && <div className="w-2 h-2 bg-[#111111] rounded-full" />}
                       </div>
                     </label>
                   ))}
                 </div>
               </section>

               <div className="h-px bg-[#E4E3DE] w-full" />

               {/* Origin Section */}
               <section>
                 <h4 className="text-[12px] font-medium text-[#111111] mb-4">发货地版本</h4>
                 <div className="flex gap-2">
                   <button className="flex-1 py-2.5 border border-[#111111] bg-[#111111] text-[#FFFFFF] text-[12px] rounded-sm">不限</button>
                   <button className="flex-1 py-2.5 border border-[#E4E3DE] bg-[#FFFFFF] text-[#111111] text-[12px] rounded-sm hover:border-[#111111] transition-colors">海外直发</button>
                   <button className="flex-1 py-2.5 border border-[#E4E3DE] bg-[#FFFFFF] text-[#111111] text-[12px] rounded-sm hover:border-[#111111] transition-colors">大陆现货</button>
                 </div>
               </section>

               <div className="h-px bg-[#E4E3DE] w-full" />

               {/* Brand Section */}
               <section>
                 <div className="flex justify-between items-center mb-4">
                   <h4 className="text-[12px] font-medium text-[#111111]">品牌</h4>
                   <span className="text-[11px] text-[#666663] underline underline-offset-2">展开全部</span>
                 </div>
                 <div className="flex flex-col gap-4">
                   {['The Row', 'Loro Piana', 'Bottega Veneta', 'Jil Sander'].map((brand, i) => (
                     <label key={i} className="flex items-center gap-3 cursor-pointer group">
                       <div className={`w-4 h-4 border rounded-sm flex items-center justify-center ${i === 0 ? 'border-[#111111] bg-[#111111]' : 'border-[#E4E3DE] bg-[#FFFFFF]'}`}>
                         {i === 0 && <span className="material-symbols-outlined text-[12px] text-[#FFFFFF]">check</span>}
                       </div>
                       <span className={`text-[13px] ${i === 0 ? 'text-[#111111] font-medium' : 'text-[#666663] group-hover:text-[#111111]'}`}>{brand}</span>
                     </label>
                   ))}
                 </div>
               </section>
               
               <div className="h-px bg-[#E4E3DE] w-full" />
               
               {/* Price Section */}
               <section>
                 <h4 className="text-[12px] font-medium text-[#111111] mb-4">价格区间 (¥)</h4>
                 <div className="flex items-center gap-3">
                   <input type="number" placeholder="最低" className="w-full h-10 border border-[#E4E3DE] rounded-sm px-3 text-[13px] outline-none focus:border-[#111111] bg-[#F7F7F5]" />
                   <span className="text-[#666663]">-</span>
                   <input type="number" placeholder="最高" className="w-full h-10 border border-[#E4E3DE] rounded-sm px-3 text-[13px] outline-none focus:border-[#111111] bg-[#F7F7F5]" />
                 </div>
               </section>

             </div>
             
             {/* Bottom Action */}
             <div className="p-4 border-t border-[#E4E3DE] flex gap-3 pb-safe bg-[#FFFFFF]">
                <button className="flex-1 h-11 border border-[#111111] text-[#111111] text-[13px] font-medium rounded-sm hover:bg-[#F7F7F5] transition-colors">重置</button>
                <button onClick={() => setIsFilterOpen(false)} className="flex-[2] h-11 bg-[#111111] text-[#FFFFFF] text-[13px] font-medium rounded-sm hover:opacity-90 transition-opacity">
                  查看 12 件商品
                </button>
             </div>
          </div>
        </div>
      )}
"""
ex_content = ex_content.replace("</main>", "</main>\n" + filter_drawer)
write_file('src/pages/Explore.tsx', ex_content)

