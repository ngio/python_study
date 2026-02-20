 
""" 
    pip install firebase-admin
"""

print(f"'{real_path}' 폴더에서 Firebase Realtime Database CRUD 작업을 수행합니다...")

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# 1. 인증 및 초기화
# 다운로드한 JSON 키 파일 경로와 데이터베이스 URL을 입력합니다.
cred = credentials.Certificate("path/to/your-service-account-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com/' # 본인의 URL로 변경
})

# 2. 데이터 생성 (Create) - push()는 고유 ID를 생성하며 추가합니다.
def create_user(user_id, name, email):
    ref = db.reference('users') # 'users' 노드 참조
    user_ref = ref.child(user_id)
    user_ref.set({
        'name': name,
        'email': email,
        'score': 0
    })
    print(f"✅ 유저 {name} 생성 완료")

# 3. 데이터 읽기 (Read) - get() 사용
def read_user(user_id):
    ref = db.reference(f'users/{user_id}')
    user_data = ref.get()
    if user_data:
        print(f"🔍 조회 결과: {user_data}")
        return user_data
    else:
        print("❌ 유저를 찾을 수 없습니다.")
        return None

# 4. 데이터 수정 (Update) - update() 사용 (일부 필드만 수정 가능)
def update_score(user_id, new_score):
    ref = db.reference(f'users/{user_id}')
    ref.update({
        'score': new_score
    })
    print(f"🆙 유저 {user_id}의 점수가 {new_score}로 수정되었습니다.")

# 5. 데이터 삭제 (Delete) - delete() 사용
def delete_user(user_id):
    ref = db.reference(f'users/{user_id}')
    ref.delete()
    print(f"🗑️ 유저 {user_id} 삭제 완료")

# --- 실행 예시 ---
if __name__ == "__main__":
    # 데이터 저장
    create_user("user_01", "Kim", "kim@example.com")
    
    # 데이터 조회
    read_user("user_01")
    
    # 데이터 수정
    update_score("user_01", 100)
    
    # 데이터 삭제 (필요 시 주석 해제)
    # delete_user("user_01")
    
    
    
