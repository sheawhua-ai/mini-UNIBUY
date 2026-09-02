import os

def replace_corners(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace rounded corners with sharp/editorial corners
    content = content.replace('rounded-xl', 'rounded-sm')
    content = content.replace('rounded-2xl', 'rounded-sm')
    content = content.replace('rounded-3xl', 'rounded-sm')
    content = content.replace('rounded-[16px]', 'rounded-sm')
    content = content.replace('rounded-lg', 'rounded-sm')
    content = content.replace('rounded-full', 'rounded-none') 
    
    # Keep some specific elements rounded-full like buttons/icons if needed, 
    # but for luxury, even buttons are often sharp. 
    # Let's selectively fix the Search Bar in Home.tsx manually later.

    with open(filepath, 'w') as f:
        f.write(content)

for file in ['src/pages/Home.tsx', 'src/pages/Explore.tsx', 'src/pages/ProductDetail.tsx', 'src/pages/PrivateCuration.tsx', 'src/pages/DynamicResults.tsx', 'src/pages/Profile.tsx', 'src/pages/MemberCenter.tsx']:
    replace_corners(file)
