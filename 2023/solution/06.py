import sys

with open(sys.argv[1] if len(sys.argv) > 1 else '../input/06') as f:
    time, distance = (list(map(int, line.split()[1:])) for line in f)

p1 = 1
p2time = ''
p2distance = ''

for i in range(len(time)):
    # speed * totaltime = distance
    #  speed = buttontime
    #  totaltime = time - buttontime
    # buttontime * (time - buttontime) = distance
    #  time * buttontime - buttontime^2 = distance
    #  -buttontime^2 + time * buttontime - distance = 0
    # a*x^2 + b*x + c = 0
    #  x = (-b +/- sqrt(b^2-4ac))/2a 
    # a = -1, b = time[i], c = distance[i]

    discriminant = (time[i]**2-4*distance[i])**0.5
    start = (-time[i] + discriminant)//-2 + 1 # floor + 1
    end = -((-time[i] - discriminant)//2) - 1 # ceil - 1

    p1 *= end - start + 1 # start time to end time inclusive

    p2time += str(time[i])
    p2distance += str(distance[i])

print(int(p1))

p2time = int(p2time)
p2distance = int(p2distance)

discriminant = (p2time**2-4*p2distance)**0.5
start = (-p2time + discriminant)//-2 + 1 # floor + 1
end = -((-p2time - discriminant)//2) - 1 # ceil - 1
print(int(end - start + 1))
