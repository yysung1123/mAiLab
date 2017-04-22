#!/usr/bin/env python3

# HW0002 Random Number

import random
import numpy as np
import time

# Basic
# 1. Generate 5 random numbers and print

print([random.random() for i in range(5)])

# 2. Generate N random numbers within -1 to 1 and calculate mean and stddev and
# print. Random numbers shouldn't be printed. N = 10^1, 10^2, 10^3, 10^4, 10^5

# Advanced
# 3. From 2, calculate time when generating N random numbers

def rand(N):
    # 2 * [0, 1) - 1 -> [-1, 1)
    return 2 * np.random.random_sample(N) - 1

N = [10 ** i for i in range(1, 6)]
for i in N:
    start_time = time.time()
    random_number = rand(i)
    finish_time = time.time()
    print("Avg. {}".format(random_number.mean()))
    print("Stddev. {}".format(random_number.std()))
    print("Time {:6f}s".format(finish_time - start_time))

# 4. Self-made Random Number Generator

# MT19937
# https://en.wikipedia.org/wiki/Mersenne_Twister
# An Python Implementation followed by Pseudocode on Wikipedia

class RNG:
    def __init__(self, seed=0):
        self.index = 0
        self.mt = [0] * 624
        self.mt[0] = seed
        for i in range(1, 624):
            self.mt[i] = 0xFFFFFFFF & (1812433253 * (self.mt[i - 1] ^ (self.mt[i - 1] >> 30)) +
                    i)

    def extract_number(self):
        if self.index == 0:
            self.generate_numbers()

        y = self.mt[self.index]
        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & 2636928640)
        y = y ^ ((y << 15) & 4022730752)
        y = y ^ (y >> 18)

        self.index = (self.index + 1) % 624
        return y
    
    def generate_numbers(self):
        for i in range(0, 624):
            y = (self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff)
            self.mt[i] = self.mt[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ 2567483615

    def random(self):
        return self.extract_number() / 0xFFFFFFFF

rng = RNG()
print(rng.random())

# Result
'''
[0.27209326996202254, 0.05146406301581197, 0.3601347480734888, 0.5186212302047445, 0.20193117345395162]
Avg. 0.24975908156541884
Stddev. 0.591702924832753
Time 0.000051s
Avg. -0.020429980808031826
Stddev. 0.5752739352263962
Time 0.000018s
Avg. -0.0030879321112153983
Stddev. 0.569656121602261
Time 0.000024s
Avg. -0.005963881535714546
Stddev. 0.577595743356434
Time 0.000215s
Avg. -0.00038178791171763137
Stddev. 0.5768253033763888
Time 0.002251s
'''
