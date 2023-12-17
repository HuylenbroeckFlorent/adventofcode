# To get the desired result, we can derive the formula press_time*(time-press_time) > distance from the previous part.
# To solve this, we could only look at the intersection between the two sides and take the distance between them.
# -> solve press_time*(time-press_time) = distance for press_time
# Let's rewrite this a(b-a) = c, or a(b-a)/c = 0 to solve for a
# The two solution for this equation are given by
# a1,2 = (1/2)*(b+-sqrt(b^2-4c))
# Then, a2-a1+1 gives us the number of ways to win the race, with a1 and a2 rounded up and down respectively.

import math

races = open('data.txt', 'r').readlines()
time = int(races[0].split(':')[1].strip('\n').replace(' ', ''))
distance = int(races[1].split(':')[1].strip('\n').replace(' ', ''))

intersection_1 = math.ceil((1/2)*(time-math.sqrt((time*time)-(4*distance))))
intersection_2 = math.floor((1/2)*(time+math.sqrt((time*time)-(4*distance))))

print(intersection_2-intersection_1+1)
