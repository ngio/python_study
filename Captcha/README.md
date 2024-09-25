
Generate Captcha Using Python

[captcha_main_xls.py](captcha_main_xls.py)
랜던 6영문숫자 생성 후 캡챠 이미지 생성하고, 이미지명은 엑셀에 저장한다. 


[https://www.geeksforgeeks.org/generate-captcha-using-python/](https://www.geeksforgeeks.org/generate-captcha-using-python/)


In this article, we are going to see how to generate a captcha using Python package captcha to generate our own CAPTCHA (Completely Automated Public Turing Test to Tell Computers and Humans Apart) in picture form. CAPTCHA is a form of challenge-response authentication security mechanism. CAPTCHA prevents automated systems from reading the distorted characters in the picture.



pip install captcha



Generating image captcha: 

    # Import the following modules
    from captcha.image import ImageCaptcha
     
    # Create an image instance of the given size
    image = ImageCaptcha(width = 280, height = 90)
     
    # Image captcha text
    captcha_text = 'GeeksforGeeks' 
     
    # generate the image of the given text
    data = image.generate(captcha_text)  
     
    # write the image on the given file and save it
    image.write(captcha_text, 'CAPTCHA.png')

Generating Audio captcha:

    # Import the following modules
    from captcha.audio import AudioCaptcha
    
    # Create an audio instance
    audio = AudioCaptcha() 
    
    # Audio captcha text
    captcha_text = "5454"
    
    # generate the audio of the given text
    audio_data = audio.generate(captcha_text)
    
    # Give the name of the audio file
    audio_file = "audio"+captcha_text+'.wav'
    
    # Finally write the audio file and save it
    audio.write(captcha_text, audio_file)


완성형
    
    import random
    import string
    import os
    from captcha.image import ImageCaptcha  # ImageCaptcha 라이브러리를 사용해야 합니다.
    
    # 랜덤 6자리 문자열 생성 함수
    def generate_random_string(length=6):
        characters = string.ascii_letters + string.digits  # 영문 대소문자 + 숫자
        return ''.join(random.choices(characters, k=length))
    
    # 중복되지 않는 파일명 생성 함수
    def get_unique_filename(base_name, extension, directory="./img/"):
        counter = 1
        new_filename = f"{base_name}.{extension}"
        
        # 경로 내 파일명이 중복되면 새로운 파일명 생성
        while os.path.exists(os.path.join(directory, new_filename)):
            new_filename = f"{base_name}_{counter}.{extension}"
            counter += 1
        
        return new_filename
    
    # 메인 로직
    def main():
        # 캡차 이미지 생성기 설정
        image = ImageCaptcha(width=280, height=90)
    
        # 랜덤 6자리 문자열 생성
        captcha_text = generate_random_string()
        print(f"\n랜덤 6자리 문자열: {captcha_text}")
    
        # 이미지 생성
        data = image.generate(captcha_text)
    
        # 이미지 저장 경로 지정
        img_directory = "./img/"
        os.makedirs(img_directory, exist_ok=True)  # img 폴더가 없을 경우 생성
    
        # 중복되지 않는 파일명 생성
        unique_filename = get_unique_filename(captcha_text, 'png', directory=img_directory)
    
        # 이미지 파일 저장
        image.write(captcha_text, os.path.join(img_directory, unique_filename))
    
        print(f"이미지가 {unique_filename}으로 저장되었습니다.")
    
    # 프로그램 실행
    if __name__ == "__main__":
        main()


















