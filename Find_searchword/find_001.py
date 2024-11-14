import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QFileDialog, QMessageBox

class FileSearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle("File Search Tool")
        self.setGeometry(300, 300, 600, 400)

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

        # 검색 버튼
        self.search_button = QPushButton("Search Files", self)
        self.search_button.clicked.connect(self.search_files)
        layout.addWidget(self.search_button)

        # 검색 결과 표시 리스트
        self.result_list = QListWidget(self)
        layout.addWidget(self.result_list)

        # 메인 레이아웃 설정
        self.setLayout(layout)

        # 선택된 디렉토리 경로 저장 변수
        self.directory = None

    def select_directory(self):
        # 디렉토리 선택 다이얼로그 열기
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.directory = directory
            self.dir_label.setText(f"Selected Directory: {directory}")

    def search_files(self):
        # 검색어 가져오기
        search_word = self.search_input.text().strip()
        if not self.directory:
            QMessageBox.warning(self, "No Directory", "Please select a directory first.")
            return
        if not search_word:
            QMessageBox.warning(self, "No Search Term", "Please enter a word to search for.")
            return

        # 검색어가 포함된 파일 검색
        self.result_list.clear()
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        if search_word in content:
                            self.result_list.addItem(file_path)
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")

        # 검색 결과가 없는 경우 메시지 표시
        if self.result_list.count() == 0:
            self.result_list.addItem("No files found containing the specified word.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSearchApp()
    window.show()
    sys.exit(app.exec_())
