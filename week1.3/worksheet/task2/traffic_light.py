"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Rebecca John Valliat
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"
next_state = {"red": "red_amber", "red_amber": "green", "green": "amber", "amber": "red"}



for i in range(maxtime + 1):
    print(f"Time {systime:03} State {state}")
    systime += 1

    



# Simulate the traffic light system up to time=maxtime in 1-second steps