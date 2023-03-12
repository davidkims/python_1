# 게임 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 게임 화면 업데이트
    pygame.display.update()
