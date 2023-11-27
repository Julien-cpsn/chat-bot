from naoqi import ALProxy

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0, 0.04, 4.36])
keys.append([-0.377457, -0.377457, -0.377457])

names.append("HipPitch")
times.append([0, 0.04, 4.36])
keys.append([-0.0431505, -0.0431505, -0.0431505])

names.append("LShoulderPitch")
times.append([0, 0.04, 4.36])
keys.append([1.77102, 1.77102, 1.77102])

names.append("RElbowRoll")
times.append([0, 0.04, 1.56, 3.96, 4.36])
keys.append([0.549779, 0.539307, 0.0802851, 0.0855211, 0.482335])

names.append("RElbowYaw")
times.append([0, 0.04, 1.56, 3.96, 4.36])
keys.append([1.68655, 1.68655, -0.305972, -0.305972, 1.68655])

names.append("RHand")
times.append([1.56, 3.96])
keys.append([0.98, 0.98])

names.append("RShoulderPitch")
times.append([0, 0.04, 1.56, 3.96, 4.36])
keys.append([1.74858, 1.74858, -0.456874, -0.456875, 1.74858])

names.append("RShoulderRoll")
times.append([0, 0.04, 1.56, 3.96, 4.36])
keys.append([-0.102052, -0.102052, -0.0485764, -0.0485764, -0.102052])


# Time adjustment
for row_index in range(0, len(times)):
    for column_index in range(0, len(times[row_index])):
        times[row_index][column_index] += 2

try:
    motion = ALProxy("ALMotion", "127.0.0.1", 9559)
    motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
    print err
