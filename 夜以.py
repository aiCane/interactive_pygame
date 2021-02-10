#### 交互式游戏2.6.4

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()  # 初始化pygame
pygame.font.init()
pygame.mixer.init()
pygame.time.delay(1000)  # 初始化等待一秒
win_size = width, height = 1100, 500  # 设置窗口大小
win = pygame.display.set_mode(win_size)  # 显示窗口
pygame.display.set_caption("夜已")  # 大标题title

black = 0, 0, 0
white = 255, 255, 255
orange = 150, 50, 175
red = 255, 0, 0
dark_red = 150, 0, 0
speed_factor1 = 0.005  # 渐变色的速度
speed_factor2 = 0.05
factor1 = factor2 = factor3 = factor4 = factor5 = factor6 = 0
factor_choose_1 = factor_choose_2 = 0
factor_a1 = factor_a2 = factor_a3 = factor_a4 = factor_a5 = factor_a6 = factor_a7 = 0
factor_a8 = factor_a9 = factor_a10 = factor_a11 = factor_a12 = factor_a13 = factor_a14 = 0
factor_b1 = factor_b2 = factor_b3 = factor_b4 = factor_b5 = factor_b6 = 0
factor_b7 = factor_b8 = factor_b9 = factor_b10 = factor_b11 = factor_b12 = 0

text1 = "红艳艳的都市十分繁华"  # 剧情text
text2 = "高楼大厦林立在都市一侧"
text3 = "另一侧则是低矮的建筑"
text4 = "傍晚的黄晕抹平了天空最后的湛蓝"
text5 = "华灯初上"
text6 = "灯火零零散散地散落在都市的各个角落"

text_choose_1a = "高塔"  # 选择1a
text_a1 = "都市中有一座高塔直冲云霄"
text_a2 = "顶端并未做什么修饰"
text_a3 = "中间有一段是空旷的平地"
text_a4 = "四周有玻璃环绕"
text_a5 = "在上面可以很轻松地俯视整座都市"
text_a6 = "在很靠近玻璃的地方有一张奢华的躺椅"
text_a7 = "一位少女半倚其上"
text_a8 = "她的一只手很随意的向下搭着"
text_a9 = "另一只手则在缓缓地旋转着手中的玻璃杯"
text_a10 = "累了"
text_a11 = "就先小酌一口"
text_a12 = "再把玻璃杯放上旁边的桌子"
text_a13 = "她目不转睛地看着底下的都市"
text_a14 = "脸上没有浮现出任何表情"

text_choose_1b = "小巷"  # 选择1b
text_b1 = "在那低矮的建筑中"
text_b2 = "总有那么几条巷子是肮脏的"
text_b3 = "繁华的都市下"
text_b4 = "一条大道旁横插进去一条小巷"
text_b5 = "路灯的灯光摇曳地停在小巷口"
text_b6 = "形成一条明暗交接线"
text_b7 = "再往里走..."
text_b8 = "小道极窄"
text_b9 = "污渍斑斑"
text_b10 = "远处终于有一两盏耸拉着的灯泡"
text_b11 = "它们断断续续的泛黄的微弱的灯光"
text_b12 = "勉强能使人看清脚下的路"

clock = pygame.time.Clock()  # 创建游戏时钟

