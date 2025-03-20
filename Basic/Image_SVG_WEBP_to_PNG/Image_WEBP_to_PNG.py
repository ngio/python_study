
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 



# 입력 폴더 & 출력 폴더
input_folder = "img"
output_folder = "output_png"

# 출력 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# img 폴더 안의 모든 WEBP 파일을 PNG로 변환
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".webp"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".webp", ".png"))

        # 변환 실행
        image = Image.open(input_path)
        image.save(output_path, "PNG")

        print(f"변환 완료: {filename} → {output_path}")

print("✅ 모든 변환이 완료되었습니다!")
