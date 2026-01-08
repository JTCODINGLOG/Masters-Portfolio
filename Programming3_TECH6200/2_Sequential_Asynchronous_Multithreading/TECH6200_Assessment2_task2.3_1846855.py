# to use high level thread pool
# there is no need of using .start() and .join()
# wait is not imported because .result() is used
from concurrent.futures import ThreadPoolExecutor
# to use lock concept
import threading
import time
import random


# Global variable(upper case), easier to spot and tune if needed
# Dictionary with activity names as keys and their progress percentage as values
# Initial percentage is 0 for 0%
# The program is designed so that we can add activities straightaway in the dictionary
# Testing done adding kookaburra activity
ACTIVITY_STATE = {"Eat sandwich": 0, "Enjoy tea": 0, "Eat fruit": 0, "Check notifications": 0,
                  "Listening kookaburra laugh": 0}

# Variable to speed up or slow down the code
SPEED = 0.02
# Creating lock object to protect access to the progress percentage in 'ACTIVITY_STATE'
lock = threading.Lock()


# Creating a function which a generic code for the activities
def routine_activity(name):
    # Calculating progress variation for the activity
    # This variable changes all the time, so it is left unlocked
    progress_increase = random.randint(10, 20)
    # Simple task time calculation based on progression in seconds
    task_time = (progress_increase * 5) * SPEED
    # Simulating activity time
    time.sleep(task_time)

    # Safely managing ACTIVITY_STATE[name] thanks to lock
    # Only one thread can access the variable at a time
    # Using 'with' helps to acquire the lock for the variable
    # inside 'with lock' scope, ACTIVITY_STATE[name] in this case,
    # releasing the variable lock at the end of the 'with lock' scope.
    with lock:
        # Reading % of progress done in this activity
        total_progress = ACTIVITY_STATE[name]

    # This activity does not need from the lock, so we keep it outside its scope
    # Checking if activity has been completed
    if total_progress >= 100:
        return 100
    # Updating total progress
    # If 'updated_total_progress' goes beyond 100, we keep value 100
    updated_total_progress = min(100, total_progress + progress_increase)
    # Now we need to access again the shared resource and we use the lock again
    with lock:
        # Updating activity progress value in global scope dictionary
        ACTIVITY_STATE[name] = updated_total_progress
    # We do not need the share resource as the needed variables are already in the function scope
    # Printing activity progress information
    print(f"Activity '{name}': {updated_total_progress}% completed")


def main():
    # Counting total routine time
    start_time = time.time()
    print("Multithreading John's morning routine:\n")

    # Creating a pool of thread objects to execute our little routine tasks
    # Reusing threads in loops for efficiency
    # max_workers establishes amount of threads running at the same time
    with ThreadPoolExecutor(max_workers=5) as executor:
        # It loops until breaks
        while True:
            # Accessing global variable and creating another variable with its content...
            # ...to access global variable snapshot after lock releases it
            with lock:
                snap_dict = dict(ACTIVITY_STATE)
            # if any of the activity values (progress) is under 100 keeps going
            # when all the activity values (progress) has reached 100 breaks
            if all(progress >= 100 for progress in snap_dict.values()):
                break
            # This list will collect this round tasks
            # From the assessment question, we understand a cycle that needs to be repeated...
            # ...keeping the order of the tasks intact
            tasks = []
            # One interation for each activity
            for name, progress in list(snap_dict.items()):
                # It just applies to incomplete activities(progress < 100)
                if progress < 100:
                    # Submitting the task to the pool of worker threads
                    # tasks start running "in parallel" in the pool allowing overlap
                    # Adding task object(future) to tasks so that later we can block the main thread until...
                    # ...all tasks finish by the end of the cycle
                    tasks.append(executor.submit(routine_activity, name))
            # Wait for the tasks to finish before next while loop iteration starts
            # Chosen because result() propagates any exception
            for task in tasks:
                task.result()
            # Another wait option is:
            # wait(tasks)

            # After the for loop, tasks have updated progress, and times therefore we take another...
            # ...snapshot of the global variable ACTIVITY_STATE
            with lock:
                snap_dict = dict(ACTIVITY_STATE)
            # Calculating routine progress
            routine_progress = sum(snap_dict.values()) / len(snap_dict)
            print(f"Routine progress: {routine_progress}% completed\n")

    # Printing final activities progress
    print(f"\nActivity State %: {ACTIVITY_STATE}")
    # Printing total routine time
    print(f"Total time of John's routine is: {time.time() - start_time:.2f}")


if __name__ == "__main__":
    main()
