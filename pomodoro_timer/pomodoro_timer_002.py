import time

def pomodoro_timer(work_time=25, break_time=5):
    try:
        print(f"Starting Pomodoro Timer! Work for {work_time} minutes.")
        countdown(work_time * 60, "Work Time Remaining")
        
        print(f"Work session complete! Take a break for {break_time} minutes.")
        countdown(break_time * 60, "Break Time Remaining")
        
        print("Pomodoro session complete! Well done!")
    except KeyboardInterrupt:
        print("\nTimer interrupted. Goodbye!")

def countdown(seconds, message):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02}:{secs:02}"
        print(f"\r{message}: {time_format}", end="")
        time.sleep(1)
        seconds -= 1
    print("\r" + " " * 30, end="")  # Clear the line after the timer ends

# 실행
pomodoro_timer()



