import itertools
import random
import time

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
while True:
    length = 12 # Number of alphabet combinations
    combo = random.choices(alphabet, k=length)
    word = "".join(combo)
    print(word)
    time.sleep(0.001) #1000ms = 1s