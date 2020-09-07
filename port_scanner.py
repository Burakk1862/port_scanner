from tkinter import *
import datetime
import socket
portListe=[]
bannerListe=[]

def ip_tara():
    x = int(entry3.get())
    ipler=entry1.get()
    for ip in ipler.splitlines():
        for port in range(x,25):
            try:
                soket=socket.socket()
                soket.connect((str(ip),int(port)))
                banner=soket.recv(1024)
                banner_liste.append(str(banner))
                port_liste.append(str(port))
                soket.close()
                v.set(portListe)
                v2.set(bannerListe)
            except:
                pass
top=Tk()
top.title("PORT TARAMA")
label1=Label(top,text="PORT TARAMAYA HOŞ GELDİNİZ")
label1.place(x=50,y=80)
label1.pack()
label2=Label(top,text="İP ADRESİNİ GİRİNİZ")
label2.place(x=0,y=0)
label2.pack()
entry1=Entry(top)
entry1.place(x=50,y=90)
entry1.pack()
v=StringVar()
v2=StringVar()
label3=Label(top,text="AÇIK PORTLAR")
label3.place(x=0,y=0)
label3.pack()
entry2=Entry(top,textvariable=v)
entry2.place(x=50,y=100)
entry2.pack()
label5=Label(top,text="Çalışan servisler")
label5.place(x=0,y=0)
label5.pack()
entry4=Entry(top,textvariable=v2)
entry4.place(x=50,y=100)
entry4.pack()
label4=Label(top,text="başlangıç portunu yazınız")
label4.place(x=0,y=0)
label4.pack()
entry3=Entry(top)
entry3.place(x=50,y=110)
entry3.pack()
B=Button(top,text="PORT TARA",command=ip_tara)
B.place(x=50,y=50)
B.pack()
top.mainloop()
