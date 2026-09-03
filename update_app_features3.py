import os
import re

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# 6. Profile.tsx
write_file('src/pages/Profile.tsx', """import React from 'react';
import { useNavigate } from 'react-router-dom';
import BottomNav from '../components/BottomNav';

export default function Profile() {
  const navigate = useNavigate();

  return (
    <div className="bg-[#FFFFFF] text-[#111111] font-sans antialiased min-h-screen pb-[100px]">
      <header className="fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]">
        <div className="relative flex justify-center items-center px-4 h-14 w-full">
          <h1 className="font-serif text-[18px] tracking-widest font-bold">我的</h1>
        </div>
      </header>
      
      <main className="pt-20 px-5 w-full">
        <div className="flex items-center gap-4 mb-8">
          <div className="w-16 h-16 rounded-full overflow-hidden bg-[#E4E3DE] border border-[#E4E3DE]">
            <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=200" alt="Avatar" className="w-full h-full object-cover" />
          </div>
          <div>
            <h2 className="text-[18px] font-medium text-[#111111] mb-1">S. Wang</h2>
            <p className="text-[12px] text-[#666663] font-mono">swang.archive@example.com</p>
          </div>
        </div>

        {/* Member Tier Card */}
        <div className="bg-[#111111] text-[#FFFFFF] p-5 rounded-sm relative overflow-hidden mb-8 shadow-lg cursor-pointer" onClick={() => {}}>
          <div className="absolute top-0 right-0 w-32 h-32 bg-[#FFFFFF]/5 rounded-full blur-2xl -mr-10 -mt-10"></div>
          <div className="flex justify-between items-start mb-6 relative z-10">
            <div>
              <h2 className="font-serif text-[18px] tracking-widest mb-1">UNIBUY NOIR</h2>
              <p className="text-[11px] text-[#FFFFFF]/60 font-mono">ID: 8849 2011 44</p>
            </div>
            <span className="material-symbols-outlined text-[28px] text-[#FFFFFF]/80">diamond</span>
          </div>
          <div className="relative z-10">
            <div className="flex justify-between text-[11px] mb-2 font-mono">
              <span>当前积分: 14,500</span>
              <span className="text-[#FFFFFF]/60">距 PLATINUM 差 5,500</span>
            </div>
            <div className="w-full h-1 bg-[#FFFFFF]/20 rounded-full overflow-hidden mb-5">
              <div className="h-full bg-[#FFFFFF] w-[72%] rounded-full"></div>
            </div>
            <div className="grid grid-cols-3 gap-2 border-t border-[#FFFFFF]/20 pt-4 mt-2">
              <div className="flex flex-col items-center text-center">
                <span className="material-symbols-outlined text-[20px] mb-1.5 text-[#FFFFFF]/80">local_shipping</span>
                <span className="text-[10px] text-[#FFFFFF]/80">全球免邮</span>
              </div>
              <div className="flex flex-col items-center text-center border-l border-r border-[#FFFFFF]/20">
                <span className="material-symbols-outlined text-[20px] mb-1.5 text-[#FFFFFF]/80">support_agent</span>
                <span className="text-[10px] text-[#FFFFFF]/80">1v1顾问</span>
              </div>
              <div className="flex flex-col items-center text-center">
                <span className="material-symbols-outlined text-[20px] mb-1.5 text-[#FFFFFF]/80">redeem</span>
                <span className="text-[10px] text-[#FFFFFF]/80">生日礼遇</span>
              </div>
            </div>
          </div>
        </div>

        {/* Orders & Shortcuts */}
        <div className="mb-8">
          <div className="flex justify-between items-end mb-4">
            <h3 className="text-[14px] font-medium text-[#111111]">我的订单</h3>
            <span className="text-[12px] text-[#666663] cursor-pointer hover:text-[#111111]">查看全部</span>
          </div>
          <div className="flex justify-between items-center bg-[#F7F7F5] p-4 rounded-sm border border-[#E4E3DE]">
            {[
              { icon: 'wallet', label: '待付款' },
              { icon: 'inventory_2', label: '待发货' },
              { icon: 'local_shipping', label: '待收货' },
              { icon: 'assignment_return', label: '退换/售后' }
            ].map((item, i) => (
              <div key={i} className="flex flex-col items-center gap-1.5 cursor-pointer hover:opacity-70">
                <span className="material-symbols-outlined text-[22px] text-[#111111]">{item.icon}</span>
                <span className="text-[11px] text-[#666663]">{item.label}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Menu List */}
        <div className="flex flex-col">
          {[
            { icon: 'favorite', label: '心愿单' },
            { icon: 'location_on', label: '地址管理' },
            { icon: 'payments', label: '支付方式' },
            { icon: 'notifications', label: '消息通知' },
            { icon: 'help', label: '帮助与客服' },
            { icon: 'settings', label: '设置' },
          ].map((item, i) => (
            <button key={i} className="flex items-center justify-between py-4 border-b border-[#E4E3DE] last:border-0 hover:bg-[#F7F7F5] transition-colors -mx-5 px-5">
              <div className="flex items-center gap-3">
                <span className="material-symbols-outlined text-[20px] text-[#666663]">{item.icon}</span>
                <span className="text-[14px] text-[#111111]">{item.label}</span>
              </div>
              <span className="material-symbols-outlined text-[18px] text-[#E4E3DE]">chevron_right</span>
            </button>
          ))}
        </div>
      </main>

      <BottomNav />
    </div>
  );
}
""")

# 7. Update Home.tsx to clean up top nav
with open('src/pages/Home.tsx', 'r') as f:
    home_content = f.read()

# Replace header block
new_header = """<header className={`fixed top-0 left-1/2 -translate-x-1/2 max-w-[430px] w-full z-50 transition-colors duration-300 ${scrolled ? 'bg-[#FFFFFF]/90 backdrop-blur-xl border-b border-[#E4E3DE]' : 'bg-transparent'}`}>
        <div className="relative flex justify-center items-center px-4 h-14 w-full">
          <h1 className={`font-serif text-[20px] tracking-widest font-bold ${scrolled ? 'text-[#111111]' : 'text-white'}`}>UNIBUY</h1>
        </div>
      </header>"""

# Using regex to replace the whole header block
home_content = re.sub(r'<header.*?</header>', new_header, home_content, flags=re.DOTALL)
# Also remove Slide-out Menu Drawer logic
home_content = re.sub(r'\{\/\* Slide-out Menu Drawer \*\/.*?\}\)', '', home_content, flags=re.DOTALL)
# Also remove `const [isMenuOpen, setIsMenuOpen] = useState(false);`
home_content = home_content.replace("const [isMenuOpen, setIsMenuOpen] = useState(false);\n", "")

write_file('src/pages/Home.tsx', home_content)

