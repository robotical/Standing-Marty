import martypy

from time import sleep
m = martypy.Marty('socket://192.168.0.43')
m.enable_motors()
m.enable_safeties(False)
m.fall_protection(False)


#Hands up
m.move_joint(6, -127, 200)
m.move_joint(7, -127, 200)

#Bend knee
m.move_joint(2, -100, 200)
m.move_joint(5, 100, 200)
sleep(1)

#Lean Forward
m.move_joint(0, 100, 200)
m.move_joint(3, 100, 200)
sleep(1)

#Twist
m.move_joint(1, -100, 200)
m.move_joint(4, 100, 200)
sleep(1)

x = raw_input()
m.enable_motors()

#Hands down
m.move_joint(6, 127, 200)
m.move_joint(7, 127, 200)

x = raw_input()

#Twist back
m.move_joint(1, 10, 200)
m.move_joint(4, 10, 200)
sleep(1)

x = raw_input()


#Pull legs in
m.move_joint(2, 0, 200)
m.move_joint(5, 0, 200)
sleep(1)

#Lean back
m.move_joint(0, 0, 200)
m.move_joint(3, 0, 200)
