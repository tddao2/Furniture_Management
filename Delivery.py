from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk
import random
import pyodbc
from tkinter import messagebox
from connection import Connect
class Delivery_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Delivery")
        self.root.geometry("1295x730+230+220")
        self.root.resizable(False, False)
#=================================================================Variables========================================================
        x = random.randint(1000,9999)

        self.var_Delivery_ID = StringVar()
        self.var_Delivery_ID.set(str(x))
        self.var_Vehicle_ID_1 = StringVar()
        self.var_Vehicle_ID_2 = StringVar()
        self.var_Year_vehicle  = StringVar()
        self.var_Model = StringVar()
        self.var_Trim = StringVar()
        self.var_Color = StringVar()
        self.var_License_Plate = StringVar()
        self.var_shipment_ID = StringVar()
        self.var_employee_ID = StringVar()
        self.var_delivery_start_at = StringVar()
        self.var_delivery_area = StringVar()
        self.var_delivery_status = StringVar()
        self.var_details1 = StringVar()
        self.var_details2 = StringVar()

#=================================================================title========================================================
        lbl_title = Label(self.root, text = "ADD DELIVERY DETAILS", font = ("times new roman", 18, "bold"), bg = "black", fg = "gold")
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

#=================================================================Logo========================================================
        img2 = Image.open(r"Images\icon.jpg")
        img2 = img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image = self.photoimg2, bd = 0, relief = RIDGE)
        lblimg.place(x = 5, y = 2, width = 100, height = 50)

#=================================================================labelFrame========================================================
        labelframeleft1 = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Vehicle Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        labelframeleft1.place(x = 5, y = 50, width = 425, height = 310)

        labelframeleft2 = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Delivery Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        labelframeleft2.place(x = 5, y = 370, width = 425, height = 358)

