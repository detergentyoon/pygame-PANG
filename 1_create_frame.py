import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 (제목)
pygame.display.set_caption("Nado Game") # 게임 이름

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        # pygame 에서는 무조건 작성해야하는 부분
        # event loop : 계속 프로그램이 종료되지 않도록 대기하는 것. 중간에 사용자가 키보드로 무언가를 입력하는지, 마우스에 어떤 동작이 들어오는지 체크
        # 키보드에 맞는 이미지를 움직임, 혹은 무기 발사 등의 이벤트 동작을 처리하는 코드
        if event.type == pygame.QUIT: # QUIT : 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

# pygame 종료
pygame.quit()