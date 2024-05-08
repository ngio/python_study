Python에서 문자열을 포맷하는 방법은 다양하게 제공됩니다. 각각의 방법은 특정한 상황에 맞게 선택하여 사용할 수 있습니다. 주요한 문자열 포맷 방법에 대해 알아보겠습니다.

1. % 포맷팅 (Old Style)
% 연산자를 사용하여 문자열 포맷팅을 수행하는 방식으로, C 언어의 printf 함수와 유사합니다. % 기호 뒤에 포맷 문자열을 사용하여 변수 값을 문자열에 삽입할 수 있습니다.

       name = "Alice"
       age = 30
       formatted_string = "Name: %s, Age: %d" % (name, age)
       print(formatted_string)
      
      %s: 문자열(string)
      %d: 정수(integer)
      %f: 부동소수점수(float)
      %x, %X: 16진수(hexadecimal)

2. str.format() 메서드 (str.format() Method)
str.format() 메서드를 사용하여 문자열을 포맷할 수 있습니다. 중괄호 {} 안에 인덱스나 변수명을 넣어 값을 삽입할 수 있습니다.

       name = "Bob"
       age = 25
       formatted_string = "Name: {}, Age: {}".format(name, age)
       print(formatted_string)

위치 인덱스를 사용한 포맷팅: "Name: {0}, Age: {1}".format(name, age)
변수명을 사용한 포맷팅: "Name: {name}, Age: {age}".format(name=name, age=age)

3. f-문자열 (f-Strings, Formatted String Literals)
Python 3.6부터 도입된 f-문자열은 가독성과 사용 편의성을 제공합니다. 문자열 앞에 f 또는 F를 붙여 사용하며, 중괄호 {} 안에 변수나 표현식을 사용하여 값을 삽입할 수 있습니다.

 
       name = "Charlie"
       age = 35
       formatted_string = f"Name: {name}, Age: {age}"
       print(formatted_string)

변수 및 표현식 사용: f"Age next year: {age + 1}"

4. Template 문자열 (string.Template)
string.Template 클래스를 사용하여 간단한 문자열 템플릿을 만들고 치환할 수 있습니다.

 
       from string import Template
    
       name = "David"
       age = 40
       template = Template("Name: $name, Age: $age")
       formatted_string = template.substitute(name=name, age=age)
       print(formatted_string)

선택적 포맷 지정
각 포맷 방법은 다양한 선택적 옵션을 제공합니다. 예를 들어, 소수점 이하 자릿수, 정렬, 공백 채우기 등의 옵션을 사용할 수 있습니다.
 
    # 소수점 이하 자릿수 지정
    pi = 3.14159
    formatted_pi = f"Pi value: {pi:.2f}"  # 소수점 이하 2자리까지 표시
    print(formatted_pi)

    # 정렬과 공백 채우기
    message = "Hello"
    formatted_message = f"{message:>10}"  # 우측 정렬, 전체 너비 10
    print(formatted_message)

이러한 방식들을 조합하여 다양한 문자열 포맷팅을 수행할 수 있습니다. 각 방법은 문법적인 차이와 사용 편의성 측면에서 장단점이 있으므로 상황에 맞게 선택하여 사용하시면 됩니다. Python의 버전에 따라 f-문자열을 사용할 수 있는지 확인하고, 자주 사용하는 방법을 익숙하게 활용하세요.
