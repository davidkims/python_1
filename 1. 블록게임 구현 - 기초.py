import pygame
import random

# 색깔 상수 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# 게임 설정
WIDTH = 600
HEIGHT = 800
BLOCK_SIZE = 40
FPS = 35

# 초기화
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록 게임")
clock = pygame.time.Clock()

# 블록 클래스 정의
class Block:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

    def move_down(self):
        self.y += BLOCK_SIZE

# 게임 루프
def game_loop():
    # 블록 생성
    blocks = [Block(BLUE, BLOCK_SIZE * i, 1) for i in range(WIDTH // BLOCK_SIZE)]

    # 게임 루프
    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 블록 이동
        for block in blocks:
            block.move_down()

        # 화면 그리기
        screen.fill(WHITE)
        for block in blocks:
            block.draw(screen)
        pygame.display.update()

        # 게임 속도 조절
        clock.tick(FPS)

# 게임 시작
game_loop()
