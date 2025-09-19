import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Random Starfield")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 별 클래스 정의
class Star:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.size = random.randint(1, 3)
        self.speed = random.randint(1, 4)

    def move(self):
        self.y += self.speed
        # 화면 아래로 벗어나면 맨 위로 다시 이동
        if self.y > SCREEN_HEIGHT:
            self.y = 0
            self.x = random.randint(0, SCREEN_WIDTH)
            self.size = random.randint(1, 3)
            self.speed = random.randint(1, 4)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

# 별 객체 생성
num_stars = 200
stars = [Star() for _ in range(num_stars)]

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면을 검은색으로 채움 (이전 프레임 삭제)
    screen.fill(BLACK)

    # 별 업데이트 및 그리기
    for star in stars:
        star.move()
        star.draw()

    # 화면 업데이트
    pygame.display.flip()

    # FPS (초당 프레임 수) 조절
    clock.tick(60)

# Pygame 종료
pygame.quit()
