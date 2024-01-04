import pygame
import random

# 初始化游戏
pygame.init()
# 显示开始游戏界面
font = pygame.font.Font(None, 36)


def show_start_screen():
    screen.fill(black)
    title_text = font.render("打飞机游戏", True, white)
    instruction_text = font.render("按任意键开始游戏", True, white)
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    instruction_rect = instruction_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(title_text, title_rect)
    screen.blit(instruction_text, instruction_rect)
    pygame.display.flip()


# 设置窗口尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("IKUN小游戏")

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 加载飞机和敌人图片
player_img = pygame.image.load("player4.png")
enemy_img = pygame.image.load("enemy6.png")

# 获取飞机和敌人图片的宽度和高度
player_width = player_img.get_width()
player_height = player_img.get_height()
enemy_width = enemy_img.get_width()
enemy_height = enemy_img.get_height()

# 设置游戏时钟
clock = pygame.time.Clock()


# 定义玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2 - player_width // 2
        self.rect.y = screen_height - player_height - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < screen_width - player_width:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.x + player_width // 2, self.rect.y)
        all_sprites.add(bullet)
        bullets.add(bullet)


# 定义敌人飞机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - enemy_width)
        self.rect.y = random.randint(-enemy_height, -10)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > screen_height:
            self.rect.x = random.randint(0, screen_width - enemy_width)
            self.rect.y = random.randint(-enemy_height, -10)
            self.speed = random.randint(1, 3)


# 定义子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("basketball1.png")  # 加载篮球图片
        self.image = pygame.transform.scale(self.image, (20, 20))  # 调整篮球图片尺寸
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = -8  # 调整篮球的移动速度

    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


# 创建玩家飞机和敌人飞机的精灵组
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 创建敌人飞机
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# 游戏主循环
running = True
game_over = False

while running:
    if game_over:
        # 游戏结束界面
        screen.fill(black)
        game_over_text = font.render("游戏结束", True, white)
        restart_text = font.render("按R键重新开始", True, white)
        game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        restart_rect = restart_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(restart_text, restart_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # 重新开始游戏
                    game_over = False
                    all_sprites.empty()
                    enemies.empty()
                    bullets.empty()
                    player = Player()
                    all_sprites.add(player)
                    for _ in range(10):
                        enemy = Enemy()
                        all_sprites.add(enemy)
                        enemies.add(enemy)
    else:
        # 游戏逻辑
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            game_over = True

        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

        screen.fill(black)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)

# 退出游戏
pygame.quit()