

# https://wikidocs.net/15213
# gTTS : Google Text to Speech API : Google에서 제공하는 TTS 서비스. gTTS라는 모듈을 인스톨해야 함
"""
    'en'으로 지정했을 때 한글이 text에 포함되어 있으면 이를 무시하지만, 'ko'일때 text내의 영문은 무시되지 않고 음성합성을 수행한다(아주 이상함)
    영어는 여자 성우, 한글은 남자 성우이다(변경 불가능)
"""

from gtts import gTTS
import pygame
import time

text ="안녕하세요, 여러분. 파이썬으로 노는 것은 재미있습니다!!!"

tts = gTTS(text=text, lang='ko')

tts.save("helloKO.mp3")



# Initialize Pygame mixer
pygame.mixer.init()

# Load the audio file
pygame.mixer.music.load("helloKO.mp3")

# Play the audio file
pygame.mixer.music.play()

# Allow time for the audio to play
time.sleep(10)

# Stop the playback
pygame.mixer.music.stop()
