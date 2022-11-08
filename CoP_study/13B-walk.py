"""
13-2
키보드로 거북이 조종해서 그림 그리기

"""
import turtle as t

def turn_right():                  # 오른쪽으로 이동하는 함수
    t.setheading(0)                # t.seth(0) 으로 입력해도 됩니다.
    t.forward(10)                  # t.fd(10) 으로 입력해도 됩니다.
    
def turn_up():                     # 위로 이동하는 함수
    t.setheading(90)
    t.forward(10)
    
def turn_left():                   # 아래로 이동하는 함수
    t.setheading(180)
    t.forward(10)
    
def turn_down():                   # 화면을 지우는 함수
    t.setheading(270)
    t.forward(10)
    
def blank():
    t.clear()                      # 화면을 지우는 함수

t.shape("turtle")                  # 거북이 모양을 사용합니다.
t.speed(0)                         # 거북이 속도를 가장 빠르게 지정합니다.
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(blank, "Escape")      # Esc 를 누르면 blank 함수를 실행합니다.
t.listen()                         # 거북이 그래픽 창이 키보드 입력을 받습니다.
t.mainloop()                       # 사용자가 거북이 그래픽 창을 종료할 때까지 프로그램을 시행하면서 마우스나 키보드 입력을 계속 처리하도록 하는 함수


def blank():
    t.clear()                      # 화면을 지우는 함수
    
     
