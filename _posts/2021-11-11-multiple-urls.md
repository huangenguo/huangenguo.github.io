---
title: "超链接的打开、复制或收藏"
last_modified_at: 2025-08-13
excerpt_separator: "<!--more-->"
categories:
  - Tech
tags:
  - 超链接
  - 浏览器扩展
---

当你在搜索引擎输入某个关键词后得到无数条结果，当你浏览网页时看到一串网址或者遍布网页各处的链接……

如果你有这样的需求：

1. 我想在新标签页**打开**超链接
2. 我想批量**操作**一串连续的超链接
3. 我想选择性地**操作**多个超链接 

<!--more-->

那么不妨继续阅读下去🙃

## 超链接的新标签页打开

网页的超链接是否带有 _blank 元素影响链接的打开方式。

超链接 target 属性的两个关键字：

_self: 当前页面加载（默认值）

_blank: blank 是空白的意思，也就是说带有 _blank 元素的超链接，鼠标左键点击即可在新标签页打开。

代码如下所示：

```html
<a href="" target="_blank">超链接带有 _blank 元素</a>
<a href="" target="_self">超链接带有 _self 元素，当前页面加载</a>
<a href="">超链接无 _blank 元素,当前页面加载</a>
```
<a href="https://huangenguo.github.io/" target="_blank">超链接带有 _blank 元素</a>

<a href="https://huangenguo.github.io/">超链接无 _blank 元素</a>

