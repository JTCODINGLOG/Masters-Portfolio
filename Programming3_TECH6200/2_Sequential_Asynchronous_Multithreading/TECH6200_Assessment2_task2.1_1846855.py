# In this task there is no need of using asynchronous, multithreading or multiprocessing programming.
# The flow is strictly sequential, therefore regular synchronous programming with the use of time.sleep()...
# ...will be easier to read and understand.
# Routine (sequential tasks, one after the other):
# Eat sandwich (8min), enjoy tea (3min), eat fruit(2min), social media(10min)
import time

# Calculating time for each activity in seconds
# Global variables(upper case), easier to spot and tune if needed
SANDWICH_SECS = 8 * 60
TEA_SECS = 3 * 60
FRUIT_SECS = 2 * 60
SOCIAL_MEDIA_SECS = 10 * 60
# Adding variable to measure seconds between tasks
TASK_TRANSITION_SECS = 5
# Adding speed variable with testing purposes:
# 1 is real time scenario, < 1 to speed up, > 1 to slow down.
SPEED = 0.01


# Creating a function which a generic code for the activities
# Two variables, the name of the activity and how long it takes in seconds
def routine_activity(name, secs):
    # Tracking time
    start_time = time.time()
    # Printing start of activity
    print(f"\n'{name}' activity has been started.")
    # Blocking the code activity for the corresponding amount of time
    time.sleep(secs * SPEED)
    # Printing information
    print(f"Activity '{name}' completed in {time.time() - start_time:.2f} seconds")


def main():
    # Counting total routine time
    start_time = time.time()
    # Including all the 'routine_activity' function parameters in a list
    activity_list = [("Eat sandwich", SANDWICH_SECS), ("Enjoy tea", TEA_SECS), ("Eat fruit", FRUIT_SECS),
                     ("Scroll through social media", SOCIAL_MEDIA_SECS)]
    print(f"Sequential John's morning routine: ")
    # Calling each activity
    for string, seconds in activity_list:
        routine_activity(string, seconds)
        # Adding 5 seconds time that elapses between activities
        # Could have been included in the routine function but is included here for an easy visualisation
        time.sleep(TASK_TRANSITION_SECS * SPEED)
    # Printing total routine time
    print(f"\nTotal time of John's routine is: {time.time() - start_time:.2f}")


if __name__ == "__main__":
    main()
