 실행파일 만들기 (PyInstaller)  https://wikidocs.net/21952#_1

PyInstaller Manual

요구 사항이 설치되어 있는지 확인한 다음 PyPI에서 PyInstaller를 설치합니다.

> pip install -U pyinstaller

명령 프롬프트/셸 창을 열고 .py 파일이 있는 디렉터리로 이동한 후 다음 명령을 사용하여 앱을 빌드합니다.

> pyinstaller your_program.py


요구 사항


윈도우

PyInstaller는 Windows 8 이상에서 실행됩니다. 그래픽 창 앱(명령 창이 필요하지 않은 앱)을 만들 수 있습니다.

맥 OS

PyInstaller는 macOS 10.15(Catalina) 이상에서 실행됩니다. 그래픽 창 앱(터미널 창을 사용하지 않는 앱)을 빌드할 수 있습니다. 
PyInstaller는 실행하는 macOS 릴리스 및 후속 릴리스와 호환되는 앱을 빌드합니다. 두 아키텍처 중 하나의 macOS 시스템에서 또는 하이브리드 범용 2 바이너리를 x86_64빌드 arm64할 수 있습니다 .
자세한 내용은 macOS 다중 아키텍처 지원을 참조하세요 .






 
