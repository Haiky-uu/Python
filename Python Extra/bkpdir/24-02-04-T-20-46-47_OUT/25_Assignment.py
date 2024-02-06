#Pattern Program
'''
(  @   #   $   )
(  @   #   $   )
(  @   #   $   )
(  @   #   $   )
(  @   #   $   )
'''

for i in range(5):
    for j in range(1):
        print('(', end="  ")
        print('@', end="   ")
        print('#', end="   ")
        print('$', end="   ")
        print(')', end="  ")
    print()
