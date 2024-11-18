import time

def pomodoro_timer(work_time=25, break_time=5):
    print(f"Work for {work_time} minutes.")
    time.sleep(work_time * 60)
    print(f"Take a break for {break_time} minutes.")
    time.sleep(break_time * 60)

pomodoro_timer()