> [a 元素（或称锚元素）- HTML（超文本标记语言）- MDN](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/a)
>
> [Markdown中如何显示HTML标签_张木期的博客-CSDN博客_markdown怎么写html](https://blog.csdn.net/qq_27674439/article/details/93116914)

这就是我们在日常浏览不同网页时，有的链接在当前页打开，有的链接在新标签页打开背后的原理。

如果我们想在新标签页打开网页，其实不需要查看链接是否带有 _blank 元素，而是**在浏览网页时默认超链接所指向的网页都是在当前页打开的**，这个时候有两种交互方式：

- 按住键盘上的 Ctrl 键同时鼠标左键点击链接
- 鼠标右键打开菜单栏，选择新标签页打开

当然，我们也可以通过一些脚本来实现相同的功能，不过目前还不够智能，要么超链接全在当前页打开，要么全在新标签页打开，有点一刀切的感觉，需要自行动手填入需要匹配的网址。感兴趣的可以参考👇

> [链接地址全在【当前/新建】标签页中打开](https://greasyfork.org/zh-CN/scripts/404870)

## linkclump 让你同时打开、复制或收藏多条链接的拓展

![可视化的方式框选链接，图片源自 linkclump 官方](https://cdn.jsdelivr.net/gh/huangenguo/img@main/Linkclump1.png)



![新标签页打开超链接](https://cdn.jsdelivr.net/gh/huangenguo/img@main/Linkclump4.png)

![复制超链接至剪贴板，包括链接、标题、Markdown 等多种格式选择](https://cdn.jsdelivr.net/gh/huangenguo/img@main/Linkclump3.png)

该拓展的使用包括特征、用法和安装三个部分。

### 特征

激活：也就是选择拓展的触发事件、激活方式（鼠标和快捷键），比如三大组合键shift/alt/ctrl；

动作：也就是能够对超链接进行的操作，比如是打开链接、在新窗口打开、复制还是保存这些链接，也可以组合这些功能；

智能选择：只选择网页中重要的链接；关闭此选项以打开所有选定的链接；

自动滚动：鼠标在边缘时自动滚动，方便跨页选中；

过滤器：根据预设的关键词过滤链接；

延时：在每个链接之间加入延时（应该是方便低配机的性能天花板）；

多系统兼容：三大系统可用；

### 用法

在搜索结果或有链接树状表的网页中按住 alt + 鼠标左键勾选，松开会直接打开链接。

注意：要掂量自己内存容量兜不兜得住，不然卡了慢了自己难受。

不足：扩展选项中勾选允许访问文件 URL，尝试了一下本地的 HTML 文件是可以使用的，但并不适用于 Edge 的 PDF 文件。

> 摘自 [Linkclump - 一口气打开多个链接 - 讨论 - 小众软件官方论坛](https://meta.appinn.net/t/topic/17029/2)

### 安装

> [Linkclump - Chrome 网上应用店](https://chrome.google.com/webstore/detail/linkclump/lfpjkncokllnfokkgpkobnkbkmelfefj) 👍
>
> 338★ [benblack86/linkclump: Google chrome extension that allows you to open multiple links at once.](https://github.com/benblack86/linkclump)
>
> Firefox 有个移植版 [Linkclump for Firefox](https://addons.mozilla.org/zh-CN/firefox/addon/linkclump-for-firefox/)
>
> Firefox 上面的替代品就是 [Snap Links Plus ](https://addons.mozilla.org/zh-CN/firefox/addon/snaplinksplus/)

### Open-Multiple-URLs 打开多个链接（仅作备用）

![图片源自Open-Multiple-URLs官方](https://cdn.jsdelivr.net/gh/huangenguo/img@main/Open-Multiple-URLs.png)

这个工具使用**纯文本格式的网页列表**，将列表粘贴到文本区域(每行一个网站地址) ，选择您的选项并单击“打开网址”就可以在新的选项卡中打开它们。

> 108★ [htrinter/Open-Multiple-URLs: Browser extension for opening lists of URLs](https://github.com/htrinter/Open-Multiple-URLs)

以上多是用鼠标或者键鼠配合的方式实现对超链接的操作，下面介绍扩展和键盘来操作超链接。

## Surfingkeys 用扩展和键盘操作你的浏览器（包括但不限于超链接）

Vim 是命令行界面下的编辑器。我用的不多。

教程可以参考这个👇

> [如何学习 Vim ? @狐狸教程](https://www.freeaihub.com/vim/)

如果你熟悉浏览器的常用快捷键，然后简单用过 Vim，那么，类 vimium 插件非常容易上手。

本文推荐 **Surfingkeys**

通过丰富的键盘快捷命令来**操作链接/切换标签页/滚动页面或捕获完整页面截屏**，让你的浏览器具备 Vim 一样的生产力。

### 同类 vimium 插件

>  16.8k★ [philc/vimium: The hacker's browser.](https://github.com/philc/vimium)
>
>  1.1k★ [gdh1995/vimium-c: 一个基于键盘的浏览器扩展快捷键和一个高级的标签栏操作](https://github.com/gdh1995/vimium-c)

### 用法

![图片源自Surfingkeys官方](https://cdn.jsdelivr.net/gh/huangenguo/img@main/图片源自Surfingkeys官方.png)

在标准模式下，可以通过 **f** 来打开一个链接，按住 SHIFT 翻转重叠提示，按住 SPACE 隐藏提示。

同理通过 **cf** 在新标签页连续打开多个选中的链接。

优点：扩展选项中勾选允许访问文件 URL，适用于 Edge 的 PDF 文件。

### 安装

官方以及网上的解读非常详细了，参考以下两篇进行更详细的了解：

> 3.7k★ [Surfingkeys/README_CN.md at master · brookhong/Surfingkeys](https://github.com/brookhong/Surfingkeys/blob/master/README_CN.md)
>
> [Surfingkeys 实用向推荐 - 少数派](https://sspai.com/post/63692)

### 配置

相对于上面列举的两款类 vimium 插件，Surfingkeys 提供的自定义配置非常方便使用者扩展个性化的功能。

这里附上我的配置，时间和能力关系只码了部分功能，非常需要大佬 fork 并进行功能上的整合与拓展，针对常用网站进行个性化的定制，例如知乎带上关注数和浏览数等等。

个性化功能如下：

- 代替 TabCopy（网页标题和网址拷贝为 markdown 格式），并针对特定网站进行定制，如 净化链接 修改微信公众号文章title标题；本文所呈现的GitHub 带上 star 数😝；知乎去掉「X 条消息 - 知乎」；
- 额外添加的京东、豆瓣图书、淘宝搜索的关键词搜索功能；

> [Surfingkeys customization with jd/douban/taobao search and copy tab(s) as markdown feature.](https://gist.github.com/huangenguo/dd8aea39f321bc8ebf29644036d4bd50)

配置的导入非常简单，打开👆我给的网址，Raw 处右键复制链接。

![](https://cdn.jsdelivr.net/gh/huangenguo/img@main/Surfingkeys-配置1.png)



打开 Surfingkeys 扩展选项，选择高级模式 Advance mode，粘贴链接并保存即可。

### 其他拓展或脚本作补充

> [TabCopy - Chrome 网上应用店](https://chrome.google.com/webstore/detail/tabcopy/micdllihgoppmejpecmkilggmaagfdmb/) 👍👍👍
>
> [引用链接生成器](https://greasyfork.org/zh-CN/scripts/11800-reflinkgenerator)
>
> [链接地址洗白白](https://greasyfork.org/zh-CN/scripts/373270) 👍
>
> [Easy Search Help.](https://s.appinn.me/help.html)

这些拓展或脚本的主要功能是链接的复制以及快捷搜索，可作为 Surfingkeys 的补充。

## 小结

1. 按住 Ctrl 键同时鼠标左键点击链接，能够在新标签页打开网页中无 _blank 元素的超链接

2. linkclump 用可视化的鼠标框选方式来操作多条超链接

3. Open-Multiple-URLs 列表的方式来打开多个超链接

4. 通过 Surfingkeys 和键盘命令选择性地对多个超链接进行操作

当然，还可以通过编写浏览器脚本或 Python 程序来优雅地实现同样的效果，不过我研究的不多。

以上，就是我对于如何批量操作链接，提升上网体验的探索和思考。

现学现用，试着对本文的超链接进行操作吧！