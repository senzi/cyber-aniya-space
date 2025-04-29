// src/utils/ogImage.ts

function hashString(str: string): number {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = (hash << 5) - hash + str.charCodeAt(i);
    hash |= 0;
  }
  return Math.abs(hash);
}

function seededRandom(seed: number): () => number {
  return function() {
    seed = (seed * 48271) % 0x7fffffff;
    return seed / 0x7fffffff;
  };
}

function seededShuffle<T>(array: T[], random: () => number): T[] {
  const arr = array.slice();
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export function generateOgImage(title: string): string {
  const canvas = document.createElement('canvas');
  const width = 1200;
  const height = 630;
  canvas.width = width;
  canvas.height = height;
  const ctx = canvas.getContext('2d');
  if (!ctx) throw new Error('Canvas not supported');

  const seed = hashString(title);
  const random = seededRandom(seed);

  // 背景渐变
  const baseColors = ['#ff9a9e', '#fad0c4', '#a1c4fd', '#c2e9fb', '#d4fc79'];
  const colors = seededShuffle(baseColors, random);

  // 渐变角度基于 hash 随机
  const angle = random() * Math.PI * 2;
  const x1 = width / 2 + Math.cos(angle) * width;
  const y1 = height / 2 + Math.sin(angle) * height;
  const x0 = width / 2 - Math.cos(angle) * width;
  const y0 = height / 2 - Math.sin(angle) * height;

  const gradient = ctx.createLinearGradient(x0, y0, x1, y1);
  colors.forEach((color, idx) => {
    gradient.addColorStop(idx / (colors.length - 1), color);
  });
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, width, height);

  // 文字
  ctx.fillStyle = '#333333';
  ctx.font = 'bold 90px "LXGW WenKai", sans-serif';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';

  const maxWidth = width * 0.8;
  const lines: string[] = [];
  let currentLine = '';
  for (const char of title) {
    const testLine = currentLine + char;
    const testWidth = ctx.measureText(testLine).width;
    if (testWidth > maxWidth && currentLine.length > 0) {
      lines.push(currentLine);
      currentLine = char;
    } else {
      currentLine = testLine;
    }
  }
  if (currentLine) lines.push(currentLine);

  const lineHeight = 80;
  const totalHeight = lines.length * lineHeight;
  const startY = (height - totalHeight) / 2 + lineHeight / 2;

  lines.forEach((line, index) => {
    ctx.fillText(line, width / 2, startY + index * lineHeight);
  });

  return canvas.toDataURL('image/png');
}
