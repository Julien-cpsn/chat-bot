from naoqi import ALProxy

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0, 0.04, 5.36])
keys.append([-0.377457, -0.377457, -0.377457])

names.append("HipPitch")
times.append([0, 0.04, 5.36])
keys.append([-0.0431505, -0.0431505, -0.0431505])

names.append("LElbowRoll")
times.append([0.04, 5.36])
keys.append([-0.467057, -0.467057])

names.append("LElbowYaw")
times.append([1.96])
keys.append([-1.1866])

names.append("LHand")
times.append([1.96, 2.36, 2.76, 3.16, 3.56])
keys.append([0.98, -0.146283, 0.98, 0.02, 0.98])

names.append("LShoulderPitch")
times.append([0, 0.04, 1.96, 2.36, 2.76, 3.16, 3.56, 4.76, 5.36])
keys.append([1.77102, 1.77102, 0.461752, 0.0666969, 0.0666969, 0.0666969, 0.0666969, 0.0666969, 1.77102])

names.append("LShoulderRoll")
times.append([1.96])
keys.append([0.241485])

names.append("RElbowRoll")
times.append([0, 0.04, 2.36, 5.36])
keys.append([0.549779, 0.444428, 0.581154, 0.444427])

names.append("RElbowYaw")
times.append([0, 0.04, 1.96, 2.36, 5.36])
keys.append([1.68655, 1.51742, 0.553238, 0.744148, 1.51742])

names.append("RHand")
times.append([1.96, 2.36, 2.76, 3.16, 3.56])
keys.append([0.98, 0.04, 0.98, 0.02, 0.98])

names.append("RShoulderPitch")
times.append([0, 0.04, 1.96, 2.36, 2.76, 3.16, 3.56, 4.76, 5.36])
keys.append([1.74858, 1.74858, 0.471654, 0.0693366, 0.0693367, 0.0693367, 0.0693367, 0.0693367, 1.74858])

names.append("RShoulderRoll")
times.append([0, 0.04, 1.96, 5.36])
keys.append([-0.102052, -0.102052, -0.481011, -0.102052])


# Time adjustment
for row_index in range(0, len(times)):
    for column_index in range(0, len(times[row_index])):
        times[row_index][column_index] += 2

try:
    motion = ALProxy("ALMotion", "127.0.0.1", 9559)
    motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
    print err
