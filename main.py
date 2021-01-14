#!/bin/env python3

import hashlib

def read():
    f = open('phpbb.txt')
    ar = f.read()
    return (ar)

def get_hash():
    mdp = "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"

    h = hashlib.sha256(mdp.encode('utf-8'))
    print(h)

def compare_string():
    if "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b" == "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b":
        print ("a = b")

def new_tab():
    array = [1, 2, 3]
    for i in array:
        print("array = ", i)

def main():
    get_hash()
    read()
    new_tab()
    compare_string()