---
title: "基于 Mixgo Mini 的AI灯带编程"
excerpt_separator: "<!--more-->"
categories:
  - Tech
  - Education
tags:
  - 米思齐
  - Mixgo Mini
  - LED编程
  - AI编程
  - MicroPython
  - 创客教育
---

AI辅助硬件编程成为一项新的范式逐步走进公众视野，除了前一阵推出的linkboy AI以外，还有诸多生成式人工智能为硬件编程带来了新的可能，本文受微信视频号的启发，结合Kimi生成式人工智能与米思齐编程平台开展基于 Mixgo Mini 的灯带编程实验。

<!--more-->

## 硬件准备

- Mixgo Mini 开发板
- WS2812B 灯带（30颗）
- 杜邦线

## 开发流程

1. AI提示工程
2. 代码生成
3. 实机测试
4. 优化改进

## 提示词

>项目名称：人工智能Esp32灯带编程测试
角色设定：你是micropython和esp32c2的专家，请帮我设计一个程序，控制WS2812B灯带，有30个灯。使用3号端口控制。

## 功能一描述词与代码示例

>功能一描述：灯带循环显示红绿蓝三种颜色，每一种颜色显示1秒钟。

```python
# main.py
# ESP32-C2 + WS2812B ×30，GPIO3
# 功能：红→绿→蓝 循环，每色 1 s

import time
from machine import Pin
from neopixel import NeoPixel

NUM_LEDS = 30
PIN_DATA = 3          # GPIO3

# 初始化灯带
strip = NeoPixel(Pin(PIN_DATA, Pin.OUT), NUM_LEDS)

# 颜色表（R,G,B）
COLORS = (
    (255, 0, 0),   # 红
    (0, 255, 0),   # 绿
    (0, 0, 255)    # 蓝
)

def fill_color(r, g, b):
    """整带刷统一颜色并立即刷新"""
    for i in range(NUM_LEDS):
        strip[i] = (r, g, b)
    strip.write()

def main_loop():
    while True:
        for color in COLORS:
            fill_color(*color)
            time.sleep(1)          # 每色停留 1 秒

# 如果作为脚本运行则启动循环
if __name__ == "__main__":
    main_loop()
```

## 功能二描述词与代码示例

>功能二描述：红色流水灯，3颗红灯（亮度分别为200，80，20），从头到尾流动，再从头循环。

```python
# main_flow_red.py
# 功能：3 颗红灯从 0→29 流动，亮度 200→80→20，到尾后循环

import time
from machine import Pin
from neopixel import NeoPixel

NUM_LEDS = 30
PIN_DATA = 3
strip = NeoPixel(Pin(PIN_DATA, Pin.OUT), NUM_LEDS)

# 3 级亮度
HEAD_BRIGHT = 200
MID_BRIGHT  = 80
TAIL_BRIGHT = 20

DELAY_MS = 60          # 每步间隔，越小越快

def clear():
    for i in range(NUM_LEDS):
        strip[i] = (0, 0, 0)

def draw_flow(head_pos):
    """
    在 head_pos 位置画出 200-80-20 三颗红灯，
    其余熄灭。head_pos 可以是负值或 >= NUM_LEDS
    """
    clear()
    for offset, br in enumerate((HEAD_BRIGHT, MID_BRIGHT, TAIL_BRIGHT)):
        pos = head_pos - offset
        if 0 <= pos < NUM_LEDS:
            strip[pos] = (br, 0, 0)
    strip.write()

def flow_loop():
    pos = 0
    while True:
        draw_flow(pos)
        time.sleep_ms(DELAY_MS)
        pos += 1
        if pos >= NUM_LEDS + 3:   # 多跑 3 格让尾巴完全消失
            pos = 0

if __name__ == "__main__":
    flow_loop()
```

## 功能三描述词与代码示例

>功能三描述：用灯带模拟红、绿、蓝三个独立波形在灯带上左右移动，每个波形由5个灯组成。波形亮度使用高斯函数分布，中心最亮，向两边逐渐变暗。波形相遇时颜色叠加，RGB分量超过255时取255。每个波形显示时间在20到30秒之间随机选择，显示结束后消失1秒，然后在随机位置重新出现，继续参与运动。波形移动到灯带边缘时自动反弹，反弹时保持当前颜色。

