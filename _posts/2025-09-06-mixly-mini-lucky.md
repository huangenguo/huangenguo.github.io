---
title: "[项目分享]基于 Mixly Mini 的幸运抽签小程序！"
excerpt_separator: "<!--more-->"
categories:
  - Tech
  - Education
tags:
  - 米思齐
  - Mixly Mini
  - 信息科技
  - 创客教育
  - MicroPython编程教学
  - STEAM教育
  - 幸运抽签
---
# 开源可控信息科技教育行动计划
去年有幸参加[米思齐](https://mixly.cn/)团队的[开源可控信息科技教育行动计划实施办法](https://mp.weixin.qq.com/s/r1v_C-D0fuN_bJOD6t8Mdw)。苦于第一批生产的板子在旧机房遇到驱动适配问题，没有规模化开课。仅小范围在社团中进行推广，后续批次的板子已改进驱动问题。

<!--more-->

# Mixgo Mini 硬件特点

[Mixgo Mini](https://mixly.cn/fredqian/mixgomini) 是一款面向信息科技教育的开源硬件，具有以下特点：
1. 极致性价比
   - 适合大班教学
   - 降低教学成本
   - 方便批量采购

2. 教学友好性
   - 接口设计简洁，甚至使用超前的Type-c接口
   - 不易损坏

3. 技术规格
   - 主控：ESP32-C2
   - 内置丰富板载传感器

# Mixly 3.0 平台创新
[Mixly v3.0](https://go.mixly.cn/) 平台更新带来的变化：

1. 编程语言升级
   - 全面拥抱 MicroPython、Python 语法，在编程教学方面涉及较多概念和有趣方法。
   - 去除 Arduino 语法支持

2. 教学特色
   - 图形化编程，适合入门学习
   - 代码实时转换
   - 提供丰富的示例代码

# 示例一：幸运抽签小程序

幸运抽签是一个深受师生欢迎的互动项目，包括社区也有相关的分享，如[行空板K10 幸运抽签（摇晃、语音）- Makelog(造物记)](https://makelog.dfrobot.com.cn/article-315747.html)。本项目基于 Mixgo Mini 开发，适用于开学祝福、课堂抽奖等使用场景，通过简单的摇晃动作，即可随机获得一条温馨祝福。
最开始的程序设计思路如下，当板载的加速度传感器强度检测达到一定阈值时，随机抽选一个数值，根据数值呈现对应的字符串。
可以发现这里面有代码冗余（重复）的情况，另外祝福话语维护起来并不方便，于是，引入列表这一数据结构。
本项目就分享到这里，欢迎老师和同学们一起交流学习!

完整内容参考[幸运抽签小程序](https://mc.dfrobot.com.cn/thread-397559-1-1.html?fromuid=843218)

# 参考资源
[米思齐信息科技开放课程第三期——Mixgo MINI（元控奋斗板）课程重磅发布！](https://mp.weixin.qq.com/s/HpgGZ9o3_o7Ra0EzMYZLPQ)