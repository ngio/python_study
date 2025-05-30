import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QFileDialog, QMessageBox, QTextEdit
from PyQt5.QtCore import Qt

class FileSearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle("File Search Tool")
        self.setGeometry(300, 300, 600, 600)

        # 레이아웃 설정
        layout = QVBoxLayout()

        # 디렉토리 선택 버튼
        self.select_dir_button = QPushButton("Select Directory", self)
        self.select_dir_button.clicked.connect(self.select_directory)
        layout.addWidget(self.select_dir_button)

        # 선택된 디렉토리 경로 표시 라벨
        self.dir_label = QLabel("Selected Directory: None", self)
        layout.addWidget(self.dir_label)

        # 검색어 입력 필드
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Enter word to search for...")
        layout.addWidget(self.search_input)

        # 검색 진행 상태 라벨
        self.status_label = QLabel("Status: Waiting for input", self)
        layout.addWidget(self.status_label)

        # 검색 버튼
        self.search_button = QPushButton("Search Files", self)
        self.search_button.clicked.connect(self.start_search)
        layout.addWidget(self.search_button)

        # 검색 종료 버튼
        self.stop_search_button = QPushButton("Stop Search", self)
        self.stop_search_button.clicked.connect(self.stop_search)
        self.stop_search_button.setEnabled(False)  # 검색 중일 때만 활성화
        layout.addWidget(self.stop_search_button)

        # 검색 결과 표시 리스트
        self.result_list = QListWidget(self)
        self.result_list.itemDoubleClicked.connect(self.open_file)  # 더블 클릭 시 파일 열기
        layout.addWidget(self.result_list)

        # 검색된 내용 요약 표시 텍스트 필드
        self.summary_text = QTextEdit(self)
        self.summary_text.setReadOnly(True)
        layout.addWidget(self.summary_text)

        # 메인 레이아웃 설정
        self.setLayout(layout)

        # 선택된 디렉토리 경로 저장 변수와 검색 중 상태 변수
        self.directory = None
        self.searching = False  # 검색 중인지 여부

    def select_directory(self):
        # 디렉토리 선택 다이얼로그 열기
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.directory = directory
            self.dir_label.setText(f"Selected Directory: {directory}")

    def start_search(self):
        # 검색어 가져오기
        search_word = self.search_input.text().strip()
        if not self.directory:
            QMessageBox.warning(self, "No Directory", "Please select a directory first.")
            return
        if not search_word:
            QMessageBox.warning(self, "No Search Term", "Please enter a word to search for.")
            return

        # 검색 상태 초기화
        self.result_list.clear()
        self.summary_text.clear()
        self.searching = True
        self.search_button.setEnabled(False)
        self.stop_search_button.setEnabled(True)
        self.status_label.setText("Status: Searching...")

        # 파일 검색 시작
        self.search_files(search_word)

    def search_files(self, search_word):
        found_files = False
        for root, dirs, files in os.walk(self.directory):
            if not self.searching:  # 중단 요청 시 루프 탈출
                break
            for file in files:
                file_path = os.path.join(root, file)
                
                # 현재 검색 중인 파일 표시
                self.status_label.setText(f"Searching in: {file_path}")
                QApplication.processEvents()  # UI 업데이트를 위해 이벤트 처리

                try:
                    with open(file_path, 'r', encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        if search_word in content:
                            self.result_list.addItem(file_path)
                            found_files = True
                            # 검색된 내용에서 해당 단어가 포함된 첫 번째 문장 요약 추가
                            match_summary = self.extract_summary(content, search_word)
                            self.summary_text.append(f"{file}: {match_summary}\n")
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")

        # 검색 완료 메시지
        if not found_files:
            self.result_list.addItem("No files found containing the specified word.")
        self.status_label.setText("Search complete.")
        self.search_button.setEnabled(True)
        self.stop_search_button.setEnabled(False)

    def stop_search(self):
        self.searching = False
        self.status_label.setText("Status: Search stopped.")
        self.search_button.setEnabled(True)
        self.stop_search_button.setEnabled(False)

    def open_file(self, item):
        # 파일을 기본 프로그램으로 실행
        file_path = item.text()
        if os.path.isfile(file_path):
            try:
                subprocess.Popen(['open', file_path] if sys.platform == 'darwin' else ['xdg-open', file_path] if sys.platform == 'linux' else ['start', file_path], shell=True)
                self.status_label.setText(f"Opened file: {item.text()}")
            except Exception as e:
                self.status_label.setText(f"Could not open file: {e}")

    def extract_summary(self, content, search_word):
        # 검색어가 포함된 첫 번째 문장을 요약으로 추출
        sentences = content.split('.')
        for sentence in sentences:
            if search_word in sentence:
                return sentence.strip() + "."
        return "Summary not available."

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSearchApp()
    window.show()
    sys.exit(app.exec_())
