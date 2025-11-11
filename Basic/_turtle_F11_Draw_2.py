import turtle
import random
import time # sleep 함수를 사용하기 위해 추가

# 화면 설정
def setup_screen():
    """창을 설정하고 전체 화면과 유사하게 최대화합니다."""
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    screen.title("거북이 이동 관찰 (느린 속도)")
    screen.colormode(255)
    screen.bgcolor("black") 
    
    # 📌 변경 1: tracer를 켜거나 (1 이상), 매우 느리게 업데이트하도록 설정합니다.
    # tracer(1)은 명령마다 업데이트하지만, 그리기 속도는 여전히 빠를 수 있습니다.
    # 여기서는 tracer를 1로 설정하고, 루프 내에서 강제 지연(sleep)을 추가하여 속도를 조절하겠습니다.
    screen.tracer(1) 
    
    return screen

# 거북이 설정
def setup_turtle(screen):
    """선을 그릴 거북이를 설정합니다."""
    t = turtle.Turtle()
    t.shape("turtle") # 📌 변경 2: 거북이 아이콘을 보이게 합니다.
    
    # 📌 변경 3: 거북이의 속도를 느린 값(1~6)으로 설정합니다. (0은 가장 빠름)
    t.speed(3) 
    
    t.pensize(2)
    t.penup() # 처음에는 펜을 들고 시작
    t.goto(0, 0) # 중앙에서 시작
    t.pendown()
    return t

# 무작위 색상 생성
def get_random_color():
    """무작위 RGB 색상 튜플을 반환합니다."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# 메인 그리기 루프
def draw_random_lines(t, screen):
    """거북이의 이동이 보이도록 선을 그립니다."""
    while True:
        # 무작위 색상 및 위치 설정
        t.pencolor(get_random_color())
        t.fillcolor(get_random_color()) # 거북이 색상도 변경 가능
        
        # 무작위로 방향을 돌립니다.
        t.left(random.randint(10, 170)) 
        
        # 무작위 길이만큼 앞으로 이동 (선을 그림)
        distance = random.randint(50, 150)
        t.forward(distance)

        # 화면 가장자리를 벗어났는지 확인하고, 벗어났다면 반대 방향으로 회전
        current_x, current_y = t.position()
        screen_width = screen.window_width()
        screen_height = screen.window_height()
        
        # 화면 경계에 가까워지면 방향 전환
        if abs(current_x) > screen_width / 2.1 or abs(current_y) > screen_height / 2.1:
            t.right(180) # 180도 회전하여 반대 방향으로 이동
            
        # 📌 속도를 더 관찰하기 위해 루프마다 약간의 지연 시간을 줍니다. (선택 사항)
        # time.sleep(0.05) 
        
# 프로그램 실행
if __name__ == "__main__":
    screen = setup_screen()
    t = setup_turtle(screen)
    
    try:
        draw_random_lines(t, screen)
    except turtle.Terminator:
        print("프로그램이 종료되었습니다.")
    except Exception as e:
        print(f"예외 발생: {e}")
        
    # 창을 닫기 전까지 대기
    # turtle.done() # 무한 루프이므로 이 코드는 실행되지 않습니다.
