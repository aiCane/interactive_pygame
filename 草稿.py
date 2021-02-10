import pygame
from pygame.locals import *
from sys import exit
from random import randint

text1 = "红艳艳的都市十分繁华"  # 剧情text
red = 255, 0, 0
black = 0, 0, 0
white = 255, 255, 255
SPEED_FACTOR = 0.005  # 渐变色的速度
factor1 = 0
ticks = 0
speed_text = -2
pos_x1 = randint(25, 725)  # 前剧情文本x坐标(最好定制)
pos_y1 = 490  # 前剧情文本y坐标(在界面下方)

global_v_idx = 0


pygame.init()  # 初始化pygame
pygame.font.init()
pygame.mixer.init()
pygame.time.delay(1000)  # 初始化等待一秒
win_size = width, height = 1100, 500  # 设置窗口大小
win = pygame.display.set_mode(win_size)  # 显示窗口
pygame.display.set_caption("夜已—测试版")  # 大标题title

clock = pygame.time.Clock()  # 创建游戏时钟


def drawText(contect, color=red, size=50):  # 创建一个字的函数
    myfont = pygame.font.Font("Xingkai.ttc", size)  # 字体、大小
    textImage = myfont.render(contect, True, color)
    return textImage

def blend_color(color1=red, color2=black, blend_factor=0.5):  # 渐变色的实现
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = r1 + (r2 - r1) * blend_factor
    g = g1 + (g2 - g1) * blend_factor
    b = b1 + (b2 - b1) * blend_factor
    return int(r), int(g), int(b)

def draw_subtitles(text, pos_x, pos_y, factor):
    ## global speed_text
    #if time1 <= tick <= time2:
    position = pos_x, pos_y
    pos_y += speed_text

    # win.blit(drawText(text, white), position)

    win.blit(drawText(text, blend_color(blend_factor=factor)), position)


def draw_from_arr(in_idx, tick):
    if 0 <= in_idx < len(text_arr):
        itemarr = text_arr[in_idx]
        txt = itemarr[0]
        tmp_posx = int(itemarr[1])

        tmp_posy = int(itemarr[2]) - 1
        text_arr[in_idx][2] = str(tmp_posy)

        tmp_factor = float(itemarr[3]) + SPEED_FACTOR
        if tmp_factor >= 1:
            tmp_factor = 1
        text_arr[in_idx][3] = str(tmp_factor)


        draw_subtitles(txt, tmp_posx, tmp_posy, tmp_factor)  # 文本1


text_arr = []
with open("subtitles.txt") as fdata:
    while True:
        line = fdata.readline()
        if not line:
            break
        if line.startswith("#") == False:
            text_arr.append(line.split("|"))
    for i in range(len(text_arr)):
        if int(text_arr[i][1]) == 0:
            text_arr[i][1] = str(randint(25,750))


idx = 0
print(text_arr)
curr_txt = ''

slow_tick = 0

while True:
    win.fill(black)  # 背景颜色bgcolor,位置放前以不至于遮挡

    clock.tick(150)  # 每秒运行150次

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 退出游戏
            pygame.quit()
            exit()

    tisks = pygame.time.get_ticks()  # 游戏开始绝对时间
    tmp_tick = tisks
    idx = int(tmp_tick/3000) - 2

    if 0 <= idx < len(text_arr):
        if curr_txt != text_arr[idx][0]:
            curr_txt = text_arr[idx][0]
            print("idx=",idx, " 字幕为:", curr_txt)

    draw_from_arr(idx - 4, tmp_tick)
    draw_from_arr(idx - 3, tmp_tick)
    draw_from_arr(idx - 2, tmp_tick)
    draw_from_arr(idx - 1, tmp_tick)
    draw_from_arr(idx, tmp_tick)

    pygame.display.update()  # 更新全部显示
