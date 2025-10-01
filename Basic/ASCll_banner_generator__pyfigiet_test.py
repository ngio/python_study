"""
    pip install pyfiglet
"""

import pyfiglet
import sys

def generate_ascii_banner(text, font_name='slant'):
    """
    주어진 텍스트와 폰트 이름으로 ASCII 배너를 생성하고 출력합니다.
    
    :param text: ASCII 아트로 변환할 문자열
    :param font_name: 사용할 pyfiglet 폰트 이름 (기본값: 'slant')
    """
    try:
        # pyfiglet Figlet 객체 생성 및 폰트 설정
        fig = pyfiglet.Figlet(font=font_name)
        
        # 텍스트를 ASCII 아트로 변환
        banner = fig.renderText(text)
        
        # 결과 출력
        print("=" * 50)
        print(f"사용된 폰트: {font_name}")
        print("-" * 50)
        print(banner)
        print("=" * 50)
        
    except pyfiglet.FigletError:
        # 존재하지 않는 폰트 이름을 입력했을 때 발생하는 오류 처리
        print(f"\n[오류] '{font_name}' 폰트는 존재하지 않습니다.")
        print("사용 가능한 폰트 목록을 확인해주세요.")
    except Exception as e:
        print(f"\n[예외 발생] 예상치 못한 오류가 발생했습니다: {e}")


# --- 메인 실행 로직 ---
if __name__ == "__main__":
    # 사용자로부터 입력 텍스트 받기
    input_text = input("ASCII 배너로 만들 텍스트를 입력하세요: ")
    
    if not input_text:
        print("입력된 텍스트가 없습니다. 프로그램을 종료합니다.")
        sys.exit()

    # (선택 사항) 다양한 폰트로 테스트
    print("\n--- 다양한 폰트로 테스트 ---")
    
    # 1. 'slant' 폰트 (기본값)
    generate_ascii_banner(input_text, 'slant')
    
    # 2. 'big' 폰트
    generate_ascii_banner(input_text, 'big')
    
    # 3. 'digital' 폰트
    generate_ascii_banner(input_text, 'digital')
    
    # 4. 'banner3-D' 폰트
    generate_ascii_banner(input_text, 'banner3-D')

    # 모든 사용 가능한 폰트 목록을 보려면 다음 코드를 사용하세요.
    # print("\n--- 사용 가능한 모든 폰트 목록 ---")
    # print(pyfiglet.Figlet().getFonts())


