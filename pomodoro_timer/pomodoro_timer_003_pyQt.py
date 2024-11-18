"""_summary_
    PyQt를 사용하여 Pomodoro 타이머와 거북이 애니메이션을 구현한 코드입니다. 이 프로그램은 다음 기능을 포함합니다:

    원 위를 따라 움직이는 거북이: 25분 동안 원을 따라 거북이가 한 바퀴 돕니다.
    Start/Stop 버튼: 타이머와 애니메이션을 시작하고 중지할 수 있습니다.
    PyQt5와 QTimer 활용: QTimer를 사용하여 애니메이션과 시간을 제어합니다.
"""

import sys
import math
from PyQt5.QtCore import QTimer, Qt, QPointF
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QPen, QBrush, QFont

class PomodoroApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # Timer and Animation parameters
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.time_elapsed = 0
        self.total_time = 25 * 60  # 25 minutes in seconds
        self.running = False

    def initUI(self):
        # Window setup
        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(100, 100, 400, 500)
        
        # Layout and widgets
        self.layout = QVBoxLayout()
        
        # Circle animation area
        self.label = QLabel(self)
        self.label.setFixedSize(400, 400)
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # Start button
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_button, alignment=Qt.AlignCenter)

        # Stop button
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_timer)
        self.layout.addWidget(self.stop_button, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.timer.start(1000)  # Update every second

    def stop_timer(self):
        if self.running:
            self.running = False
            self.timer.stop()
            self.time_elapsed = 0  # Reset time
            self.update()

    def update_animation(self):
        if self.running:
            self.time_elapsed += 1
            if self.time_elapsed >= self.total_time:
                self.stop_timer()
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw circle
        center = QPointF(self.width() / 2, 200)  # Center of the circle
        radius = 150
        painter.setPen(QPen(Qt.black, 2))
        painter.drawEllipse(center, radius, radius)
        
        # Calculate turtle position
        if self.running:
            progress = self.time_elapsed / self.total_time
            angle = -progress * 2 * math.pi  # Negative for clockwise movement
            x = center.x() + radius * math.cos(angle)
            y = center.y() - radius * math.sin(angle)
            
            # Draw turtle
            painter.setBrush(QBrush(Qt.green))
            painter.drawEllipse(QPointF(x, y), 10, 10)  # Turtle as a small circle

        # Draw timer text in the center
        remaining_time = max(0, self.total_time - self.time_elapsed)
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_text = f"{minutes:02}:{seconds:02}"

        # Center the text
        painter.setFont(QFont("Arial", 24, QFont.Bold))
        painter.setPen(Qt.black)
        text_rect = self.rect()
        text_rect.setTop(150)  # Adjust top to align with the circle center
        text_rect.setHeight(100)  # Define height for central text placement
        painter.drawText(text_rect, Qt.AlignCenter, timer_text)

        # Draw static turtle if stopped
        if not self.running and self.time_elapsed == 0:
            painter.setBrush(QBrush(Qt.red))
            painter.drawEllipse(center, 10, 10)  # Turtle at the starting point


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PomodoroApp()
    window.show()
    sys.exit(app.exec_())
