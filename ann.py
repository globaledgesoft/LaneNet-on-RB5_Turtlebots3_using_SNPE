import cv2
import numpy as np
import json

img = cv2.imread('/path_to_DATASET/train_set/clips/1-50/1.jpg')
def serialize_int64(obj):
    if isinstance(obj, np.int64):
        return int(obj)
    raise TypeError ("Type %s is not serializable" % type(obj))

y = list(range(240,720,10)) #hsamples--height
x = np.array(y)
x[:] = -2

for i in range (240, 720, 10):
    cv2.line(img, (0, i), (1280, i), (255,128,64), 1)
cv2.imshow('image', img)

l_list = list(x)
r_list = list(x)
lm_list = list(x)
rm_list = list(x)
m_list = list(x)
#mm_list = list(x)

def mouse_click(event, x, y, flags, param):
    index_y = round((y - 240) / 10)
    if event == cv2.EVENT_LBUTTONDOWN:
        l_list[index_y] = x
        cv2.circle(img, (x, y), 5, (255, 255, 0), -1)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        r_list[index_y] = x
        cv2.circle(img, (x, y), 5, (0, 255, 255), -1)
        cv2.imshow('image', img)
    if event == cv2.EVENT_MBUTTONDOWN:
        m_list[index_y] = x
        cv2.circle(img, (x, y), 5, (255, 0, 255), -1)
        cv2.imshow('image', img)

cv2.setMouseCallback('image', mouse_click)
cv2.waitKey(0)
filename='167.jpg'
cv2.imwrite(filename, img)

lane = [lm_list, l_list, m_list, r_list, rm_list]
#lane = [l_list, m_list, r_list]
lane_ann = dict()
lane_ann["lanes"] = lane
lane_ann["h_samples"] = y
lane_ann["raw_file"] = "167.jpg"
print (lane_ann)

# json.dump(str(lane_ann), open("frame0.json", "w"))
with open("167.json", "w", encoding="utf8") as outfile:
    json.dump(lane_ann, outfile, default=serialize_int64)
# json_str = json.dumps(score_dict, )

# close all the opened windows.
cv2.destroyAllWindows()

