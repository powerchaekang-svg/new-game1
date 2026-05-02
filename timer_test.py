import turtle
import time

# 화면 설정
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # 애니메이션을 부드럽게 하기 위해 자동 업데이트 끔

# 물병 테두리 그리기 전용 거북이
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.penup()
border.goto(-250, -100) # 타이머 위치
border.pendown()
for _ in range(2):
    border.forward(40)
    border.left(90)
    border.forward(200)
    border.left(90)

# 게이지(액체) 전용 거북이
gauge = turtle.Turtle()
gauge.hideturtle()
gauge.penup()
gauge.pensize(36) # 물병 안을 채울 두께
gauge.color("deep sky blue")
gauge.left(90) # 위를 보게 함

MAX_TIME = 10
current_time = MAX_TIME

def draw_gauge(t):
    gauge.clear()
    gauge.goto(-230, -98) # 물병 바닥 안쪽
    gauge.pendown()
    # 남은 시간에 비례해서 선을 긋음 (최대 높이 196)
    fill_height = (t / MAX_TIME) * 196
    if fill_height > 0:
        gauge.forward(fill_height)
    gauge.penup()

# 게임 루프
start_time = time.time()
while current_time > 0:
    elapsed = time.time() - start_time
    current_time = MAX_TIME - elapsed
    
    draw_gauge(current_time)
    screen.update()
    time.sleep(0.01)

print("배고파서 게임 오버!")
screen.mainloop()
