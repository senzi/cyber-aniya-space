<script setup>
import { ref, onMounted } from 'vue'
import ProjectCard from '../components/ProjectCard.vue'

// 项目数据
const projects = ref([])
// live 状态：{ [id]: 'success' | 'fail' | 'unknown' }
const liveStatusMap = ref({})

// 读取本地 JSON
async function loadProjects() {
  const res = await fetch('/src/data/projects.json')
  projects.value = await res.json()
}

// 并发 ping demo 链接
async function checkLiveStatus() {
  const status = {}
  await Promise.all(
    projects.value.map(async (p) => {
      if (p.demo) {
        try {
          // 只请求 HEAD，超时3s
          const controller = new AbortController()
          const timeout = setTimeout(() => controller.abort(), 3000)
          const resp = await fetch(p.demo, { method: 'HEAD', signal: controller.signal })
          clearTimeout(timeout)
          status[p.id] = resp.ok ? 'success' : 'fail'
        } catch {
          status[p.id] = 'fail'
        }
      } else {
        status[p.id] = 'unknown'
      }
    })
  )
  liveStatusMap.value = status
}

onMounted(async () => {
  await loadProjects()
  await checkLiveStatus()
})
</script>

<template>
  <div class="min-h-screen bg-base-200 flex flex-col">
    <header class="py-8 text-center">
      <h1 class="text-3xl font-bold tracking-widest text-primary drop-shadow">
        🛰️ 阿尼亚的赛博空间站
      </h1>
      <p class="text-base-content/70 mt-2">个人项目展示 · 模块化空间站风格</p>
    </header>
    <main class="flex-1 w-full max-w-5xl mx-auto px-4">
      <div class="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
        <ProjectCard
          v-for="project in projects"
          :key="project.id"
          :project="project"
          :liveStatus="liveStatusMap[project.id] || 'unknown'"
        />
      </div>
      <div class="text-center text-xs text-base-content/50 mt-10 mb-4">
        Powered by Vite · Vue3 · TailwindCSS · DaisyUI
      </div>
    </main>
  </div>
</template>
