# 사용자가 초 단위로 시간을 입력하면 카운트다운을 실행하는 간단한 Python 프로그램입니다. 
# time 모듈을 사용하여 매초 업데이트하며, 남은 시간을 출력합니다.
import time

def countdown(seconds):
    """
    Counts down from the given number of seconds.
    
    :param seconds: Total seconds to count down
    """
    try:
        while seconds >= 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02}:{secs:02}"  # Format as MM:SS
            
            # 매초마다 동일한 줄에 시간을 출력.
            # end="\r"를 사용하여 이전 출력 내용을 덮어씁니다.
            print(timer, end="\r")  # Print on the same line 
            
            time.sleep(1)  # Wait for 1 second
            seconds -= 1
        print("Time's up!")
    except KeyboardInterrupt:
        print("\nCountdown stopped.")

# Example: Enter seconds to countdown
if __name__ == "__main__":
    try:
        user_input = int(input("Enter the number of seconds for countdown: "))
        countdown(user_input)
    except ValueError:
        print("Please enter a valid integer.")
