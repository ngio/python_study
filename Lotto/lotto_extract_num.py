

"""
    python 기존 로또 당첨번호를 이용한 로또 번호 추출 프로그램

"""



import pandas as pd
import random
from collections import Counter

def load_winning_numbers(filepath="winning_numbers.csv"):
    """
    CSV 파일에서 로또 당첨 번호를 불러옵니다.
    """
    try:
        df = pd.read_csv(filepath)
        # 추첨 번호(drwtNo1 ~ drwtNo6)만 추출합니다.
        winning_nums_cols = [f'drwtNo{i}' for i in range(1, 7)]
        return df[winning_nums_cols]
    except FileNotFoundError:
        print(f"오류: '{filepath}' 파일을 찾을 수 없습니다.")
        print("동행복권 웹사이트 등에서 당첨 번호 데이터를 CSV 파일로 다운로드하여 같은 폴더에 넣어주세요.")
        return None
    except Exception as e:
        print(f"데이터 로딩 중 오류 발생: {e}")
        return None

def analyze_number_frequency(winning_numbers_df):
    """
    각 숫자의 출현 빈도를 분석합니다.
    """
    all_numbers = []
    # 모든 당첨 번호 목록을 하나로 합칩니다.
    for index, row in winning_numbers_df.iterrows():
        all_numbers.extend(row.tolist())
    
    # 각 숫자의 출현 횟수를 셉니다.
    number_counts = Counter(all_numbers)
    
    # 빈도수 기준으로 내림차순 정렬
    sorted_counts = sorted(number_counts.items(), key=lambda item: item[1], reverse=True)
    
    return dict(sorted_counts) # {숫자: 빈도수} 형태로 반환

def generate_random_numbers():
    """
    가장 기본적인 방법으로 6개의 무작위 로또 번호를 생성합니다.
    """
    return sorted(random.sample(range(1, 46), 6))


def generate_numbers_based_on_frequency(number_frequency, num_recommendations=1, exclude_numbers=None):
    """
    과거 당첨 빈도를 기반으로 로또 번호를 추천합니다.
    (이 전략은 통계적 예측이 아닌, 자주 나온 번호 중에서 무작위로 선택하는 방식입니다.)
    """
    if number_frequency is None:
        print("경고: 번호 빈도 분석 데이터를 찾을 수 없어 무작위 번호를 생성합니다.")
        return [generate_random_numbers() for _ in range(num_recommendations)]

    # 빈도수가 높은 순서대로 숫자 목록을 만듭니다.
    # (실제로는 빈도수에 가중치를 두어 추출하는 더 복잡한 알고리즘도 가능합니다)
    sorted_numbers = list(number_frequency.keys())
    
    recommendations = []
    for _ in range(num_recommendations):
        generated_numbers = set()
        
        # 이미 추천된 번호들을 제외할 경우
        if exclude_numbers:
            available_numbers = [num for num in sorted_numbers if num not in exclude_numbers]
        else:
            available_numbers = sorted_numbers
        
        # 혹시 available_numbers가 6개 미만일 경우를 대비
        if len(available_numbers) < 6:
            print("경고: 추천할 수 있는 숫자가 충분하지 않습니다. 모든 번호에서 추출합니다.")
            available_numbers = list(range(1, 46))

        # 빈도수 기반으로 6개의 고유한 번호 추출
        # (단순히 빈도수 높은 순서대로 앞에서 6개 뽑는 것이 아니라,
        # 빈도수를 가중치로 해서 랜덤 샘플링하는 것이 더 무작위적입니다.)
        # 여기서는 편의상, 빈도수 높은 순서대로 나열된 리스트에서 랜덤하게 뽑습니다.
        
        # 더 나은 방법: 빈도수에 비례하여 숫자를 뽑기 (예: [1,1,1,2,2,3] -> 1,2,3이 나올 확률이 다름)
        # 이 예시에서는 단순화하여, 빈도수 순서대로 나열된 숫자 리스트에서 6개를 고유하게 뽑습니다.
        
        # 자주 나온 번호들 중에서 (예: 상위 20개) 무작위로 6개 선택
        top_n_numbers = sorted_numbers[:20] # 상위 20개 번호
        if len(top_n_numbers) < 6:
             # 혹시 상위 20개보다 전체 숫자가 적다면
             top_n_numbers = sorted_numbers

        # 상위 번호들 또는 전체 번호에서 무작위로 6개 선택
        try:
            chosen_numbers = sorted(random.sample(top_n_numbers, 6))
        except ValueError: # 만약 top_n_numbers가 6개 미만일 경우
            chosen_numbers = sorted(random.sample(available_numbers, 6))

        recommendations.append(chosen_numbers)
        
    return recommendations

# --- 메인 프로그램 ---
if __name__ == "__main__":
    file_path = "winning_numbers.csv" # 로또 당첨 번호 CSV 파일 경로
    
    print("==== 로또 번호 추천 프로그램 ====")
    
    # 1. 과거 당첨 번호 로드
    winning_numbers_df = load_winning_numbers(file_path)
    
    if winning_numbers_df is not None:
        # 2. 번호 빈도 분석
        number_frequency = analyze_number_frequency(winning_numbers_df)
        print("\n[과거 당첨 번호 출현 빈도 (상위 10개)]")
        for number, count in list(number_frequency.items())[:10]:
            print(f"  - 숫자 {number}: {count}회")

        # 3. 로또 번호 추천
        num_sets_to_recommend = 5 # 몇 세트의 번호를 추천받을지 설정
        
        # 빈도 기반 추천
        frequency_based_recommendations = generate_numbers_based_on_frequency(
            number_frequency, 
            num_recommendations=num_sets_to_recommend
        )
        
        print(f"\n[과거 당첨 빈도 기반 추천 번호 ({num_sets_to_recommend} 세트)]")
        for i, numbers in enumerate(frequency_based_recommendations):
            print(f"  세트 {i+1}: {numbers}")
            
        # 단순 무작위 추천 (비교용)
        random_recommendations = [generate_random_numbers() for _ in range(num_sets_to_recommend)]
        print(f"\n[단순 무작위 추천 번호 ({num_sets_to_recommend} 세트)]")
        for i, numbers in enumerate(random_recommendations):
            print(f"  세트 {i+1}: {numbers}")
            
    else:
        print("\n데이터 로딩 실패로 인해 번호 추천을 진행할 수 없습니다.")
        print("프로그램을 종료합니다.")
