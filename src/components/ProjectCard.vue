<script setup>
import { computed } from 'vue'
import { generateOgImage } from '../utils/ogImage'

const props = defineProps({
  project: {
    type: Object,
    required: true
  },
  liveStatus: {
    type: String, // 'success' | 'fail' | 'unknown'
    default: 'unknown'
  }
})

// og:image 生成
const coverImage = computed(() => {
  if (props.project.cover_image) return props.project.cover_image
  // 本地 Canvas 生成 og:image 占位
  return generateOgImage(props.project.title)
})

// 状态灯颜色
const statusColor = computed(() => {
  if (!props.project.demo) return 'bg-gray-400'
  if (props.liveStatus === 'success') return 'bg-green-500'
  if (props.liveStatus === 'fail') return 'bg-red-500'
  return 'bg-gray-400'
})

/**
 * 状态标签颜色映射
 * Active: 绿色，WIP: 蓝色，Idea: 灰色，Paused: 黄色，Stale: 橙色，Archived: 深灰
 */
const statusTag = computed(() => {
  switch (props.project.status) {
    case 'Active': return 'badge-success'
    case 'WIP': return 'badge-info'
    case 'Idea': return 'badge-ghost'
    case 'Paused': return 'badge-warning'
    case 'Stale': return 'badge-error'
    case 'Archived': return 'badge-neutral'
    default: return 'badge-outline'
  }
})
</script>

<template>
  <div class="card w-full bg-base-100 shadow-lg transition-transform hover:scale-105 hover:shadow-2xl">
    <figure v-if="coverImage">
      <img :src="coverImage" :alt="project.title" class="h-40 w-full object-cover" />
    </figure>
    <div class="card-body">
      <div class="flex items-center gap-2 mb-2">
        <span class="font-bold text-lg">{{ project.title }}</span>
        <span class="badge" :class="statusTag">{{ project.status }}</span>
        <span v-if="project.demo" class="ml-auto flex items-center gap-1">
          <span class="w-3 h-3 rounded-full border" :class="statusColor"></span>
        </span>
      </div>
      <p class="text-base-content/80 mb-2">{{ project.description }}</p>
      <div class="flex flex-wrap gap-1 mb-2">
        <span v-for="tag in project.tags" :key="tag" class="badge badge-outline badge-sm">{{ tag }}</span>
      </div>
      <div class="flex gap-2 mt-auto">
        <a v-if="project.repo" :href="project.repo" target="_blank" class="btn btn-xs btn-outline">Repo</a>
        <a v-if="project.demo" :href="project.demo" target="_blank" class="btn btn-xs btn-primary">Demo</a>
      </div>
      <div class="text-xs text-right text-base-content/60 mt-2">
        <span>更新于 {{ project.updated_at }}</span>
      </div>
    </div>
  </div>
</template>
