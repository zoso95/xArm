from xarm.arm import *
import math
import time

grip_close()


def reset():
    movej((500, 500, 500, 500, 500), 2000)
    power_off()


#jDepart = (497, 426, 738, 55, 500)
jDepart = (497, 426, 700, 55, 500)
movej(jDepart, 2000)

eye_x = 10
z_up = 0
z_down = -18

center_origin = get_position(True)
# y(+), x(inv), up(+)
#movel(appro(pA, (30, 0, 0)), 1000)
movel(appro(center_origin, (50, eye_x, z_up)), 1000)
movel(appro(center_origin, (50, eye_x, z_down)), 100)

movel(appro(center_origin, (30, eye_x, z_down)), 3000)
movel(appro(center_origin, (30, eye_x, z_up)), 100)

movel(appro(center_origin, (50, -eye_x, z_up)), 1000)
movel(appro(center_origin, (50, -eye_x, z_down)), 100)

movel(appro(center_origin, (30, -eye_x, z_down)), 3000)
movel(appro(center_origin, (30, -eye_x, z_up)), 100)

cx, cy = 0, 30
r = 30

for theta in range(0, -180, -15):
    angle = (theta/360)*2*math.pi

    x,y = cx+r*math.cos(angle), cy+r*math.sin(angle)

    movel(appro(center_origin, (y, x, z_down)), 1000)


reset()


"""
x_start = 40
movel(appro(center_origin, (50, -x_start, 5)), 1000)
movel(appro(center_origin, (50, -x_start, 0)), 100)
"""

"""

pA = get_position(True)

movel(appro(pA, (30, 0, 5)), 1000)
grip_close(850)

pAppr = appro(pA, (30, 0, 25))
movel(pAppr, 1000)

movel(appro(pA, (30, 0, 5)), 1000)

grip_open()

time.sleep(2)

movej((500, 500, 500, 500, 500), 2000)
power_off()
"""

#import code
#code.interact(local=locals())
