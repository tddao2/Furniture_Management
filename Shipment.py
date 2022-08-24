from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk
import random
import pyodbc
from tkinter import messagebox
from connection import Connect
class Shipment_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Shipment")
        self.root.geometry("1295x730+230+220")
        self.root.resizable(False, False)
#=================================================================Variables========================================================
        x = random.randint(1000,9999)

        self.var_Shipment_ID = StringVar()
        self.var_Shipment_ID.set(str(x))

        self.var_invoice_id = StringVar()
        self.var_street = StringVar()
        self.var_city = StringVar()
        self.var_state = StringVar()
        self.var_zipcode = StringVar()
        self.var_billing_address = StringVar()
        self.var_time_created = StringVar()
        self.var_shipment_type = StringVar()
        self.var_shipment_status = StringVar()

#=================================================================title========================================================
        lbl_title = Label(self.root, text = "ADD SHIPMENT DETAILS", font = ("times new roman", 18, "bold"), bg = "black", fg = "gold")
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

#=================================================================Logo========================================================
        img2 = Image.open(r"Images\icon.jpg")
        img2 = img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image = self.photoimg2, bd = 0, relief = RIDGE)
        lblimg.place(x = 5, y = 2, width = 100, height = 50)

#=================================================================labelFrame========================================================
        labelframeleft = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Shipment Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        labelframeleft.place(x = 5, y = 50, width = 425, height = 677)

