_파이썬_가상환경_VENV.md



파이썬 가상환경과 아나콘다 가상환경은 프로젝트 간의 종속성 충돌을 피하고, 각 프로젝트별로 필요한 패키지를 독립적으로 관리할 수 있도록 도와줍니다. 아래는 각각의 가상환경 사용법을 설명합니다.

### Python 가상환경 사용법

Python의 `venv` 모듈을 사용하여 가상환경을 만드는 방법을 설명합니다.

#### 1. 가상환경 생성

```bash
# 가상환경 생성
python -m venv myenv
```

위 명령어는 현재 디렉토리에 `myenv`라는 이름의 가상환경을 생성합니다.

#### 2. 가상환경 활성화

- **Windows:**

  ```bash
  myenv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source myenv/bin/activate
  ```

가상환경이 활성화되면 명령줄에 `(myenv)`가 추가되어 현재 가상환경이 활성화된 상태임을 나타냅니다.

#### 3. 패키지 설치

가상환경이 활성화된 상태에서 `pip`를 사용하여 필요한 패키지를 설치합니다.

```bash
pip install package_name
```

#### 4. 가상환경 비활성화

가상환경 사용을 마쳤으면 비활성화합니다.

```bash
deactivate
```

### Anaconda 가상환경 사용법

Anaconda의 `conda` 명령어를 사용하여 가상환경을 만드는 방법을 설명합니다.

#### 1. 가상환경 생성

```bash
# 가상환경 생성
conda create --name myenv
```

`myenv`는 가상환경의 이름입니다. 필요에 따라 특정 Python 버전을 지정할 수도 있습니다.

```bash
conda create --name myenv python=3.8
```

#### 2. 가상환경 활성화

```bash
conda activate myenv
```

가상환경이 활성화되면 명령줄에 `(myenv)`가 추가되어 현재 가상환경이 활성화된 상태임을 나타냅니다.

#### 3. 패키지 설치

가상환경이 활성화된 상태에서 `conda`를 사용하여 필요한 패키지를 설치합니다.

```bash
conda install package_name
```

`pip`를 사용할 수도 있습니다.

```bash
pip install package_name
```

#### 4. 가상환경 비활성화

가상환경 사용을 마쳤으면 비활성화합니다.

```bash
conda deactivate
```

#### 5. 가상환경 목록 확인

```bash
conda env list
```

#### 6. 가상환경 삭제

```bash
conda remove --name myenv --all
```

위 명령어를 사용하면 `myenv` 가상환경이 삭제됩니다.

이와 같이 Python의 `venv` 모듈과 Anaconda의 `conda` 명령어를 사용하여 가상환경을 만들고 관리할 수 있습니다. 가상환경을 통해 프로젝트 간의 종속성 문제를 효과적으로 관리할 수 있습니다.
