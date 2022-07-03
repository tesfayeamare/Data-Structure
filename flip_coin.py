"""
Flip a coin until we get 10 heads in row,
and record how long it took 
"""

import random 
total_flips = 0
heads_in_row = 0

while heads_in_row < 10:
  # Flip  a coin 
  if random.choice([0,1]) == 1:
    # Flip  a head 
    heads_in_row += 1
  else:
    # Flip a tail 
    heads_in_row = 0 # Resetting 
  total_flips  += 1

print(total_flips)