import cv2
import numpy as np
cascade=cv2.CascadeClassifier('D:\\PROJECT\\Face detection live\\haarcascade_frontalface_default.xml')
  
url = 'http://192.168.1.2:8080/video'
cap = cv2.VideoCapture(url)
vid = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("D:\\PROJECT\\2Cam\\cam_video1.mp4", vid_cod, 20.0, (400,400))
while(True):
    ret, frame = cap.read()
    ret1, frame1 = vid.read()
    frame=cv2.resize(frame,(400,400))
    frame1=cv2.resize(frame1,(400,400))
    both = np.concatenate((frame, frame1), axis=1)
    #############################################################################
    gray=cv2.cvtColor(both,cv2.COLOR_BGR2GRAY)
    face=cascade.detectMultiScale(gray,1.3,5)
    for (fx,fy,fw,fh) in face:
        cv2.rectangle(both,(fx,fy),(fx+fw,fy+fh),(0,0,255),3)
    #############################################################################
    
    cv2.imshow('Both',both)
 
    output.write(both)  
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
# After the loop release the cap object 
vid.release()
cap.release()
# Destroy all the windows 
cv2.destroyAllWindows()

#########################################################################################################################

def jsontocsv(Input_File,Output_File,Dataset_Name='NULL',header=1):
    import json
    import csv
    with open(Input_File) as json_file:
        data=json.load(json_file)
    if Dataset_Name!='NULL':
        data=data[Dataset_Name]
    O_file=open(Output_File+'.csv','w')
    csv_writer=csv.writer(O_file)
    for d in data:
        if header==1:
            h=d.keys()
            csv_writer.writerow(h)
            header+=1
        csv_writer.writerow(d.values())
    O_file.close()

