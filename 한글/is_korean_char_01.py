""" 한글 자음인지 확인 
"""
# Define the list of Korean initial consonants (초성)
INITIAL_CONSONANTS = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 
    'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 
    'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

def is_korean_char(ch):
    """Check if the character is a Korean syllable."""
    return 0xAC00 <= ord(ch) <= 0xD7A3

def get_initial_consonant(ch):
    """Extract the initial consonant from a Korean syllable."""
    if not is_korean_char(ch):
        return None  # or you could return an empty string or raise an exception
    
    # Calculate the index for the initial consonant
    initial_index = (ord(ch) - 0xAC00) // (21 * 28)
    return INITIAL_CONSONANTS[initial_index]

# Example usage
sentence = "안녕하세요"
initials = [get_initial_consonant(ch) for ch in sentence if is_korean_char(ch)]
print(''.join(initials))  # Output: ㅇㄴㅎㅅㅇ
