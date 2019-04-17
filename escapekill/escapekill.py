# 1. 引入pygame-zero
import math

import pgzrun
import pygame

GUN_LOCATION = 25  # 枪在枪手的位置
GUNNER_SPEED = 20  # 枪手移动速度
BULLET_SPEED = 5  # 子弹移动速度

# 定义一个枪手角色，Actor 是中文演员的意思。这里Actor是python的一个类
# 我们看括号里面传入的两部分数据，第一部分'gunner'是一个字符串，这里写的是枪手对应的图片。
# 这里需要额外注意的是，gunner这个图片是存在images目录下面的，要严格准守这个规范。
# 括号里第二部分的数据(400, 400) 枪手在舞台上的初始位置（x坐标,y坐标）
gunner = Actor('gunner', (400, 400))

# 瞄准线
# 这里要特别注意的一个参数 anchor是锚的意思，锚是船舶靠岸是拴着的栓。在pyzero里，anchor
# 代表了‘演员’的‘中心点’。当演员旋转时，会以这个点为原点旋转。我们让瞄准线的锚点设置为x方向的
# 左侧，y方向的中部，也就是位于瞄准线的左中。
aim_line = Actor('aimline', anchor=('left', 'center'))
# 子弹列表
bullet_list = []
enemy = Actor('enemy', (300, 300))

delta = 0


# 当键盘被按下是触发这个函数
def on_key_down(key):
    # 按键等于上/下/左/右时
    if key == keys.LEFT:
        # 改变枪手x坐标
        gunner.x -= GUNNER_SPEED
    elif key == keys.RIGHT:
        gunner.x += GUNNER_SPEED
    elif key == keys.UP:
        gunner.y -= GUNNER_SPEED
    elif key == keys.DOWN:
        gunner.y += GUNNER_SPEED
    elif key == keys.SPACE:
        # 按下空格键发射子弹，首先要定义一个子弹，子弹的位置位于枪手手上枪的位置
        bullet = Actor('bullet', (gunner.x + gunner.width / 2, gunner.y + GUN_LOCATION))
        # 子弹的角度设置为瞄准线的角度。
        bullet.angle = aim_line.angle
        bullet_list.append(bullet)


# 当鼠标移动的时候会自动触发这个函数，然后瞄准镜要对准鼠标位置。
def on_mouse_move(pos):
    # 下面两行代码是用来算一个角度的。我们已知 鼠标的位置(pos), 瞄准线的位置(aim_line)。需要计算出这两个点连接在一起与水平方先生形成的夹角。
    # 这句话好难理解啊，看下面的图吧。
    # 那下面两行代码又是什么鬼呢？atan2是什么东西，然后又是乘又是除的，说实话，阿达老师没有看懂，初中数学忘完了啊~~
    # 那这两行代码阿达老师怎么会写呢？这就要用到两个技巧了。1）理解信息：我们把上面那一堆话抽象出来就可以拿到这样的信息，已知两个点，求这两个点连成线在水平方向上的夹角。
    # 2）搜索信息：把这句话放到google或者百度里搜索，就能得到下面的复杂公式啦。
    angle = math.atan2(pos[1] - aim_line.y, pos[0] - aim_line.x)
    angle = -angle * 180 / 3.14
    aim_line.angle = angle


# 2. 游戏里的每一帧要先改变游戏里各个角色的状态
def update():
    # 瞄准线要随时位于枪手的枪旁边。
    aim_line.x = gunner.x + gunner.width / 2
    aim_line.y = gunner.y + GUN_LOCATION
    for bullet in bullet_list:
        # 如果子弹打中敌方，就结束游戏
        if bullet.colliderect(enemy):
            print('game over')
            enemy.dead = True
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        # 根据角度算出x方向速度和y方向速度
        bullet.x = bullet.x + BULLET_SPEED * math.cos(math.radians(bullet.angle))
        bullet.y = bullet.y - BULLET_SPEED * math.sin(math.radians(bullet.angle))
    # 每隔n秒移动一次
    global delta
    delta += 1
    if (delta == 10):
        enemy.x += 5
        enemy.y += 5
        delta = 0


# 3. 改变完状态后，重新把各个角色渲染到游戏舞台上
def draw():
    # screen 是屏幕的意思，clear是清除的意思，screen.clear() 就是清空屏幕。
    screen.clear()
    # blit 中文是 块传输的意思。我们知道，手机、电脑的屏幕是由一个个像素点组成的，blit 就是往这些像素点上画画。
    # 括号里的第一个参数是画什么图片，第二个参数是从哪个位置上画
    screen.blit('background', (0, 0))
    # 我们刚刚知道，gunner是一个枪手演员，gunner.draw()，就是调用枪手演员的画方法，把枪手画到舞台上。
    gunner.draw()
    # 瞄准线
    aim_line.draw()
    enemy.draw()
    # 渲染子弹
    for bullet in bullet_list:
        bullet.draw()


# 4. 执行pygame-zero主逻辑
pgzrun.go()
