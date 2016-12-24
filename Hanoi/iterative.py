# Set up array of towers
towers = []
towers.append([])
towers.append([])
towers.append([])
chars = ['A','B','C']
step = 0

n = int(input('How many rings are we playing with?: '))
odd = n%2

# Initialize towers
i = n+1
while i >= 1:
    towers[0].append(i)
    i -= 1
towers[1].append(n+1)
towers[2].append(n+1)

# Initialize first move
fromT = 0
if odd:
    toT = 1
else:
    toT = 2
candidate = 1

while len(towers[1]) < n+1:
    # Print out current step
    step += 1
    print("Step #", step, ": Move ring ", candidate, " from tower ",
    chars[fromT], " to tower ", chars[toT], sep='')

    # Move the ring in towers for current step
    towers[toT].append(candidate)
    towers[fromT].pop()

    # Get the next 'from' tower
    if towers[(toT+1)%3][len(towers[(toT+1)%3])-1] < towers[(toT+2)%3][len(towers[(toT+2)%3])-1]:
        fromT = (toT+1)%3
    else:
        fromT = (toT+2)%3

    # Get the next 'to' tower
    if odd:
        if towers[fromT][len(towers[fromT])-1] < towers[(fromT+1)%3][len(towers[(fromT+1)%3])-1]:
            toT = (fromT+1)%3
        else:
            toT = (fromT+2)%3
    else:
        if towers[fromT][len(towers[fromT])-1] < towers[(fromT+2)%3][len(towers[(fromT+2)%3])-1]:
            toT = (fromT+2)%3
        else:
            toT = (fromT+1)%3

    candidate = towers[fromT][len(towers[fromT])-1]
