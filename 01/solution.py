#!/usr/bin/env python3
x = input()
cals = []
while x:
    curr_elf=0
    while x:
        curr_elf += int(x)
        try:
            x=input()
        except:
            x = None
    try:
        x = input()
    except:
        x = None
    cals.append(curr_elf)
print(sum(sorted(cals)[-3:]))
