# cairosvg
# pip install cairosvg 
 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 
 



import cairosvg

# 변환할 폴더 경로
input_folder = "img"
output_folder = "output_png"

# 출력 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# img 폴더 안의 모든 SVG 파일 변환
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".svg"):  # 확장자가 .svg인 파일만 처리
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".svg", ".png"))

        # SVG → PNG 변환
        cairosvg.svg2png(url=input_path, write_to=output_path)
        print(f"변환 완료: {filename} → {output_path}")

print("✅ 모든 변환이 완료되었습니다!")

 
