import pygame

# 윈도우 크기 설정
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# pygame 초기화
pygame.init()

# 윈도우 생성
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('비행기 게임')

# 게임 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 게임 화면 업데이트
    pygame.display.update()

