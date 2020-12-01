from tkinter import *
from tkinter import messagebox
import os,random
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        self.total_bill=IntVar()
        self.soap = IntVar()
        self.creame = IntVar()
        self.gel = IntVar()
        self.oil = IntVar()
        self.talcum = IntVar()
        self.balm = IntVar()
        self.string = IntVar()
        self.fizzy = IntVar()
        self.beer = IntVar()
        self.coke = IntVar()
        self.appy = IntVar()
        self.cafe = IntVar()
        self.wheat = IntVar()
        self.pulses = IntVar()
        self.maaze = IntVar()
        self.rice = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()
        self.cosmetic_price=IntVar()
        self.grocery_price=IntVar()
        self.drink_price=IntVar()
        self.cosmetic_tax=IntVar()
        self.grocery_tax=IntVar()
        self.drink_tax=IntVar()
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white",font=("times new roman", 20, "bold"), pady=2).pack()
        F1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 18, "bold"),fg="Gold", bg=bg_color)
        F1.place(x=0, y=0, relwidth=1)
        cname = Label(F1, text="Customer Name", bg=bg_color, fg="White", font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cnme = Entry(F1, width=15, textvariable=self.c_name, font=("arial", 14), bd=7, relief=SUNKEN).grid(row=0,column=1,padx=20,pady=5)
        cph = Label(F1, text="Customer Phone", bg=bg_color, fg="White", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cph = Entry(F1, width=15, textvariable=self.c_phone, font=("arial", 14), bd=7, relief=SUNKEN).grid(row=0, column=3,padx=20, pady=5)
        cbill = Label(F1, text="Bill", bg=bg_color, fg="White", font=("times new roman", 18, "bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill = Entry(F1, width=15,textvariable=self.search_bill, font=("arial", 14), bd=7, relief=SUNKEN).grid(row=0,column=5,padx=20,pady=5)
        bill_btn = Button(F1, text="Search",command=self.search,width=10, bd=7, font="arial 12 bold").grid(row=0,column=6,padx=5)
        # ----------------------------------Cosmetic Frame-------------------------------------------------------------------
        F2 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 18, "bold"),fg="Gold", bg=bg_color)
        F2.place(x=5, y=100, width=325, height=480)
        soap = Label(F2, text="Bath Saop", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10)
        soap_txt = Entry(F2, width=10, textvariable=self.soap, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10, sticky="w")
        cream = Label(F2, text="Creme", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1,column=0,padx=10,pady=10)
        cream_txt = Entry(F2, width=10, textvariable=self.creame, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10, sticky="w")
        gel = Label(F2, text="Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2,column=0,padx=10,pady=10)
        gel_txt = Entry(F2, width=10, textvariable=self.gel, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10, sticky="w")
        oil = Label(F2, text="oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3,column=0,padx=10,pady=10)
        oil_txt = Entry(F2, width=10, textvariable=self.oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10, sticky="w")
        powder = Label(F2, text="Talcum", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid( row=4, column=0, padx=10, pady=10)
        powder_txt = Entry(F2, width=10, textvariable=self.talcum, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10, sticky="w")
        lip = Label(F2, text="Lip Balm", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10)
        lip_txt = Entry(F2, width=10, textvariable=self.balm, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10, sticky="w")
        # ---------------------------------Soft Drink----------------------------------------------------------------------
        F3 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 18, "bold"),
                        fg="Gold", bg=bg_color)
        F3.place(x=325, y=100, width=325, height=480)
        g1 = Label(F3, text="String", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,column=0,padx=10,pady=10)
        g1_txt = Entry(F3, width=10, textvariable=self.string, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10, sticky="w")
        g2 = Label(F3, text="Fizzy", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1,column=0,padx=10,pady=10)
        g2_txt = Entry(F3, width=10, textvariable=self.fizzy, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10, sticky="w")
        g3 = Label(F3, text="Beer", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10)
        g3txt = Entry(F3, width=10, textvariable=self.beer, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10, sticky="w")
        g4 = Label(F3, text="coke", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3,column=0,padx=10,pady=10)
        g4_txt = Entry(F3, width=10, textvariable=self.coke, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10, sticky="w")
        g5 = Label(F3, text="Appy Fizz", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,column=0,padx=10,pady=10)
        g5_txt = Entry(F3, width=10, textvariable=self.appy, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10, sticky="w")
        g6 = Label(F3, text="cafe cuba", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10)
        g6_txt = Entry(F3, width=10, textvariable=self.cafe, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10, sticky="w")
        # -------------------------------------Grocery Frame---------------------------------------------------------------
        F4 = LabelFrame(self.root, text="Grocery", bd=10, relief=GROOVE, font=("times new roman", 18, "bold"),
                        fg="Gold", bg=bg_color)
        F4.place(x=625, y=100, width=325, height=480)
        c1 = Label(F4, text="String", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,column=0,padx=10,pady=10)
        c1_txt = Entry(F4, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10, sticky="w")
        c2 = Label(F4, text="Fizzy", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1,column=0,padx=10,pady=10)
        c2_txt = Entry(F4, width=10, textvariable=self.pulses, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10, sticky="w")
        c3 = Label(F4, text="Fruit Beer", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10)
        c3txt = Entry(F4, width=10, textvariable=self.maaze, font=("times new roman", 16, "bold"), bd=5,
                      relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10, sticky="w")
        c4 = Label(F4, text="coke", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10)
        c4_txt = Entry(F4, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10, sticky="w")
        c5 = Label(F4, text="Appy Fizz", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10)
        c5_txt = Entry(F4, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10, sticky="w")
        c6 = Label(F4, text="cafe cuba", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10)
        c6_txt = Entry(F4, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10, sticky="w")
        # --------------------------------------Bill Area-------------------------------------------------------------------
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=965, y=100, width=480, height=470)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill="x")
        scrol_y = Scrollbar(F5, orient="vertical")
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill="both", expand=1)
        # --------------------------------------Tax Frame---------------------------------------------------------------
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 16, "bold"), fg="gold",
                        bg=bg_color)
        F6.place(x=0, y=580, relwidth=1, height=350)
        m1 = Label(F6, text="Total Cosmetic Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=0, column=0, padx=20, pady=1, sticky="W")
        m1 = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=1)
        m2 = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=0, padx=20, pady=1, sticky="W")
        m2 = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1,
                                                                                                                  column=1,
                                                                                                                  padx=10,
                                                                                                                  pady=1)
        m3 = Label(F6, text="Total Cold Drink Price", bg=bg_color, fg="white",
                   font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="W")
        m3 = Entry(F6, width=18, textvariable=self.drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2,
                                                                                                                column=1,
                                                                                                                padx=10,
                                                                                                                pady=1)
        m4 = Label(F6, text="Total Cosmetic Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=0, column=2, padx=20, pady=1, sticky="W")
        m4 = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                                 column=3,
                                                                                                                 padx=10,
                                                                                                                 pady=1)
        m5 = Label(F6, text="Total Grocery Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=2, padx=20, pady=1, sticky="W")
        m5 = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1,
                                                                                                                column=3,
                                                                                                                padx=10,
                                                                                                                pady=1)
        m6 = Label(F6, text="Total Drink Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=2, column=2, padx=20, pady=1, sticky="W")
        m6 = Entry(F6, width=18, textvariable=self.drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2,
                                                                                                              column=3,
                                                                                                              padx=10,
                                                                                                              pady=1)
        # ---------------------------------------Button Frame-------------------------------------------------------------
        btn = Frame(F6, bd=7, relief=GROOVE)
        btn.place(x=790, width=700, height=105)
        total_btn = Button(btn, command=self.total, text="Total", bg="cadetblue", fg="white", width=13,
                           font=("arial 15"), bd=5, pady=15).grid(row=0, column=0, padx=5, pady=5)
        gbill_btn = Button(btn, command=self.bill_area, text="Generate Bill", bg="cadetblue", fg="white", width=13,
                           font=("arial 15"), bd=5, pady=15).grid(row=0, column=1, padx=5, pady=5)
        clear_btn = Button(btn, command=self.clear, text="clear", bg="cadetblue", fg="white", width=13,
                           font=("arial 15"), bd=5, pady=15).grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn,command=self.exit ,text="Exit", bg="cadetblue", fg="white", width=13, font=("arial 15"),
                          bd=5, pady=15).grid(row=0, column=3, padx=5, pady=5)

    def total(self):
        self.gwheat = self.wheat.get() * 40
        self.gpulses = self.pulses.get() * 36
        self.grice = self.rice.get() * 22
        self.gsugar = self.sugar.get() * 44
        self.gtea = self.tea.get() * 50
        self.gmaaze = self.maaze.get() * 102
        self.total_grocery = float(self.gwheat
                                   + self.gpulses
                                   + self.grice
                                   + self.gsugar
                                   + self.gtea
                                   + self.gmaaze)
        self.grocery_price.set("Rs" + str(self.total_grocery))
        self.g_tax = round((self.total_grocery * 0.03), 2)
        self.grocery_tax.set("Rs" + str(self.g_tax))

        self.cool_1 = self.string.get() * 40
        self.cool_2 = self.fizzy.get() * 30
        self.cool_3 = self.beer.get() * 22
        self.cool_4 = self.cafe.get() * 44
        self.cool_5 = self.coke.get() * 50
        self.cool_6 = self.appy.get() * 10
        self.total_cold_drink_price = float(
            self.cool_1 +
            self.cool_2 +
            self.cool_3 +
            self.cool_4 +
            self.cool_5 +
            self.cool_6
        )
        self.drink_price.set("Rs" + str(self.total_cold_drink_price))
        self.d_tax1 = round((self.total_cold_drink_price * 0.02), 2)
        self.drink_tax.set("Rs" + str(self.d_tax1))

        self.c_s_p = self.soap.get() * 40
        self.c_fc_c = self.creame.get() * 30
        self.c_gell = self.gel.get() * 22
        self.c_hair = self.talcum.get() * 44
        self.c_powder = self.balm.get() * 50
        self.c_lipbalm = self.oil.get() * 10
        self.total_cosmetic_price = float(
            self.c_s_p +
            self.c_fc_c +
            self.c_gell +
            self.c_hair +
            self.c_powder +
            self.c_lipbalm
        )
        self.cosmetic_price.set("Rs" + str(self.total_cosmetic_price))
        self.d_tax =round((self.total_cosmetic_price * 0.02),2)
        self.cosmetic_tax.set("Rs" + str(self.d_tax))
        self.total_bill = (self.total_grocery +
                           self.total_cold_drink_price +
                           self.total_cosmetic_price +
                           self.g_tax +
                           self.d_tax +
                           self.d_tax1)

    def welcome_bill(self):
        self.txtarea.delete(1.0, END)
        self.txtarea.insert(END, "\t\t Welcome Webcode \n")
        self.txtarea.insert(END, f"\nBill Number :{self.bill_no}")
        self.txtarea.insert(END, f"\nCustomer Name :{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number :{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n------------------------------------------------------")
        self.txtarea.insert(END, f"\n Products\t\tQty\t\tPrice")
        self.txtarea.insert(END, f"\n------------------------------------------------------")

    def clear(self):
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        self.soap.set(0)
        self.creame.set(0)
        self.gel.set(0)
        self.oil.set(0)
        self.talcum.set(0)
        self.balm.set(0)
        self.wheat.set(0)
        self.rice.set(0)
        self.pulses.set(0)
        self.maaze.set(0)
        self.sugar.set(0)
        self.tea.set(0)
        self.string.set(0)
        self.cafe.set(0)
        self.fizzy.set(0)
        self.appy.set(0)
        self.coke.set(0)
        self.beer.set(0)
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.drink_price.set("")
        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.drink_tax.set("")
        self.welcome_bill()

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        else:
            self.welcome_bill()
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\nBath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

            if self.creame.get() != 0:
                self.txtarea.insert(END, f"\nCream\t\t{self.creame.get()}\t\t{self.c_fc_c}")

            if self.gel.get() != 0:
                self.txtarea.insert(END, f"\nGel\t\t{self.gel.get()}\t\t{self.c_gell}")

            if self.oil.get() != 0:
                self.txtarea.insert(END, f"\nOil\t\t{self.oil.get()}\t\t{self.c_hair}")

            if self.talcum.get() != 0:
                self.txtarea.insert(END, f"\nTalcum\t\t{self.talcum.get()}\t\t{self.c_powder}")

            if self.balm.get() != 0:
                self.txtarea.insert(END, f"\nBalm\t\t{self.balm.get()}\t\t{self.c_lipbalm}")

            if self.pulses.get() != 0:
                self.txtarea.insert(END, f"\npulses\t\t{self.pulses.get()}\t\t{self.gpulses}")

            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t\t{self.grice}")

            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t\t{self.gsugar}")

            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\nTea\t\t{self.tea.get()}\t\t{self.gtea}")

            if self.maaze.get() != 0:
                self.txtarea.insert(END, f"\nMaaze\t\t{self.maaze.get()}\t\t{self.gmaaze}")

            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t\t{self.gwheat}")

            if self.string.get() != 0:
                self.txtarea.insert(END, f"\nString\t\t{self.string.get()}\t\t{self.cool_1}")

            if self.fizzy.get() != 0:
                self.txtarea.insert(END, f"\nFizzy\t\t{self.fizzy.get()}\t\t{self.cool_2}")

            if self.beer.get() != 0:
                self.txtarea.insert(END, f"\nBeer\t\t{self.beer.get()}\t\t{self.cool_3}")

            if self.cafe.get() != 0:
                self.txtarea.insert(END, f"\nCafe\t\t{self.cafe.get()}\t\t{self.cool_4}")

            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\nCoke\t\t{self.coke.get()}\t\t{self.cool_5}")

            if self.appy.get() != 0:
                self.txtarea.insert(END, f"\nAppy\t\t{self.appy.get()}\t\t{self.cool_6}")
            self.txtarea.insert(END, f"\n------------------------------------------------------")
            self.txtarea.insert(END, f"\nTotal Bill\t\t\t\t{self.total_bill}")
            self.txtarea.insert(END,f"\n-------------------------------------------------------")
            self.save_bill()
            self.welcome_bill()

    def search(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
                    messagebox.showerror("Error", "Invalid Number")
    def save_bill(self):
        op=messagebox.askyesno("Save bill","do you want to save the bill")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
        else:
            return
    def exit(self):
        op=messagebox.askyesno("Exit","do you really want to exit")
        if op>0:
            self.Bill_App.distroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()