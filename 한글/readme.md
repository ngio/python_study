한글 관련

한글 자음모음 추출


https://pypi.org/project/jamo/

    pip install jamo
    
    jamo 0.4.1

Github : https://github.com/jdongian/python-jamo


    Python-jamo는 한글 문자 및 jamo 작업을 위한 Python 한글 음절 분해 및 합성 라이브러리입니다.
    
    현재 베타 릴리스에서는 함수 이름이 변경될 수 있지만 Unicode 7.0에서는 거의 모든 한글 관련 코드 포인트가 적용됩니다.
    
    원래 학생들이 (ㅔ,ㅐ) 또는 (ㅗ,ㅜㅜ)가 포함된 철자하기 어려운 단어를 식별할 수 있도록 돕기 위해 고안된 이 프로젝트는 한국어 음성 및 철자 분석의 틈새를 채우고자 합니다.


---

pip install jamotools

https://pypi.org/project/jamotools/

A library for Korean Jamo split and vectorize.  한국어 Jamo를 분할하고 벡터화하는 라이브러리입니다.

![image](https://github.com/ngio/python_study/assets/3784942/b2b6cd18-3344-405d-89b2-570663f2addc)

API for split syllables and join jamos to syllable is based on hangul-utils.

    split_syllables: Converts a string of syllables to a string of jamos, can be select which convert unicode type.    
    join_jamos: Converts a string of jamos to a string of syllables.    
    normalize_to_compat_jamo: Normalize a string of jamos to a string of Hangul Compatibility Jamo.

음절 분할 및 jamos를 음절에 결합하는 API는 hangul-utils 를 기반으로 합니다 .

    Split_syllables : 음절 문자열을 jamos 문자열로 변환하고 유니코드 유형을 변환하도록 선택할 수 있습니다.
    Join_jamos : jamos 문자열을 음절 문자열로 변환합니다.
    Normalize_to_compat_jamo : jamos 문자열을 한글 호환성 Jamo 문자열로 정규화합니다 .

.
