from rich.progress import Progress
import time

def main():
    with Progress() as progress:
        task1 = progress.add_task("[cyan]Downloading...", total=100)
        task2 = progress.add_task("[magenta]Processing...", total=200)

        while not progress.finished:
            time.sleep(0.03)  # Simulate some work
            progress.update(task1, advance=1)
            progress.update(task2, advance=0.5)

if __name__ == "__main__":
    main()
