# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0, 0.04, 5.96])
keys.append([-0.377457, -0.377457, -0.377457])

names.append("HipPitch")
times.append([0, 0.04, 5.96])
keys.append([-0.0431505, -0.0431505, -0.0431505])

names.append("LElbowRoll")
times.append([1.56, 2.36, 2.76, 3.16, 3.56, 3.96, 4.36])
keys.append([-0.755284, -0.939588, -0.564563, -0.939588, -0.564563, -0.939588, -0.564563])

names.append("LShoulderPitch")
times.append([0, 0.04, 1.56, 1.96, 2.36, 3.16, 3.96, 5.96])
keys.append([1.77102, 1.77102, 1.3276, 1.542, 1.29716, 1.29716, 1.29716, 1.77102])

names.append("RElbowRoll")
times.append([0, 0.04, 1.56, 1.96, 5.96])
keys.append([0.0985441, 0.0985441, 0.851545, 0.909483, 0.0985441])

names.append("RElbowYaw")
times.append([0, 0.04, 1.56, 5.96])
keys.append([1.68655, 1.68655, 1.35367, 1.68655])

names.append("RHand")
times.append([1.56, 1.96, 2.36, 2.76, 3.16, 3.56, 3.96, 4.36])
keys.append([-0.751755, 0.93, 0.02, 0.98, 0.02, 0.98, 0.02, 0.98])

names.append("RShoulderPitch")
times.append([0, 0.04, 1.56, 2.36, 2.76, 3.16, 3.56, 3.96, 4.36, 5.96])
keys.append([1.74858, 1.74858, 0.0523639, 0.217673, 0.15196, 0.217674, 0.15196, 0.217674, 0.15196, 1.74858])

names.append("RShoulderRoll")
times.append([0, 0.04, 5.96])
keys.append([-0.102052, -0.102052, -0.102052])

names.append("RWristYaw")
times.append([1.96])
keys.append([0.381309])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
