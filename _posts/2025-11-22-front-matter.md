---
title: "front-matter 字段"
comments: false
toc: false
categories:
  - Blog
tags:
  - Jekyll
---

## front-matter 字段

Jekyll 本身不限制 front-matter 字段，主题决定哪些字段被使用。

常见且常被主题（如 Minimal Mistakes）识别的字段包括：

基本：title / date / layout / permalink / published / draft

文章描述：excerpt / excerpt_separator / description / last_modified_at

分类与标签：categories / tags

作者与社交：author / authors / author_profile / social

页面显示：toc / toc_label / read_time / comments / share / related

资源/SEO：image / social_image / canonical_url / redirect_from / seo相关字段

主题/站点：url / baseurl / repository / minimal_mistakes_skin / search 等

自定义变量：任意自定义键（在模板中通过 site.xxx 或 page.xxx 访问）

推荐用法示例（front-matter）：

```markdown
title: "示例文章"
date: 2025-11-22
excerpt_separator: "<!--more-->"
excerpt: "这是摘要，可手写也可由分隔符截取。"
categories:
  - Tech
tags:
  - 笔电改装
last_modified_at: 2025-11-22
comments: true
toc: true
```

## 摘要

若同时提供 excerpt 和 excerpt_separator：多数主题优先使用 excerpt（手写）；若未写 excerpt，Jekyll 会用分隔符前的内容或自动生成。
想要在模板中显示摘要，确认主题模板使用 page.excerpt 或 page.description；不同主题命名可能不同。
可自由添加自定义字段（如 hardware_compatibility: true），再在布局中引用。

TL;DR 是 “Too long; didn’t read” 的缩写，中文常用作文章开头的简短摘要或结论段，作用是快速传达核心要点，方便读者快速判断是否继续阅读，也便于社媒/目录/搜索显示。

用法要点（简短）：

放在文章开头，用 1–3 行概述核心结论或行动建议。
在 Jekyll/Hexo 等静态站点可用 front-matter 的 excerpt 或自定义字段存储，模板中调用显示。
写法简洁明确，优先用动词和数字，便于快速扫描。

示例 — Markdown 段落写法：

```markdown
## TL;DR
- 优先升级：内存 DDR3L 8GB + SATA SSD 256GB
- 预算参考：￥300–900；难度：中等
```

示例 使用 excerpt：

```markdown
title: "华硕 X455LJ 改装记"
excerpt: "TL;DR：优先升级内存与 SSD，可显著提升性能，预算约￥300–900。"
excerpt_separator: "<!--more-->"
```

示例 — 自定义字段并在模板调用（Jekyll/Liquid）：

```markdown
title: "示例"
tl_dr: "TL;DR：内存+SSD，快速提升体验。"
```

```html
<p class="tldr">{{ page.tl_dr | default: page.excerpt }}</p>
```
