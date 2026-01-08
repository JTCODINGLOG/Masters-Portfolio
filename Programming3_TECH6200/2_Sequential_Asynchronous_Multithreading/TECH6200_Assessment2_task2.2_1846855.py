# While waiting for tea, John checks notifications
# While eating fruit, John scrolls down through Social media
# John is using the waiting time of some tasks to do others
# The programming choice is then, asynchronous programming
# This is because the waiting period is used to run coroutines
# With a simple routine I tried to implement several asynchronous tasks...
# ...trying different case scenarios
# Routine (asynchronous tasks and sequential tasks):
# First eats sandwich(jumbo size), needs both hands, no overlap
# Second enjoys tea, and check Work Notifications WHILE tea gradually cools down
# Third eats fruit, while he chews, he finishes checking work notifications...
# ...and then starts scrolling down through social media
# Fourth, when he finishes the fruit he keeps scrolling down social media
# Bonus, fifth: imagine social media is taking some time to load, and...
# ...John gets distracted by a Kookaburra laughing (which finish at the same time...
# ...than social media scrolling). His routine has finished, he has to go to work.

import asyncio
import time

# Calculating time for each activity in seconds
# Global variables(upper case), easier to spot and tune if needed
SANDWICH_SECS = 8 * 60
TEA_SECS = 3 * 60
FRUIT_SECS = 2 * 60
# Work notifications take longer to read than just enjoying tea
# Reading work notifications finishes while eating fruit
WORK_NOTIFICATIONS = 4 * 60
SOCIAL_MEDIA_SECS = 10 * 60
# Adding variable to measure seconds between tasks
TASK_TRANSITION_SECS = 5
# Adding speed variable with testing purposes:
# 1 is real time scenario, < 1 to speed up, > 1 to slow down.
SPEED = 0.02


# Creating a coroutine function which a generic code for the asynchronous activities
# Two variables, the name of the activity and how long it takes in seconds
async def routine_activity(name, secs):
    # Tracking time
    start_time = time.time()
    # Printing start of activity
    print(f"\n'{name}' activity has been started.")
    # non-blocking
    # other tasks will overlap while this one is "sleeping"
    await asyncio.sleep(secs * SPEED)
    # Printing information
    print(f"Activity '{name}' completed in {time.time() - start_time:.2f} seconds")


# Tasks (coroutines)

# Eat sandwich has no overlap:
# We keep this task asynchronous to stay consistent with the rest of the code,...
# ...but it could have been defined like a normal function,...
# ...using blocking command 'time.sleep' for the waiting period
async def eat_sandwich():
    return await routine_activity("Eat sandwich", SANDWICH_SECS)


# Enjoy tea, will be overlapped with work notifications
async def enjoy_tea():
    return await routine_activity("Enjoy tea", TEA_SECS)


# Eat sandwich, will be overlapped with social media scrolling
async def eat_fruit():
    return await routine_activity("Eat fruit", FRUIT_SECS)


# Overlapping tasks
# Checking work notifications will overlap 'enjoy tea', transition time, and a part of 'eat fruit'
async def check_work_notifications():
    return await routine_activity("Check work notifications", WORK_NOTIFICATIONS)


# Scrolling down through social media will overlap 'eat fruit' and then...
# ...the scrolling will become John's main activity without overlap
async def scroll_through_social_media():
    return await routine_activity("Scroll through social media", SOCIAL_MEDIA_SECS)


# Transition task between other tasks of the routine
async def task_transition():
    await asyncio.sleep(TASK_TRANSITION_SECS * SPEED)


# Kookaburra laugh follows social media scrolling (follow task) and does not have specific duration
async def kookaburra_laugh(follow_task):
    # Tracking time
    start_time = time.time()
    print("Every morning a Kookaburra come and starts laughing of John")
    try:
        # Last until John stops scrolling
        await follow_task
    finally:
        print("Kookaburra stopped laughing as soon as John stopped scrolling and went to work.")
        # Printing time duration information
        print(f"Kookaburra was laughing for {time.time() - start_time:.2f} seconds!!!")


# Tasks coordination happens in main
async def main():
    print("Asynchronous John's morning routine: ")
    # Counting total routine time
    start_time = time.time()

    # Calling activities
    # 1. Sandwich, no overlap
    await eat_sandwich()
    await task_transition()

    # 2. Tea and work notifications overlapping
    tea_task = asyncio.create_task(enjoy_tea())
    notification_task = asyncio.create_task(check_work_notifications())
    # Tea finishes but work notifications are still being checked after
    # That is why there is no await for the work notifications yet
    await tea_task
    await task_transition()

    # 3. Fruit and Social Scrolling
    fruit_task = asyncio.create_task(eat_fruit())
    # Now, because we share the same device for work apps and social media...
    # ...we let work notifications task to finish before we scroll through social media
    await notification_task
    social_task = asyncio.create_task(scroll_through_social_media())

    # 4. Wait for fruit to finish, social media scrolling keeps running until time finishes
    await fruit_task
    kookaburra_distraction = asyncio.create_task(kookaburra_laugh(social_task))
    await asyncio.gather(social_task, kookaburra_distraction)

    # Printing total routine time
    print(f"\nTotal time of John's routine is: {time.time() - start_time:.2f}")


if __name__ == "__main__":
    asyncio.run(main())
