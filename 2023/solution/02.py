
p1sum = 0
p2sum = 0
with open('../input/02', 'r') as f:
    for line in f:
        gameid, cubes = line.split(':') 
        red = 0
        green = 0
        blue = 0
        possible = True
        for cubeset in cubes.split(';'):
            for cube in cubeset.split(','):
                count, color = cube.strip().split(' ')
                count = int(count)
                match color:
                    case 'red':
                        red = max(red, count)
                        if count > 12:
                            possible = False

                    case 'green':
                        green = max(green, count)
                        if count > 13:
                            possible = False

                    case 'blue':
                        blue = max(blue, count)
                        if count > 14:
                            possible = False

        if possible:
            p1sum += int(gameid[5:])
        p2sum += red*green*blue

    print(f'{p1sum=}')
    print(f'{p2sum=}')
