#!/bin/env python3

import hashlib 

mdp = "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"

h = hashlib.sha256(mdp.encode('utf-8'))
print(h)

f = open("phpbb.txt")
ar = f.read()
print(ar)

if "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b" == "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b":
    print ("a = b")

ar = ["1", "2", "3"]
for i in ar:
    print("arr =", i)