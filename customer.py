from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk
import random
import pyodbc
from tkinter import messagebox
from connection import Connect
class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer")
        self.root.geometry("1295x730+230+220")
        self.root.resizable(False, False)
#=================================================================Variables========================================================
        x = random.randint(1000,9999)

        self.var_customer_id = StringVar()
        self.var_customer_id.set(str(x))

        self.var_address_id = StringVar()
        self.var_address_id.set(str(x))

        self.var_customer_status_id = StringVar()
        self.var_customer_status_id.set(str(x))

        self.var_address_type_id = StringVar()
        self.var_address_type_id.set(str(x))

        self.var_first_name = StringVar()
        self.var_middle_name = StringVar()
        self.var_last_name = StringVar()
        self.var_email_address = StringVar()
        self.var_phone_number = StringVar()
        self.var_customer_decription = StringVar()
        self.var_street_name = StringVar()
        self.var_city = StringVar()
        self.var_state = StringVar()
        self.var_address_description = StringVar()
        self.var_zip_code = StringVar()
        self.var_country = StringVar()
#=================================================================title========================================================
        lbl_title = Label(self.root, text = "ADD CUSTOMER DETAILS", font = ("times new roman", 18, "bold"), bg = "black", fg = "gold")
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

#=================================================================Logo========================================================
        img2 = Image.open(r"Images\icon.jpg")
        img2 = img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image = self.photoimg2, bd = 0, relief = RIDGE)
        lblimg.place(x = 5, y = 2, width = 100, height = 50)

#=================================================================labelFrame========================================================
        labelframeleft = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Customer Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        labelframeleft.place(x = 5, y = 50, width = 425, height = 677)

