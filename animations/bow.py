# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0, 0.04, 1.56, 2.36, 6.36, 7.16, 7.96])
keys.append([-0.377458, -0.377457, -0.3735, 0.445059, 0.445059, -0.378736, -0.377457])

names.append("HipPitch")
times.append([0, 0.04, 1.56, 7.16, 7.96])
keys.append([-0.0431505, -0.0431505, -1.03847, -1.03847, -0.0431505])

names.append("LShoulderPitch")
times.append([0, 0.04, 7.96])
keys.append([1.77102, 1.77102, 1.77102])

names.append("RElbowRoll")
times.append([0, 0.04, 7.96])
keys.append([0.0985442, 0.0985441, 0.0985441])

names.append("RElbowYaw")
times.append([0, 0.04, 7.96])
keys.append([1.68655, 1.68655, 1.68655])

names.append("RShoulderPitch")
times.append([0, 0.04, 7.96])
keys.append([1.74858, 1.74858, 1.74858])

names.append("RShoulderRoll")
times.append([0, 0.04, 7.96])
keys.append([-0.102052, -0.102052, -0.102052])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
