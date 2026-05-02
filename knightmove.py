import turtle

# 1. 화면 설정
screen = turtle.Screen()
screen.title("Knight Move (WASD) - Turtle Mode")
screen.bgcolor("#2c3e50") # 어두운 배경색
screen.setup(width=800, height=600)
screen.tracer(0) # 화면 애니메이션 최적화 (버벅임 방지)

# 2. 기사 생성
knight = turtle.Turtle()
knight.shape("square") # 기사 모양 (기본 사각형)
knight.color("#f1c40f") # 금색
knight.penup()          # 이동할 때 선이 그려지지 않게 함
knight.speed(0)         # 애니메이션 속도 최대로

# 기사 속도 설정
move_speed = 20

# 3. 이동 함수 정의
def move_up():
    y = knight.ycor()
    if y < 280: # 화면 위쪽 경계 제한
        knight.sety(y + move_speed)

def move_down():
    y = knight.ycor()
    if y > -280: # 화면 아래쪽 경계 제한
        knight.sety(y - move_speed)

def move_left():
    x = knight.xcor()
    if x > -380: # 화면 왼쪽 경계 제한
        knight.setx(x - move_speed)

def move_right():
    x = knight.xcor()
    if x < 380: # 화면 오른쪽 경계 제한
        knight.setx(x + move_speed)

# 4. 키보드 입력 연결 (WASD)
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# 대문자 입력 대비 (Caps Lock이 켜져 있을 때를 위해)
screen.onkeypress(move_up, "W")
screen.onkeypress(move_down, "S")
screen.onkeypress(move_left, "A")
screen.onkeypress(move_right, "D")

# 5. 게임 루프
while True:
    screen.update() # tracer(0)를 썼으므로 수동으로 화면을 갱신해줌