#=================================================================label and entries========================================================
# Customer ID        
        lbl_cust_left = Label(labelframeleft, text = "Customer ID", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lbl_cust_left.grid(row = 0, column = 0, sticky = W)

        entry_ref = ttk.Entry(labelframeleft, textvariable = self.var_customer_id, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        entry_ref.grid(row = 0, column = 1)

# FirstName
        lblFirstName = Label(labelframeleft, text = "First Name:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblFirstName.grid(row = 1, column = 0, sticky = W)

        txtFirstName = ttk.Entry(labelframeleft, textvariable = self.var_first_name, width = 25, font = ("times new roman", 13, "bold"))
        txtFirstName.grid(row = 1, column = 1)

# MiddleName
        lblMiddleName = Label(labelframeleft, text = "Middle Name:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblMiddleName.grid(row = 2, column = 0, sticky = W)

        txtMiddleName = ttk.Entry(labelframeleft, textvariable = self.var_middle_name, width = 25, font = ("times new roman", 13, "bold"))
        txtMiddleName.grid(row = 2, column = 1)

# LastName
        lblLastName = Label(labelframeleft, text = "Last Name:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblLastName.grid(row = 3, column = 0, sticky = W)

        txtLastName = ttk.Entry(labelframeleft, textvariable = self.var_last_name, width = 25, font = ("times new roman", 13, "bold"))
        txtLastName.grid(row = 3, column = 1)

# Email Address
        lblEmailAddress = Label(labelframeleft, text = "Email Address:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblEmailAddress.grid(row = 4, column = 0, sticky = W)

        txtEmailAddress = ttk.Entry(labelframeleft, textvariable = self.var_email_address, width = 25, font = ("times new roman", 13, "bold"))
        txtEmailAddress.grid(row = 4, column = 1)

# Phone Number
        lblPhoneNumber = Label(labelframeleft, text = "Phone:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblPhoneNumber.grid(row = 5, column = 0, sticky = W)

        txtPhoneNumber = ttk.Entry(labelframeleft, textvariable = self.var_phone_number, width = 25, font = ("times new roman", 13, "bold"))
        txtPhoneNumber.grid(row = 5, column = 1)

# Address ID
        lblEmail = Label(labelframeleft, text = "Address ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblEmail.grid(row = 6, column = 0, sticky = W)

        txtEmail = ttk.Entry(labelframeleft, textvariable = self.var_address_id, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtEmail.grid(row = 6, column = 1)

# StreetName
        lblStreetName = Label(labelframeleft, text = "Street Name:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblStreetName.grid(row = 7, column = 0, sticky = W)

        txtStreetName = ttk.Entry(labelframeleft, textvariable = self.var_street_name, width = 25, font = ("times new roman", 13, "bold"))
        txtStreetName.grid(row = 7, column = 1)
# City
        lblCity = Label(labelframeleft, text = "City:", font = ("times new roman", 13, "bold"), padx = 2, pady = 6)
        lblCity.grid(row = 8, column = 0, sticky = W)

        txtCity = ttk.Entry(labelframeleft, textvariable = self.var_city, width = 25, font = ("times new roman", 13, "bold"))
        txtCity.grid(row = 8, column = 1)
# State
        lblIdState = Label(labelframeleft, text = "State:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblIdState.grid(row = 9, column = 0, sticky = W)

        txtIdState = ttk.Entry(labelframeleft, textvariable = self.var_state, width = 25, font = ("times new roman", 13, "bold"))
        txtIdState.grid(row = 9, column = 1)

# ZipCode
        lblZipCode = Label(labelframeleft, text = "ZipCode:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblZipCode.grid(row = 10, column = 0, sticky = W)

        txtZipCode = ttk.Entry(labelframeleft, textvariable = self.var_zip_code, width = 25, font = ("times new roman", 13, "bold"))
        txtZipCode.grid(row = 10, column = 1)

# Country
        lblCountry = Label(labelframeleft, text = "Country:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblCountry.grid(row = 11, column = 0, sticky = W)

        txtCountry = ttk.Entry(labelframeleft, textvariable = self.var_country, width = 25, font = ("times new roman", 13, "bold"))
        txtCountry.grid(row = 11, column = 1)

# Customer_Status_ID
        lblCustomer_Status_ID = Label(labelframeleft, text = "Customer Status ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblCustomer_Status_ID.grid(row = 12, column = 0, sticky = W)

        txtCustomer_Status_ID = ttk.Entry(labelframeleft, textvariable = self.var_customer_status_id, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtCustomer_Status_ID.grid(row = 12, column = 1)

# Customer_Description
        lblCustomer_Description = Label(labelframeleft, text = "Customer Description:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblCustomer_Description.grid(row = 13, column = 0, sticky = W)

        combo_Customer_Description = ttk.Combobox(labelframeleft, textvariable = self.var_customer_decription, font = ("times new roman", 12, "bold"), width = 26, state = "readonly")
        combo_Customer_Description["value"] = ("Active", "Inactive")
        combo_Customer_Description.current(0)
        combo_Customer_Description.grid(row = 13, column = 1)

# Address_Type_ID
        lblAddress_Type_ID = Label(labelframeleft, text = "Address Type ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblAddress_Type_ID.grid(row = 14, column = 0, sticky = W)

        txtAddress_Type_ID = ttk.Entry(labelframeleft, textvariable = self.var_address_type_id, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtAddress_Type_ID.grid(row = 14, column = 1)

# Address_Description
        lblAddressDescription = Label(labelframeleft, text = "Address Description:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblAddressDescription.grid(row = 15, column = 0, sticky = W)

        combo_AddressDescription = ttk.Combobox(labelframeleft, textvariable = self.var_address_description, font = ("times new roman", 12, "bold"), width = 26, state = "readonly")
        combo_AddressDescription["value"] = ("In state", "Out of State", "Out of Country")
        combo_AddressDescription.current(0)
        combo_AddressDescription.grid(row = 15, column = 1)

#=================================================================btns========================================================
        btn_frame = Frame(labelframeleft, bd = 2, relief = RIDGE)
        btn_frame.place(x = 0, y = 615, width = 412, height = 35)

        btnAdd = Button(btn_frame, text = "Add", command = self.add_customer, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnAdd.grid(row = 0, column = 0, padx = 1)

        btnUpadate = Button(btn_frame, text = "Update", command = self.update, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnUpadate.grid(row = 0, column = 1, padx = 1)

        btnDelete = Button(btn_frame, text = "Delete", command = self.Delete, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnDelete.grid(row = 0, column = 2, padx = 1)

        btnReset = Button(btn_frame, text = "Reset",  command = self.Reset, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnReset.grid(row = 0, column = 3, padx = 1)

#=================================================================table Frame search system========================================================
        Table_Frame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        Table_Frame.place(x = 435, y = 50, width = 860, height = 677)

#=================================================================Show data table========================================================        
        details_table = Frame(Table_Frame, bd = 2, relief = RIDGE)
        details_table.place(x = 0, y = 0, width = 860, height = 652)

        scroll_x = ttk.Scrollbar(details_table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient = VERTICAL)

        self.Cust_details_Table = ttk.Treeview(details_table, column = ("Customer ID", "First Name", "Middle Name", "Last Name", "Email", "Phone", "Street", "City", "State", "ZipCode",
                                                                        "Country", "Customer Status", "Address Type"),
                                                                        xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Cust_details_Table.xview)
        scroll_y.config(command = self.Cust_details_Table.yview)

        self.Cust_details_Table.heading("Customer ID", text = "Customer ID")
        self.Cust_details_Table.heading("First Name", text = "First Name")
        self.Cust_details_Table.heading("Middle Name", text = "Middle Name")
        self.Cust_details_Table.heading("Last Name", text = "Last Name")
        self.Cust_details_Table.heading("Email", text = "Email")
        self.Cust_details_Table.heading("Phone", text = "Phone")
        self.Cust_details_Table.heading("Street", text = "Street")
        self.Cust_details_Table.heading("City", text = "City")
        self.Cust_details_Table.heading("State", text = "State")
        self.Cust_details_Table.heading("ZipCode", text = "ZipCode")
        self.Cust_details_Table.heading("Country", text = "Country")
        self.Cust_details_Table.heading("Customer Status", text = "Customer Status")
        self.Cust_details_Table.heading("Address Type", text = "Address Type")

        self.Cust_details_Table["show"] = "headings"

        self.Cust_details_Table.column("Customer ID", width = 80, anchor = CENTER)
        self.Cust_details_Table.column("First Name", width = 80, anchor = CENTER)
        self.Cust_details_Table.column("Middle Name", width = 80, anchor = CENTER)
        self.Cust_details_Table.column("Last Name", width = 80, anchor = CENTER)
        self.Cust_details_Table.column("Email", width = 180, anchor = CENTER)
        self.Cust_details_Table.column("Phone", width = 80, anchor = CENTER)
        self.Cust_details_Table.column("Street", width = 180, anchor = CENTER)
        self.Cust_details_Table.column("City", width = 80, anchor = CENTER)
        self.Cust_details_Table.column("State", width = 60, anchor = CENTER)
        self.Cust_details_Table.column("ZipCode", width = 60, anchor = CENTER)
        self.Cust_details_Table.column("Country", width = 60, anchor = CENTER)
        self.Cust_details_Table.column("Customer Status", width = 100, anchor = CENTER)
        self.Cust_details_Table.column("Address Type", width = 80, anchor = CENTER)

        self.Cust_details_Table.pack(fill = BOTH, expand = 1)
        self.Cust_details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

#=================================================================Commands========================================================  
    def add_customer(self):
        if self.var_first_name.get() == "" or self.var_last_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("INSERT INTO Address_Type (Address_Type_ID, Address_Description) VALUES (?, ?)", self.var_address_type_id.get(), self.var_address_description.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Customer_Addresses (Address_ID, Street_Name, City, State, ZipCode, Country, Address_Type_ID) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                            self.var_address_id.get(), self.var_street_name.get(), self.var_city.get(), self.var_state.get(),
                                            self.var_zip_code.get(), self.var_country.get(), self.var_address_type_id.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Customer_Status (Customer_Status_ID, Customer_Description) VALUES (?, ?)", self.var_customer_status_id.get(), self.var_customer_decription.get())  
                        conn.commit()

                        my_cursor.execute("INSERT into Customers (Customer_ID, First_Name, Middle_Name, Last_Name, Email_Address, Phone_Number, Address_ID, Customer_Status_ID)\
                                            values (?, ?, ?, ?, ?, ?, ?, ?)",
                                            self.var_customer_id.get(), self.var_first_name.get(), self.var_middle_name.get(), self.var_last_name.get(),
                                            self.var_email_address.get(), self.var_phone_number.get(), self.var_address_id.get(), self.var_customer_status_id.get())
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Customer has been added", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
     
    def fetch_data(self):
        try:
                conn = pyodbc.connect(Connect)
                print("Connection to MySQL DB successful")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Customers.Customer_ID, Customers.First_Name, Customers.Middle_Name, Customers.Last_Name, Customers.Email_Address, Customers.Phone_Number,\
		                        Customer_Addresses.Street_Name, Customer_Addresses.City, Customer_Addresses.State, Customer_Addresses.ZipCode, Customer_Addresses.Country,\
		                        Address_Type.Address_Description,\
		                        Customer_Status.Customer_Description\
                                FROM Customer_Status\
                                INNER JOIN Customers ON Customers.Customer_Status_ID = Customer_Status.Customer_Status_ID\
                                INNER JOIN Customer_Addresses ON Customer_Addresses.Address_ID = Customers.Address_ID\
                                INNER JOIN Address_Type ON Customer_Addresses.Address_Type_ID = Address_Type.Address_Type_ID")
                
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                        self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
                        for i in rows:
                                self.Cust_details_Table.insert("",END,values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12]))
                        conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)

    def get_cursor(self, event = ""):
        cursor_row = self.Cust_details_Table.focus()
        content = self.Cust_details_Table.item(cursor_row)
        row = content["values"]

        self.var_customer_id.set(row[0])
        self.var_first_name.set(row[1])
        self.var_middle_name.set(row[2])
        self.var_last_name.set(row[3])
        self.var_email_address.set(row[4])
        self.var_phone_number.set(row[5])
        self.var_street_name.set(row[6])
        self.var_city.set(row[7])
        self.var_state.set(row[8])
        self.var_zip_code.set(row[9])
        self.var_country.set(row[10])
        self.var_address_description.set(row[11])
        self.var_customer_decription.set(row[12])

    def update(self):
        if self.var_first_name.get() == "" or self.var_last_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("UPDATE Address_Type SET Address_Description = ?\
                                        WHERE Address_Type_ID = ?",
                                        self.var_address_description.get(), self.var_customer_id.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Customer_Addresses SET Street_Name = ?, City = ?, State = ?, ZipCode = ?, Country = ?\
                                        WHERE Address_ID = ?",
                                        self.var_street_name.get(), self.var_city.get(), self.var_state.get(),
                                        self.var_zip_code.get(), self.var_country.get(), self.var_customer_id.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Customer_Status SET Customer_Description = ?\
                                        WHERE Customer_Status_ID = ?",
                                        self.var_customer_decription.get(), self.var_customer_id.get())  
                        conn.commit()

                        my_cursor.execute("UPDATE Customers SET First_Name = ?, Middle_Name = ?, Last_Name = ?, Email_Address = ?, Phone_Number = ?\
                                        WHERE Customer_ID = ?",
                                        self.var_first_name.get(), self.var_middle_name.get(), self.var_last_name.get(),
                                        self.var_email_address.get(), self.var_phone_number.get(), self.var_customer_id.get())
                        conn.commit()

                        self.fetch_data()
                        conn.close()

                        messagebox.showinfo("Update", "Customer details has been updated successfully", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)  

    def Delete(self):
        Delete = messagebox.askyesno("Furniture Management Apllication", "Do you want to delete this customer", parent = self.root)
        if Delete > 0:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("DELETE FROM Customers WHERE Customer_ID = ?", self.var_customer_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Customer_Status WHERE Customer_Status_ID = ?", self.var_customer_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Customer_Addresses WHERE Address_ID = ?", self.var_customer_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Address_Type WHERE Address_Type_ID = ?", self.var_customer_id.get())
                        conn.commit()

                        # self.fetch_data()
                        # conn.close()
                        # self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
        else:
                if not Delete:
                        return
        self.fetch_data()
        conn.close()
        self.Reset()

    def Reset(self):
        x = random.randint(1000,9999)
        self.var_customer_id.set(str(x)),
        self.var_address_id.set(str(x)),
        self.var_customer_status_id.set(str(x)),
        self.var_address_type_id.set(str(x)),
        self.var_first_name.set(""),
        self.var_middle_name.set(""),
        self.var_last_name.set(""),
        self.var_email_address.set(""),
        self.var_phone_number.set(""),
        self.var_customer_decription.set(""),
        self.var_street_name.set(""),
        self.var_city.set(""),
        self.var_state.set(""),
        self.var_address_description.set(""),
        self.var_zip_code.set(""),
        self.var_country.set("")
           
if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
