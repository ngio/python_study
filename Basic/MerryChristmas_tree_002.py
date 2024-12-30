# HAPPY NEW YEAR 패턴 출력
rows = 10  # 트리 높이 조정 가능

# 트리 본체 출력
for i in range(1, rows + 1):
    # 공백 출력
    print(" " * (rows - i), end="")
    # 별과 HAPPY NEW YEAR 출력
    if i == rows:
        print("HAPPY NEW YEAR")
    else:
        print("*" * (2 * i - 1))

# 트리 줄기 출력
for j in range(3):  # 줄기 높이
    print(" " * (rows - 2) + "|||")
