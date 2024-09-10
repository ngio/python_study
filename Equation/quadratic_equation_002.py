"""_summary_
방정식/eqation
方程式은 영어 equation의 번역어로 알려져 있다. equation에는 '서로 똑같게 하기'라는 뜻이 있다.
사실 방정식에는 '서로 똑같게 한다'는 의미가 없다. 그런데도, equation을 방정식이라 번역한 것은 '방정(方程)'이 <九章算術(구장산술)>의 8번째 장의 이름인 것과 무관하지 않다. 중국의 <代數學(대수학)>(1859년), <代數術(대수술)>(1873)에서 '방정식'이라는 용어를 볼 수 있다. '방정'에 '제대로 된 모양새를 갖춘다'라는 의미를 가진 '식(式)'이 붙어 '방정식'이라는 용어가 만들어 진 것이다. '방정'의 의미가 무엇인지에 관해서는 여러 가지 의견이 있다.
옛 중국에서는 연립일차방정식을 풀 때, 계수를 계산판 위에 산목(算木)으로 나타낸 뒤, 가감법으로 해결했다. 이와 같이 계산판 위에 계수를 나란히 할당하는 것이 '方程'이다. 이때 사용한 계산판이 사각형처럼 생겨서 모서리가 있으므로 方이라는 단어를 사용한 것으로 보인다.
이렇게 볼 때, 대략 程은 '할당', 方은 '사각'이라는 뜻이 있는 것으로 보인다. 이 이외에 방은 비방(比方, 즉 조사하다)이고, 정은 법정(法程 즉, 법규) 또는 정과(程課 즉, 할당)라든지, 또는 方은 비(比)이고 程은 式이라는 해석 등도 있다.
"""
import math  # 수학 함수들을 사용하기 위한 모듈
from IPython.display import display  # 주피터 노트북 등에서 깔끔하게 출력하기 위한 display 모듈

def solve_quadratic(a, b, c):
    # 판별식 계산
    discriminant = b**2 - 4*a*c
    
    # 판별식의 값에 따라 해의 종류를 결정
    if discriminant > 0:
        # 두 개의 실수 해를 가짐
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        display(f"두 개의 실근: {root1:.2f}과 {root2:.2f}")
        
    elif discriminant == 0:
        # 중복된 하나의 실수 해를 가짐
        root = -b / (2 * a)
        display(f"중복된 실근: {root:.2f}")
        
    else:
        # 복소수 해를 가짐
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        display(f"복소수 해: {real_part:.2f} ± {imaginary_part:.2f}i")

# 예시: 계수 입력
a = 1  # x^2의 계수
b = -3  # x의 계수
c = 2  # 상수항

# 함수 호출하여 근 구하기
solve_quadratic(a, b, c)