#=================================================================label and entries========================================================
# Shipment ID       
        lblShipmentID = Label(labelframeleft, text = "Shipment ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 15)
        lblShipmentID.grid(row = 0, column = 0, sticky = W)

        txtShipmentID = ttk.Entry(labelframeleft, textvariable = self.var_Shipment_ID, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtShipmentID.grid(row = 0, column = 1)

# Street
        lblStreet = Label(labelframeleft, text = "Street:", font = ("times new roman", 12, "bold"), padx = 2, pady = 15)
        lblStreet.grid(row = 1, column = 0, sticky = W)

        txtStreet = ttk.Entry(labelframeleft, textvariable = self.var_street, width = 25, font = ("times new roman", 13, "bold"))
        txtStreet.grid(row = 1, column = 1)

# City
        lblCity = Label(labelframeleft, text = "City:", font = ("times new roman", 12, "bold"), padx = 2, pady = 15)
        lblCity.grid(row = 2, column = 0, sticky = W)

        txtCity = ttk.Entry(labelframeleft, textvariable = self.var_city, width = 25, font = ("times new roman", 13, "bold"))
        txtCity.grid(row = 2, column = 1)

# State
        lblState = Label(labelframeleft, text = "State:", font = ("times new roman", 12, "bold"), padx = 2, pady = 15)
        lblState.grid(row = 3, column = 0, sticky = W)

        txtState = ttk.Entry(labelframeleft, textvariable = self.var_state, width = 25, font = ("times new roman", 13, "bold"))
        txtState.grid(row = 3, column = 1)

# ZipCode
        lblZipCode = Label(labelframeleft, text = "ZipCode:", font = ("times new roman", 12, "bold"), padx = 2, pady = 15)
        lblZipCode.grid(row = 4, column = 0, sticky = W)

        txtZipCode = ttk.Entry(labelframeleft, textvariable = self.var_zipcode, width = 25, font = ("times new roman", 13, "bold"))
        txtZipCode.grid(row = 4, column = 1)

# Billing Address
        lblBillingAddress = Label(labelframeleft, text = "Billing Address:", font = ("times new roman", 12, "bold"), padx = 2, pady = 15)
        lblBillingAddress.grid(row = 5, column = 0, sticky = W)

        txtBillingAddress = ttk.Entry(labelframeleft, textvariable = self.var_billing_address, width = 25, font = ("times new roman", 13, "bold"))
        txtBillingAddress.grid(row = 5, column = 1)

# Time Created
        lblTimeCreated = Label(labelframeleft, text = "Time Created:", font = ("times new roman", 12, "bold"), padx = 2, pady = 15)
        lblTimeCreated.grid(row = 6, column = 0, sticky = W)

        txtTimeCreated = ttk.Entry(labelframeleft, textvariable = self.var_time_created, width = 25, font = ("times new roman", 13, "bold"))
        txtTimeCreated.grid(row = 6, column = 1)

# Shipment Type
        lblShipmentType = Label(labelframeleft, text = "Shipment Type:", font = ("times new roman", 13, "bold"), padx = 2, pady = 15)
        lblShipmentType.grid(row = 7, column = 0, sticky = W)

        combo_ShipmentType = ttk.Combobox(labelframeleft, textvariable = self.var_shipment_type, font = ("times new roman", 12, "bold"), width = 26)
        combo_ShipmentType["value"] = ("Standard", "Fast Ship")
        combo_ShipmentType.current(0)
        combo_ShipmentType.grid(row = 7, column = 1)

# Invoice ID
        lblInvoiceID = Label(labelframeleft, text = "Invoice ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 15)
        lblInvoiceID.grid(row = 8, column = 0, sticky = W)

        txtInvoiceID = ttk.Entry(labelframeleft, textvariable = self.var_invoice_id, width = 25, font = ("times new roman", 13, "bold"))
        txtInvoiceID.grid(row = 8, column = 1)

# Shipment Status
        lblShipmentStatus = Label(labelframeleft, text = "Status:", font = ("times new roman", 12, "bold"), padx = 2, pady = 15)
        lblShipmentStatus.grid(row = 9, column = 0, sticky = W)

        txtShipmentStatus = ttk.Entry(labelframeleft, textvariable = self.var_shipment_status, width = 25, font = ("times new roman", 13, "bold"))
        txtShipmentStatus.grid(row = 9, column = 1)

#=================================================================btns========================================================
        btn_frame = Frame(labelframeleft, bd = 2, relief = RIDGE)
        btn_frame.place(x = 0, y = 615, width = 412, height = 35)

        btnAdd = Button(btn_frame, text = "Add", command = self.add, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnAdd.grid(row = 0, column = 0, padx = 1)

        btnUpadate = Button(btn_frame, text = "Update", command = self.update, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnUpadate.grid(row = 0, column = 1, padx = 1)

        btnDelete = Button(btn_frame, text = "Delete", command = self.Delete, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnDelete.grid(row = 0, column = 2, padx = 1)

        btnReset = Button(btn_frame, text = "Reset", command = self.Reset, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnReset.grid(row = 0, column = 3, padx = 1)

#=================================================================table Frame search system========================================================
        Table_Frame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        Table_Frame.place(x = 435, y = 50, width = 860, height = 677)

#=================================================================Show data table========================================================        
        details_table = Frame(Table_Frame, bd = 2, relief = RIDGE)
        details_table.place(x = 0, y = 0, width = 860, height = 652)

        scroll_x = ttk.Scrollbar(details_table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient = VERTICAL)

        self.Shipment_details_Table = ttk.Treeview(details_table, column = ("Shipment ID", "Street", "City", "State", "ZipCode", "Billing Address",
                                                                        "Time Creation", "Shipment Type", "Order ID", "Status"),
                                                                        xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Shipment_details_Table.xview)
        scroll_y.config(command = self.Shipment_details_Table.yview)

        self.Shipment_details_Table.heading("Shipment ID", text = "Shipment ID")
        self.Shipment_details_Table.heading("Street", text = "Street")
        self.Shipment_details_Table.heading("City", text = "City")
        self.Shipment_details_Table.heading("State", text = "State")
        self.Shipment_details_Table.heading("ZipCode", text = "ZipCode")
        self.Shipment_details_Table.heading("Billing Address", text = "Billing Address")
        self.Shipment_details_Table.heading("Time Creation", text = "Time Creation")
        self.Shipment_details_Table.heading("Shipment Type", text = "Shipment Type")
        self.Shipment_details_Table.heading("Order ID", text = "Order ID")
        self.Shipment_details_Table.heading("Status", text = "Status")

        self.Shipment_details_Table["show"] = "headings"

        self.Shipment_details_Table.column("Shipment ID", width = 100, anchor = CENTER)
        self.Shipment_details_Table.column("Street", width = 100, anchor = CENTER)
        self.Shipment_details_Table.column("City", width = 100, anchor = CENTER)
        self.Shipment_details_Table.column("State", width = 100, anchor = CENTER)
        self.Shipment_details_Table.column("ZipCode", width = 100, anchor = CENTER)
        self.Shipment_details_Table.column("Billing Address", width = 100, anchor = CENTER)
        self.Shipment_details_Table.column("Time Creation", width = 100, anchor = CENTER)
        self.Shipment_details_Table.column("Shipment Type", width = 100, anchor = CENTER)
        self.Shipment_details_Table.column("Order ID", width = 100, anchor = CENTER)
        self.Shipment_details_Table.column("Status", width = 100, anchor = CENTER)

        self.Shipment_details_Table.pack(fill = BOTH, expand = 1)
        self.Shipment_details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

#=================================================================Commands========================================================  
    def add(self):
        if self.var_invoice_id.get() == "" or self.var_street.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("INSERT INTO Shipment_Status (Shipment_Status_ID, Status) VALUES (?, ?)", self.var_Shipment_ID.get(), self.var_shipment_status.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Shipment_Type (Shipment_Type_ID, Type) VALUES (?, ?)",
                                            self.var_Shipment_ID.get(), self.var_shipment_type.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Billing_Address (Billing_Address_ID, Description) VALUES (?, ?)",
                                        self.var_Shipment_ID.get(), self.var_billing_address.get())  
                        conn.commit()

                        my_cursor.execute("INSERT INTO Shipment (Shipment_ID, Street, City, State, ZipCode, Billing_Address_ID, Time_Created, Shipment_Type_ID, Invoice_ID, Shipment_Status_ID)\
                                            values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                            self.var_Shipment_ID.get(), self.var_street.get(), self.var_city.get(), self.var_state.get(), self.var_zipcode.get(),
                                            self.var_Shipment_ID.get(), self.var_time_created.get(), self.var_Shipment_ID.get(), self.var_invoice_id.get(), self.var_Shipment_ID.get())
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Shipment has been added", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
                        print(es)
     
    def fetch_data(self):
        try:
                conn = pyodbc.connect(Connect)
                print("Connection to MySQL DB successful")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Shipment.Shipment_ID, Shipment.Street, Shipment.City, Shipment.State, Shipment.ZipCode,\
		                                Billing_Address.Description, Shipment.Time_Created,\
		                                Shipment_Type.Type, Shipment.Invoice_ID,\
		                                Shipment_Status.Status\
                                    FROM Shipment\
                                    INNER JOIN Billing_Address ON Billing_Address.Billing_Address_ID = Shipment.Billing_Address_ID\
                                    INNER JOIN Shipment_Status ON Shipment_Status.Shipment_Status_ID = Shipment.Shipment_Status_ID\
                                    INNER JOIN Shipment_Type ON Shipment_Type.Shipment_Type_ID = Shipment.Shipment_Type_ID\
                                    ORDER BY Shipment.Shipment_ID")
                
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                        self.Shipment_details_Table.delete(*self.Shipment_details_Table.get_children())
                        for i in rows:
                                self.Shipment_details_Table.insert("",END,values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
                        conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)

    def get_cursor(self, event = ""):
        cursor_row = self.Shipment_details_Table.focus()
        content = self.Shipment_details_Table.item(cursor_row)
        row = content["values"]

        self.var_Shipment_ID.set(row[0])
        self.var_street.set(row[1])
        self.var_city.set(row[2])
        self.var_state.set(row[3])
        self.var_zipcode.set(row[4])
        self.var_billing_address.set(row[5])
        self.var_time_created.set(row[6])
        self.var_shipment_type.set(row[7])
        self.var_invoice_id.set(row[8])
        self.var_shipment_status.set(row[9])

    def update(self):
        if self.var_invoice_id.get() == "" or self.var_street.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("UPDATE Shipment_Status SET Status = ?\
                                        WHERE Shipment_Status_ID = ?",
                                        self.var_shipment_status.get(), self.var_Shipment_ID.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Shipment_Type SET Type = ?\
                                        WHERE Shipment_Type_ID = ?",
                                        self.var_shipment_type.get(), self.var_Shipment_ID.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Billing_Address SET Description = ?\
                                        WHERE Billing_Address_ID = ?",
                                        self.var_billing_address.get(), self.var_Shipment_ID.get())  
                        conn.commit()

                        my_cursor.execute("UPDATE Shipment SET Street = ?, City = ?, State = ?, ZipCode = ?, Time_Created = ?, Invoice_ID = ?\
                                        WHERE Shipment_ID = ?",
                                        self.var_street.get(), self.var_city.get(), self.var_state.get(),
                                        self.var_zipcode.get(), self.var_time_created.get(), self.var_invoice_id.get(), self.var_Shipment_ID.get())
                        conn.commit()

                        self.fetch_data()
                        conn.close()

                        messagebox.showinfo("Update", "Shipment details have been updated successfully", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)  

    def Delete(self):
        Delete = messagebox.askyesno("Furniture Management Apllication", "Do you want to delete this shipment?", parent = self.root)
        if Delete > 0:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("DELETE FROM Shipment WHERE Shipment_ID = ?", self.var_Shipment_ID.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Billing_Address WHERE Billing_Address_ID = ?", self.var_Shipment_ID.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Shipment_Status WHERE Shipment_Status_ID = ?", self.var_Shipment_ID.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Shipment_Type WHERE Shipment_Type_ID = ?", self.var_Shipment_ID.get())
                        conn.commit()

                        self.fetch_data()
                        conn.close()

                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
        else:
                if not Delete:
                        return

    def Reset(self):
        x = random.randint(1000,9999)
        self.var_Shipment_ID.set(str(x))
        self.var_invoice_id.set(""),
        self.var_street.set(""),
        self.var_city.set(""),
        self.var_state.set(""),
        self.var_zipcode.set(""),
        self.var_billing_address.set(""),
        self.var_time_created.set(""),
        self.var_shipment_type.set(""),
        self.var_shipment_status.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Shipment_Win(root)
    root.mainloop()
