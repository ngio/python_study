# img_to_sketch_001.py
# 스케치 변환 프로그램 


# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 


import cv2
import numpy as np
import os

def convert_to_sketch(image_path, output_path="sketch_output.jpg"):
    """
    사진을 읽어들여 스케치 형식으로 변환하고 저장합니다.
    """
    try:
        # 1. 이미지 로드
        img = cv2.imread(image_path)
        if img is None:
            print(f"오류: 이미지를 로드할 수 없습니다. 경로를 확인하세요: {image_path}")
            return

        # 2. 이미지를 회색조로 변환
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # 3. 이미지 반전 (어두운 부분은 밝게, 밝은 부분은 어둡게)
        # 펜으로 그린 선처럼 보이게 합니다.
        inverted_img = 255 - gray_img
        
        # 4. 가우시안 블러 적용
        # 이미지를 부드럽게 만들고, 반전된 이미지와 블렌딩할 때 경계를 부드럽게 합니다.
        # (21, 21)은 커널 크기, 0은 시그마 값 (자동 계산)
        blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)
        
        # 5. 컬러 닷지 블렌드 모드 적용 (스케치 효과의 핵심)
        # 원본 회색조 이미지와 블러 처리된 반전 이미지를 혼합합니다.
        # "닷지(Dodge)" 모드는 밝은 영역을 더 밝게 만들고, 어두운 영역의 디테일을 유지합니다.
        # OpenCV에서는 직접적인 닷지 블렌드 모드 함수를 제공하지 않으므로, 수학적 연산을 사용합니다.
        # result = (gray_img * 256) / (255 - blurred_img + epsilon)
        # 여기서 255 - blurred_img가 0이 되는 것을 방지하기 위해 작은 값(epsilon)을 더합니다.
        epsilon = 10 # 0으로 나누는 것을 방지하기 위한 작은 상수
        sketch_img = cv2.divide(gray_img, 255 - blurred_img + epsilon, scale=256)
        
        # 6. 결과 이미지 저장
        cv2.imwrite(output_path, sketch_img)
        print(f"스케치 이미지가 '{output_path}'로 성공적으로 저장되었습니다.")

    except Exception as e:
        print(f"스케치 변환 중 오류 발생: {e}")

# --- 사용 예시 ---
# 1. 'input_image.jpg' 라는 이름의 사진 파일을 이 파이썬 스크립트와 같은 폴더에 놓으세요.
# 2. 또는 정확한 이미지 파일 경로를 지정하세요.
input_image_path = "person_01.jpg"

# 파일명과 확장자 분리 및 새 파일명 생성
file_name_without_extension, file_extension = os.path.splitext(input_image_path)
output_sketch_path = f"{file_name_without_extension}_sketch{file_extension}"
 
print(f"원본 파일명: {input_image_path}")
print(f"확장자 없는 파일명: {file_name_without_extension}")
print(f"확장자: {file_extension}")

#output_caricature_path = file_name_without_extension + "_caricature_result." + file_extension
# F-string을 사용하여 문자열 내부에 변수를 직접 삽입합니다.
output_sketch_path = f"{file_name_without_extension}_caricature_result{file_extension}"



convert_to_sketch(input_image_path, output_sketch_path)

# 결과 이미지 확인 (선택 사항)
# try:
#     # OpenCV로 이미지 표시 (OpenCV 창을 사용)
#     result_img = cv2.imread(output_sketch_path)
#     if result_img is not None:
#         cv2.imshow("Sketch Image", result_img)
#         cv2.waitKey(0)  # 아무 키나 누를 때까지 대기
#         cv2.destroyAllWindows() # 모든 OpenCV 창 닫기
#     else:
#         print("결과 이미지를 읽을 수 없습니다.")
# except FileNotFoundError:
#     print("결과 이미지를 찾을 수 없어 미리보기를 실행할 수 없습니다.")
# except Exception as e:
#     print(f"결과 이미지 미리보기 중 오류 발생: {e}")


