[python] 폴더 안의 .webp 이미지를 .png 로 변환

.webp 이미지를 .png로 변환하는 Python 프로그램을 작성할 수 있습니다. 이를 위해 Pillow 라이브러리를 사용합니다. Pillow는 Python의 이미지 처리 라이브러리로, 다양한 이미지 형식을 다룰 수 있습니다.

다음은 특정 폴더 내의 모든 .webp 이미지를 .png로 변환하는 프로그램입니다:

1. Pillow 설치
먼저 Pillow 라이브러리를 설치해야 합니다. 터미널이나 명령 프롬프트에서 다음 명령어를 실행하세요:

        pip install Pillow


2. .webp 이미지를 .png로 변환하는 코드
아래 코드 예시는 지정된 폴더 내의 모든 .webp 파일을 .png 파일로 변환합니다:


        from PIL import Image
        import os
        
        def convert_webp_to_png(folder_path):
            # 폴더 내 모든 파일을 반복
            for filename in os.listdir(folder_path):
                if filename.endswith(".webp"):
                    # 파일의 전체 경로 생성
                    webp_file_path = os.path.join(folder_path, filename)
        
                    # .webp 파일을 열고 .png로 저장
                    png_filename = filename[:-5] + ".png"  # 파일 확장자를 .png로 변경
                    png_file_path = os.path.join(folder_path, png_filename)
        
                    with Image.open(webp_file_path) as img:
                        img.save(png_file_path, "png")
                    
                    print(f"Converted: '{filename}' -> '{png_filename}'")
        
        # 사용 예시
        folder_path = 'path_to_your_folder'  # 여기에 폴더 경로를 입력하세요
        convert_webp_to_png(folder_path)

## 코드 설명
Pillow 라이브러리 사용: Pillow의 Image 모듈을 사용하여 이미지를 열고 변환합니다.

## 폴더 내 파일 탐색:

os.listdir(folder_path)를 사용하여 지정된 폴더 내의 모든 파일을 가져옵니다.
if filename.endswith(".webp"): 조건문을 사용하여 .webp 확장자를 가진 파일만 필터링합니다.

## 파일 경로 생성:

webp_file_path는 원본 .webp 파일의 전체 경로입니다.
png_filename은 .webp 확장자를 .png로 대체한 새 파일 이름입니다.
png_file_path는 변환된 .png 파일의 전체 경로입니다.

## 이미지 변환 및 저장:

Image.open(webp_file_path)를 사용하여 .webp 파일을 열고, img.save(png_file_path, "png")를 사용하여 .png 파일로 저장합니다.

## 사용 방법:

folder_path 변수에 변환할 .webp 파일이 있는 폴더 경로를 입력합니다.
프로그램을 실행하면 폴더 내 모든 .webp 파일이 .png 파일로 변환됩니다.

## 사용 예시
  예를 들어, 폴더 경로가 C:/Users/YourName/Documents/Images인 경우:

    folder_path = 'C:/Users/YourName/Documents/Images'
    convert_webp_to_png(folder_path)

위 코드를 실행하면 해당 폴더 내의 모든 .webp 파일이 .png 형식으로 변환됩니다.


   
