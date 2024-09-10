2차 방정식은 2차 다항식 방정식으로, 일반적인 형태는 다음과 같습니다:

![image](https://github.com/user-attachments/assets/2977dfaa-97e8-4101-a0b9-4d2cee7c1f54)

Python으로 2차 방정식 풀기
아래는 Python을 사용하여 2차 방정식의 해를 구하는 예제 코드입니다:

import cmath  # 복소수 계산을 위해 cmath 모듈 사용

    def solve_quadratic(a, b, c):
        # 판별식 계산
        discriminant = b**2 - 4*a*c
        
        # 근의 공식 사용
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        
        return root1, root2
    
    # 예시: a, b, c 값 입력
    a = 1  # x^2의 계수
    b = -3  # x의 계수
    c = 2  # 상수항
    
    # 함수 호출하여 근 구하기
    roots = solve_quadratic(a, b, c)
    
    # 결과 출력
    print(f"방정식의 근: {roots[0]} 과 {roots[1]}")

![image](https://github.com/user-attachments/assets/406317fb-e4d5-42bc-bd65-5c6775cd3dfb)

