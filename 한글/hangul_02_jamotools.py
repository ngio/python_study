# pip install jamotools 
# https://pypi.org/project/jamotools/
# A library for Korean Jamo split and vectorize. 
#
# 음절 분할 및 jamos를 음절에 결합하는 API는 hangul-utils 를 기반으로 합니다 .
# 
# Split_syllables : 음절 문자열을 jamos 문자열로 변환하고 유니코드 유형을 변환하도록 선택할 수 있습니다.
# Join_jamos : jamos 문자열을 음절 문자열로 변환합니다.
# Normalize_to_compat_jamo : jamos 문자열을 한글 호환성 Jamo 문자열로 정규화합니다 .
import jamotools

print(jamotools.split_syllable_char(u"안"))
#('ㅇ', 'ㅏ', 'ㄴ')

print(jamotools.split_syllables(u"안녕하세요"))
# ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ


sentence = u"앞 집 팥죽은 붉은 팥 풋팥죽이고, 뒷집 콩죽은 햇콩 단콩 콩죽.우리 집  깨죽은 검은 깨 깨죽인데 사람들은 햇콩 단콩 콩죽 깨죽 죽먹기를 싫어하더라."
s = jamotools.split_syllables(sentence)
print(s, '\n')

""" ㅇㅏㅍ ㅈㅣㅂ ㅍㅏㅌㅈㅜㄱㅇㅡㄴ ㅂㅜㄺㅇㅡㄴ ㅍㅏㅌ ㅍㅜㅅㅍㅏㅌㅈㅜㄱㅇㅣㄱㅗ,
ㄷㅟㅅㅈㅣㅂ ㅋㅗㅇㅈㅜㄱㅇㅡㄴ ㅎㅐㅅㅋㅗㅇ ㄷㅏㄴㅋㅗㅇ ㅋㅗㅇㅈㅜㄱ.ㅇㅜㄹㅣ
ㅈㅣㅂ ㄲㅐㅈㅜㄱㅇㅡㄴ ㄱㅓㅁㅇㅡㄴ ㄲㅐ ㄲㅐㅈㅜㄱㅇㅣㄴㄷㅔ ㅅㅏㄹㅏㅁㄷㅡㄹㅇㅡㄴ
ㅎㅐㅅㅋㅗㅇ ㄷㅏㄴㅋㅗㅇ ㅋㅗㅇㅈㅜㄱ ㄲㅐㅈㅜㄱ ㅈㅜㄱㅁㅓㄱㄱㅣㄹㅡㄹ
ㅅㅣㅀㅇㅓㅎㅏㄷㅓㄹㅏ. """

sentence2 = jamotools.join_jamos(s)
print(sentence2)
""" 앞 집 팥죽은 붉은 팥 풋팥죽이고, 뒷집 콩죽은 햇콩 단콩 콩죽.우리 집 깨죽은 검은 깨
깨죽인데 사람들은 햇콩 단콩 콩죽 깨죽 죽먹기를 싫어하더라. """

print(sentence == sentence2)
# True


# 자음만 추출
def extract_vowels(text):
    vowels = set(['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅐ', 'ㅒ', 'ㅔ', 'ㅖ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ'])
    result = ''
    for char in text:
        if '가' <= char <= '힣':  # Check if the character is Hangul
            syllables = jamotools.split_syllables(char)
            for syllable in syllables:
                if syllable in vowels:
                    result += syllable
    return result

sentence = u"앞 집 팥죽은 붉은 팥 풋팥죽이고, 뒷집 콩죽은 햇콩 단콩 콩죽.우리 집  깨죽은 검은 깨 깨죽인데 사람들은 햇콩 단콩 콩죽 깨죽 죽먹기를 싫어하더라."
vowels_only = extract_vowels(sentence)
print(vowels_only)
# ㅏㅣㅏㅜㅡㅜㅡㅏㅜㅏㅜㅣㅗㅟㅣㅗㅜㅡㅐㅗㅏㅗㅗㅜㅜㅣㅣㅐㅜㅡㅓㅡㅐㅐㅜㅣㅔㅏㅏㅡㅡㅐㅗㅏㅗㅗㅜㅐㅜㅜㅓㅣㅡㅣㅓㅏㅓㅏ


# 모음만 추출 
def extract_consonants(text):
    consonants = set(['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'])
    result = ''
    for char in text:
        if '가' <= char <= '힣':  # Check if the character is Hangul
            syllables = jamotools.split_syllables(char)
            for syllable in syllables:
                if syllable in consonants:
                    result += syllable
    return result

sentence = u"앞 집 팥죽은 붉은 팥 풋팥죽이고, 뒷집 콩죽은 햇콩 단콩 콩죽.우리 집  깨죽은 검은 깨 깨죽인데 사람들은 햇콩 단콩 콩죽 깨죽 죽먹기를 싫어하더라."
consonants_only = extract_consonants(sentence)
print(consonants_only)
# ㅇㅍㅈㅂㅍㅌㅈㄱㅇㄴㅂㅇㄴㅍㅌㅍㅅㅍㅌㅈㄱㅇㄱㄷㅅㅈㅂㅋㅇㅈㄱㅇㄴㅎㅅㅋㅇㄷㄴㅋㅇㅋㅇㅈㄱㅇㄹㅈㅂㄲㅈㄱㅇㄴㄱㅁㅇㄴㄲㄲㅈㄱㅇㄴㄷㅅㄹㅁㄷㄹㅇㄴㅎㅅㅋㅇㄷㄴㅋㅇㅋㅇㅈㄱㄲㅈㄱㅈㄱㅁㄱㄱㄹㄹㅅㅇㅎㄷㄹ


# 초성만 추출 


