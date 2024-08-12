폴더 안의 파일들 이름의 공백 또는 - 를 언더바로 변경하는 프로그램


공백( ) 또는 하이픈(-)을 언더바(_)로 변경하는 프로그램을 작성할 수 있습니다. 이 프로그램은 지정된 폴더 내 모든 파일의 이름을 확인하고, 공백 또는 하이픈이 포함된 경우 이를 언더바로 대체하여 이름을 변경합니다.

### 1.프로그램 설명
  os 모듈: 파일 경로와 관련된 작업을 수행하기 위해 os 모듈을 사용합니다.

### 2.폴더 내 파일 탐색:
  os.listdir(folder_path)를 사용하여 지정된 폴더 내의 모든 파일 및 하위 디렉토리 이름을 가져옵니다.
  for filename in os.listdir(folder_path)를 사용하여 각 파일을 순회합니다.  

### 3.공백과 하이픈을 언더바로 변경:

  if ' ' in filename or '-' in filename: 조건문을 사용하여 파일 이름에 공백 또는 하이픈이 포함되어 있는지 확인합니다.
  filename.replace(' ', '_').replace('-', '_')를 사용하여 공백과 하이픈을 언더바로 대체합니다.

### 4.파일 이름 변경:

  os.rename(old_file_path, new_file_path)를 사용하여 파일 이름을 변경합니다.

### 5.사용 방법:

folder_path에 파일 이름을 변경할 폴더의 경로를 입력합니다.
프로그램을 실행하면 폴더 내 모든 파일의 이름에서 공백과 하이픈이 언더바로 변경됩니다.

사용 예시
폴더 경로를 지정하여 프로그램을 실행하면, 그 폴더 안의 모든 파일 이름에서 공백 또는 하이픈이 언더바로 변경됩니다. 예를 들어, path_to_your_folder가 
  C:/Users/YourName/Documents/TestFolder인 경우:

    folder_path = 'C:/Users/YourName/Documents/TestFolder'
    replace_spaces_and_hyphens_in_filenames(folder_path)

