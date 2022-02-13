print("")
print("/  ██╗     ██╗███╗   ██╗███████╗███████╗   ██████╗ ██╗   ██╗")
print("/  ██║     ██║████╗  ██║██╔════╝██╔════╝   ██╔══██╗╚██╗ ██╔╝")
print("/  ██║     ██║██╔██╗ ██║█████╗  ███████╗   ██████╔╝ ╚████╔╝ ")
print("/  ██║     ██║██║╚██╗██║██╔══╝  ╚════██║   ██╔═══╝   ╚██╔╝  ")
print("/  ███████╗██║██║ ╚████║███████╗███████║██╗██║        ██║   ")
print("/  ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝╚═╝        ╚═╝   ")
print("")

u1 = [int(item) for item in input("/  First location vector: ").split()]
v1 = [int(item) for item in input("/  First direction vector: ").split()]
u2 = [int(item) for item in input("/  Second location vector: ").split()]
v2 = [int(item) for item in input("/  Second direction vector: ").split()]
print("")

if 0 in v2:
    x1 = [i / j for i, j in zip(v2, v1)]
else:
    x1 = [i / j for i, j in zip(v1, v2)]

if (x1[0] == x1[1] == x1[2]):
    print("/  The direction vectors are related!")
    x2 = [i - j for i, j in zip(u2, u1)]
    x3 = [i / j for i, j in zip(x2, v1)]
    if(x3[0] == x3[1] == x3[2]):
        print("/  The lines are identical!")
    else:
        print("/  The lines are parallel!")
else:
    print("/  The direction vectors have no relation!")
    x4 = [(u2[0] - u1[0]) / v1[0], v2[0] / v1[0]]
    x5 = u1[1] * x4
    if not x5:
        print("/  The lines are distorted")
    else:
        x6 = v2[1] - x5[1]
        x7 = u2[1] - u1[1]
        x8 = x7 / x6
        print("/  x1 = "+str(x8))
        x9 = x4[0] + x4[1] * x8
        print("/  x2 = "+str(x9))
        x10 = u1[2] + v1[2] * x9
        x11 = u2[2] + v2[2] * x8
        if(x10 == x11):
            print("/  The lines intersect!")
            x12 = x9 * v1 + u1
            print("/  Intersection = "+str(x12))
        else:
            print("/  The lines are distorted")
            x13 = [x10, x11]
        print("/  LGS: "+str(x13[0])+" = "+str(x13[1]))