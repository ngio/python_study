 
Firebase Realtime Database를 Python에서 사용하는 방법은 매우 직관적입니다. Firebase는 NoSQL 클라우드 데이터베이스로, 데이터를 JSON 형태로 저장하며 실시간 동기화가 가능하다는 장점이 있습니다.

firebase-admin 라이브러리를 사용하여 인증부터 데이터 CRUD(생성, 읽기, 수정, 삭제)까지 수행하는 완전한 예제를 가이드해 드립니다.

1. ⚙️ 사전 준비 (Firebase 설정)
    1.Firebase Console(https://console.firebase.google.com/)에서 프로젝트를 생성합니다.

    2.Realtime Database를 생성하고 '테스트 모드'로 시작합니다.

    3.프로젝트 설정 > 서비스 계정 탭으로 이동하여 **"새 비공개 키 생성"**을 클릭해 .json 키 파일을 다운로드합니다. (이 파일이 파이썬과 파이어베이스를 연결하는 열쇠입니다.)

    4.데이터베이스 상단에 있는 URL(https://your-project-id.firebaseio.com/)을 복사해 둡니다.

        import firebase_admin
        from firebase_admin import credentials

        cred = credentials.Certificate("path/to/serviceAccountKey.json")
        firebase_admin.initialize_app(cred)



        https://fb-test-1001-default-rtdb.firebaseio.com/



2. 📦 라이브러리 설치
    터미널에서 관리자 권한으로 필수 라이브러리를 설치합니다.
 
        pip install firebase-admin

3.주요 기능 설명 (MSSQL 사용자 관점)
  ref.push(data) (Insert):
  
    MSSQL의 INSERT INTO Table과 유사합니다.
    
    데이터를 넣을 때마다 Firebase가 -Nabc123...과 같은 고유한 문자열 ID를 자동으로 생성합니다. 이는 MSSQL의 Identity(1,1) 컬럼과 같은 역할을 하여 데이터 중복을 방지합니다.
  
  ref.get() (Select):
  
    SELECT * FROM Items와 유사합니다.
    
    해당 경로의 모든 데이터를 Python의 딕셔너리(Dictionary) 형태로 가져옵니다.
  
  ref.child(target_id).delete() (Delete):
  
    DELETE FROM Items WHERE ID = '...'와 유사합니다.
    
    특정 고유 ID(Key)를 가진 노드를 찾아 그 하위 데이터를 모두 삭제합니다.
  
  while True 루프:
  
    프롬프트에서 사용자가 직접 '4'를 눌러 종료하기 전까지 인터페이스를 유지하여, 연속적인 데이터 관리가 가능하게 합니다.
  


<img width="451" height="303" alt="image" src="https://github.com/user-attachments/assets/997a30c0-3650-4b1c-96dd-d9eb7db4ac8f" />
