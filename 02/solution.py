#!/usr/bin/env python3
def main():
    match = tuple(input().strip().split())
    item_map = {'X':1,'Y':2,'Z':3}
    game_map = {('A','X'):3, ('A','Y'):6, ('A','Z'):0, ( 'B','X'):0, ('B','Y'):3,
                ('B','Z'):6, ('C','X'):6, ('C','Y'):0, ('C','Z'):3}
    matches = []
    score = 0
    while match:
        matches.append(match)    
        score += item_map[match[1]] + game_map[match] 
        try:
            match = tuple(input().strip().split())
        except:
            match = False
    print(score)
if __name__ == '__main__':
    main()

