from tkinter import *
from PIL import Image, ImageTk
from client import Fenetre_Client
from chambre import Fenetre_chambre
from details import Fenetre_Details

class GestionHotelSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("SYSTEME DE GESTION D'HOTEL")
        self.root.geometry("1550x800+0+0")


        #=========sary ambony iny===========
        img1 = Image.open(r"E:\Lorniot Marcel (leçons) L2\Python\Projet\ProjetPython\GestionHotel\image\HorizonGolden.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimag = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimag.place(x=0, y=0, width=1550, height=140)


         #=========logo ambony iny===========
        img2 = Image.open(r"E:\Lorniot Marcel (leçons) L2\Python\Projet\ProjetPython\GestionHotel\image\logo.jpg")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimag = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimag.place(x=0, y=0, width=230, height=140)


         #=========Titre ambony eo iny===========
        lbl_title =Label(self.root,text="LORNIOT'S HOTEL MANAGEMENT", font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #=========Principal toy ===========
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)


        #=========Menu toy ===========
        lbl_menu =Label(main_frame,text="MENU", font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

         #=========amin'ny partie menu eo toy ===========
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=190)

        cust_btn=Button(btn_frame,text="CLIENT",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="CHAMBRE",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",width=22,font=("times new roman",14,"bold"),command=self.details,bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="Generation du facture",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,command=self.logout,text="DECONNEXION",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=3,column=0,pady=1)



        #======image a droite anatiny menu ao io=============
        img3 = Image.open(r"E:\Lorniot Marcel (leçons) L2\Python\Projet\ProjetPython\GestionHotel\image\FantoriaAminPiscine.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimag1= Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimag1.place(x=225, y=0, width=1310, height=590)

        #======image a droite anatiny menu ao io=============
        img4 = Image.open(r"E:\Lorniot Marcel (leçons) L2\Python\Projet\ProjetPython\GestionHotel\image\SalleReceptionChicRouge.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimag1= Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimag1.place(x=0, y=225, width=230, height=210)



        img5 = Image.open(r"E:\Lorniot Marcel (leçons) L2\Python\Projet\ProjetPython\GestionHotel\image\ChambreVueMer.jpg")
        img5 = img5.resize((230, 190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimag1= Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimag1.place(x=0, y=420, width=230, height=190)
    

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Fenetre_Client(self.new_window)



    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Fenetre_chambre(self.new_window)



    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=Fenetre_Details(self.new_window)

    def logout(self):
        self.root.destroy()







if __name__ == "__main__":
    root = Tk()
    obj = GestionHotelSystem(root)
    root.mainloop()

    