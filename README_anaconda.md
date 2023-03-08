
# 아나콘다 패키지 업데이트

현재 설치된 아나콘다의 버전을 확인해 보겠습니다.
(base) C:\Users\사용자계정>conda -–version


아나콘다를 사용하다 보면 아나콘다 자체 및 부속 라이브러리들을 업데이트 해야 할 일이 생기곤 합니다. 그럴 때에는 다음과 같이 하면 쉽게 전체 업데이트를 할 수 있습니다.
아나콘다 자체를 최신 버전으로 업데이트 하는 명령은 다음과 같습니다.
(base) C:\Users\사용자계정>conda update conda
(base) C:\Users\사용자계정>conda update anaconda
(base) C:\Users\사용자계정>conda update –n base conda


아나콘다의 파이썬 패키지 전체를 업데이트 하는 명령은 다음과 같습니다.
(base) C:\Users\사용자계정>conda update --all



# 아나콘다 파이썬 가상환경 생성

>conda create -n <환경명> python=<버전(ex:3.5이나 3.7 등)>

>conda create -n pyboj python=3.7

# 가상환경 활성화

>conda activate pyboj


# 가상환경 삭제

>conda remove -n pyboj --all


https://sdc-james.gitbook.io/onebook/2./2.1./2.1.1./1

