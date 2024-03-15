# [python] 한글 자음 모음 분리하기 
# https://pypi.org/project/jamo/

from jamo import h2j, j2hcj

sample_text = "가나다한글"

output_txt = j2hcj(h2j(sample_text))


print(output_txt)
# 'ㄱㅏㄴㅏㄷㅏㅎㅏㄴㄱㅡㄹ'

# 11172개의 모든 한국어 음절을 19 x 21 x 28 크기의 넘파이 배열로 만드는 코드
import numpy as np
syllables = np.array([chr(code) for code in range(44032, 55204)])
syllables = syllables.reshape(19, 21, 28)

output_txt = chr(44032) #  유니코드 번호를 받아서 해당하는 문자를 반환하는 함수
print(output_txt)
# 가

output_txt = ord('가') # 문자를 받아서 대응하는 유니코드 번호를 반환
print(output_txt)
# 44032

sample_text = "쉟"
output_txt = j2hcj(h2j(sample_text))
print(output_txt)
# 'ㅅㅞㅀ'



