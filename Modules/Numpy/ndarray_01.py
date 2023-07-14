# https://wikidocs.net/14606
import numpy as np

print("x는 float64를 요소타입으로 갖는 크기 3의 1차원 배열이다.")
x = np.array((0.1,0.2,0.3))
print(x)
print(x.shape)  # 차원 : 1자원 배열의 shape는 (m,)
print(x.dtype) # 요소 타입 : float64

print("y는 int32를 요소 타입으로 하는 (2,3) 크기의 2차원 배열이다.")
y = np.array(((1,2,3),(4,5,6)))
print(y)
print(y.shape)  # 차원 : 2자원 배열의 shape는 (m,n)  3차원은 (p,q,r)
print(y.dtype) # 요소 타입 : int32

print("생성시 입력된 값을 통해 dtype을 추천하는데, 강제로 지정하는 것은 다음과 같다.")
z = np.array([1,2,3],dtype='float64')
print(z)
print(z.shape)
print(z.dtype)

"""_summary_
ndarray의 중요 속성을 정리하면 다음과 같다.

shape : 배열의 형태
dtype : 요소의 데이터 타입, int32, float32 등등
ndim : 차원수. x.ndim = 1, y.ndim=2 등이며 len(x.shape) 와 동일
size : 요소의 개수. shape의 모든 값의 곱. x.size = 3, y.size=6 등
itemsize : 요소 데이터 타입의 크기(byte 단위), x.itemsize=8 등
data : 실제 데이터. 직접 사용자가 접근할 필요는 없음
"""

print("초기화 관련 편의함수")
Y = np.zeros((3,3))
print(Y)
Y = np.ones((3,3),dtype='int32')
Z = np.empty((3,3))

print("\n미리 크기지정없이 순차적으로 만들때, 크기 0인 배열을 생성하고 append()를 수행")
A = np.array([])
for i in range(3):
    A = np.append(A,[1,2,3])

print(A)

print("단순한 시퀀스는 range() 함수의 실수버전인 arange(from,to,step)이나 \nlinspace(from,to,npoints)를 사용하면 편리하다. \n또한 단위행렬을 위한 eye(n) 함수를 제공한다.")
print(np.arange(1,2,0.1))
#array([ 1. ,  1.1,  1.2,  1.3,  1.4,  1.5,  1.6,  1.7,  1.8,  1.9])
print(np.arange(10))   # start, step 생략가능. 정수로 생성
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np.arange(10.))  # start, step 생략가능. 실수로 생성
#array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
print(np.linspace(0.,20.,11))
#array([  0.,   2.,   4., ...,  16.,  18.,  20.])
print(np.eye(3))
#array([[ 1.,  0.,  0.],
#       [ 0.,  1.,  0.],
#       [ 0.,  0.,  1.]])

print("\n\nshape과 dtype 변경")
msg = "ndarray는 고정된 크기를 유지하면서 shape을 변경할 수 있다. 예를 들어 크기 9의 1차원 배열을 3*3 2차원 배열로 바꿀 수 있다. \n이때 사용하는 함수는 reshape() 인데 함수 또는 메쏘드 형태로 제공한다."
print(msg)

X = np.arange(0,9,1.)
print(X)
Y = np.reshape(X,(3,3)) # 또는 Y=X.reshape((3,3))
print(Y)

#만약 자기 자신을 대상을 변경하면 shape 속성을 강제로 변경하면 된다.
X.shape = (3,3)
print(X)

print("astype() 메쏘드를 사용하면 배열에서 dtype을 바꿀 수 있다.")

a = np.arange(3);
a.astype(int)  # a.astype('int34') 와 동일
a.astype('int34') 
a.astype('int64')
a.astype(float)    # a.astype('float64')
a.astype('float32')
a.astype('float64')
print(a)







