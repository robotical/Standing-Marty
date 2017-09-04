import martypy

from time import sleep
m = martypy.Marty('socket://192.168.0.28')
m.enable_motors()

#Disable safeties to allow motors to consume the extra current needed to push Marty up
'''
Be Aware that the motor protection is there for a reason, to prevent you from breaking the motors.
It can be surprisingly easy to destroy a microservo motor by forcing it to move when it doesn’t want to.
We won’t cover warranty replacements for motors if you disable protections and then break a motor.
'''
m.enable_safeties(False)
m.fall_protection(False)    #This is to stop Marty from turning off the motors when it detects the change in orientation.


#Rasie arms up
m.move_joint(6, 127, 200)
m.move_joint(7, 127, 200)

#Bend knee
m.move_joint(2, -100, 200)
m.move_joint(5, 100, 200)
sleep(1)

#Lean forward
m.move_joint(0, 100, 200)
m.move_joint(3, 100, 200)
sleep(1)

#Twist knees
m.move_joint(1, -100, 200)
m.move_joint(4, 100, 200)
sleep(1)

m.enable_motors()

#Put arms down to push the body up
m.move_joint(6, -127, 200)
m.move_joint(7, -127, 200)

sleep(2)    #Wait for Marty to stablise

#Twist knees back
m.move_joint(1, 10, 200)
m.move_joint(4, 10, 200)

sleep(2)    #Wait for Marty to stablise

#Pull legs in
m.move_joint(2, 0, 200)
m.move_joint(5, 0, 200)
sleep(1)

#Lean back
m.move_joint(0, 0, 200)
m.move_joint(3, 0, 200

#Re-enable safeties
m.enable_safeties(True)
m.fall_protection(True)
