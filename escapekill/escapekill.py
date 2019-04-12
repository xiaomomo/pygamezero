import pgzrun

# 枪手
gunner = Actor('gunner', (0, 0))

# 瞄准线
sights = Actor('sights', (0, 0))

# 子弹(这里要用数组的)
bullet = []

# 敌人
enemy = Actor('enemy', (0, 0))


def update():
    return


def draw():
    screen.blit('background', (0, 0))
    screen.clear()
    enemy.draw()


pgzrun.go()