```python
# main_wave.py
# ESP32-C2 + WS2812B×30，GPIO3
# 三条高斯波包（R/G/B）左右反弹 + 叠加 + 随机重生
import time, random
from machine import Pin
from neopixel import NeoPixel

NUM_LEDS   = 30
PIN_DATA   = 3
FPS        = 30               # 刷新率
SIGMA      = 0.8              # 高斯宽度
HALF_W     = 2                # 半宽 2→5 颗灯
PEAK       = 255

strip = NeoPixel(Pin(PIN_DATA, Pin.OUT), NUM_LEDS)

# 预计算高斯模板（长度 5，中心索引 2）
gauss_template = []
for dx in range(-HALF_W, HALF_W+1):
    gauss_template.append( int(PEAK * (2.718281828 ** (-0.5*(dx/SIGMA)**2))) )

def clear_strip():
    for i in range(NUM_LEDS):
        strip[i] = (0,0,0)

class Wave:
    def __init__(self, rgb):
        self.rgb = rgb          # (r,g,b) 基色，只有一个分量非零
        self.pos = random.uniform(2, NUM_LEDS-3)  # 浮点中心
        self.v  = random.choice([-1, 1]) * 0.45   # 每帧移动像素
        self.life = random.randint(20, 30)        # 寿命秒数
        self.dead = False

    def update(self, dt):
        """更新位置 & 寿命，返回当前每灯亮度列表（长度 NUM_LEDS）"""
        self.pos += self.v
        # 撞墙反弹
        if self.pos <= HALF_W:
            self.pos = HALF_W
            self.v = abs(self.v)
        elif self.pos >= NUM_LEDS - 1 - HALF_W:
            self.pos = NUM_LEDS - 1 - HALF_W
            self.v = -abs(self.v)

        self.life -= dt
        if self.life <= 0:
            self.dead = True

        # 生成当前帧亮度分布
        brightness = [0]*NUM_LEDS
        center = int(self.pos + 0.5)          # 四舍五入
        for dx, br in enumerate(gauss_template):
            idx = center + dx - HALF_W
            if 0 <= idx < NUM_LEDS:
                brightness[idx] = br
        return brightness

def random_respawn(wave):
    """原地复活：随机位置 + 随机方向 + 新寿命"""
    wave.pos   = random.uniform(2, NUM_LEDS-3)
    wave.v     = random.choice([-1, 1]) * 0.45
    wave.life  = random.randint(20, 30)
    wave.dead  = False

def main():
    waves = [Wave((255,0,0)), Wave((0,255,0)), Wave((0,0,255))]
    frame_us = int(1_000_000/FPS)
    next_us = time.ticks_us()

    while True:
        # 稳帧
        while time.ticks_diff(time.ticks_us(), next_us) < 0:
            pass
        next_us = time.ticks_add(next_us, frame_us)
        dt = 1.0/FPS

        # 三路亮度缓冲
        r_buf = [0]*NUM_LEDS
        g_buf = [0]*NUM_LEDS
        b_buf = [0]*NUM_LEDS

        for w in waves:
            if w.dead:
                continue
            br = w.update(dt)
            r_add, g_add, b_add = w.rgb
            for i in range(NUM_LEDS):
                if r_add: r_buf[i] += br[i]
                if g_add: g_buf[i] += br[i]
                if b_add: b_buf[i] += br[i]

        # 截断 & 写带
        for i in range(NUM_LEDS):
            strip[i] = (min(255, r_buf[i]),
                        min(255, g_buf[i]),
                        min(255, b_buf[i]))
        strip.write()

        # 处理死亡 & 重生
        for w in waves:
            if w.dead:
                # 熄灭 1 s（用帧数近似）
                for _ in range(FPS):
                    next_us = time.ticks_add(next_us, frame_us)
                    while time.ticks_diff(time.ticks_us(), next_us) < 0:
                        pass
                random_respawn(w)

if __name__ == "__main__":
    main()
```

完美复现~
你也来试试吧！
