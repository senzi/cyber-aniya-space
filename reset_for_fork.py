import os
import json
import re
from datetime import datetime

# === 路径定义 ===
VUE_FILE = 'src/pages/Home.vue'
JSON_FILE = 'public/projects.json'

# === 获取用户输入 ===
def get_site_meta():
    print("🛰️ 初始化你的项目站点")
    site_title = input("请输入你的站点主标题（如：我的项目站）: ").strip() or "你的项目站点名称"
    site_subtitle = input("请输入副标题（如：用于展示你的个人项目）: ").strip() or "项目展示 · 自定义站点描述"
    return site_title, site_subtitle

# === 替换 Home.vue 中的站点标题 ===
def reset_home_vue(title, subtitle):
    with open(VUE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'🛰️ .*?的赛博空间站', f'🛰️ {title}', content)
    content = re.sub(r'个人项目展示 · 模块化空间站风格', subtitle, content)

    with open(VUE_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 已更新 {VUE_FILE} 中的标题和副标题")

# === 初始化 projects.json ===
def reset_projects_json():
    today = datetime.today().strftime('%Y-%m-%d')

    template_project = {
        "id": "example-project",
        "title": "示例项目标题",
        "description": "这里是你项目的简要描述",
        "tags": ["标签1", "标签2"],
        "repo": "",
        "demo": "",
        "status": "Idea",
        "cover_image": "",
        "created_at": today,
        "updated_at": today
    }

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump([template_project], f, indent=2, ensure_ascii=False)

    print(f"✅ 已初始化 {JSON_FILE}，使用当前日期 {today}")

# === 主程序入口 ===
if __name__ == '__main__':
    title, subtitle = get_site_meta()
    reset_home_vue(title, subtitle)
    reset_projects_json()
    print("\n🎉 初始化完成！现在你可以开始填写你自己的项目啦。\n")
