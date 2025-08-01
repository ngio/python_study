 PyQt5로 만든 초미니 시계 프로그램을 바탕화면에서 .exe 파일로 실행할 수 있도록 변환하는 방법을 알려드릴게요. 이를 위해서는 PyInstaller라는 파이썬 패키지를 사용합니다. PyInstaller는 파이썬 스크립트와 모든 의존성(라이브러리, 데이터 파일 등)을 묶어서 독립 실행 가능한 파일로 만들어 줍니다.


pyinstaller --noconfirm --onefile --windowed "mini_clock_final.py"


dist 폴더로 이동:
파일 탐색기(Windows)나 Finder(macOS)를 열어 dist 폴더로 이동합니다.



