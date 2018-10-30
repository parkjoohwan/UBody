import json

json_data=open("test2.json").read()

data = json.loads(json_data)

parts = []

for i in range (0,18):
    parts += [data["people"][0]["pose_keypoints_2d"][i*3],data["people"][0]["pose_keypoints_2d"][i*3+1]]

people_data = {
    "Nos"  : [parts[0],parts[1]],
    "Nck"  : [parts[2],parts[3]],
    "Rsh"  : [parts[4],parts[5]],
    "Rel"  : [parts[6],parts[7]],
    "Rwr"  : [parts[8],parts[9]],
    "Lsh"  : [parts[10],parts[11]],
    "Lel"  : [parts[12],parts[13]],
    "Lwr"  : [parts[14],parts[15]],
    "Rhp"  : [parts[16],parts[17]],
    "Rkn"  : [parts[18],parts[19]],
    "Ran"  : [parts[20],parts[21]],
    "Lhp"  : [parts[22],parts[23]],
    "Lkn"  : [parts[24],parts[25]],
    "Lan"  : [parts[26],parts[27]],
    "Rey"  : [parts[28],parts[29]],
    "Ley"  : [parts[30],parts[31]],
    "Rer"  : [parts[32],parts[33]],
    "Ler"  : [parts[34],parts[35]],}
