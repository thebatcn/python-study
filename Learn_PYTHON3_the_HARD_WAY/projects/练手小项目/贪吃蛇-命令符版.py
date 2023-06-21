import random

# 初始化游戏信息
WIDTH, HEIGHT = 20, 10
score = 0
snake = [(WIDTH // 2, HEIGHT // 2)]
food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
direction = (0, -1)  # initial direction: up

# 游戏循环
while True:
    # 显示游戏区域
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in snake:
                print("o", end="")
            elif (x, y) == food:
                print("X", end="")
            else:
                print(".", end="")
        print()

    # 获取用户输入
    key = input()
    if key == "a" and direction != (1, 0):
        direction = (-1, 0)  # left
    elif key == "d" and direction != (-1, 0):
        direction = (1, 0)   # right
    elif key == "w" and direction != (0, 1):
        direction = (0, -1)  # up
    elif key == "s" and direction != (0, -1):
        direction = (0, 1)   # down

    # 添加蛇头
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if head == food:
        score += 1
        food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
    else:
        snake.pop()
    snake.insert(0, head)

    # 检查游戏是否结束
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        print("Game over! Your score is:", score)
        break
    for i in range(1, len(snake)):
        if head == snake[i]:
            print("Game over! Your score is:", score)
            break
    else:
        continue
    break