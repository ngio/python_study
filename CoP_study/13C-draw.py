"""
13-3
마우스로 거북이 조종해서 그림 그리기

"""
import turtle as t


def blank():
    t.clear()                 # 화면을 지우는 함수
    
    
t.shape("turtle")              # 거북이 모양을 사용합니다.
t.speed(0)                     # 거북이 속도를 가장 빠르게 지정합니다.
t.pensize(2)                   # 펜 굵기를 2로 지정합니다.
t.hideturtle()                 # 거북이를 화면에서 숨긴다
t.onkeypress(blank, "Escape")  # Esc 를 누르면 blank 함수를 실행합니다.
t.onscreenclick(t.goto)        # 마우스 버튼을 누르면 t.goto 함수를 호출합니다. 
t.listen()                     # 거북이 그래픽 창이 키보드 입력을 받습니다.
t.mainloop()                   # 사용자가 거북이 그래픽 창을 종료할 때까지 프로그램을 시행하면서 마우스나 키보드 입력을 계속 처리하도록 하는 함수
