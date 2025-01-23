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




directory_base  = str(real_path)+"./img/"  # 경로object를 문자열로 변경해서 합친다. 
directory_out   = str(real_path)+"./output/"


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
    return base_name + new_extension



if __name__ == "__main__":
    # List all files in the directory
    file_list = [f for f in os.listdir(directory_base) if os.path.isfile(os.path.join(directory_base, f))]


    # Print the list of files
    for file in file_list:
        print(f"Processing: {file}")
        # Open an image file
        image_path = os.path.join(directory_base, file)
        original_image = Image.open(image_path) 

        # 엣지 감지 적용
        #edges_image = original_image.filter(ImageFilter.FIND_EDGES)
        edges_image = original_image.convert("L").filter(ImageFilter.FIND_EDGES)

        # 엣지 반전 처리 (배경 흰색, 엣지 검은색)
        edges_inverted = ImageOps.invert(edges_image)
        
        # JPG 파일명 생성 및 저장
        new_file_name = change_file_extension(file, ".jpg")
        output_path = os.path.join(directory_out, new_file_name)
        edges_inverted.convert("RGB").save(output_path, "JPEG")  # JPG 저장을 위해 RGB로 변환

        print(f"Edge image saved as: {output_path}")
         



