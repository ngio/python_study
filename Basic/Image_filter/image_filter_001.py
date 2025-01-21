""" 
Pillow 라이브러리의 ImageFilter 모듈을 사용하여 FIND_EDGES 필터를 적용하는 예제입니다. 
이 필터는 이미지의 경계를 감지하여 윤곽선을 강조하는 효과를 제공합니다.
"""

from PIL import Image, ImageFilter

# 1. 이미지 열기
image_path = "test_001.png"  # 경로를 적절히 수정하세요
original_image = Image.open(image_path)

# 2. FIND_EDGES 필터 적용
edges_image = original_image.filter(ImageFilter.FIND_EDGES)  #filter(ImageFilter.FIND_EDGES)를 사용하여 경계선 필터를 적용합니다.

# 3. 원본 이미지와 필터 적용된 이미지 저장 및 출력
edges_image.save("test_001_output.jpg")
original_image.show(title="Original Image")
edges_image.show(title="Edges Image")
