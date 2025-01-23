# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

#========================================
""" 
Pillow 라이브러리의 ImageFilter 모듈을 사용하여 FIND_EDGES 필터를 적용하는 예제입니다. 
이 필터는 이미지의 경계를 감지하여 윤곽선을 강조하는 효과를 제공합니다.
"""

from PIL import Image, ImageFilter, ImageOps
import os

# 경로 설정
###real_path = os.getcwd()  # 현재 작업 디렉토리 가져오기  --> 제일 상단에서 대치.
directory_base = str(real_path) + "/img/"  # 입력 이미지 경로
directory_out = str(real_path) + "/output/"  # 출력 이미지 경로

# 출력 디렉토리가 없으면 생성
if not os.path.exists(directory_out):
    os.makedirs(directory_out)

def change_file_extension(file_path, new_extension):
    """
    파일 경로에서 확장자를 변경하여 새 경로를 반환하는 함수.

    Args:
        file_path (str): 기존 파일 경로
        new_extension (str): 새 확장자 (예: '.jpg', '.png')

    Returns:
        str: 새 확장자가 적용된 파일 경로
    """
    base_name, _ = os.path.splitext(file_path)  # 확장자를 제외한 경로와 파일명
    if not new_extension.startswith("."):
        new_extension = f".{new_extension}"  # 확장자 앞에 '.' 추가
    #return base_name + new_extension
    return base_name + "_edge" + new_extension

def process_edge_image(input_path, output_path, threshold=128, expand_size=3):
    """
    엣지 감지 후 선 굵게 하기 및 배경 제거.

    Args:
        input_path (str): 입력 이미지 경로
        output_path (str): 출력 이미지 경로
        threshold (int): 이진화 임계값 (0-255)
        expand_size (int): 선 굵기 확장 크기

    Returns:
        None
    """
    # 이미지 열기
    original_image = Image.open(input_path).convert("L")  # 흑백으로 변환

    # 엣지 감지
    #edges_image = original_image.filter(ImageFilter.FIND_EDGES)    
    edges_image = original_image.convert("L").filter(ImageFilter.FIND_EDGES)
    
    ## 선 굵게 하기
    #expanded_edges = edges_image.filter(ImageFilter.MaxFilter(size=expand_size))
    ## 배경 제거 (이진화)
    #binary_edges = expanded_edges.point(lambda p: 255 if p > threshold else 0)
    
    
    # 엣지 반전 처리 (배경 흰색, 엣지 검은색)
    edges_inverted = ImageOps.invert(edges_image)

    # 결과 저장
    edges_inverted.save(output_path, "JPEG")
    print(f"Processed image saved at: {output_path}")

if __name__ == "__main__":
    # 입력 디렉토리 내 파일 리스트
    file_list = [f for f in os.listdir(directory_base) if os.path.isfile(os.path.join(directory_base, f))]

    # 파일 처리
    for file in file_list:
        print(f"Processing: {file}")
        # 입력 파일 경로
        image_path = os.path.join(directory_base, file)
        
        # 출력 파일 경로
        new_file_name = change_file_extension(file, ".jpg")
        output_path = os.path.join(directory_out, new_file_name)
        
        # 엣지 처리 및 저장
        process_edge_image(image_path, output_path)
