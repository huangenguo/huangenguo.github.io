---
title: "基于 Mixgo Mini 的投球机"
excerpt_separator: "<!--more-->"
categories:
  - Tech
  - Education
tags:
  - 米思齐
---

## 接收器

基于 Mixgo Mini 的红外测距传感器的计数器

硬件准备

- Mixgo Mini开发板：作为主控板，负责处理传感器数据和控制游戏逻辑。
- 板载红外测距传感器：用于检测目标物体的距离
- 板载LED灯或显示屏：用于显示游戏状态，如得分等信息。
- 板载按钮开始游戏
- 外接LED灯带显示剩余次数或颜色提示

<!--more-->
软件编程
1.初始化传感器：在代码中初始化红外测距传感器，设置其工作参数，如测量范围、采样频率等。
2.读取传感器数据：通过循环不断读取红外测距传感器的测量值，获取目标物体的距离信息。
3.设置射击触发条件：当按钮被按下时，触发射击动作。可以结合传感器数据，判断是否击中目标。例如，当目标物体距离在一定范围内时，视为击中。
4.游戏逻辑实现：根据击中情况更新游戏状态，如增加得分、减少剩余生命等。可以通过LED灯或显示屏显示游戏状态的变化。
5.循环运行游戏：将上述步骤组合成一个循环，使游戏持续运行，直到满足结束条件（如剩余生命为0或达到最高得分）。

示例代码框架（基于MicroPython）

```python
from mixgo_mini import onboard_matrix
import mixgo_mini
from mixgo_mini import onboard_als
import machine
import time


while True:
    onboard_matrix.scroll_way(1)
    while True:
        onboard_matrix.shows('B1', space=0, center=True)
        if (mixgo_mini.B1key.was_pressed()):
            break
    得分 = 0
    while True:
        if onboard_als.ps_nl() > 50:
            得分 = 得分 + 1
        print(onboard_als.ps_nl())
        onboard_matrix.shows(得分, space=0, center=True)
        time.sleep(0.1)
        if (mixgo_mini.B2key.was_pressed()):
            break
    得分 = 0
    onboard_matrix.shows(得分, space=0, center=True)

```

[智控万物 Microbit控制PC射击游戏](https://mc.dfrobot.com.cn/thread-308395-1-1.html?fromuid=843218)

[自己也来做射击编程游戏 DF创客社区](https://mc.dfrobot.com.cn/thread-305448-1-1.html?fromuid=843218)

## 发射器

基于激光切割的橡皮筋枪
3D打印设计和制作发射器，手指投篮装置与比赛
物料 乒乓球

[手指轻弹篮球比赛：14 个步骤（附图片） - Instructables](https://www.instructables.com/Finger-Flick-Basketball-Game/)

[micro:bit篮球计分器 DF创客社区](https://mc.dfrobot.com.cn/thread-267814-1-1.html)
