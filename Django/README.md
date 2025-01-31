
djangorestframework 3.14.0

![image](https://github.com/ngio/python_study/assets/3784942/f5257c7d-b6a9-4b65-98c2-b62aa50d6321)
 

https://www.django-rest-framework.org/



*** 참고 : https://towardsdatascience.com/designing-and-deploying-a-machine-learning-python-application-part-2-99eb37787b2b

[https://pypi.org/project/djangorestframework/](https://pypi.org/project/djangorestframework/)

pip install djangorestframework


Requirements
Python 3.6+
Django 4.1, 4.0, 3.2, 3.1, 3.0
We highly recommend and only officially support the latest patch release of each Python and Django series.

Installation
Install using pip...

    pip install djangorestframework
    
Add 'rest_framework' to your INSTALLED_APPS setting.

    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]


# 마이그레이션 

    터미널에서 장고 프로젝트 디렉토리인 mysite 로 이동 합니다.
    
    (.conda) (c:\dev\django\.conda) C:\dev\django>cd mysite
    
    터미널에서 python manage.py makemigrations 라는 명령어를 실행합니다.
    
    (.conda) (c:\dev\django\.conda) C:\dev\django\mysite>python manage.py makemigrations
    
    터미널에서 python manage.py migrate 라는 명령어를 실행합니다.
    
    (.conda) (c:\dev\django\.conda) C:\dev\django\mysite>python manage.py migrate

    

![image](https://github.com/user-attachments/assets/f7540752-1fe1-4367-8387-99233741684c)


# [Python] 서버 실행

## http://127.0.0.1:8000/

    터미널에서 장고 프로젝트 디렉토리인 mysite 로 이동 합니다.
    
    (.conda) (c:\dev\django\.conda) C:\dev\django>cd mysite
    
    터미널에서 mysite 디렉터리로 이동 후 python manage.py runserver 라는 명령어를 실행합니다.
    
    (.conda) (c:\dev\django\.conda) C:\dev\django\mysite>python manage.py runserver
    
    서버가 정상적으로 실행되었다면 웹브라우저를 이용하여 http://127.0.0.1:8000/ 에 접속합니다.

![image](https://github.com/user-attachments/assets/420d25cd-db65-40cc-ae07-0b62e22ed6dc)





.

    
