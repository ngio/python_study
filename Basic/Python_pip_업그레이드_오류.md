
Python pip 업그레이드 오류

    C:\ProgramData\anaconda3\python.exe -m pip install --upgrade pip



    ValueError: Unable to find resource t64.exe in package pip._vendor.distlib

Python 3.x에서도 pip을 업그레이드할 때 오류가 발생하는 경우가 있다. 이런 경우에는 다음과 같이 upgrade하라는 말만 앵무새처럼 반복하게 된다.

그럴 때에는 get-pip.py 파일을 받아서 실행하면 된다. get-pip.py는 다음 URL에서 받을 수 있는데, 그냥 누르면 파일 내용이 열리므로 마우스 우클릭 후 "다른 이름으로 링크 저장..." 메뉴를 선택하여 get-pip.py란 이름으로 저장한다.

https://bootstrap.pypa.io/get-pip.py

get-pip.py를 받은 후에는 저장된 폴더를 열고 그 폴더에서 Shift-우클릭을 통해 명령 프롬프트를 연 다음 일반 Python 프로그램처럼 이를 실행해 준다.


출처: https://woogyun.tistory.com/698 [살아가는 이야기:티스토리]

