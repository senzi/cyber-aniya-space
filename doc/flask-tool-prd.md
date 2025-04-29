# 🧰 项目名称：**Cyber Project Manager (for Flask)**

> 本地运行的 Flask 工具，作为你的「赛博空间站」项目数据管理面板。用于快速维护 JSON 数据，不部署，仅用于本地生成。

---

## 🎯 项目目标

提供一个轻量级、直观的后台工具：

- 管理用于前端展示的项目列表（项目卡片）
- 输出符合规范的 `projects.json`
- 本地运行，非线上部署，便于随时修改项目数据并同步至仓库

---

## 🧱 技术栈

- **后端**：Flask（本地运行）
- **模板**：Jinja2 + Tailwind（可选）
- **数据格式**：项目数据储存在 `src/data/projects.json`
- **运行方式**：手动运行 `python app.py` 启动管理界面

---

## 📦 功能模块

### 1. 项目列表页 `/`
- 展示当前所有项目（从 `projects.json` 读取）
- 支持筛选、搜索（按 tag/status/title）
- 每条项目支持「编辑」「删除」操作
- 显示状态指示（是否有 demo、状态灯）

---

### 2. 添加新项目 `/add`
- 表单字段：
  - title（项目名）
  - description（一句话介绍）
  - tags（可逗号分隔）
  - repo URL（可选）
  - demo URL（可选）
  - status（Active / WIP / Archived）
  - cover_image（URL，可为空）
- 自动生成：
  - id（根据 title slug 化）
  - created_at（首次创建）
  - updated_at（每次修改时更新）

---

### 3. 编辑项目 `/edit/<id>`
- 打开对应项目字段预填的编辑页面
- 修改字段后，更新 `updated_at`
- 保存后回到列表页

---

### 4. 删除项目 `/delete/<id>`
- 删除确认后从 JSON 中移除该项目

---

### 5. JSON 文件写入
- 所有改动自动写入 `src/data/projects.json`
- 保存时自动按 `updated_at` 排序（降序显示）

---

### 6. Demo 可用性检测（可选扩展）
- 在添加或编辑页面点击「检测 Demo 状态」
- Flask 后端发起 `requests.head()` 检测 demo URL 是否可访问
- 前端显示小提示（🟢在线 / 🔴无法访问）

---

## 📂 文件结构建议

```
cyber-aniya-manager/
├─ app.py                 # Flask 主程序
├─ templates/
│  ├─ layout.html         # 基础模板
│  ├─ index.html          # 项目列表页
│  ├─ add.html            # 添加页面
│  └─ edit.html           # 编辑页面
├─ static/                # 可选，Tailwind 编译后样式
├─ data/
│  └─ projects.json       # 主数据文件（用于前端展示）
```

---

## 🚀 使用流程

```bash
cd cyber-aniya-manager
python app.py  # 启动 Flask 开发服务器
```

访问 [http://localhost:5000](http://localhost:5000) 进行管理。

编辑完毕后，将 `data/projects.json` 拷贝（或软链）到前端项目的 `src/data/projects.json` 目录。
