import pygame
import sys
# 初始化pygame
pygame.init()

# 设置窗口大小和标题
screen = pygame.display.set_mode((150, 50), pygame.RESIZABLE)
pygame.display.set_caption("切牌助手1.0")
# 定义颜色
colors = [(255, 255, 0),(0, 0, 255), (255, 0, 0) ]
current_color = 0

# 创建自定义事件
CHANGE_COLOR = pygame.USEREVENT + 1

# 设置定时器，每500毫秒触发一次CHANGE_COLOR事件
pygame.time.set_timer(CHANGE_COLOR, 535)

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CHANGE_COLOR:  # 检测到CHANGE_COLOR事件
            current_color += 1
            if current_color >= len(colors):
                current_color = 0
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_l):  # 添加监听L键
                print("取消定时器")
                # 取消定时器
                pygame.time.set_timer(CHANGE_COLOR, 0)
                # 重新设置定时器
                current_color = 0
                print("设置定时器")
                pygame.time.set_timer(CHANGE_COLOR, 535)
        if event.type == pygame.VIDEORESIZE:  # 检测到窗口大小调整事件
            width, height = event.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    # 更新颜色
    screen.fill(colors[current_color])
    pygame.display.update()
