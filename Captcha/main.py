# 2023-05-26 ngio add
# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

import _random_word_001 as rw001

def main():
    # 프로그램의 주요 로직
    print("Hello, this is the main function.")
        
    # 함수 호출 - captcha word
    random_string = rw001.generate_random_string("A",6)
    print(f"랜덤 6자리 영문 숫자 난수: {random_string}")
    
    # 함수 호출 - captcha file word
    random_string = rw001.generate_random_string()
    print(f"랜덤 20자리 영문 숫자 난수: {random_string}")    
    

# 메인 함수 호출
if __name__ == "__main__":
    main()
    
    
    
    
    