#!/bin/env python3

import hashlib

def read():
    f = open('phpbb.txt')
    ar = f.read()
    array = ar

def get_hash():
    mdp = "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"

    h = hashlib.sha256(mdp.encode('utf-8'))
    print(h)

def compare_string():
    if "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b" == "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b":
        print ("3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b = 3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b")

#def new_tab():
 #   print()

def main():
    get_hash()
    read()
    compare_string()