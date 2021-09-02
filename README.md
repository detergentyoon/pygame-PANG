# **4_ keyboard_event**

### 가로 경계값 처리 코드 해설
```python
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
```
가로 경계값의 좌측 처리를 하는 `if character_x_pos < 0: character_x_pos = 0` 에서 `character_x_pos = 0` 은 화면 상에서는 캐릭터의 움직임이 멈춘 것처럼 보이지만 프로그램 상에서는 캐릭터를 x 좌표 0 으로 순간이동시키는 것과 같기 때문에 `elif`문으로 오른쪽 화면 제어를 따로 하는 것이며, 세로 경계값 처리 코드 또한 이와 동일한 맥락임.

<br>

# **5_ FPS**
frame의 높고 낮음에 따라 이동 애니메이션이 더 부드러워지거나 덜 부드러워질 수는 있지만, 게임 자체의 속도가 달라지면 안되기 때문에 `character_speed = `를 통해 캐릭터 고유의 이동속도를 부여함

<br>

캐릭터가 1초 동안에 100 만큼 이동을 해야한다면?
* `10 fps` : 1초 동안에 10번 동작 &nbsp;&nbsp;-> 1번에 10만큼 &nbsp;&nbsp;=> 10 * 10 = 100
* `20 fps` : 1초 동안에 20번 동작 &nbsp;&nbsp;-> 1번에 5만큼 &nbsp;&nbsp;=> 5 * 20 = 100

<br>

# **6_ collision**
적 캐릭터 생성 process 에서 이미지와 이미지가 위치할 좌표는 할당이 되었지만 실제 `enemy_rect` 개체 자체에는 할당이 되지 않았기 때문에 충돌 이벤트를 발생시키기 위해서는 rect 정보 업데이트 process 에서 이미지에 할당된 좌표 값을 `enemy_rect` 에 할당해야함

<br>

### `enemy` 에 저장된 좌표값을 `enemy_rect` 에 저장하여 충돌 처리가 가능하게끔 구성 
```python
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
```
<br>

# **7_ text(timer structure)**
>내림차순으로 1초씩 감소하는 제한시간을 화면 좌측 상단에 표시하는 process

<br>

### define process
```python
# 시간을 나타낼 폰트 정의
game_font = pygame.font.Font(None, 30) # 폰트 객체 생성 (폰트, 크기)

# 총 시간(s)
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()
```
감소하는 시간을 구성하기 위한 process 에서는 총 시간 `total_time` 을 정의하고, `pygame.time.get_ticks()` 를 통해 시작 시간 `start_ticks` 과 경과 시간 `elapsed_time` 의 tick 정보를 불러와 정의함


위 코드에서 정의한 변수들은 이벤트 루프 내에서 `str(int(총 시간 - 경과 시간)))` 형식으로 시간 정보 `timer` 를 계산하기 위한 것
* `int()` : 소수점으로 표시되지 않게함
* `str()` : 문자열 형식 출력에 대한 호환성

pygame 뿐만 아니라 다른 프로그램에서도 시간 계산을 할 때는 계산 직전에 현재 tick 정보를 받아왔다가 차후에 tick을 빼는 식으로 계산함

<br>

### `timer` process in event loop
```python
    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # render : 실제로 글자를 그리기
    # 출력할 글자, 안티앨리어스 유무, rgb 글자 색상
```
<br>

### `timer` 가 음수(-) 상태로 무한정 흐르지 않도록 제어
```python
    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("Time Out!")
        running = False
```
`if`문에서 `timer` 가 아닌 `total_time - elapsed_time`을 사용하는 이유?
* `timer`는 `render` 함수로 화면에 새겨진 문자열 형태기 때문에 int 값과 호환되지 않음

# QUIZ)
하늘에서 떨어지는 똥 피하기 게임 만들기

<br>

[게임 조건]  
✅ 1. 캐릭터는 화면 가장 아래 중앙에 위치, 좌우로만 이동 가능  
⬜ 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정  
⬜ 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐  
⬜ 4. 캐릭터가 똥과 충돌하면 게임 종료  
✅ 5. FPS 는 60 으로 고정

<br>

[게임 이미지]  
✅ 1. 배경 : 640 * 480 (세로 가로) - background.png  
✅ 2. 캐릭터 : 70 * 70 - character.png  
✅ 3. 똥 : 70 * 70 - enemy.png  
