'''
a. ( True  )  2 * 4 == 24/3
b. ( False )  (15 % 4) < (19 % 6)
c. ( True  )  !(2 < 5) != (8 == 8)
d. ( True  )  True or False
e. ( True  )  2**2 == math.pow(2, 2)
f. ( False )  False and ( (7 / 2) > 3.5 )
g. ( True  )  ( math.ceil( 2.5 ) == 3) and (math.sqrt( 9) == 3)
'''
import math

print(2 * 4 == 24/3)  # a
print((15 % 4) < (19 % 6))  # b
print(not(2 < 5) != (8 == 8))  # c
print(True or False)  # d
print(2**2 == math.pow(2, 2))  # e
print(False and ((7 / 2) > 3.5))  # f
print((math.ceil(2.5) == 3) and (math.sqrt(9) == 3))  # g
