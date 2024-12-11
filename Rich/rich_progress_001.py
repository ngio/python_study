from rich.progress import Progress
import time

def main():
    # Create a progress bar
    with Progress() as progress:
        # Add a task
        task = progress.add_task("[cyan]Processing...", total=100)
        
        # Update progress
        for i in range(100):
            time.sleep(0.05)  # Simulate some work
            progress.update(task, advance=1)  # Advance the progress bar by 1

if __name__ == "__main__":
    main()
