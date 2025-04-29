# 🛰️ 项目名称：**Cyber Aniya Space**
> 「阿尼亚是安妮亞」的个人项目展示站，采用模块化空间站风格，展示各种摸鱼项目、Demo页面与Git仓库。

---

## 🎯 项目目标

构建一个部署在 Cloudflare Pages 上的静态站点，用模块化空间站风格展示你的 side-projects，包括：

- 已上线的 Demo 项目（带 Live 检测）
- 仅有 GitHub 仓库的项目
- 未来可能开发的 idea slot（保留但标注为未开发）

---

## 🧱 技术栈

- **前端框架**：Vite + Vue 3 + Script Setup
- **样式系统**：Tailwind CSS v4 + DaisyUI（主题为 `caramellatte`）
- **数据管理**：本地维护一个 JSON 项目清单，使用 Flask 工具编辑与生成（不部署，仅本地使用）
- **部署平台**：Cloudflare Pages（自动构建）
- **运行命令工具**：Bun（主）+ npm（兼容性用）

---

## 🧩 模块功能列表

### 1. 项目展示区（模块化卡片）
- 使用 CSS Grid 实现响应式排布
- 每个卡片模块展示：
  - `title`（项目名）
  - `description`（一句话介绍）
  - `tags`（如 Vue、Demo、摸鱼、Tool 等）
  - `repo` 链接（可选）
  - `demo` 链接（可选，自动 ping）
  - `cover_image`（可选，未配置则生成 Vercel 风格 og:image）
  - `status`（Active / Archived / WIP 等）

### 2. Live 状态检测
- 页面加载时，对所有 `demo` 地址进行一次性 ping 检测
- 超时或失败显示红灯；成功显示绿灯
- 不重复 ping，节省资源

### 3. 后台管理工具（本地 Flask）
- JSON 数据文件手动管理或用 Flask 表单编辑器维护
- 支持：
  - 添加/删除项目
  - 自动生成 `updated_at` 字段
  - 检查 demo 可用性
  - 预览 og:image 效果

---

## 🧾 数据结构（JSON Schema）

```json
{
  "id": "deepluck",
  "title": "DeepLuck",
  "description": "一个签文小应用，生成好运签文",
  "tags": ["Vue", "Demo", "摸鱼"],
  "repo": "https://github.com/aniya/deepluck",
  "demo": "https://deepluck.pages.dev",
  "status": "Active",
  "cover_image": "",  // 可选，不填使用 og:image
  "created_at": "2024-06-01",
  "updated_at": "2025-04-28"
}
```

---

## 🎨 UI 设计要点

- 使用 DaisyUI 提供的 `caramellatte` 主题
- 页面背景采用 `bg-base-200`，风格明亮柔和
- 卡片悬浮时微微放大 (`hover:scale-105`) 并发光 (`shadow-lg`)
- 每个项目卡片显示状态灯（绿/红）
- 页面顶部 Logo 或标题可使用：
  > `阿尼亚的赛博空间站` / `Cyber Aniya Space`

---

## 🔧 目录结构建议

```
cyber-aniya-space/
├─ public/
├─ src/
│  ├─ assets/
│  │  └─ tailwind.css
│  ├─ components/
│  │  └─ ProjectCard.vue
│  ├─ pages/
│  │  └─ Home.vue
│  ├─ data/
│  │  └─ projects.json
│  └─ App.vue
├─ tailwind.config.js
├─ postcss.config.js
├─ vite.config.js
├─ package.json
├─ bun.lockb
```

