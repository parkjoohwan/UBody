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

img_color = cv2.imread('test_rendered.png', cv2.IMREAD_COLOR )

cv2.imshow("color image", img_color)
print(type(img_color))

flag = False;

def getData(a):
    if(a not in js.people_data.keys()):
        print("그런 값은 없습니다.")
    else:
        return [ js.people_data[a][0],js.people_data[a][1]]



data = getData("Rhp")

while True:

    k = cv2.waitKey(0) & 0xFF
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
        break

    elif k == ord('s'): # wait for 's' key to save


        flag = not flag
        img_show = None

        if flag :
             img_show = cv2.circle(img_color, (int(data[0]),int(data[1]) ), 15, (0,0,255), -1)

        else :
            img_show = img_color

        cv2.imwrite('savedimage.png',img_show)
        cv2.imshow("color image", img_show)

