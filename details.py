from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Fenetre_Details:
    def __init__(self, root):
        self.root = root
        self.root.title("SYSTEME DE GESTION D'HOTEL")
        self.root.geometry("1128x520+230+220")


        #=========Titre ambony eo iny===========
        lbl_title =Label(self.root,text="DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

         #=========logo ambony iny===========
        img2 = Image.open(r"E:\Lorniot Marcel (leçons) L2\Python\Projet\ProjetPython\GestionHotel\image\logo.jpg")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimag = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimag.place(x=5, y=2, width=100, height=40)

                #=========label ===========
        labelframeleft=LabelFrame(self.root,relief=RIDGE,text="Ajouter une chambre",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=540,height=350)

         # etage iny koa lahy toy eeeee
        lbl_etage=Label(labelframeleft,text="Numéro d'Etage :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_etage.grid(row=0,column=0,sticky=W)
        self.var_Numero_d_Etage=StringVar()
        entry_etage=ttk.Entry(labelframeleft,textvariable=self.var_Numero_d_Etage,width=20,font=("arial",10,"bold"))
        entry_etage.grid(row=0,column=1,sticky=W)

         # numero chambre iny koa lahy toy eeeee
        lbl_NumeroChambre=Label(labelframeleft,text="Numéro de la chambre :",font=("arial",10,"bold"),padx=2,pady=6)
        self.var_Numero_de_la_chambre=StringVar()
        lbl_NumeroChambre.grid(row=1,column=0,sticky=W)
        entry_NumeroChambre=ttk.Entry(labelframeleft,textvariable=self.var_Numero_de_la_chambre,width=20,font=("arial",10,"bold"))
        entry_NumeroChambre.grid(row=1,column=1,sticky=W)


         # type iny koa lahy toy eeeee
        lbl_Type_chambre=Label(labelframeleft,text="Type de la chambre :",font=("arial",10,"bold"),padx=2,pady=6)
        self.var_Type_de_la_chambre=StringVar()
        lbl_Type_chambre.grid(row=2,column=0,sticky=W)
        entry_Type_chambre=ttk.Entry(labelframeleft,textvariable=self.var_Type_de_la_chambre,width=20,font=("arial",10,"bold"))
        entry_Type_chambre.grid(row=2,column=1,sticky=W)

                # ======== boutton CRUD reny==========
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=390,height=40)

        btnAdd=Button(btn_frame,command=self.add_data,text="Ajouter",font=("arial",12,"bold"),bg="green",fg="white",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,command=self.update,text="Modifier",font=("arial",11,"bold"),bg="purple",fg="white",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,command=self.mDelete,text="Supprimer",font=("arial",11,"bold"),bg="red",fg="white",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,command=self.reset,text="Vider",font=("arial",12,"bold"),bg="black",fg="white",width=9)
        btnReset.grid(row=0,column=3,padx=1)




         # ======== Table amin'ny CRUD==========
         #=========label ===========
        Table_Frame=LabelFrame(self.root,relief=RIDGE,text="Affichage des chambres",font=("times new roman",12,"bold"),padx=2,)
        Table_Frame.place(x=550,y=51,width=570,height=350)


        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,columns=("Numero_d_Etage ","Numero_de_la_chambre ","Type_de_la_chambre "),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("Numero_d_Etage ",text="Numero_d_Etage ")
        self.room_table.heading("Numero_de_la_chambre ",text="Numero_de_la_chambre ")
        self.room_table.heading("Type_de_la_chambre ",text="Type_de_la_chambre ")

        self.room_table["show"]="headings"

        self.room_table.column("Numero_d_Etage ",width=100)
        self.room_table.column("Numero_de_la_chambre ",width=100)
        self.room_table.column("Type_de_la_chambre ",width=100)
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    # l'ajout des donnees
    def add_data(self):
            if self.var_Numero_d_Etage.get() == "" or self.var_Type_de_la_chambre.get() == "":
                messagebox.showerror("Erreur","Veuillez remplir les champs",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
                    my_cursor=conn.cursor()
                    my_cursor.execute("INSERT INTO details VALUES(%s,%s,%s)", (
                        self.var_Numero_d_Etage.get(),
                        self.var_Numero_de_la_chambre.get(),
                        self.var_Type_de_la_chambre.get()
                    ))  
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Chambre ajouté avec succès",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Attention",f"Veuillez vérifier l'erreur : {str(es)}",parent=self.root)

    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM details")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close()



       # affichage donnees fa amin'ny table eo ho amin'ny champ eo 
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_Numero_d_Etage.set(row[0])
        self.var_Numero_de_la_chambre.set(row[1])
        self.var_Type_de_la_chambre.set(row[2])


    # toy ty modification koa lahy eeeee
    def update(self):
        if self.var_Numero_d_Etage.get() == "":
            messagebox.showerror("Erreur", "Veuillez remplir le numéro", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE details SET Numero_d_Etage=%s,Type_de_la_chambre=%s WHERE Numero_de_la_chambre=%s", (
                        self.var_Numero_d_Etage.get(),
                        self.var_Type_de_la_chambre.get(),
                        self.var_Numero_de_la_chambre.get()
            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Modification", "La modification a réussi", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Attention", f"Veuillez vérifier l'erreur : {str(es)}", parent=self.root)

        # supprimer toy lahy 
    def mDelete(self):
        mDelete=messagebox.askyesno("Systeme Gestion d'Hotel","Voulez-vous supprimer cette Chambre ?",parent=self.root)
        if mDelete > 0 :
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
            my_cursor=conn.cursor()
            query="DELETE FROM details WHERE Numero_de_la_chambre=%s"
            value=(self.var_Numero_de_la_chambre.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.var_Numero_d_Etage.set("")
        self.var_Numero_de_la_chambre.set("")
        self.var_Type_de_la_chambre.set("")








if __name__ == "__main__":
    root=Tk()
    obj=Fenetre_Details(root)
    root.mainloop()