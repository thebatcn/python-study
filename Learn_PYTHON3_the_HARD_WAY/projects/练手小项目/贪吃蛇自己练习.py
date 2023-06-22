import random
import time

width = 20
height = 16
# 随机生成3个食物坐标
foods = [(random.randint(0, width-1), random.randint(0, height-1))
         for i in range(3)]
# foods = (random.randint(0, width-1), random.randint(0, height-1))
snake = [(width//2, height//2), (width//2, height//2+1),
         (width//2, height//2+2)]
direction = [0, 0]  # 初始停止

print('direction : {}'.format(direction))
print(snake)

snake_head = snake[0]

while True:
    # 显示游戏区域
    for y in range(height):
        for x in range(width):
            if (x, y) in foods:
                print('M', end=' ')
                # continue
            elif (x, y) in snake:
                print('o', end=' ')
                # continue
            else:
                print('.', end=' ')
        print()

    # 根据输入键盘来确定方向值
    key = input()
    match key:
        case  'w' | 'W' if snake_head[1] > 0:
            direction = (0, -1)
        case 's' | 'S' if snake_head[1] < height:
            direction = (0, 1) 
        case 'a' | 'A' if snake_head[0] > 0:
            direction = (-1, 0) 
        case 'd' | 'D' if snake_head[0] <width:
            direction = (1, 0)
  
    # 更新snake_head
    snake_head = (snake[0][0]+direction[0], snake[0][1]+direction[1])
    if snake_head in foods:
        foods.remove(snake_head)
        if len(foods) <=1:
            foods = [(random.randint(0, width-1), random.randint(0, height-1))
            for i in range(3)]
    else:
        snake.pop()
    snake.insert(0, snake_head)
    print(snake)

    if snake_head[0] <0 or snake_head[0] >= width or snake_head[1] < 0 or snake_head[1] >= height:
        print('Game Over')
        break
    if snake_head in snake[1::]:
        print('Game Over')
        break