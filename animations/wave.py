from naoqi import ALProxy

names = list()
times = list()
keys = list()

names.append("LShoulderPitch")
times.append([0.01, 5.96])
keys.append([1.83609, 1.83609])

names.append("RElbowRoll")
times.append([0.01, 1.56, 1.76, 1.96, 2.16, 2.36, 2.56, 2.76, 2.96, 3.16, 3.36, 5.96])
keys.append(
    [0.116937, 0.501723, 1.03031, 0.366519, 1.03031, 0.366519, 1.03031, 0.366519, 1.03031, 0.366519, 1.03031, 0.116937])

names.append("RElbowYaw")
times.append([0.01, 1.56, 5.96])
keys.append([1.71391, 0.315578, 1.71391])

names.append("RShoulderPitch")
times.append([0.01, 1.56, 5.96])
keys.append([1.83609, -1.16413, 1.83609])

names.append("RShoulderRoll")
times.append([0.01, 1.56, 5.96])
keys.append([-0.116937, -0.840046, -0.116937])


# Time adjustment
for row_index in range(0, len(times)):
    for column_index in range(0, len(times[row_index])):
        times[row_index][column_index] += 2

try:
    motion = ALProxy("ALMotion", "127.0.0.1", 9559)
    motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
    print err
