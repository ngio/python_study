"""
입력된 웹 페이지 내에서 모든 <img> 요소를 추출하는 프로그램을 **requests**와 BeautifulSoup 라이브러리를 사용하여 구현해 드리겠습니다. 🔎

이 방법은 웹 크롤링(Web Crawling)의 가장 기본적인 형태이며, HTML을 파싱(Parsing)하여 원하는 특정 태그를 쉽게 찾아낼 수 있습니다.
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys

def extract_images_from_url(url):
    """
    주어진 URL의 웹 페이지에서 모든 <img> 태그의 src 속성을 추출합니다.
    
    :param url: 분석할 웹 페이지의 URL
    :return: 이미지 URL 리스트
    """
    if not (url.startswith('http://') or url.startswith('https://')):
        # 사용자가 프로토콜을 생략했을 경우 https://를 기본으로 추가
        url = 'https://' + url
        
    image_list = []
    
    print(f"URL에 접속 중: {url}")
    
    try:
        # 1. HTTP 요청 보내기
        # User-Agent를 설정하여 봇 접근이 아님을 알리고 접속 거부를 방지합니다.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # HTTP 오류가 발생하면 예외 발생
        
        # 2. HTML 파싱 (BeautifulSoup 사용)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 3. 모든 <img> 태그 찾기
        img_tags = soup.find_all('img')
        
        # 4. 각 태그에서 src 속성 추출
        for img in img_tags:
            src = img.get('src')
            if src:
                # 5. 상대 경로를 절대 경로로 변환
                # <img src="/images/logo.png">와 같은 상대 경로를 처리하기 위해 필요합니다.
                absolute_url = urljoin(url, src)
                image_list.append(absolute_url)
                
    except requests.exceptions.RequestException as e:
        print(f"\n[오류] 웹 페이지에 접속할 수 없습니다: {e}")
        return None
    except Exception as e:
        print(f"\n[오류] 예상치 못한 오류가 발생했습니다: {e}")
        return None
        
    return image_list

if __name__ == "__main__":
    
    # 1. 사용자로부터 URL 입력 받기
    target_url = input("이미지 리스트를 추출할 웹 페이지 URL을 입력하세요 (예: google.com): ").strip()
    
    if not target_url:
        print("URL이 입력되지 않았습니다. 프로그램을 종료합니다.")
        sys.exit()

    # 2. 이미지 추출 실행
    images = extract_images_from_url(target_url)

    # 3. 결과 출력
    print("\n" + "="*50)
    
    if images is not None:
        print(f"📌 발견된 이미지 요소 개수: {len(images)}개")
        print("--- 추출된 이미지 URL 리스트 ---")
        
        # 최대 10개만 출력 (너무 길어지는 것을 방지)
        for i, img_url in enumerate(images[:10]):
            print(f"{i+1}. {img_url}")

        if len(images) > 10:
            print(f"...\n(총 {len(images)}개의 이미지 URL이 발견되었습니다.)")
    
    print("="*50)
