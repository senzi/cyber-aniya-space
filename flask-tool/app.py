import os
import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'cyber-aniya-space-tool'

# JSON 数据文件路径（假设 flask-tool 与 src 同级）
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/data/projects.json'))

def load_projects():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_projects(projects):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(projects, f, ensure_ascii=False, indent=2)

def get_project_by_id(pid):
    projects = load_projects()
    for p in projects:
        if p['id'] == pid:
            return p
    return None

@app.route('/')
def index():
    projects = load_projects()
    return render_template('list.html', projects=projects)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        projects = load_projects()
        data = dict(request.form)
        data['tags'] = [t.strip() for t in data.get('tags', '').split(',') if t.strip()]
        now = datetime.now().strftime('%Y-%m-%d')
        data['created_at'] = now
        data['updated_at'] = now
        projects.append(data)
        save_projects(projects)
        flash('项目已添加', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', project=None)

@app.route('/edit/<pid>', methods=['GET', 'POST'])
def edit(pid):
    projects = load_projects()
    project = get_project_by_id(pid)
    if not project:
        flash('未找到项目', 'danger')
        return redirect(url_for('index'))
    if request.method == 'POST':
        for p in projects:
            if p['id'] == pid:
                for k in p.keys():
                    if k in request.form:
                        p[k] = request.form[k]
                p['tags'] = [t.strip() for t in request.form.get('tags', '').split(',') if t.strip()]
                p['updated_at'] = datetime.now().strftime('%Y-%m-%d')
        save_projects(projects)
        flash('项目已更新', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', project=project)

@app.route('/delete/<pid>', methods=['POST'])
def delete(pid):
    projects = load_projects()
    projects = [p for p in projects if p['id'] != pid]
    save_projects(projects)
    flash('项目已删除', 'info')
    return redirect(url_for('index'))

@app.route('/ping', methods=['POST'])
def ping():
    import requests
    url = request.form.get('demo')
    try:
        resp = requests.head(url, timeout=3)
        return jsonify({'ok': resp.ok})
    except Exception:
        return jsonify({'ok': False})

if __name__ == '__main__':
    app.run(debug=True)
