import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt

class FileSearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle("File Search Tool")
        self.setGeometry(300, 300, 600, 500)

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
        found_files = False  # 검색 결과가 있는지 확인
        for root, dirs, files in os.walk(self.directory):
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
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")

        # 검색 완료 메시지
        if not found_files:
            self.result_list.addItem("No files found containing the specified word.")
        self.status_label.setText("Search complete.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSearchApp()
    window.show()
    sys.exit(app.exec_())
