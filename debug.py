import time 

list_urls=[]
base_ar="C:\\Users\\ogome\\Videos\\Blue Shark\\"
f=open('links.txt','r')
f_lines=f.readlines()
#print(len(f_lines)) #len(f_lines) da el número de links/lineas en el archivo

# for x in f_lines: #Este for nos va dando cada elemnto (link) en el .txt 
#     print(x)
#     time.sleep(1)

number_to_save=int(input('Inserta el consecutivo para tu vid: '))
for x in range(len(f_lines)):
    i=number_to_save+x
    name_video=base_ar+str(i)+'.mp4'
    #print(name_video)
    list_urls.append(name_video)

for (a,b) in zip(f_lines,list_urls):
    print(b)

    
    