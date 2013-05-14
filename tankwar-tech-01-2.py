#!/usr/bin/env python  
#-*-coding:utf-8-*-
import pygame
# Initialize the game engine
pygame.init()    #pygame初始化
red =   [255,  0,  0]
size=[700,500]    #指定窗口尺寸
screen=pygame.display.set_mode(size)    #新建一个窗口
pygame.display.set_caption("坦克大战")    #设置窗口标题
done=False
while done==False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True
    pygame.draw.circle(screen,red,[200,200],50)
    pygame.display.flip()#刷新屏幕
pygame.quit ()