pos_x1r, pos_y1r= 200, 300  # 选择矩形坐标1
pos1r = pos_x1r, pos_y1r, 150, 100
pos_x2r, pos_y2r= 750, 300  # 选择矩形坐标2
pos2r = pos_x2r, pos_y2r, 150, 100
## win_size = width, height = 1100, 500  # 设置窗口大小
pos_x1 = randint(25, 725)  # 前剧情文本x坐标(最好定制)
pos_x2 = randint(25, 700)
pos_x3 = randint(25, 725)
pos_x4 = randint(25, 650)
pos_x5 = randint(25, 800)
pos_x6 = randint(25, 625)
pos_x_a1 = randint(25, 650)  # 选择1a文本
pos_x_a2 = randint(25, 650)
pos_x_a3 = randint(25, 650)
pos_x_a4 = randint(25, 650)
pos_x_a5 = randint(25, 650)
pos_x_a6 = randint(25, 650)
pos_x_a7 = randint(25, 650)
pos_x_a8 = randint(25, 650)
pos_x_a9 = randint(25, 650)
pos_x_a10 = randint(25, 650)
pos_x_a11 = randint(25, 650)
pos_x_a12 = randint(25, 650)
pos_x_a13 = randint(25, 650)
pos_x_a14 = randint(25, 650)
pos_x_b1 = randint(25, 650)  # 选择1b文本
pos_x_b2 = randint(25, 650)
pos_x_b3 = randint(25, 650)
pos_x_b4 = randint(25, 650)
pos_x_b5 = randint(25, 650)
pos_x_b6 = randint(25, 650)
pos_x_b7 = randint(25, 650)
pos_x_b8 = randint(25, 650)
pos_x_b9 = randint(25, 650)
pos_x_b10 = randint(25, 650)
pos_x_b11 = randint(25, 650)
pos_x_b12 = randint(25, 650)
speed_text = -2  # 字体速度
pos_y1 = pos_y2 = pos_y3 = pos_y4 = pos_y5 = pos_y6 = 505  # 前剧情文本y坐标(在界面下方)
pos_y_a1 = pos_y_a2 = pos_y_a3 = pos_y_a4 = pos_y_a5 = pos_y_a6 = pos_y_a7 = 505  # 选择1a_y坐标
pos_y_a8 = pos_y_a9 = pos_y_a10 = pos_y_a11 = pos_y_a12 = pos_y_a13 = pos_y_a14 = 505
pos_y_b1 = pos_y_b2 = pos_y_b3 = pos_y_b4 = pos_y_b5 = pos_y_b6 = 505  # 选择1b_y坐标
pos_y_b7 = pos_y_b8 = pos_y_b9 = pos_y_b10 = pos_y_b11 = pos_y_b12 = 505

pos_c_1a = 240, 325  # 选择文本坐标
pos_c_1b = 790, 325

def drawText(contect, color=red, size=30):  # 创建一个字的函数
    myfont = pygame.font.Font("Xingkai.ttc", size)  # 字体、大小
    textImage = myfont.render(contect, True, color)
    return textImage

def drawRect(pos, color=dark_red, width=0):  # 创建一个矩形的函数
    return pygame.draw.rect(win, color, pos, width)

def blend_color(color1=red, color2=black, blend_factor=0.5):  # 渐变色的实现
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = r1 + (r2 - r1) * blend_factor
    g = g1 + (g2 - g1) * blend_factor
    b = b1 + (b2 - b1) * blend_factor
    return int(r), int(g), int(b)

def in_rect(pos, rect):
    x, y = pos
    rx, ry, rw, rh = rect
    if rx <= x <= rx + rw and ry <= y <= ry + rh:
        return True
    else:
        return False

musiccc = pygame.mixer.Sound("musiccc.ogg")  # 背景音乐bgmusic
channel = pygame.mixer.find_channel(True)
channel.play(musiccc)

mouse_x = mouse_y = 0
move_x = move_y = 0
pygame.mouse.set_visible(False)  # 光标不可视
cursor_dark = pygame.image.load("cursor_dark.gif").convert_alpha()  # 加载鼠标光标
cursor_light = pygame.image.load("cursor_light.gif").convert_alpha()

game_over = True
game_pause = False
choose_1 = 0
ticks_pause = 0
ticks_h1 = 0

