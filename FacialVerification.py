
import face_recognition
import os
import glob




def Compute():
    count1=0
    count2=0
    count3=0
    print("Location1 %s \n Location2 %s"% (e1.get(), e2.get()))
    path1=e1.get()
    path2=e2.get()
    s=e3.get()
    spec=float(s)
    htmlp="<html><head> <style > img{width:35%;height:60% } </style> </head> <body>"
    htmlnp="<html><head> <style > img{width:35%;height:60% } </style> </head> <body>"
    search1=path1+"/*.jpg"
    for filepath in glob.iglob(search1):
        str1=str(filepath)
        sp=str1.split('\\',1)[1]
        search2=path2 + "/" +sp     
        if os.path.isfile(search2):
                       
         
            name1=path1+"/"+sp
            name2=path2+"/"+sp
            known=face_recognition.load_image_file(name1)
            enc1=face_recognition.face_encodings(known)
            if len(enc1)>0:
                obama_face=enc1[0]
                known_encodings=[
                    obama_face
                ] 
                image_to_test=face_recognition.load_image_file(name2)
                enc2=face_recognition.face_encodings(image_to_test)

                if len(enc2)>0:
                    image_to_test_encoding=enc2[0]    
                    face_dist=face_recognition.face_distance(known_encodings,image_to_test_encoding)
                    if face_dist<=spec:
                        htmlp+="<br><tr><td>" + str(count1)  +"</td><td> <img src=\"" + name1 + "\" > </td> <td> <img src=\"" + name2 + "\" > </td><td>" + str(face_dist) + " </td></tr> \n" 
                        count1=count1+1
                        
                    else:
                        htmlnp+="<br><tr><td>" +str(count2) + "</td><td><img src=\"" + name1 + "\" > </td>   <img src=\"" + name2 + "\" > </td><td> " + str(face_dist) + "</td></tr> \n"
                        #print(htmlp)    
                        count2=count2+1

                    for i,face_distance in enumerate(face_dist):
                        print("The image is " + sp)
                        print("The distance is has a distance of {:2} from known image #{}".format(face_distance,i))
                    
        
                else:    
                    print("No face found in second image")        
                    htmlnp+="<br><tr><td> "+str(count2)+ "</td><td> <img src=\"" + name1 + "\" > </td><td>  <img src=\"" + name2 + "\" > </td></tr> \n"        
                    count2=count2+1
        #print("########")


            else:
                print("No face for image " + sp)
                print("####")
                htmlnp+="<br><tr><td>" + str(count2) + "</td><td><img src=\"" + name1 + "\" > </td><td>  <img src=\"" + name2 + "\" ></td></tr> \n"
                count2=count2+1
    
       

    htmlp=htmlp + "</body></html>"     
    f=open("Matched.html","w+")
    f.write(htmlp)
    f.close()

    htmlnp=htmlnp + "</body></html>"     
    f=open("NoFaceDetected.html","w+")
    f.write(htmlnp)
    f.close()


    print("The number of people detected correctly is " + str(count1))
    print("The number of people above spec  is " + str(count2))
#    print("The number of people whose face is not found is " + str(count3))

from tkinter import *
master=Tk()
Label(master, text='Bigger Folder').grid(row=0) 
Label(master, text='Lesser Folder').grid(row=1)
Label(master, text='Enter Specificity').grid(row=2)

e1 = Entry(master) 
e2 = Entry(master) 
e3 = Entry(master)
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)
e3.grid(row=2,column=1)
Button(master, text='Show', command=Compute).grid(row=3, column=1, sticky=W, pady=4)



mainloop() 


