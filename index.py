from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
from customer import Cust_Win
from Employee import Employee_Win
from Product import Product_Win
from Order import Order_Win
from Payment import Payment_Win
from Loan import Loan_Win
from Shipment import Shipment_Win
from Delivery import Delivery_Win
class AffordableFurniture:
    def __init__(self,root):
        self.root = root
        self.root.title("Affordable Furniture")
        self.root.geometry("1550x800+0+0")
        self.root.resizable(False, False)
#=================================================================ist Images========================================================
        img1 = Image.open(r"Images\AF.JPG")
        img1 = img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image = self.photoimg1, bd = 4, relief = RIDGE)
        lblimg.place(x = 0, y = 0, width = 1550, height = 140)

#=================================================================Logo========================================================
        img2 = Image.open(r"Images\icon.jpg")
        img2 = img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image = self.photoimg2, bd = 4, relief = RIDGE)
        lblimg.place(x = 0, y = 0, width = 230, height = 140)

#=================================================================title========================================================
        lbl_title = Label(self.root, text = "FURNITURE MANAGEMENT APPLICATION", font = ("times new roman", 40, "bold"), bg = "black", fg = "gold")
        lbl_title.place(x = 0, y = 140, width = 1690, height = 50)

#=================================================================main Frame========================================================   
        main_frame = Frame(self.root, bd = 4, relief = RIDGE)
        main_frame.place(x = 0, y = 190, width = 1550, height = 620)

#=================================================================menu======================================================== 
        lbl_menu = Label(main_frame, text = "MENU", font = ("times new roman", 20, "bold"), bg = "black", fg = "gold", bd = 4, relief = RIDGE)
        lbl_menu.place(x = 0, y = 0, width = 230)

#=================================================================btn Frame======================================================== 
        btn_frame = Frame(main_frame, bd = 4, relief = RIDGE)
        btn_frame.place(x = 0, y = 35, width = 228, height = 298)

        cust_btn = Button(btn_frame, text = "CUSTOMER", command = self.customer_details, width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor = "hand1")
        cust_btn.grid(row = 0, column = 0, pady = 1)

        Employee_btn = Button(btn_frame, text = "EMPLOYEE", command = self.employee_details, width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor = "hand1")
        Employee_btn.grid(row = 1, column = 0, pady = 1)

        Product_btn = Button(btn_frame, text = "PRODUCT", command = self.product_details, width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor = "hand1")
        Product_btn.grid(row = 2, column = 0, pady = 1)

        Order_btn = Button(btn_frame, text = "ORDER", command = self.order_details, width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor = "hand1")
        Order_btn.grid(row = 3, column = 0, pady = 1)

        Payment_btn = Button(btn_frame, text = "PAYMENT", command = self.payment_details, width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor = "hand1")
        Payment_btn.grid(row = 4, column = 0, pady = 1)

        Loan_btn = Button(btn_frame, text = "LOAN", command = self.loan_details, width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor = "hand1")
        Loan_btn.grid(row = 5, column = 0, pady = 1)

        Shipment_btn = Button(btn_frame, text = "SHIPMENT", command = self.shipment_details, width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor = "hand1")
        Shipment_btn.grid(row = 6, column = 0, pady = 1)

        Delivery_btn = Button(btn_frame, text = "DELIVERY", command = self.delivery_details, width = 22, font = ("times new roman", 14, "bold"), bg = "black", fg = "gold", bd = 0, cursor = "hand1")
        Delivery_btn.grid(row = 7, column = 0, pady = 1)

#=================================================================right side image======================================================== 
        img3 = Image.open(r"Images\Background.JPG")
        img3 = img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image = self.photoimg3, bd = 4, relief = RIDGE)
        lblimg1.place(x = 225, y = 0, width = 1324, height = 605)

#=================================================================down images======================================================== 
        # img4 = Image.open(r"C:\Users\herok\Documents\Tri's documents\Education\CIS 3365\Background.JPG")
        # img4 = img4.resize((230,210),Image.ANTIALIAS)
        # self.photoimg4 = ImageTk.PhotoImage(img4)

        # lblimg1 = Label(main_frame, image = self.photoimg3, bd = 4, relief = RIDGE)
        # lblimg1.place(x = 0, y = 260, width = 230, height = 210)

        img5 = Image.open(r"Images\Background.JPG")
        img5 = img5.resize((230,260),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image = self.photoimg5, bd = 4, relief = RIDGE)
        lblimg1.place(x = 0, y = 334, width = 230, height = 271)

    def customer_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Employee_Win(self.new_window)

    def product_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Product_Win(self.new_window)

    def order_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Order_Win(self.new_window)

    def payment_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Payment_Win(self.new_window)

    def loan_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Loan_Win(self.new_window)

    def shipment_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Shipment_Win(self.new_window)

    def delivery_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Delivery_Win(self.new_window)         
#=================================================================main Frame======================================================== 

if __name__=="__main__":
    root = Tk()
    obj = AffordableFurniture(root)
    root.mainloop()

#==============================================================References=============================================================
#https://www.freepik.com/free-vector/furniture-logo_9292740.htm#page=1&query=furniture%20icon&position=0
#https://www.youtube.com/channel/UCP1HhCg0ZwOyLFssftBCDIA
#https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw
