import os
import re

with open('src/pages/IntentCanvas.tsx', 'r') as f:
    content = f.read()

# Replace relative path with fixed viewport calculation to fix input overlapping chat
content = content.replace(
    '<div className="max-w-[430px] mx-auto px-4 pt-6 pb-32 flex flex-col gap-6">',
    '<div className="max-w-[430px] mx-auto px-4 pt-6 pb-40 flex flex-col gap-6">'
)

content = content.replace(
    '<main className="flex-1 overflow-y-auto w-full hide-scrollbar">',
    '<main className="flex-1 overflow-y-auto w-full hide-scrollbar scroll-smooth relative">'
)

with open('src/pages/IntentCanvas.tsx', 'w') as f:
    f.write(content)

