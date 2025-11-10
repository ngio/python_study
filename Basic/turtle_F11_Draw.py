import turtle
import random

# 화면 설정
def setup_screen():
    """창을 설정하고 전체 화면과 유사하게 최대화합니다."""
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0) # 화면 크기를 최대화합니다.
    screen.title("무작위 선 그리기 (전체 화면)")
    screen.colormode(255) # RGB 색상 모드를 0-255로 설정합니다.
    screen.bgcolor("black") # 배경색을 검은색으로 설정합니다.
    screen.tracer(0) # 그리기 속도를 높이기 위해 자동 화면 업데이트를 끕니다.
    return screen

# 거북이 설정
def setup_turtle():
    """선을 그릴 거북이를 설정합니다."""
    t = turtle.Turtle()
    t.hideturtle() # 거북이 아이콘을 숨깁니다.
    t.speed(0) # 최고 속도로 설정합니다.
    t.pensize(2) # 펜 두께를 설정합니다.
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
    """화면이 종료될 때까지 무작위 선을 계속 그립니다."""
    while True:
        # 무작위 색상 및 위치 설정
        color = get_random_color()
        t.pencolor(color)
        
        # 펜을 든 상태로 무작위 위치로 이동 (현재 위치에서 그리기 시작)
        t.left(random.randint(-180, 180)) # 무작위로 방향을 돌립니다.
        
        # 무작위 길이만큼 앞으로 이동 (선을 그림)
        distance = random.randint(50, 300)
        t.forward(distance)

        # 화면 가장자리를 벗어났는지 확인하고, 벗어났다면 펜을 들고 중앙 근처로 이동
        # 이 과정이 없으면 거북이가 화면 밖으로 나가버려 그림이 멈춘 것처럼 보일 수 있습니다.
        current_x, current_y = t.position()
        screen_width = screen.window_width()
        screen_height = screen.window_height()
        
        if abs(current_x) > screen_width / 2 or abs(current_y) > screen_height / 2:
            t.penup() # 펜 들기
            t.goto(0, 0) # 중앙으로 이동
            t.left(random.randint(-180, 180)) # 방향을 다시 무작위로 설정
            t.pendown() # 펜 내리기
            
        # 화면 업데이트 (tracer(0)를 사용했으므로 수동으로 업데이트)
        screen.update()

# 프로그램 실행
if __name__ == "__main__":
    screen = setup_screen()
    t = setup_turtle()
    
    try:
        draw_random_lines(t, screen)
    except turtle.Terminator:
        # 창 닫기 버튼을 눌렀을 때 발생하는 예외 처리
        print("프로그램이 종료되었습니다.")
    except Exception as e:
        print(f"예외 발생: {e}")
        
    # 창을 닫을 때까지 프로그램이 대기하도록 함 (실제 draw_random_lines 루프에서는 필요 없음)
    # turtle.done()
