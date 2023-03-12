과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")
  
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)  

리스트 = [1, 2, 3]
for 변수 in 리스트:
  print("3 x " + str(변수))  
  
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if 변수.isupper():
    print(변수)  

리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for 변수 in 리스트:
  split = 변수.split(".")
  print(split[0])  
