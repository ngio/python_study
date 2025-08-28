


# pip install pandas openpyxl


"""
    ./input/ 폴더 안에 있는 엑셀파일을 찾아서 데이터 있는 셀의 앞뒤 공백을 삭제

"""

import pandas as pd
import os

# 엑셀 파일이 있는 폴더 경로
input_folder = "./input/"

# 공백이 제거된 파일을 저장할 폴더 (원본 폴더에 저장)
output_folder = "./output/"

# 출력 폴더가 없으면 생성
if not os.path.isdir(output_folder):
    os.makedirs(output_folder)

# input 폴더 내의 모든 파일 목록 가져오기
files = os.listdir(input_folder)

print(f"'{input_folder}' 폴더에서 엑셀 파일을 찾고 있습니다...")

# 파일 목록을 순회
for filename in files:
    # 파일 확장자가 .xlsx 또는 .xls인지 확인
    if filename.endswith(".xlsx") or filename.endswith(".xls"):
        print(f"\n파일 '{filename}' 처리 중...")
        
        # 전체 파일 경로 설정
        file_path = os.path.join(input_folder, filename)
        
        try:
            # 엑셀 파일을 데이터프레임으로 읽어오기
            # 모든 시트를 읽어오기 위해 sheet_name=None 옵션 사용
            #excel_data = pd.read_excel(file_path, sheet_name=None) # 헤더 제외
            excel_data = pd.read_excel(file_path, sheet_name=None, header=0, dtype=str) # 모든 데이터를 문자열로 읽기
            
            # 수정한 내용을 저장할 새로운 엑셀 파일 객체 생성
            output_filepath = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_cleaned{os.path.splitext(filename)[1]}")
            
            with pd.ExcelWriter(output_filepath, engine='openpyxl') as writer:
                # 각 시트(Sheet)를 순회하며 작업
                for sheet_name, df in excel_data.items():
                    print(f"  - 시트 '{sheet_name}' 공백 삭제 중...")
                    
                    # 문자열 타입의 열만 선택하여 공백 제거
                    for col in df.columns:
                        if df[col].dtype == 'object':
                            # .str.strip() 메서드로 앞뒤 공백 제거
                            #df[col] = df[col].astype(str).str.strip()                            
                            df[col] = df[col].fillna('').astype(str).str.strip() # NaN 값이 있을 때 오류 방지
                            print(df[col])
                    
                    # 수정된 데이터프레임을 새로운 엑셀 파일의 해당 시트에 저장
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            print(f"'{filename}' 파일 처리가 완료되었습니다. '{output_filepath}'에 저장됨.")

        except Exception as e:
            print(f"  - 오류 발생: '{filename}' 파일을 처리할 수 없습니다. 오류: {e}")

print("\n모든 엑셀 파일 처리가 완료되었습니다.")
