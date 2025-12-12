---
title: "图片和视频嵌入"
date: 2025-08-23
# excerpt_separator: "<!--more-->"
toc: false
categories:
  - Blog
tags:
  - Bilibili
  - unsplash
gallery:
  - url: https://unsplash.com/photos/the-sun-is-setting-over-the-ocean-at-the-beach-1yjzCjwYcOo
    image_path: https://images.unsplash.com/photo-1645355405065-ba34cf28532c?q=80&w=973&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
    alt: "南澳岛日出"
---

{% include video id="BV1sxS7Y9EnC" provider="bilibili" danmaku="1" %}

```markdown
{% include video id="BV1sxS7Y9EnC" provider="bilibili" danmaku="1" %}
```

{% include gallery id="gallery" caption="这是一个图库示例" %}

```yaml
gallery:
  - url: /assets/images/unsplash-gallery-image-1.jpg
    image_path: /assets/images/unsplash-gallery-image-1-th.jpg
    alt: "placeholder image 1"
    title: "Image 1 title caption"
  - url: /assets/images/unsplash-gallery-image-2.jpg
    image_path: /assets/images/unsplash-gallery-image-2-th.jpg
    alt: "placeholder image 2"
    title: "Image 2 title caption"
  - url: /assets/images/unsplash-gallery-image-3.jpg
    image_path: /assets/images/unsplash-gallery-image-3-th.jpg
    alt: "placeholder image 3"
    title: "Image 3 title caption"
```

```markdown
{% include gallery id="gallery" caption="这是一个图库示例" %}
```

## 参考教程

[帮助者 - 最小错误](https://mmistakes.github.io/minimal-mistakes/docs/helpers/#bilibili)
