# You are given two positive integers 1. Height of ladder and 2. Max number of steps you
# can take at a time to reach the top.
# Write a program to list all possible ways in which one can reach to the top of the ladder.

def ladder(var: int, steps: int, cnt: int, no_steps_ladder: list):

    if (var == 0):
        return cnt, no_steps_ladder
    # print(var,steps)
    if var >= steps:
        cnt+=1
        no_steps_ladder.append((steps,var))
        return ladder(var-steps, steps, cnt, no_steps_ladder)
    else:
        return ladder(var, steps-1, cnt, no_steps_ladder)


height = 18
steps = 5
cnt = 0
lst = []
print(ladder(height,steps,cnt,lst))
