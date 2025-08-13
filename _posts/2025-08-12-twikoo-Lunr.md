---
title: "尝试添加 Twikoo 评论和 Lunr 搜索功能"
last_modified_at: 2025-08-13
# excerpt_separator: "<!--more-->"
# comments: true
toc: true
toc_sticky: true #将目录“粘贴”到页面顶部。
categories:
  - Blog
tags:
  - twikoo
  - Jekyll
  - Lunr
---
# 评论系统选型

尝试用[Twikoo](https://twikoo.js.org/)部署静态网站评论系统。

备选[giscus](https://giscus.app/zh-CN)

# 云函数部署

采用 Hugging Face 和 MongoDB 部署，失败了。

改用 Vercel 和 MongoDB 部署。

# 前端部署

当然所使用的主题[Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/)并没有提供主动适配，需要自己去定义前端的调用。

参考教程[Configuration - Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/docs/configuration/#comments)

# 搜索功能选型

本来优先想用 Algolia。不过有点复杂，内容年久失修。所以优先选用默认的 Lunr 搜索功能。