"""
몇 줄의 Python 코드로 멋진 그림을 그리고 싶습니까? SketchPy가 도와드리겠습니다. 
이 글에서는 스케치파이가 무엇인지, 컴퓨터에서 파이썬으로 그림을 그리는 데 어떻게 활용할 수 있는지 알아보자.

https://pypi.org/project/sketchpy/

    Install
    
        pip install sketchpy
        
    it should probably work, If not then try the following code

        pip install turtle open-cv wheel sketchpy
  
  
"""



# Example
from sketchpy import library as lib
obj = lib.rdj()
obj.draw()


from sketchpy import library
myObject = library.tom_holland()
myObject.draw()


from sketchpy import library
myObject = library.ironman_ascii()
myObject.draw()



