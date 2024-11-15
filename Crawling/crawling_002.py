import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QTextBrowser, QTextEdit
from PyQt5.QtCore import Qt

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
        
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.fetch_web_content)
        layout.addWidget(self.submit_button)
        
        # HTML 내용 표시 (링크 지원을 위해 QTextBrowser 사용)
        self.html_label = QLabel("Page HTML Content:")
        layout.addWidget(self.html_label)
        
        self.html_content = QTextBrowser(self)
        self.html_content.setOpenExternalLinks(False)  # QTextBrowser 내부에서 링크 클릭 이벤트를 처리
        self.html_content.anchorClicked.connect(self.handle_link_click)
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
            self.html_content.setHtml(html_text)
            
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

    def handle_link_click(self, url):
        # 링크를 클릭하면 URL 입력창에 설정하고 자동으로 Submit
        self.url_input.setText(url.toString())
        self.fetch_web_content()

# 애플리케이션 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebCrawlerApp()
    window.show()
    sys.exit(app.exec_())
