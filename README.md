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

<br>

# **QUIZ)**
하늘에서 떨어지는 똥 피하기 게임 만들기

<br>

[게임 조건]  
✅ 1. 캐릭터는 화면 가장 아래 중앙에 위치, 좌우로만 이동 가능  
✅ 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정  
✅ 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐  
✅ 4. 캐릭터가 똥과 충돌하면 게임 종료  
✅ 5. FPS 는 60 으로 고정

<br>

[게임 이미지]  
✅ 1. 배경 : 640 * 480 (세로 가로) - background.png  
✅ 2. 캐릭터 : 70 * 70 - character.png  
✅ 3. 똥 : 70 * 70 - enemy.png

<br>

# **Project) 오락실 PANG 게임 제작**

[게임 조건]
✅ 1. 캐릭터는 화면 하단 중앙에 위치, 좌우로만 이동 가능
✅ 2. 스페이스를 누르면 무기를 쏘아 올림
✅ 3. 큰 공 1개가 나타나서 바운스
✅ 4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
✅ 5. 모든 공을 없애면 게임 종료 (성공)
✅ 6. 캐릭터는 공에 닿으면 게임 종료 (실패)
✅ 7. 시간 제한 99초 초과 시 게임 종료 (실패)
✅ 8. FPS 는 30 으로 고정 (필요시 speed 값을 조정)

[게임 이미지]
✅ 1. 배경 : 640 * 480(가로 세로) - background.png
✅ 2. 무대 : 640 * 50 - stage.png
✅ 3. 캐릭터 : 33 * 60 - character.png
✅ 4. 무기 : 20 * 430 - weapon.png
✅ 5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - balloon1.png ~ balloon4.png

<br>

# **2_ weapon_keyevent**
```python
    # 발사체 y축 상승
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    # 발사체 화면 최상단 도달 시 소멸
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
```
하나의 `weapon` 발사체의 x축 `w[0]` 은 그대로 유지하고, y축 `w[1]` 에는 `weapon_speed` 를 빼주어 발사체가 상승하는 이미지를 연출

화면 y축의 0(최상단) 보다 큰 값의 weapon 만 나타내는 코드를 작성하여 0에 도달했을 때 발사체가 사라지는 이미지를 연출

<br>

```python
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons: # weapons 리스트에 x,y 좌표를 받음
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
        
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
```
`blit` 의 레이아웃은 먼저 입력된 순서대로 가장 아래에 배치되기 때문에 `weapons` 의 발사체가 스테이지나 캐릭터의 외관 위에 나타나지 않도록 배경 다음으로 배치

<br>

# **3_ ball_movement**
### `enumerate()`
```python
lst = ["A", "B", "C"]

for lst_idx, lst_val in enumerate(lst):
    print(lst_idx, lst_val)
```
```
0 가
1 나
2 다
```
`for`문 내에서 정의된 `lst_idx` 에 key(index) 값을, `lst_val` 에 value 값을 각각 저장해주는 함수로, 이 파트에서는 각각 4가지 형태의 고유한 튕기는 공 동작을 구성하기 위해 필요한 여러 개의 변화값을 쉽게 처리할 수 있도록 사용함

<br>

### 스테이지에 튕겨서 올라가는 처리
```python
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그 외의 모든 경우에는 속도를 증가
            ball_val["to_y"] += 0.5
```
y축은 위에서 아래로 `screen.blit` 이 적용되기 때문에 최상단(0)에서 하단으로 갈 수록 양수로 늘어남.

가장 큰 1단계 공이 스테이지에 닿았을 때 공의 y축 추가 이동 좌표를 제공하는 `ball_val["to_y"]` 에 -18, 즉 `ball_val["init_spd_y"]` 를 더하면 화면 하단에 위치에 있는 `ball_val["to_y"]` 의 int값이 -18 만큼 깎이기 때문에 공이 튕겨서 상승하는 모습을 나타낼 수 있는 것

<br>

# **5_ ball_division**
### 튕겨나가는 다음 단계의 공 위치 설정
```python
balls.append({
    "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공 x 좌표
    "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공 y 좌표
```
현 단계 공의 현 위치 `ball_pos_x` 에서 `ball_width / 2` 를 연산하여 정 생성 시작 x 좌표를 중앙에 위치시키고, 두 갈래로 나뉘어지는 공의 자연스러운 갈라짐 효과를 위해 두 개 공 사이의 거리를 이격시킴

좌우 2갈래로 나뉘어지는 위치 `- (small_ball_width / 2)`  

<br>

![nextIndexBallPos](pygame_project\img\nextIndexBallPos.png)

<br>

# **6_ gamemover**
### 근접상태에서 공 파괴 시 다음 단계 공 비정상적 생성 디버깅
![preBallDelBug](pygame_project\img\preBallDelBug.png)
위 사진과 같은 공의 비정상적 생성 버그는 `ball` 과 `weapon` 의 충돌 처리를 하는 2중 `for`문 과정에서 바깥 `for`문을 코드 상에서 제대로 탈출하지 못했기 때문에 이전 단계의 공이 다시 생성되는 버그임.

아래의 코드에서 `for`문에 `else` 를 사용함으로써 2중 `for`문을 탈출하는 트릭을 이용함.
```python
# 충돌 처리 2중 for문 버그 디버깅

for ball_idx, ball_val in enumerate(balls):
    ...
    # 공과 무기들 충돌 처리
    for weapon_idx, weapon_val in enumerate(weapons):
        ...
        # 충돌 체크
        if weapon_rect.colliderect(ball_rect):
            ...
            if ball_img_idx < 3:
                ...
            break # 안쪽 for문 탈출
    else: # 계속 게임을 진행 (for 문의 else)
        continue # 안쪽 for 문의 조건이 맞지 않으면 continue. 바깥for 문 계속 수행
    break # 안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중for 문 한 번에 탈출
```