while True:
    clock.tick(150)  # 每秒运行150次
    tisks_ab = pygame.time.get_ticks()  # 游戏开始绝对时间

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 退出游戏
            pygame.quit()
            exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos  # 获取鼠标位置
            move_x, move_y = event.rel  # 获取鼠标一系列的活动
        elif event.type == MOUSEBUTTONUP:
            if game_over:  # 游戏开始
                game_over = False

    keys = pygame.key.get_pressed()  # 键盘事件
    if keys[K_ESCAPE]:
        pygame.quit()
        exit()
    elif keys[K_SPACE]:
        if game_over == False and game_pause == False:  # 点击空格以暂停
            game_pause = True
        elif game_pause == True:  # 点击空格以继续
            game_pause = False
    b1, b2, b3 = pygame.mouse.get_pressed()

    if game_over:  # 在游戏开始时(封面)
        win.fill(dark_red)
        win.blit(drawText("夜以", white, 75), (470, 150))
        win.blit(drawText("<点击以开始>", white, 40), (430, 300))
        win.blit(drawText("作者:皑藤", white, 20), (15, 470))
        win.blit(drawText("版本号: 2. 2. 1", white, 20), (975, 470))
        ticks_h = tisks_ab

    elif game_pause:  # 在游戏暂停时
        win.fill(black)
        win.blit(drawText("<按空格以继续>", dark_red, 35), (425, 250))
        ticks_pause = tisks_ab
    else:
        win.fill(black)  # 背景颜色bgcolor,位置放前以不至于遮挡
        if choose_1 == 0:
            win.blit(drawText("前剧情", white, 20), (15, 15))

        if ticks_pause == 0:
            ticks = tisks_ab - ticks_h  # 前剧情相对时间
        else:
            ticks = 2 * tisks_ab - ticks_h - ticks_pause

        if ticks <= 6000:  # 文本1
            position1 = pos_x1, pos_y1
            pos_y1 += speed_text
            win.blit(drawText(text1, blend_color(blend_factor=factor1)), position1)
            if factor1 <= 1:
                factor1 += speed_factor1

        if 2000 <= ticks <= 8000:  # 文本2
            position2 = pos_x2, pos_y2
            pos_y2 += speed_text
            win.blit(drawText(text2, blend_color(blend_factor=factor2)), position2)
            if factor2 <= 1:
                factor2 += speed_factor1

        if 4000 <= ticks <= 10000:  # 文本3
            position3 = pos_x3, pos_y3
            pos_y3 += speed_text
            win.blit(drawText(text3, blend_color(blend_factor=factor3)), position3)
            if factor3 <= 1:
                factor3 += speed_factor1

        if 6000 <= ticks <= 12000:  # 文本4
            position4 = pos_x4, pos_y4
            pos_y4 += speed_text
            win.blit(drawText(text4, blend_color(blend_factor=factor4)), position4)
            if factor4 <= 1:
                factor4 += speed_factor1

        if 8000 <= ticks <= 14000:  # 文本5
            position5 = pos_x5, pos_y5
            pos_y5 += speed_text
            win.blit(drawText(text5, blend_color(blend_factor=factor5)), position5)
            if factor5 <= 1:
                factor5 += speed_factor1

        if 10000 <= ticks <= 16000:  # 文本6
            position6 = pos_x6, pos_y6
            pos_y6 += speed_text
            win.blit(drawText(text6, blend_color(blend_factor=factor6)), position6)
            if factor6 <= 1:
                factor6 += speed_factor1

        if 15000 <= ticks and choose_1 == 0:  # 第一次选择
            win.blit(drawText("你选择---"), (500, 150))
            drawRect(pos1r, blend_color(black, dark_red, factor_choose_1))  # 选择方块
            drawRect(pos2r, blend_color(black, dark_red, factor_choose_1))
            if factor_choose_1 <= 1:
                factor_choose_1 += speed_factor2
            win.blit(drawText(text_choose_1a, orange), pos_c_1a)
            win.blit(drawText(text_choose_1b, orange), pos_c_1b)

            if in_rect((mouse_x, mouse_y), pos1r):  # 选择左边
                drawRect(pos1r, orange)
                win.blit(drawText(text_choose_1a, dark_red), pos_c_1a)
                if b1:
                    ticks_h1 = tisks_ab
                    choose_1 = 1
            elif in_rect((mouse_x, mouse_y), pos2r):  # 选择右边
                drawRect(pos2r, orange)
                win.blit(drawText(text_choose_1b, dark_red), pos_c_1b)
                if b1:
                    ticks_h1 = tisks_ab
                    choose_1 = 2

        ticks1 = tisks_ab - ticks_h1  # 第一次选择相对时间

        if choose_1 == 1:
            win.blit(drawText("高塔", white, 20), (15, 15))

            if ticks1 <= 6000:  # 文本a1
                position_a1 = pos_x_a1, pos_y_a1
                pos_y_a1 += speed_text
                win.blit(drawText(text_a1, blend_color(blend_factor=factor_a1)), position_a1)
                if factor_a1 <= 1:
                    factor_a1 += speed_factor1

            if 2000 <= ticks1 <= 8000:  # 文本a2
                position_a2 = pos_x_a2, pos_y_a2
                pos_y_a2 += speed_text
                win.blit(drawText(text_a2, blend_color(blend_factor=factor_a2)), position_a2)
                if factor_a2 <= 1:
                    factor_a2 += speed_factor1

            if 4000 <= ticks1 <= 10000:  # 文本a3
                position_a3 = pos_x_a3, pos_y_a3
                pos_y_a3 += speed_text
                win.blit(drawText(text_a3, blend_color(blend_factor=factor_a3)), position_a3)
                if factor_a3 <= 1:
                    factor_a3 += speed_factor1

            if 6000 <= ticks1 <= 12000:  # 文本a4
                position_a4 = pos_x_a4, pos_y_a4
                pos_y_a4 += speed_text
                win.blit(drawText(text_a4, blend_color(blend_factor=factor_a4)), position_a4)
                if factor_a4 <= 1:
                    factor_a4 += speed_factor1

            if 8000 <= ticks1 <= 14000:  # 文本a5
                position_a5 = pos_x_a5, pos_y_a5
                pos_y_a5 += speed_text
                win.blit(drawText(text_a5, blend_color(blend_factor=factor_a5)), position_a5)
                if factor_a5 <= 1:
                    factor_a5 += speed_factor1

            if 10000 <= ticks1 <= 16000:  # 文本a6
                position_a6 = pos_x_a6, pos_y_a6
                pos_y_a6 += speed_text
                win.blit(drawText(text_a6, blend_color(blend_factor=factor_a6)), position_a6)
                if factor_a6 <= 1:
                    factor_a6 += speed_factor1

            if 12000 <= ticks1 <= 18000:  # 文本a7
                position_a7 = pos_x_a7, pos_y_a7
                pos_y_a7 += speed_text
                win.blit(drawText(text_a7, blend_color(blend_factor=factor_a7)), position_a7)
                if factor_a7 <= 1:
                    factor_a7 += speed_factor1

            if 14000 <= ticks1 <= 20000:  # 文本a8
                position_a8 = pos_x_a8, pos_y_a8
                pos_y_a8 += speed_text
                win.blit(drawText(text_a8, blend_color(blend_factor=factor_a8)), position_a8)
                if factor_a8 <= 1:
                    factor_a8 += speed_factor1

            if 16000 <= ticks1 <= 22000:  # 文本a9
                position_a9 = pos_x_a9, pos_y_a9
                pos_y_a9 += speed_text
                win.blit(drawText(text_a9, blend_color(blend_factor=factor_a9)), position_a9)
                if factor_a9 <= 1:
                    factor_a9 += speed_factor1

            if 18000 <= ticks1 <= 24000:  # 文本a10
                position_a10 = pos_x_a10, pos_y_a10
                pos_y_a10 += speed_text
                win.blit(drawText(text_a10, blend_color(blend_factor=factor_a10)), position_a10)
                if factor_a10 <= 1:
                    factor_a10 += speed_factor1

            if 20000 <= ticks1 <= 26000:  # 文本a11
                position_a11 = pos_x_a11, pos_y_a11
                pos_y_a11 += speed_text
                win.blit(drawText(text_a11, blend_color(blend_factor=factor_a11)), position_a11)
                if factor_a11 <= 1:
                    factor_a11 += speed_factor1

            if 22000 <= ticks1 <= 28000:  # 文本a12
                position_a12 = pos_x_a12, pos_y_a12
                pos_y_a12 += speed_text
                win.blit(drawText(text_a12, blend_color(blend_factor=factor_a12)), position_a12)
                if factor_a12 <= 1:
                    factor_a12 += speed_factor1

            if 24000 <= ticks1 <= 30000:  # 文本a13
                position_a13 = pos_x_a13, pos_y_a13
                pos_y_a13 += speed_text
                win.blit(drawText(text_a13, blend_color(blend_factor=factor_a13)), position_a13)
                if factor_a13 <= 1:
                    factor_a13 += speed_factor1

            if 26000 <= ticks1 <= 32000:  # 文本a14
                position_a14 = pos_x_a14, pos_y_a14
                pos_y_a14 += speed_text
                win.blit(drawText(text_a14, blend_color(blend_factor=factor_a14)), position_a14)
                if factor_a14 <= 1:
                    factor_a14 += speed_factor1

            if 30000 <= ticks1:
                win.blit(drawText("恭喜达成成就—", white, 35), (350, 150))
                win.blit(drawText("慵懒的少女", white, 40), (500, 250))

        elif choose_1 == 2:
            win.blit(drawText("小巷", white, 20), (15, 15))

            if 1000 <= ticks1 <= 6000:  # 文本b1
                position_b1 = pos_x_b1, pos_y_b1
                pos_y_b1 += speed_text
                win.blit(drawText(text_b1, blend_color(blend_factor=factor_b1)), position_b1)
                if factor_b1 <= 1:
                    factor_b1 += speed_factor1

            if 2000 <= ticks1 <= 8000:  # 文本b2
                position_b2 = pos_x_b2, pos_y_b2
                pos_y_b2 += speed_text
                win.blit(drawText(text_b2, blend_color(blend_factor=factor_b2)), position_b2)
                if factor_b2 <= 1:
                    factor_b2 += speed_factor1

            if 4000 <= ticks1 <= 10000:  # 文本b3
                position_b3 = pos_x_b3, pos_y_b3
                pos_y_b3 += speed_text
                win.blit(drawText(text_a3, blend_color(blend_factor=factor_b3)), position_b3)
                if factor_b3 <= 1:
                    factor_b3 += speed_factor1

            if 6000 <= ticks1 <= 12000:  # 文本b4
                position_b4 = pos_x_b4, pos_y_b4
                pos_y_b4 += speed_text
                win.blit(drawText(text_b4, blend_color(blend_factor=factor_b4)), position_b4)
                if factor_b4 <= 1:
                    factor_b4 += speed_factor1

            if 8000 <= ticks1 <= 14000:  # 文本b5
                position_b5 = pos_x_b5, pos_y_b5
                pos_y_b5 += speed_text
                win.blit(drawText(text_b5, blend_color(blend_factor=factor_b5)), position_b5)
                if factor_b5 <= 1:
                    factor_b5 += speed_factor1

            if 10000 <= ticks1 <= 16000:  # 文本b6
                position_b6 = pos_x_b6, pos_y_b6
                pos_y_b6 += speed_text
                win.blit(drawText(text_b6, blend_color(blend_factor=factor_b6)), position_b6)
                if factor_b6 <= 1:
                    factor_b6 += speed_factor1

            if 12000 <= ticks1 <= 18000:  # 文本b7
                position_b7 = pos_x_b7, pos_y_b7
                pos_y_b7 += speed_text
                win.blit(drawText(text_b7, blend_color(blend_factor=factor_b7)), position_b7)
                if factor_b7 <= 1:
                    factor_b7 += speed_factor1

            if 14000 <= ticks1 <= 20000:  # 文本b8
                position_b8 = pos_x_b8, pos_y_b8
                pos_y_b8 += speed_text
                win.blit(drawText(text_b8, blend_color(blend_factor=factor_b8)), position_b8)
                if factor_b8 <= 1:
                    factor_b8 += speed_factor1

            if 16000 <= ticks1 <= 22000:  # 文本b9
                position_b9 = pos_x_b9, pos_y_b9
                pos_y_b9 += speed_text
                win.blit(drawText(text_b9, blend_color(blend_factor=factor_b9)), position_b9)
                if factor_b9 <= 1:
                    factor_b9 += speed_factor1

            elif 18000 <= ticks1 <= 24000:  # 文本b10
                position_b10 = pos_x_b10, pos_y_b10
                pos_y_b10 += speed_text
                win.blit(drawText(text_b10, blend_color(blend_factor=factor_b10)), position_b10)
                if factor_b10 <= 1:
                    factor_b10 += speed_factor1

            if 20000 <= ticks1 <= 26000:  # 文本b11
                position_b11 = pos_x_b11, pos_y_b11
                pos_y_b11 += speed_text
                win.blit(drawText(text_b11, blend_color(blend_factor=factor_b11)), position_b11)
                if factor_b11 <= 1:
                    factor_b11 += speed_factor1

            if 22000 <= ticks1 <= 28000:  # 文本b12
                position_b12 = pos_x_b12, pos_y_b12
                pos_y_b12 += speed_text
                win.blit(drawText(text_b12, blend_color(blend_factor=factor_b12)), position_b12)
                if factor_b12 <= 1:
                    factor_b12 += speed_factor1

            if 27000 <= ticks1:
                win.blit(drawText("恭喜达成成就—", white, 35), (350, 150))
                win.blit(drawText("昏灯小巷", white, 40), (500, 250))

    mouse_x, mouse_y = pygame.mouse.get_pos()  # 获取鼠标当前位置
    pos_mouse = (mouse_x, mouse_y)
    win.blit(cursor_dark, pos_mouse)  # 替代游戏光标(没扣好)

    pygame.display.update()  # 更新全部显示