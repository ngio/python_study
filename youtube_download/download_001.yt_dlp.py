
import yt_dlp

def main():
    # 다운로드할 YouTube 비디오의 URL
    #url = 'https://www.youtube.com/watch?v=vjcuQLjSUz4'
    
    # 사용자로부터 YouTube 비디오 URL 입력받기
    url = input("다운로드할 YouTube 비디오의 URL을 입력하세요: ")

    # 다운로드 옵션 설정
    ydl_opts = {
        'format': 'best',                   # 최고 화질 선택 (audio와 video 포함)
        'outtmpl': './downloads/%(title)s.%(ext)s',  # 다운로드 파일 경로 및 이름 템플릿
    }

    # yt-dlp를 사용하여 다운로드
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Video has been downloaded successfully!")


# 메인 함수 호출
if __name__ == "__main__":
    main()

