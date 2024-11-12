# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path 

from moviepy.editor import *

# MP4 파일이 있는 폴더 경로 지정
folder_path = './downloads'

import file_rename_underbar as fru

# 폴더내의 파일명 rename
fru.replace_spaces_in_filenames(folder_path)


# 폴더 내의 모든 파일 확인
for filename in os.listdir(folder_path):
    if filename.endswith('.mp4'):
        mp4_path = os.path.join(folder_path, filename)
        mp3_path = os.path.join(folder_path, filename.replace('.mp4', '.mp3'))
        
        # 비디오에서 오디오 추출 후 MP3로 저장
        video = VideoFileClip(mp4_path)
        video.audio.write_audiofile(mp3_path)
        video.close()  # 명시적으로 close 호출하여 자원 해제

        print(f"Converted: {filename} to MP3")
    else:
        print(f"Converted Not: {filename} to MP3")

