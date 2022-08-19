import json
import os
import shutil
import os
import math
import cv2

transforms = json.load(open("./fox/transforms.json"))
w = 1440.0
h = 1920.0
fl_x = 1470.5321044921875
fl_y = 1470.5321044921875
cx = 721.2457275390625
cy = 949.34326171875
aabb_scale = 1
scale = 1
offset = [0.5, 0.7, 0.5]


transforms["camera_angle_x"] = math.atan(w / (fl_x * 2)) * 2
transforms["camera_angle_y"] = math.atan(h / (fl_y * 2)) * 2
transforms["fl_x"] = fl_x
transforms["fl_y"] = fl_y
transforms["cx"] = cx
transforms["cy"] = cy
transforms["w"] = w
transforms["h"] = h
transforms["aabb_scale"] = aabb_scale
transforms["scale"] = scale
transforms["offset"] = offset
transforms["k1"] = 0
transforms["k2"] = 0
transforms["p1"] = 0
transforms["p2"] = 0

trans_example = transforms["frames"][0]

max = [-1000.0, -1000.0, -1000.0]
min = [1000.0, 1000.0, 1000.0]

for t in transforms["frames"]:
    tt = t["transform_matrix"]
    point = [tt[0][3], tt[1][3], tt[2][3]]
    for k in range(3):
        if min[k] > point[k]:
            min[k] = point[k]
        if max[k] < point[k]:
            max[k] = point[k]

print(min)
print(max)
s = 0
for k in range(3):
    s += (max[k] - min[k])**2
print(math.sqrt(s))

transforms["frames"] = []

max = [-1000.0, -1000.0, -1000.0]
min = [1000.0, 1000.0, 1000.0]

dataset_path = "horse/"
transform_path = dataset_path + "transforms"
for base_path, folder_list, file_list in os.walk(transform_path):
    for file_name in file_list:
        file_path = os.path.join(base_path, file_name)
        file_ext = file_path.rsplit('.', maxsplit=1)
        if len(file_ext) != 2:
            continue
        if file_ext[1] != 'json':
            continue
        temp = json.load(open(file_path))
        frame_id = temp["frame_index"]
        frame_path = "images/frame_{:05}.jpg".format(frame_id)
        full_frame_path = dataset_path + frame_path
        # if not os.path.exists(full_frame_path):
        #     continue

        tm = temp["cameraPoseARFrame"]
        tt = [[0 for c0 in range(4)] for c1 in range(4)]
        for c0 in range(4):
            for c1 in range(4):
                tt[c0][c1] = tm[c0 * 4 + c1]
        tt[3][3] = 1

        point = [tt[0][3], tt[1][3], tt[2][3]]
        for k in range(3):
            if min[k] > point[k]:
                min[k] = point[k]
            if max[k] < point[k]:
                max[k] = point[k]
        t = dict(trans_example)
        t["file_path"] = frame_path
        t["transform_matrix"] = tt
        transforms["frames"].append(t)

center = [(min[i] + max[i]) / 2 for i in range(3)]

transforms["frames"].sort(key=lambda x: x["file_path"])
cnt = 0
for frame in transforms["frames"]:
    trans = frame["transform_matrix"]
    for k in range(3):
        trans[k][3] -= center[k]
        trans[k][3] *= 1
    point = [trans[0][3], trans[1][3], trans[2][3]]
    frame["transform_matrix"] = trans
    print(cnt, point)
    cnt+=1


print(min)
print(max)
s = 0
for k in range(3):
    s += (max[k] - min[k])**2
print(math.sqrt(s))

f = open(dataset_path + "transforms.json", "w")
json.dump(transforms, f)
# print(len(transforms["frames"]))
# # for i in range()
# print(transforms["frames"][0])
# j = 0
# for i in range(115):
#     pth = "images/{:04}.jpg".format(i)
#     if os.path.exists(pth):
#         if j % 5 == 0:
#             shutil.copy(pth, "images_/{:04}.jpg".format(i))
#             j = 0
#     j += 1
