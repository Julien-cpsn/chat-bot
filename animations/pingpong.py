from naoqi import ALProxy

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0, 0.04, 3.96])
keys.append([-0.377457, -0.377457, -0.377457])

names.append("HipPitch")
times.append([0, 0.04, 3.96])
keys.append([-0.0431505, -0.0431505, -0.0431505])

names.append("LElbowRoll")
times.append([0, 0.04, 1.96, 3.16, 3.96])
keys.append([-0.629568, -0.629568, -0.842382, -1.02556, -0.629568])

names.append("LElbowYaw")
times.append([0, 0.04, 3.16, 3.96])
keys.append([-1.86401, -1.86401, -1.03621, -1.86401])

names.append("LShoulderPitch")
times.append([0, 0.04, 1.96, 3.16, 3.96])
keys.append([1.77102, 1.77102, -0.237718, 0.0204344, 1.77102])

names.append("LShoulderRoll")
times.append([1.96, 3.16])
keys.append([1.13426, 0.0750492])

names.append("RElbowRoll")
times.append([0, 0.04, 1.96, 3.96])
keys.append([0.549779, 0.549779, -0.633784, 0.549779])

names.append("RElbowYaw")
times.append([0, 0.04, 1.96, 3.96])
keys.append([1.68655, 1.68655, -0.426974, 1.68655])

names.append("RShoulderPitch")
times.append([0, 0.04, 1.96, 3.96])
keys.append([1.74858, 1.74858, 0.925562, 1.74858])

names.append("RShoulderRoll")
times.append([0, 0.04, 3.96])
keys.append([-0.102052, -0.102052, -0.102052])


# Time adjustment
for row_index in range(0, len(times)):
    for column_index in range(0, len(times[row_index])):
        times[row_index][column_index] += 2

try:
    motion = ALProxy("ALMotion", "127.0.0.1", 9559)
    motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
    print err
