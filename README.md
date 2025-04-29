# 🛰️ Cyber Aniya Space

> A modular cyber space station to showcase @阿尼亚是安妮亞's side projects, demos, and repositories.

这是一个用 Vite + Vue + DaisyUI 构建的个人项目展示站点，采用模块化空间站风格，展示了各种上线/未上线的摸鱼项目与 GitHub 仓库。同时，配有一个本地 Flask 管理工具用于维护项目数据。

---

## 🧱 技术栈

### 前端展示页面

- **Vite + Vue 3**：现代构建工具 + 组合式 API
- **Tailwind CSS v4 + DaisyUI v5**：快速构建响应式美学界面
- **部署平台**：Cloudflare Pages
- **风格主题**：`caramellatte`（由 DaisyUI 提供）

### 本地管理工具（Flask）

- **Flask**：轻量后端管理页面，仅本地运行
- **数据源**：JSON 格式的项目列表（可热更新）
- **功能**：项目增删改查、生成字段、状态检测

---

## 🖥️ 使用方式

### 🚀 启动前端项目

```bash
bun install         # 安装依赖（或 npm install）
bun run dev         # 启动开发服务器
```

前端数据来自 `src/data/projects.json`，页面加载时自动对 demo 进行 ping 检测（显示绿/红灯）。

### 🧰 启动 Flask 本地管理工具

```bash
cd cyber-aniya-manager
python app.py       # 启动 Flask 服务，访问 http://localhost:5000
```

管理页面支持：

- 添加 / 编辑 / 删除项目
- 自动生成 `id`、时间戳
- Demo 可用性状态检测（选填）
- 写入更新至 `projects.json`，用于前端展示

---

## 📁 项目结构简述

```
├─ cyber-aniya-space/         # 主前端项目（Vite + Vue）
│  ├─ src/
│  │  ├─ components/          # 卡片组件
│  │  ├─ data/projects.json   # 项目列表数据源
│  │  ├─ assets/tailwind.css  # Tailwind 样式入口
│  └─ ...
├─ cyber-aniya-manager/       # 本地 Flask 管理工具
│  ├─ app.py
│  ├─ templates/
│  └─ data/projects.json      # 管理输出文件
```

---

## 📜 License

MIT License  
