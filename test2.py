#-*-coding:utf-8-*-
import cv2
from subprocess import call
import Jsontest as js
#오픈포즈 실행 렌더링파일 만들기 && json 파일 만들기
#cmd = '''./build/examples/openpose/openpose.bin --image_dir ./CVimg/ --write_images ./CVredering/ --display 0'''
#cmd2 = '''./build/examples/openpose/openpose.bin --image_dir ./CVimg/ --write_json ./CVjson/ --display 0'''
#cmd_args = cmd.split()
#cmd2_args = cmd2.split()
#call(cmd_args)
#call(cmd2_args)

 # 해야할것
 # 각 포인트 별 좌표 받아오는 함수 만들고 (17? 19개)
 # 일단 어깨 y값 비교하는 함수 만들기(1개)
 # 원하는 포인트부터 끝 포인트까지 선으로 두께 두껍게해서 그리는 함수 만들기

# 노터치 

img_color = cv2.imread('test2_origin.jpg', cv2.IMREAD_COLOR )

cv2.imshow("color image", img_color)
print(type(img_color))

flag = False;

def getData(a):
    if(a not in js.people_data.keys()):
        print("그런 값은 없습니다.")
    else:
        return [ js.people_data[a][0],js.people_data[a][1]]

#왼어깨 - 오른어깨
#왼골반 - 오른골반
#왼무릎 - 오른무릎
#각 부위 별

Rsh = getData("Rsh")
Lsh = getData("Lsh")
Rhp = getData("Rhp")
Lhp = getData("Lhp")
Rkn = getData("Rkn")
Lkn = getData("Lkn")

img_h = img_color.shape[0]
img_w = img_color.shape[1]

#data1 = getData("Rsh") - getData("Lsh")
#data2 = getData("Rhp") - getData("Lhp")
#data3 = getData("Rkn") - getData("Lkn")


#data = getData("Lsh")
#data2 = getData("Rhp")
#data3 = getData("Lhp")

while True:

    k = cv2.waitKey(0) & 0xFF
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
        break

    elif k == ord('s'): # wait for 's' key to save


        flag = not flag
        img_show = None

        if flag :
            for w in range(1,img_w):
                if( w%int((img_w/10)) == 0 ):
                    img_show = cv2.line(img_color, (w, 0), (w, img_h), (189, 189, 189), 1)
                if( w == int(img_w/10)*5 ):
                    img_show = cv2.line(img_color, (w, 0), (w, img_h), (0, 0, 255), 1)
            for h in range(1,img_h):
                if( h%int((img_h/10)) == 0 ):
                    img_show = cv2.line(img_color, (0, h), (img_w, h), (189, 189, 189), 1)
                if (h == int(img_h / 10) * 5):
                    img_show = cv2.line(img_color, (0, h), (img_w, h), (0, 0, 255), 1)
            img_show = cv2.line(img_color, ( int(Rsh[0]),int(Rsh[1]) ) , ( int(Lsh[0]),int(Lsh[1]) ), (255,255,255), 2)
            img_show = cv2.line(img_color, (int(Rhp[0]), int(Rhp[1])), (int(Lhp[0]), int(Lhp[1])), (255, 255, 255), 2)
            img_show = cv2.line(img_color, (int(Rkn[0]), int(Rkn[1])), (int(Lkn[0]), int(Lkn[1])), (255, 255, 255), 2)
            img_show = cv2.circle(img_color, (int(Rsh[0]),int(Rsh[1]) ), 5, (0,0,255), -1)
            img_show = cv2.circle(img_color, (int(Lsh[0]), int(Lsh[1])), 5, (0, 0, 255), -1)
            img_show = cv2.circle(img_color, (int(Rhp[0]), int(Rhp[1])), 5, (0, 0, 255), -1)
            img_show = cv2.circle(img_color, (int(Lhp[0]), int(Lhp[1])), 5, (0, 0, 255), -1)
            img_show = cv2.circle(img_color, (int(Rkn[0]), int(Rkn[1])), 5, (0, 0, 255), -1)
            img_show = cv2.circle(img_color, (int(Lkn[0]), int(Lkn[1])), 5, (0, 0, 255), -1)
        else :
            img_show = img_color

        cv2.imwrite('savedimage.png',img_show)
        cv2.imshow("color image", img_show)

