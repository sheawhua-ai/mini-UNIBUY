const fs = require('fs');
const path = require('path');
const pagesDir = path.join(process.cwd(), 'src', 'pages');
const componentsDir = path.join(process.cwd(), 'src', 'components');

const fixContent = (content) => {
  // Replace 'fixed top-0 left-0 w-full' with 'fixed top-0 left-1/2 -translate-x-1/2 w-full max-w-[430px]'
  // We need to handle variations. 
  // Let's just find 'fixed' and 'w-full' and 'left-0', and replace them.
  // A simpler way: replace 'left-0 w-full' with 'left-1/2 -translate-x-1/2 w-full max-w-[430px]' in any line that contains 'fixed'.
  
  let lines = content.split('\n');
  let changed = false;
  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];
    if (line.includes('fixed ') || line.includes('"fixed"')) {
      if (line.includes('left-0') && line.includes('w-full')) {
        lines[i] = line.replace('left-0', 'left-1/2 -translate-x-1/2 max-w-[430px]');
        changed = true;
      }
    }
  }
  return changed ? lines.join('\n') : content;
};

const processDir = (dir) => {
  if (!fs.existsSync(dir)) return;
  const files = fs.readdirSync(dir);
  for (let file of files) {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      processDir(fullPath);
    } else if (fullPath.endsWith('.tsx') || fullPath.endsWith('.jsx')) {
      let content = fs.readFileSync(fullPath, 'utf8');
      let newContent = fixContent(content);
      if (newContent !== content) {
        fs.writeFileSync(fullPath, newContent);
        console.log(`Updated ${fullPath}`);
      }
    }
  }
};

processDir(pagesDir);
processDir(componentsDir);
console.log("Done");
