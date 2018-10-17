"""This problem was asked by Apple.

Implement a job scheduler which takes in a function
f and an integer n, and calls f after n milliseconds."""

import time as t

def dummy():
    print("I'm Called")

def job_scheduller(f,n):
    start = t.time()*1000
    end = start + n
    while start < end:
        start = t.time()*1000
    f()
    
job_scheduller(dummy,1000)