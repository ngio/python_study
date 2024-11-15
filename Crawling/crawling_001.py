"""_summary_
주요 구성 요소
    URL 입력창 및 제출 버튼: URL을 입력하고 제출하여 페이지의 내용을 가져옵니다.
    HTML 내용 표시: 입력된 URL의 전체 HTML 소스가 표시됩니다.
    크롤링된 내용 표시: BeautifulSoup를 사용하여 <p> 태그의 텍스트 내용을 크롤링해 표시합니다.
추가 기능
    원하는 다른 태그를 크롤링하거나 세부 내용을 보여주려면 fetch_web_content 함수에서 soup.find_all() 등을 사용하여 다른 요소로 조정할 수 있습니다.
"""
import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QTextEdit

class WebCrawlerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 창 설정
        self.setWindowTitle("URL Web Crawler")
        self.setGeometry(300, 300, 800, 600)
        
        # 메인 레이아웃 설정
        layout = QVBoxLayout()

        # URL 입력창 및 버튼 추가
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter URL here...")
        layout.addWidget(self.url_input)
        
        self.submit_button = QPushButton("수집하라~~~", self)
        self.submit_button.clicked.connect(self.fetch_web_content)
        layout.addWidget(self.submit_button)
        
        # 원본 HTML 내용을 보여줄 스크롤 가능한 텍스트 창
        self.html_label = QLabel("Page HTML Content:")
        layout.addWidget(self.html_label)
        
        self.html_content = QTextEdit(self)
        self.html_content.setReadOnly(True)
        html_scroll = QScrollArea(self)
        html_scroll.setWidgetResizable(True)
        html_scroll.setWidget(self.html_content)
        layout.addWidget(html_scroll)

        # 크롤링된 내용을 보여줄 텍스트 창
        self.crawl_label = QLabel("Crawled Data:")
        layout.addWidget(self.crawl_label)
        
        self.crawled_content = QTextEdit(self)
        self.crawled_content.setReadOnly(True)
        crawl_scroll = QScrollArea(self)
        crawl_scroll.setWidgetResizable(True)
        crawl_scroll.setWidget(self.crawled_content)
        layout.addWidget(crawl_scroll)
        
        # 레이아웃 설정
        self.setLayout(layout)

    def fetch_web_content(self):
        # URL 가져오기
        url = self.url_input.text().strip()
        if not url:
            self.html_content.setText("Please enter a valid URL.")
            return
        
        try:
            # 웹 페이지 요청 및 파싱
            response = requests.get(url)
            response.raise_for_status()
            html_text = response.text
            
            # HTML 내용을 보여줌
            self.html_content.setText(html_text)
            
            # BeautifulSoup으로 HTML 파싱
            soup = BeautifulSoup(html_text, 'html.parser')
            
            # 특정 태그 내용 크롤링 예시 (모든 <p> 태그 내용)
            paragraphs = soup.find_all('p')
            crawled_data = "\n\n".join([p.get_text(strip=True) for p in paragraphs])
            
            # 크롤링된 내용 표시
            if crawled_data:
                self.crawled_content.setText(crawled_data)
            else:
                self.crawled_content.setText("No <p> tags found on the page.")

        except requests.exceptions.RequestException as e:
            self.html_content.setText(f"Error fetching the URL: {e}")
            self.crawled_content.setText("")

# 애플리케이션 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebCrawlerApp()
    window.show()
    sys.exit(app.exec_())
