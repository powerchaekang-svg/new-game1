import turtle
import time

# 1. 화면 설정
screen = turtle.Screen()
screen.title("Hungry Knight - Start!")
screen.bgcolor("#2c3e50")
screen.setup(width=800, height=600)
screen.tracer(0)

# 2. 기사 생성 (knightmove.py 내용)
knight = turtle.Turtle()
knight.shape("square")
knight.color("#f1c40f")
knight.penup()
knight.speed(0)

move_speed = 20

# 3. 타이머/물병 설정 (timer_test.py 내용)
# 물병 테두리
border = turtle.Turtle()
border.hideturtle()
border.color("white")
border.speed(0)
border.penup()
border.goto(-350, -100) # 화면 왼쪽 끝으로 위치 조정
border.pendown()
for _ in range(2):
    border.forward(40)
    border.left(90)
    border.forward(200)
    border.left(90)

# 게이지(액체)
gauge = turtle.Turtle()
gauge.hideturtle()
gauge.penup()
gauge.pensize(36)
gauge.color("deep sky blue")
gauge.left(90)

MAX_TIME = 10 # 10초
current_time = MAX_TIME

# 4. 함수 정의
def move_up():
    y = knight.ycor()
    if y < 280: knight.sety(y + move_speed)

def move_down():
    y = knight.ycor()
    if y > -280: knight.sety(y - move_speed)

def move_left():
    x = knight.xcor()
    if x > -380: knight.setx(x - move_speed)

def move_right():
    x = knight.xcor()
    if x < 380: knight.setx(x + move_speed)

def draw_gauge(t):
    gauge.clear()
    gauge.penup()
    gauge.goto(-330, -98) # 테두리 안쪽 위치
    gauge.pendown()
    fill_height = (t / MAX_TIME) * 196
    if fill_height > 0:
        gauge.forward(fill_height)
    gauge.penup()

# 5. 키보드 연결
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_up, "W")
screen.onkeypress(move_down, "S")
screen.onkeypress(move_left, "A")
screen.onkeypress(move_right, "D")

# 6. 메인 게임 루프
start_time = time.time()

while current_time > 0:
    # 시간 계산
    elapsed = time.time() - start_time
    current_time = MAX_TIME - elapsed
    
    # 게이지 그리기
    draw_gauge(current_time)
    
    # 화면 갱신 (기사 이동과 게이지 변화를 한 번에!)
    screen.update()
    time.sleep(0.01)

# 게임 오버 처리
gauge.clear()
print("배고파서 게임 오버!")
knight.color("gray") # 게임 오버 시 기사 색 변경
screen.update()

screen.mainloop()
