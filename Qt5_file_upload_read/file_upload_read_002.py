import sys
import os
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit
)


class FileHandlerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle("File Handler App")
        self.setGeometry(100, 100, 800, 600)

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
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select File", "", "All Files (*);;Excel Files (*.xlsx *.xls);;Text Files (*.txt)", options=options
        )

        if file_path:
            # 선택한 파일 경로 표시
            self.file_path_label.setText(f"Selected File: {file_path}")

            # 파일 확장자 확인
            _, file_extension = os.path.splitext(file_path)

            # 파일 처리
            if file_extension in [".xlsx", ".xls"]:
                self.read_excel(file_path)
            elif file_extension == ".txt":
                self.read_text(file_path)
            else:
                self.file_content.setText("Unsupported file type. Please select an Excel or text file.")

    def read_text(self, file_path):
        """텍스트 파일을 읽어와 화면에 표시"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.file_content.setText(content)
        except Exception as e:
            self.file_content.setText(f"Error reading file: {str(e)}")

    def read_excel(self, file_path):
        """엑셀 파일을 읽어와 화면에 표시"""
        try:
            excel_data = pd.ExcelFile(file_path)  # 엑셀 파일 읽기
            content = "Excel File Content:\n\n"

            # 시트별로 데이터 읽기
            for sheet_name in excel_data.sheet_names:
                content += f"Sheet: {sheet_name}\n"
                sheet_data = excel_data.parse(sheet_name).head(10)  # 각 시트의 첫 10행 읽기
                content += sheet_data.to_string(index=False)
                content += "\n\n"

            self.file_content.setText(content)
        except Exception as e:
            self.file_content.setText(f"Error reading Excel file: {str(e)}")


# 프로그램 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileHandlerApp()
    window.show()
    sys.exit(app.exec_())
