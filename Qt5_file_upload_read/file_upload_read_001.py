"""
파일 선택 창을 띄워 파일을 선택하고, 선택한 파일을 읽어서 내용을 출력하는 PyQt5 프로그램입니다. 
파일 선택 창은 QFileDialog를 사용합니다.
"""

# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit


class FileHandlerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle("File Handler App")
        self.setGeometry(100, 100, 600, 400)

        # 레이아웃 설정
        layout = QVBoxLayout()

        # 파일 선택 버튼
        self.select_button = QPushButton("Select File", self)
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        # 파일 경로 표시
        self.file_path_label = QLabel("No file selected", self)
        layout.addWidget(self.file_path_label)

        # 파일 내용 표시
        self.file_content = QTextEdit(self)
        self.file_content.setReadOnly(True)
        layout.addWidget(self.file_content)

        # 레이아웃 적용
        self.setLayout(layout)

    def select_file(self):
        # 파일 선택 창 띄우기
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*);;Text Files (*.txt)", options=options)

        if file_path:
            # 선택한 파일 경로 표시
            self.file_path_label.setText(f"Selected File: {file_path}")

            # 파일 내용 읽기
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.file_content.setText(content)  # 내용 표시
            except Exception as e:
                self.file_content.setText(f"Error reading file: {str(e)}")


# 프로그램 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileHandlerApp()
    window.show()
    sys.exit(app.exec_())
