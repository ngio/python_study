kivy

크로스 플랫폼 사용자 인터페이스의 신속한 개발을 위한 오픈 소스 파이썬 라이브러리다. 
키비 응용 프로그램을 사용하면 리눅스, 윈도우에 사용하는 GUI 프로그램뿐 아니라 안드로이드, IOS 용도로 개발할 수 있다. 

https://wikidocs.net/book/8263

https://kivy.org/

https://kivy.org/doc/stable/gettingstarted/intro.html





# pip install kivy


from kivy.app import App
from kivy.uix.button import Button

class YourApp(App):
    def build(self):
        return Button(text="Hello, Kivy!")

if __name__ == '__main__':
    YourApp().run()


====================================================================================================


## Kivy 개발 환경 설정

# conda에서 파이썬 가상 환경 (virtual environments) 생성하기

conda create -n kivy_env python=3.11

conda env list

# conda environments:
#
base                   C:\ProgramData\anaconda3
kivy_env               D:\Users\wani\.conda\envs\kivy_env
py_test              * D:\Users\wani\.conda\envs\py_test

 conda activate kivy_env

(py_test) PS D:\_py_kivy> conda activate kivy_env
(kivy_env) PS D:\_py_kivy>

# Kivy 설치
pip install kivy


# Python 코드를 안드로이드 폰에서 실행하려면 Buildozer를 사용하여 APK 파일을 생성해야 합니다.
pip install buildozer

