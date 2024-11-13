
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QScrollArea, QMessageBox
import yt_dlp
import threading
from moviepy.editor import AudioFileClip
 
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle("YouTube Downloader & MP4 to MP3 Converter")
        self.setGeometry(300, 300, 600, 400)

        # 메인 레이아웃 설정
        self.main_layout = QVBoxLayout()

        # 버튼 레이아웃 (좌에서 우로 배치)
        button_layout = QHBoxLayout()

        # 버튼 1: YouTube URL 다운로드 버튼
        self.youtube_button = QPushButton("Download YouTube Video", self)
        self.youtube_button.clicked.connect(self.show_youtube_download_form)
        button_layout.addWidget(self.youtube_button)

        # 버튼 2: MP4 to MP3 변환 버튼
        self.convert_button = QPushButton("Convert MP4 to MP3", self)
        self.convert_button.clicked.connect(self.confirm_convert_form)  # 확인 창 함수 연결
        button_layout.addWidget(self.convert_button) 

        # 버튼 3: Downloads 폴더의 파일 리스트 보기 버튼
        self.show_files_button = QPushButton("Show Downloaded Files", self)
        self.show_files_button.clicked.connect(self.show_downloaded_files)
        button_layout.addWidget(self.show_files_button)

        # 버튼 레이아웃 추가
        self.main_layout.addLayout(button_layout)

        # YouTube URL 입력 필드 (초기에는 숨김)
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter YouTube URL here...")
        self.url_input.setVisible(False)  # 초기에는 숨김
        self.main_layout.addWidget(self.url_input)

        # 상태 및 결과 표시 레이블 (스크롤 가능)
        self.result_label = QLabel(self)
        self.result_label.setWordWrap(True)
        
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.result_label)
        self.main_layout.addWidget(scroll_area)

        # 메인 레이아웃 설정
        self.setLayout(self.main_layout)

    def show_youtube_download_form(self):
        # 입력 필드가 이미 있는지 확인 후 없을 때만 추가
        # 입력 필드를 보이도록 설정하고, 플레이스홀더 텍스트 설정
        self.url_input.setVisible(True)
        self.url_input.setPlaceholderText("Enter YouTube URL here...")
        self.url_input.clear()  # 이전 입력값 지우기
        self.result_label.setText("Enter a YouTube URL to download:") 

    def download_video(self):
        url = self.url_input.text().strip()
        if url:
            self.result_label.setText("Downloading... Please wait.")
            threading.Thread(target=self.youtube_download_process, args=(url,)).start()
        else:
            self.result_label.setText("Please enter a valid YouTube URL.")

    def youtube_download_process(self, url):
        ydl_opts = {
            'format': 'best',
            'outtmpl': './downloads/%(title)s.%(ext)s',
            'progress_hooks': [self.progress_hook]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d['_percent_str']
            speed = d.get('speed', 'Unknown')
            eta = d.get('eta', 'Unknown')
            self.result_label.setText(f"Downloading: {percent} - Speed: {speed} - ETA: {eta}s")
        elif d['status'] == 'finished':
            self.result_label.setText(f"Download complete!")

    def confirm_convert_form(self):
        # 확인/취소 메시지 박스를 생성
        reply = QMessageBox.question(self, 'Convert MP4 to MP3',
                                     "Are you sure you want to convert all MP4 files in the folder to MP3?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # 사용자가 Yes를 선택한 경우에만 변환 함수 실행
        if reply == QMessageBox.Yes:
            self.show_convert_form()

    def show_convert_form(self):
        # URL 입력창 숨김
        self.url_input.setVisible(False)
        
        # MP4 파일 선택 및 MP3로 변환 메시지 설정
        self.result_label.setText("Converting all MP4 files in the folder to MP3...")
        threading.Thread(target=self.convert_mp4_to_mp3).start()

    def convert_mp4_to_mp3(self):
        folder_path = './downloads'  # MP4 파일이 있는 폴더
         
        for filename in os.listdir(folder_path):
            if filename.endswith(".mp4"):
                mp4_path = os.path.join(folder_path, filename)
                mp3_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.mp3")
                
                if os.path.exists(mp3_path):
                    self.result_label.setText(self.result_label.text() + f"\nSkipping {filename}: MP3 already exists.")
                    continue

                audio_clip = AudioFileClip(mp4_path)
                audio_clip.write_audiofile(mp3_path)
                audio_clip.close()
                self.result_label.setText(self.result_label.text() + f"\nConverted: {filename} to MP3.")

        self.result_label.setText(self.result_label.text() + "\nAll MP4 files converted to MP3.")

    def show_downloaded_files(self):
        # URL 입력창 숨김
        self.url_input.setVisible(False)
        
        # ./downloads 폴더의 파일 리스트를 표시
        folder_path = './downloads'
        if not os.path.exists(folder_path):
            self.result_label.setText("No files found. The downloads folder does not exist.")
            return

        files = os.listdir(folder_path)
        if files:
            file_list = "\n".join(files)
            self.result_label.setText(f"Files in {folder_path}:\n{file_list}")
        else:
            self.result_label.setText("No files found in the downloads folder.")



# PyQt 애플리케이션 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
