from naoqi import ALProxy

names = list()
times = list()
keys = list()

names.append("LElbowRoll")
times.append([0.01, 0.16, 1.56, 1.96, 2.36, 2.76, 3.16, 3.36, 6.56])
keys.append([-0.136136, -0.136136, -1.3631, -1.3631, -1.3631, -1.3631, -1.3631, -0.289143, -0.136136])

names.append("LElbowYaw")
times.append([0.01, 0.16, 1.56, 1.76, 1.96, 2.16, 2.36, 2.56, 2.76, 2.96, 3.16, 3.36, 6.56])
keys.append(
    [-1.70868, -1.70868, -0.903287, -1.22638, -0.903286, -1.22638, -0.903286, -1.22638, -0.903286, -1.22638, -0.903286,
     -1.23918, -1.70868])

names.append("LShoulderPitch")
times.append([0.01, 0.16, 1.56, 1.96, 2.36, 2.76, 3.16, 3.36, 6.56])
keys.append([1.83609, 1.83609, -0.413643, -0.413643, -0.413643, -0.413643, -0.413643, -0.921534, 1.83609])

names.append("LShoulderRoll")
times.append([0.01, 0.16, 1.56, 1.96, 2.36, 2.76, 3.16, 3.36, 6.56])
keys.append([0.125664, 0.125664, -0.408698, -0.408699, -0.408699, -0.408699, -0.408699, 0.600393, 0.125664])

names.append("RElbowRoll")
times.append([0.01, 0.16, 1.56, 1.96, 2.36, 2.76, 3.16, 3.36, 6.56])
keys.append([0.116937, 0.116937, 1.37008, 1.37008, 1.37008, 1.37008, 1.37008, 0.282743, 0.116937])

names.append("RElbowYaw")
times.append([0.01, 0.16, 1.56, 1.76, 1.96, 2.16, 2.36, 2.56, 2.76, 2.96, 3.16, 3.36, 6.56])
keys.append(
    [1.71391, 1.71391, 0.951038, 1.25569, 0.951039, 1.25569, 0.951039, 1.25569, 0.951039, 1.25569, 0.951039, 1.23744,
     1.71391])

names.append("RShoulderPitch")
times.append([0.01, 0.16, 1.56, 1.96, 2.36, 2.76, 3.16, 3.36, 6.56])
keys.append([1.83609, 1.83609, -0.397935, -0.397935, -0.397935, -0.397935, -0.397935, -0.904203, 1.83609])

names.append("RShoulderRoll")
times.append([0.01, 0.16, 1.56, 1.96, 2.36, 2.76, 3.16, 3.36, 6.56])
keys.append([-0.116937, -0.116937, 0.060684, 0.060684, 0.060684, 0.060684, 0.060684, -0.60912, -0.116937])


# Time adjustment
for row_index in range(0, len(times)):
    for column_index in range(0, len(times[row_index])):
        times[row_index][column_index] += 2

try:
    motion = ALProxy("ALMotion", "127.0.0.1", 9559)
    motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
    print err