#=================================================================label and entries of Vehicle========================================================
# Vehicle ID
        lblVehicleID1 = Label(labelframeleft1, text = "Vehicle ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblVehicleID1.grid(row = 0, column = 0, sticky = W)

        txtVehicleID1 = ttk.Entry(labelframeleft1, textvariable = self.var_Vehicle_ID_1, width = 25, font = ("times new roman", 13, "bold"))
        txtVehicleID1.grid(row = 0, column = 1)

# Year
        lblStreet = Label(labelframeleft1, text = "Vehicle year:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblStreet.grid(row = 1, column = 0, sticky = W)

        txtStreet = ttk.Entry(labelframeleft1, textvariable = self.var_Year_vehicle, width = 25, font = ("times new roman", 13, "bold"))
        txtStreet.grid(row = 1, column = 1)

# Model
        lblModel = Label(labelframeleft1, text = "Model:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblModel.grid(row = 2, column = 0, sticky = W)

        txtModel = ttk.Entry(labelframeleft1, textvariable = self.var_Model, width = 25, font = ("times new roman", 13, "bold"))
        txtModel.grid(row = 2, column = 1)

# Trim
        lblTrim = Label(labelframeleft1, text = "Trim:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblTrim.grid(row = 3, column = 0, sticky = W)

        txtTrim = ttk.Entry(labelframeleft1, textvariable = self.var_Trim, width = 25, font = ("times new roman", 13, "bold"))
        txtTrim.grid(row = 3, column = 1)

# Color
        lblColor = Label(labelframeleft1, text = "Color:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblColor.grid(row = 4, column = 0, sticky = W)

        txtColor = ttk.Entry(labelframeleft1, textvariable = self.var_Color, width = 25, font = ("times new roman", 13, "bold"))
        txtColor.grid(row = 4, column = 1)

# License Plate
        lblLicensePlate = Label(labelframeleft1, text = "License Plate:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblLicensePlate.grid(row = 5, column = 0, sticky = W)

        txtLicensePlate = ttk.Entry(labelframeleft1, textvariable = self.var_License_Plate, width = 25, font = ("times new roman", 13, "bold"))
        txtLicensePlate.grid(row = 5, column = 1)

# Details1
        lblDetails1 = Label(labelframeleft1, text = "Details:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDetails1.grid(row = 6, column = 0, sticky = W)

        txtDetails1 = ttk.Entry(labelframeleft1, textvariable = self.var_details1, width = 25, font = ("times new roman", 13, "bold"))
        txtDetails1.grid(row = 6, column = 1)

#=================================================================label and entries of Delivery========================================================
# Delivery ID       
        lblDeliveryID = Label(labelframeleft2, text = "Delivery ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDeliveryID.grid(row = 0, column = 0, sticky = W)

        txtDeliveryID = ttk.Entry(labelframeleft2, textvariable = self.var_Delivery_ID, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtDeliveryID.grid(row = 0, column = 1)

# Shipment ID
        lblShipmentID = Label(labelframeleft2, text = "Shipment ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblShipmentID.grid(row = 1, column = 0, sticky = W)

        txtShipmentID = ttk.Entry(labelframeleft2, textvariable = self.var_shipment_ID, width = 25, font = ("times new roman", 13, "bold"))
        txtShipmentID.grid(row = 1, column = 1)

# Employee ID
        lblEmployeeID = Label(labelframeleft2, text = "Employee ID:", font = ("times new roman", 13, "bold"), padx = 2, pady = 6)
        lblEmployeeID.grid(row = 2, column = 0, sticky = W)

        txtEmployeeID = ttk.Entry(labelframeleft2, textvariable = self.var_employee_ID, width = 25, font = ("times new roman", 13, "bold"))
        txtEmployeeID.grid(row = 2, column = 1)

# Vehicle ID
        lblVehicleID2 = Label(labelframeleft2, text = "Vehicle ID:", font = ("times new roman", 13, "bold"), padx = 2, pady = 6)
        lblVehicleID2.grid(row = 3, column = 0, sticky = W)

        txtVehicleID2 = ttk.Entry(labelframeleft2, textvariable = self.var_Vehicle_ID_2, width = 25, font = ("times new roman", 13, "bold"))
        txtVehicleID2.grid(row = 3, column = 1)

# Delivery start
        lblDeliverystart = Label(labelframeleft2, text = "Delivery start:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDeliverystart.grid(row = 4, column = 0, sticky = W)

        txtDeliverystart = ttk.Entry(labelframeleft2, textvariable = self.var_delivery_start_at, width = 25, font = ("times new roman", 13, "bold"))
        txtDeliverystart.grid(row = 4, column = 1)

# Delivery Area
        lblDeliveryArea = Label(labelframeleft2, text = "Delivery Area:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDeliveryArea.grid(row = 5, column = 0, sticky = W)

        combo_DeliveryArea = ttk.Combobox(labelframeleft2, textvariable = self.var_delivery_area, font = ("times new roman", 12, "bold"), width = 26)
        combo_DeliveryArea["value"] = ("SouthWest", "NorthWest", "NorthEast", "SouthEast")
        combo_DeliveryArea.current(0)
        combo_DeliveryArea.grid(row = 5, column = 1)

# Delivery Status
        lblDeliveryStatus = Label(labelframeleft2, text = "Delivery Status:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDeliveryStatus.grid(row = 6, column = 0, sticky = W)

        txtDeliveryStatus = ttk.Entry(labelframeleft2, textvariable = self.var_delivery_status, width = 25, font = ("times new roman", 13, "bold"))
        txtDeliveryStatus.grid(row = 6, column = 1)

# Details
        lblDetails = Label(labelframeleft2, text = "Details:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDetails.grid(row = 7, column = 0, sticky = W)

        txtDetails = ttk.Entry(labelframeleft2, textvariable = self.var_details2, width = 25, font = ("times new roman", 13, "bold"))
        txtDetails.grid(row = 7, column = 1)
#=================================================================btns of vehicle========================================================
        btn_frame1 = Frame(labelframeleft1, bd = 2, relief = RIDGE)
        btn_frame1.place(x = 0, y = 250, width = 412, height = 35)

        btnAdd1 = Button(btn_frame1, text = "Add", command = self.add1, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnAdd1.grid(row = 0, column = 0, padx = 1)

        btnUpadate1 = Button(btn_frame1, text = "Update", command = self.update1, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnUpadate1.grid(row = 0, column = 1, padx = 1)

        btnDelete1 = Button(btn_frame1, text = "Delete", command = self.Delete1, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnDelete1.grid(row = 0, column = 2, padx = 1)

        btnReset1 = Button(btn_frame1, text = "Reset", command = self.Reset1, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnReset1.grid(row = 0, column = 3, padx = 1)

#=================================================================btns of delivery========================================================
        btn_frame2 = Frame(labelframeleft2, bd = 2, relief = RIDGE)
        btn_frame2.place(x = 0, y = 297, width = 412, height = 35)

        btnAdd2 = Button(btn_frame2, text = "Add", command = self.add2, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnAdd2.grid(row = 0, column = 0, padx = 1)

        btnUpadate2 = Button(btn_frame2, text = "Update", command = self.update2, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnUpadate2.grid(row = 0, column = 1, padx = 1)

        btnDelete2 = Button(btn_frame2, text = "Delete", command = self.Delete2, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnDelete2.grid(row = 0, column = 2, padx = 1)

        btnReset2 = Button(btn_frame2, text = "Reset", command = self.Reset2, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnReset2.grid(row = 0, column = 3, padx = 1)

#=================================================================table Frame search system========================================================
        Table_Frame1 = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        Table_Frame1.place(x = 435, y = 50, width = 860, height = 280)

        Table_Frame2 = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details:", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        Table_Frame2.place(x = 435, y = 340, width = 860, height = 388)
#=================================================================Show data table Vehicle========================================================        
        details_table1 = Frame(Table_Frame1, bd = 2, relief = RIDGE)
        details_table1.place(x = 0, y = 0, width = 860, height = 255)

        scroll_x1 = ttk.Scrollbar(details_table1, orient = HORIZONTAL)
        scroll_y1 = ttk.Scrollbar(details_table1, orient = VERTICAL)

        self.Delivery_details_Table1 = ttk.Treeview(details_table1, column = ("Vehicle ID", "Year", "Model", "Trim", "Color", "License Plate", "Details"), xscrollcommand = scroll_x1.set, yscrollcommand = scroll_y1.set)
                                                                                                             
        scroll_x1.pack(side = BOTTOM, fill = X)
        scroll_y1.pack(side = RIGHT, fill = Y)

        scroll_x1.config(command = self.Delivery_details_Table1.xview)
        scroll_y1.config(command = self.Delivery_details_Table1.yview)

        self.Delivery_details_Table1.heading("Vehicle ID", text = "Vehicle ID")
        self.Delivery_details_Table1.heading("Year", text = "Year")
        self.Delivery_details_Table1.heading("Model", text = "Model")
        self.Delivery_details_Table1.heading("Trim", text = "Trim")
        self.Delivery_details_Table1.heading("Color", text = "Color")
        self.Delivery_details_Table1.heading("License Plate", text = "License Plate")
        self.Delivery_details_Table1.heading("Details", text = "Details")

        self.Delivery_details_Table1["show"] = "headings"

        self.Delivery_details_Table1.column("Vehicle ID", width = 100, anchor = CENTER)
        self.Delivery_details_Table1.column("Year", width = 100, anchor = CENTER)
        self.Delivery_details_Table1.column("Model", width = 100, anchor = CENTER)
        self.Delivery_details_Table1.column("Trim", width = 100, anchor = CENTER)
        self.Delivery_details_Table1.column("Color", width = 100, anchor = CENTER)
        self.Delivery_details_Table1.column("License Plate", width = 100, anchor = CENTER)
        self.Delivery_details_Table1.column("Details", width = 100, anchor = CENTER)

        self.Delivery_details_Table1.pack(fill = BOTH, expand = 1)
        self.Delivery_details_Table1.bind("<ButtonRelease-1>", self.get_cursor1)
        self.fetch_data1()
#=================================================================Show data table Delivery========================================================        
        details_table2 = Frame(Table_Frame2, bd = 2, relief = RIDGE)
        details_table2.place(x = 0, y = 0, width = 860, height = 364)

        scroll_x2 = ttk.Scrollbar(details_table2, orient = HORIZONTAL)
        scroll_y2 = ttk.Scrollbar(details_table2, orient = VERTICAL)

        self.Delivery_details_Table2 = ttk.Treeview(details_table2, column = ("Delivery ID", "Shipment ID", "Employee ID", "Vehicle ID", "Delivery Start", "Delivery Area", "Status", "Details"),
                                                                        xscrollcommand = scroll_x2.set, yscrollcommand = scroll_y2.set)

        scroll_x2.pack(side = BOTTOM, fill = X)
        scroll_y2.pack(side = RIGHT, fill = Y)

        scroll_x2.config(command = self.Delivery_details_Table2.xview)
        scroll_y2.config(command = self.Delivery_details_Table2.yview)

        self.Delivery_details_Table2.heading("Delivery ID", text = "Delivery ID")
        self.Delivery_details_Table2.heading("Shipment ID", text = "Shipment ID")
        self.Delivery_details_Table2.heading("Employee ID", text = "Employee ID")
        self.Delivery_details_Table2.heading("Vehicle ID", text = "Vehicle ID")
        self.Delivery_details_Table2.heading("Delivery Start", text = "Delivery Start")
        self.Delivery_details_Table2.heading("Delivery Area", text = "Delivery Area")
        self.Delivery_details_Table2.heading("Status", text = "Status")
        self.Delivery_details_Table2.heading("Details", text = "Details")

        self.Delivery_details_Table2["show"] = "headings"

        self.Delivery_details_Table2.column("Delivery ID", width = 100, anchor = CENTER)
        self.Delivery_details_Table2.column("Vehicle ID", width = 100, anchor = CENTER)
        self.Delivery_details_Table2.column("Shipment ID", width = 100, anchor = CENTER)
        self.Delivery_details_Table2.column("Employee ID", width = 100, anchor = CENTER)
        self.Delivery_details_Table2.column("Delivery Start", width = 100, anchor = CENTER)
        self.Delivery_details_Table2.column("Delivery Area", width = 100, anchor = CENTER)
        self.Delivery_details_Table2.column("Status", width = 100, anchor = CENTER)
        self.Delivery_details_Table2.column("Details", width = 100, anchor = CENTER)

        self.Delivery_details_Table2.pack(fill = BOTH, expand = 1)
        self.Delivery_details_Table2.bind("<ButtonRelease-1>", self.get_cursor2)
        self.fetch_data2()

#=================================================================Commands for Vehicle========================================================  
    def add1(self):
        if self.var_Vehicle_ID_1.get() == "" or self.var_License_Plate.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("INSERT INTO Vehicles (Vehicle_ID, Year, Model, Trim, Color, License_Plate, Details) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                                                self.var_Vehicle_ID_1.get(), self.var_Year_vehicle.get(), self.var_Model.get(), self.var_Trim.get(),
                                                                self.var_Color.get(), self.var_License_Plate.get(), self.var_details1.get())
                        conn.commit()

                        self.fetch_data1()
                        conn.close()
                        messagebox.showinfo("Success", "A vehicle has been added", parent = self.root)
                        self.Reset1()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
                        print(es)
     
    def fetch_data1(self):
        try:
                conn = pyodbc.connect(Connect)
                print("Connection to MySQL DB successful")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM Vehicles")                
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                        self.Delivery_details_Table1.delete(*self.Delivery_details_Table1.get_children())
                        for i in rows:
                                self.Delivery_details_Table1.insert("",END,values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
                        conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)

    def get_cursor1(self, event = ""):
        cursor_row = self.Delivery_details_Table1.focus()
        content = self.Delivery_details_Table1.item(cursor_row)
        row = content["values"]

        self.var_Vehicle_ID_1.set(row[0])
        self.var_Year_vehicle.set(row[1])
        self.var_Model.set(row[2])
        self.var_Trim.set(row[3])
        self.var_Color.set(row[4])
        self.var_License_Plate.set(row[5])
        self.var_details1.set(row[6])

    def update1(self):
        if self.var_Vehicle_ID_1.get() == "" or self.var_License_Plate.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("UPDATE Vehicles SET Year = ?, Model = ?, Trim = ?, Color = ?, License_Plate = ?, Details = ?\
                                        WHERE Vehicle_ID = ?",
                                        self.var_Year_vehicle.get(), self.var_Model.get(), self.var_Trim.get(), self.var_Color.get(),
                                        self.var_License_Plate.get(), self.var_details1.get(), self.var_Vehicle_ID_1.get())
                        conn.commit()
                        self.fetch_data1()
                        conn.close()

                        messagebox.showinfo("Update", "Vehicle details have been updated successfully", parent = self.root)
                        self.Reset1()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)  

    def Delete1(self):
        Delete = messagebox.askyesno("Furniture Management Apllication", "Do you want to delete this vehicle?", parent = self.root)
        if Delete > 0:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("DELETE FROM Vehicles WHERE Vehicle_ID = ?", self.var_Vehicle_ID_1.get())
                        conn.commit()

                        conn.close()
                        self.fetch_data1()
                        self.Reset1()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
        else:
                if not Delete:
                        return

    def Reset1(self):
        self.var_Vehicle_ID_1.set(""),
        self.var_Year_vehicle.set(""),
        self.var_Model.set(""),
        self.var_Trim.set(""),
        self.var_Color.set(""),
        self.var_License_Plate.set(""),
        self.var_details1.set("")

#=================================================================Commands for Deliveries========================================================  
    def add2(self):
        if self.var_shipment_ID.get() == "" or self.var_employee_ID.get() == "" or self.var_Vehicle_ID_2.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("INSERT INTO Delivery_Status (Delivery_Status_ID, Status) VALUES (?, ?)", self.var_Delivery_ID.get(), self.var_delivery_status.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Delivery_Area (Delivery_Area_ID, Area) VALUES (?, ?)",
                                            self.var_Delivery_ID.get(), self.var_delivery_area.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Deliveries (Delivery_ID, Shipment_ID, Employee_ID, Vehicle_ID, Delivery_Start, Delivery_Area_ID, Delivery_Status_ID, Details)\
                                            values (?, ?, ?, ?, ?, ?, ?, ?)",
                                            self.var_Delivery_ID.get(), self.var_shipment_ID.get(), self.var_employee_ID.get(), self.var_Vehicle_ID_2.get(), self.var_delivery_start_at.get(),
                                            self.var_Delivery_ID.get(), self.var_Delivery_ID.get(), self.var_details2.get())
                        conn.commit()
                        self.fetch_data2()
                        conn.close()
                        messagebox.showinfo("Success", "Delivery has been added", parent = self.root)
                        self.Reset2()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
                        print(es)
     
    def fetch_data2(self):
        try:
                conn = pyodbc.connect(Connect)
                print("Connection to MySQL DB successful")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Deliveries.Delivery_ID, Deliveries.Shipment_ID, Deliveries.Employee_ID, Deliveries.Vehicle_ID, Deliveries.Delivery_Start,\
		                                Delivery_Area.Area, Delivery_Status.Status, Deliveries.Details\
                                    FROM Deliveries\
                                    INNER JOIN Delivery_Area ON Delivery_Area.Delivery_Area_ID = Deliveries.Delivery_Area_ID\
                                    INNER JOIN Delivery_Status ON Delivery_Status.Delivery_Status_ID = Deliveries.Delivery_Status_ID\
                                    ORDER BY Deliveries.Delivery_ID")
                
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                        self.Delivery_details_Table2.delete(*self.Delivery_details_Table2.get_children())
                        for i in rows:
                                self.Delivery_details_Table2.insert("",END,values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                        conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)

    def get_cursor2(self, event = ""):
        cursor_row = self.Delivery_details_Table2.focus()
        content = self.Delivery_details_Table2.item(cursor_row)
        row = content["values"]

        self.var_Delivery_ID.set(row[0])
        self.var_shipment_ID.set(row[1])
        self.var_employee_ID.set(row[2])
        self.var_Vehicle_ID_2.set(row[3])
        self.var_delivery_start_at.set(row[4])
        self.var_delivery_area.set(row[5])
        self.var_delivery_status.set(row[6])
        self.var_details2.set(row[7])

    def update2(self):
        if self.var_shipment_ID.get() == "" or self.var_employee_ID.get() == "" or self.var_Vehicle_ID_2.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("UPDATE Delivery_Area SET Area = ?\
                                        WHERE Delivery_Area_ID = ?",
                                        self.var_delivery_area.get(), self.var_Delivery_ID.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Delivery_Status SET Status = ?\
                                        WHERE Delivery_Status_ID = ?",
                                        self.var_delivery_status.get(), self.var_Delivery_ID.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Deliveries SET Shipment_ID = ?, Employee_ID = ?, Vehicle_ID = ?, Delivery_Start = ?, Delivery_Area_ID = ?, Delivery_Status_ID = ?, Details = ?\
                                        WHERE Delivery_ID = ?",
                                        self.var_shipment_ID.get(), self.var_employee_ID.get(), self.var_Vehicle_ID_2.get(), self.var_delivery_start_at.get(),
                                        self.var_Delivery_ID.get(), self.var_Delivery_ID.get(), self.var_details2.get(), self.var_Delivery_ID.get())
                        conn.commit()

                        self.fetch_data2()
                        conn.close()

                        messagebox.showinfo("Update", "Delivery details have been updated successfully", parent = self.root)
                        self.Reset2()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)  

    def Delete2(self):
        Delete = messagebox.askyesno("Furniture Management Apllication", "Do you want to delete this delivery?", parent = self.root)
        if Delete > 0:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("DELETE FROM Deliveries WHERE Delivery_ID = ?", self.var_Delivery_ID.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Delivery_Area WHERE Delivery_Area_ID = ?", self.var_Delivery_ID.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Delivery_Status WHERE Delivery_Status_ID = ?", self.var_Delivery_ID.get())
                        conn.commit()

                        conn.close()
                        
                        self.fetch_data2()
                        self.Reset2()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
        else:
                if not Delete:
                        return

    def Reset2(self):
        x = random.randint(1000,9999)
        self.var_Delivery_ID.set(str(x)),
        self.var_shipment_ID.set(""),
        self.var_employee_ID.set(""),
        self.var_delivery_start_at.set(""),
        self.var_Vehicle_ID_2.set(""),
        self.var_delivery_area.set(""),
        self.var_delivery_status.set(""),
        self.var_details2.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Delivery_Win(root)
    root.mainloop()
