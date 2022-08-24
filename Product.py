from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk
import random
import pyodbc
from tkinter import messagebox
from connection import Connect
class Product_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Product")
        self.root.geometry("1295x930+230+220")
        self.root.resizable(False, False)
#=================================================================Variables========================================================
        x = random.randint(1000,9999)

        self.var_product_id = StringVar()
        self.var_product_id.set(str(x))

        self.var_product_name = StringVar()
        self.var_category_name = StringVar()
        self.var_description = StringVar()
        self.var_unit = StringVar()
        self.var_unit_price = StringVar()
        self.var_in_stock = StringVar()
        self.var_on_order = StringVar()
        self.var_reorder_level = StringVar()
        self.var_discontinued = StringVar()
        self.var_company_name = StringVar()
        self.var_contact_name = StringVar()
        self.var_contact_title = StringVar()
        self.var_homepage = StringVar()
        self.var_address = StringVar()
        self.var_city = StringVar()
        self.var_state = StringVar()
        self.var_zipcode = StringVar()
        self.var_country = StringVar()
        self.var_phone = StringVar()
        self.var_fax = StringVar()
        self.var_details = StringVar()
        self.var_status = StringVar()
#=================================================================title========================================================
        lbl_title = Label(self.root, text = "ADD PRODUCT DETAILS", font = ("times new roman", 18, "bold"), bg = "black", fg = "gold")
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

#=================================================================Logo========================================================
        img2 = Image.open(r"Images\icon.jpg")
        img2 = img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image = self.photoimg2, bd = 0, relief = RIDGE)
        lblimg.place(x = 5, y = 2, width = 100, height = 50)

#=================================================================labelFrame========================================================
        labelframeleft = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Product Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        labelframeleft.place(x = 5, y = 50, width = 425, height = 875)

#=================================================================label and entries========================================================
# Product ID       
        lblProductID = Label(labelframeleft, text = "Product ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblProductID.grid(row = 0, column = 0, sticky = W)

        txtProductID = ttk.Entry(labelframeleft, textvariable = self.var_product_id, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtProductID.grid(row = 0, column = 1)

# Product Name
        lblProductName = Label(labelframeleft, text = "Product Name:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblProductName.grid(row = 1, column = 0, sticky = W)

        txtProductName = ttk.Entry(labelframeleft, textvariable = self.var_product_name, width = 25, font = ("times new roman", 13, "bold"))
        txtProductName.grid(row = 1, column = 1)

# Category Name
        lblCategoryName = Label(labelframeleft, text = "Category Name:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblCategoryName.grid(row = 2, column = 0, sticky = W)

        txtCategoryName = ttk.Entry(labelframeleft, textvariable = self.var_category_name, width = 25, font = ("times new roman", 13, "bold"))
        txtCategoryName.grid(row = 2, column = 1)

# Description
        lblDescription = Label(labelframeleft, text = "Description:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDescription.grid(row = 3, column = 0, sticky = W)

        txtDescription = ttk.Entry(labelframeleft, textvariable = self.var_description, width = 25, font = ("times new roman", 13, "bold"))
        txtDescription.grid(row = 3, column = 1)

# Unit
        lblUnit = Label(labelframeleft, text = "Unit:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblUnit.grid(row = 4, column = 0, sticky = W)

        txtUnit = ttk.Entry(labelframeleft, textvariable = self.var_unit, width = 25, font = ("times new roman", 13, "bold"))
        txtUnit.grid(row = 4, column = 1)

# Unit Price
        lblUnitPrice = Label(labelframeleft, text = "Unit Price:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblUnitPrice.grid(row = 5, column = 0, sticky = W)

        txtUnitPrice = ttk.Entry(labelframeleft, textvariable = self.var_unit_price, width = 25, font = ("times new roman", 13, "bold"))
        txtUnitPrice.grid(row = 5, column = 1)

# In Stock
        lblInStock = Label(labelframeleft, text = "In stock:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblInStock.grid(row = 6, column = 0, sticky = W)

        txtInStock = ttk.Entry(labelframeleft, textvariable = self.var_in_stock, width = 25, font = ("times new roman", 13, "bold"))
        txtInStock.grid(row = 6, column = 1)

# On Order
        lblOnOrder = Label(labelframeleft, text = "On Order:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblOnOrder.grid(row = 7, column = 0, sticky = W)

        txtOnOrder = ttk.Entry(labelframeleft, textvariable = self.var_on_order, width = 25, font = ("times new roman", 13, "bold"))
        txtOnOrder.grid(row = 7, column = 1)

# Reorder Level
        lblReorderLevel = Label(labelframeleft, text = "Reorder Level:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblReorderLevel.grid(row = 8, column = 0, sticky = W)

        txtReorderLevel = ttk.Entry(labelframeleft, textvariable = self.var_reorder_level, width = 25, font = ("times new roman", 13, "bold"))
        txtReorderLevel.grid(row = 8, column = 1)

# Discontinued
        lblDiscontinued = Label(labelframeleft, text = "Discontinued:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDiscontinued.grid(row = 9, column = 0, sticky = W)

        combo_Discontinued = ttk.Combobox(labelframeleft, textvariable = self.var_discontinued, font = ("times new roman", 12, "bold"), width = 26)
        combo_Discontinued["value"] = ("Yes", "No")
        combo_Discontinued.current(0)
        combo_Discontinued.grid(row = 9, column = 1)

# Company Name
        lblCompanyName = Label(labelframeleft, text = "Company Name:", font = ("times new roman", 13, "bold"), padx = 2, pady = 6)
        lblCompanyName.grid(row = 10, column = 0, sticky = W)

        txtCompanyName = ttk.Entry(labelframeleft, textvariable = self.var_company_name, width = 25, font = ("times new roman", 13, "bold"))
        txtCompanyName.grid(row = 10, column = 1)

# Contact Name
        lblContactName = Label(labelframeleft, text = "Contact Name:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblContactName.grid(row = 11, column = 0, sticky = W)

        txtContactName = ttk.Entry(labelframeleft, textvariable = self.var_contact_name, width = 25, font = ("times new roman", 13, "bold"))
        txtContactName.grid(row = 11, column = 1)

# Contact Title
        lblContactTitle = Label(labelframeleft, text = "Contact Title:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblContactTitle.grid(row = 12, column = 0, sticky = W)

        combo_Location = ttk.Combobox(labelframeleft, textvariable = self.var_contact_title, font = ("times new roman", 12, "bold"), width = 26)
        combo_Location["value"] = ("Salesperson", "Sales Manager", "Agent")
        combo_Location.current(0)
        combo_Location.grid(row = 12, column = 1)

# Homepage
        lblHomepage = Label(labelframeleft, text = "Homepage:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblHomepage.grid(row = 13, column = 0, sticky = W)

        txtHomepage = ttk.Entry(labelframeleft, textvariable = self.var_homepage, width = 25, font = ("times new roman", 13, "bold"))
        txtHomepage.grid(row = 13, column = 1)

# Address
        lblAddress = Label(labelframeleft, text = "Address:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblAddress.grid(row = 14, column = 0, sticky = W)

        txtAddress = ttk.Entry(labelframeleft, textvariable = self.var_address, width = 25, font = ("times new roman", 13, "bold"))
        txtAddress.grid(row = 14, column = 1)

# City
        lblCity = Label(labelframeleft, text = "City:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblCity.grid(row = 15, column = 0, sticky = W)

        txtCity = ttk.Entry(labelframeleft, textvariable = self.var_city, width = 25, font = ("times new roman", 13, "bold"))
        txtCity.grid(row = 15, column = 1)

# State
        lblState = Label(labelframeleft, text = "State:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblState.grid(row = 16, column = 0, sticky = W)

        txtZipcode = ttk.Entry(labelframeleft, textvariable = self.var_state, width = 25, font = ("times new roman", 13, "bold"))
        txtZipcode.grid(row = 16, column = 1)

# Zipcode
        lblZipcode = Label(labelframeleft, text = "ZipCode:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblZipcode.grid(row = 17, column = 0, sticky = W)

        txtZipcode = ttk.Entry(labelframeleft, textvariable = self.var_zipcode, width = 25, font = ("times new roman", 13, "bold"))
        txtZipcode.grid(row = 17, column = 1)

# Country
        lblCountry = Label(labelframeleft, text = "Country:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblCountry.grid(row = 18, column = 0, sticky = W)

        txtCountry = ttk.Entry(labelframeleft, textvariable = self.var_country, width = 25, font = ("times new roman", 13, "bold"))
        txtCountry.grid(row = 18, column = 1)

# Phone
        lblPhone = Label(labelframeleft, text = "Phone:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblPhone.grid(row = 19, column = 0, sticky = W)

        txtPhone = ttk.Entry(labelframeleft, textvariable = self.var_phone, width = 25, font = ("times new roman", 13, "bold"))
        txtPhone.grid(row = 19, column = 1)

# Fax
        lblFax = Label(labelframeleft, text = "Fax:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblFax.grid(row = 20, column = 0, sticky = W)

        txtFax = ttk.Entry(labelframeleft, textvariable = self.var_fax, width = 25, font = ("times new roman", 13, "bold"))
        txtFax.grid(row = 20, column = 1)

# Details
        lblDetails = Label(labelframeleft, text = "Details:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDetails.grid(row = 21, column = 0, sticky = W)

        txtDetails = ttk.Entry(labelframeleft, textvariable = self.var_details, width = 25, font = ("times new roman", 13, "bold"))
        txtDetails.grid(row = 21, column = 1)

# Status
        lblStatus = Label(labelframeleft, text = "Status:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblStatus.grid(row = 22, column = 0, sticky = W)

        combo_Status = ttk.Combobox(labelframeleft, textvariable = self.var_status, font = ("times new roman", 12, "bold"), width = 26)
        combo_Status["value"] = ("Active", "Inactive")
        combo_Status.current(0)
        combo_Status.grid(row = 22, column = 1)
#=================================================================btns========================================================
        btn_frame = Frame(labelframeleft, bd = 2, relief = RIDGE)
        btn_frame.place(x = 0, y = 810, width = 412, height = 35)

        btnAdd = Button(btn_frame, text = "Add", command = self.add, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnAdd.grid(row = 0, column = 0, padx = 1)

        btnUpadate = Button(btn_frame, text = "Update", command = self.update, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnUpadate.grid(row = 0, column = 1, padx = 1)

        btnDelete = Button(btn_frame, text = "Delete", command = self.Delete, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnDelete.grid(row = 0, column = 2, padx = 1)

        btnReset = Button(btn_frame, text = "Reset", command = self.Reset, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnReset.grid(row = 0, column = 3, padx = 1)

#=================================================================table Frame View========================================================
        Table_Frame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        Table_Frame.place(x = 435, y = 50, width = 860, height = 875)

#=================================================================Show data table========================================================        
        details_table = Frame(Table_Frame, bd = 2, relief = RIDGE)
        details_table.place(x = 0, y = 0, width = 860, height = 850)

        scroll_x = ttk.Scrollbar(details_table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient = VERTICAL)

        self.Product_details_Table = ttk.Treeview(details_table, column = ("ID", "Product Name", "Category Name", "Description", "Unit", "Unit Price", "In Stock", "On Order", "Reorder Level", "Discontinued",
                                                                        "Company", "Contact", "Title", "Homepage", "Address", "City", "State", "ZipCode", "Country", "Phone", "Fax", "Details", "Status"),
                                                                        xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Product_details_Table.xview)
        scroll_y.config(command = self.Product_details_Table.yview)

        self.Product_details_Table.heading("ID", text = "ID")
        self.Product_details_Table.heading("Product Name", text = "Product Name")
        self.Product_details_Table.heading("Category Name", text = "Category Name")
        self.Product_details_Table.heading("Description", text = "Description")
        self.Product_details_Table.heading("Unit", text = "Unit")
        self.Product_details_Table.heading("Unit Price", text = "Unit Price")
        self.Product_details_Table.heading("In Stock", text = "In Stock")
        self.Product_details_Table.heading("On Order", text = "On Order")
        self.Product_details_Table.heading("Reorder Level", text = "Reorder Level")
        self.Product_details_Table.heading("Discontinued", text = "Discontinued")
        self.Product_details_Table.heading("Company", text = "Company")
        self.Product_details_Table.heading("Contact", text = "Contact")
        self.Product_details_Table.heading("Title", text = "Title")
        self.Product_details_Table.heading("Homepage", text = "Homepage")
        self.Product_details_Table.heading("Address", text = "Address")
        self.Product_details_Table.heading("City", text = "City")
        self.Product_details_Table.heading("State", text = "State")
        self.Product_details_Table.heading("ZipCode", text = "ZipCode")
        self.Product_details_Table.heading("Country", text = "Country")
        self.Product_details_Table.heading("Phone", text = "Phone")
        self.Product_details_Table.heading("Fax", text = "Fax")
        self.Product_details_Table.heading("Details", text = "Details")
        self.Product_details_Table.heading("Status", text = "Status")

        self.Product_details_Table["show"] = "headings"

        self.Product_details_Table.column("ID", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Product Name", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Category Name", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Description", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Unit", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Unit Price", width = 100, anchor = CENTER)
        self.Product_details_Table.column("In Stock", width = 100, anchor = CENTER)
        self.Product_details_Table.column("On Order", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Reorder Level", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Discontinued", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Company", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Contact", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Title", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Homepage", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Address", width = 100, anchor = CENTER)
        self.Product_details_Table.column("City", width = 100, anchor = CENTER)
        self.Product_details_Table.column("State", width = 100, anchor = CENTER)
        self.Product_details_Table.column("ZipCode", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Country", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Phone", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Fax", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Details", width = 100, anchor = CENTER)
        self.Product_details_Table.column("Status", width = 100, anchor = CENTER)

        self.Product_details_Table.pack(fill = BOTH, expand = 1)
        self.Product_details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add(self):
        if self.var_product_name.get() == "" or self.var_discontinued.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("INSERT INTO Categories (Category_ID, Category_Name, Description)\
                                                VALUES (?, ?, ?)",
                                                self.var_product_id.get(), self.var_category_name.get(), self.var_description.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Supplier_Status (Supplier_Status_ID, Status)\
                                                VALUES (?, ?)",
                                                self.var_product_id.get(), self.var_status.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Supplier_Addresses (Supplier_Address_ID, Address, City, State, ZipCode, Country, Phone, Fax, Details)\
                                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                                self.var_product_id.get(), self.var_address.get(), self.var_city.get(), self.var_state.get(), self.var_zipcode.get(),
                                                self.var_country.get(), self.var_phone.get(), self.var_fax.get(), self.var_details.get())  
                        conn.commit()

                        my_cursor.execute("INSERT INTO Suppliers (Supplier_ID, Company_Name, Contact_Name, Contact_Title, Supplier_Address_ID, Homepage, Supplier_Status_ID)\
                                                VALUES (?, ?, ?, ?, ?, ?, ?)",
                                                self.var_product_id.get(), self.var_company_name.get(), self.var_contact_name.get(), self.var_contact_title.get(),
                                                self.var_product_id.get(), self.var_homepage.get(), self.var_product_id.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Products (Product_ID, Product_Name, Supplier_ID, Category_ID, Unit, Unit_Price, In_Stock, On_Order, Reorder_Level, Discontinued)\
                                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                                self.var_product_id.get(), self.var_product_name.get(), self.var_product_id.get(), self.var_product_id.get(), self.var_unit.get(),
                                                self.var_unit_price.get(), self.var_in_stock.get(), self.var_on_order.get(), self.var_reorder_level.get(), self.var_discontinued.get())
                        conn.commit()
                        
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Product has been added", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
    
    def fetch_data(self):
        try:
                conn = pyodbc.connect(Connect)
                print("Connection to MySQL DB successful")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Products.Product_ID, Products.Product_Name, Categories.Category_Name, Categories.Description, Products.Unit, Products.Unit_Price, Products.In_Stock, Products.On_Order, Products.Reorder_Level, Products.Discontinued,\
		                                     Suppliers.Company_Name, Suppliers.Contact_Name, Suppliers.Contact_Title, Suppliers.Homepage,\
		                                     Supplier_Addresses.Address, Supplier_Addresses.City, Supplier_Addresses.State, Supplier_Addresses.ZipCode, Supplier_Addresses.Country, Supplier_Addresses.Phone, Supplier_Addresses.Fax, Supplier_Addresses.Details,\
		                                     Supplier_Status.Status\
                                    FROM Suppliers\
                                    INNER JOIN Products ON Products.Supplier_ID = Suppliers.Supplier_ID\
                                    INNER JOIN Categories ON Products.Category_ID = Categories.Category_ID\
                                    INNER JOIN Supplier_Addresses ON Suppliers.Supplier_Address_ID = Supplier_Addresses.Supplier_Address_ID\
                                    INNER JOIN Supplier_Status ON Suppliers.Supplier_Status_ID = Supplier_Status.Supplier_Status_ID")
                
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                        self.Product_details_Table.delete(*self.Product_details_Table.get_children())
                        for i in rows:
                                self.Product_details_Table.insert("",END,values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22]))
                        conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)

    def get_cursor(self, event = ""):
        cursor_row = self.Product_details_Table.focus()
        content = self.Product_details_Table.item(cursor_row)
        row = content["values"]

        self.var_product_id.set(row[0])
        self.var_product_name.set(row[1])
        self.var_category_name.set(row[2])
        self.var_description.set(row[3])
        self.var_unit.set(row[4])
        self.var_unit_price.set(row[5])
        self.var_in_stock.set(row[6])
        self.var_on_order.set(row[7])
        self.var_reorder_level.set(row[8])
        self.var_discontinued.set(row[9])
        self.var_company_name.set(row[10])
        self.var_contact_name.set(row[11])
        self.var_contact_title.set(row[12])
        self.var_homepage.set(row[13])
        self.var_address.set(row[14])
        self.var_city.set(row[15])
        self.var_state.set(row[16])
        self.var_zipcode.set(row[17])
        self.var_country.set(row[18])
        self.var_phone.set(row[19])
        self.var_fax.set(row[20])
        self.var_details.set(row[21])
        self.var_status.set(row[22])

    def update(self):
        if self.var_product_name.get() == "" or self.var_discontinued.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("UPDATE Categories\
                                            SET Category_Name = ?, Description = ?\
                                            WHERE Category_ID = ?",
                                            self.var_category_name.get(), self.var_description.get(), self.var_product_id.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Supplier_Status\
                                            SET Status = ?\
                                            WHERE Supplier_Status_ID = ?",
                                            self.var_status.get(), self.var_product_id.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Supplier_Addresses\
                                            SET Address = ?, City = ?, State = ?, ZipCode = ?, Country = ?, Phone = ?, Fax = ?, Details = ?\
                                            WHERE Supplier_Address_ID = ?",
                                            self.var_address.get(), self.var_city.get(), self.var_state.get(), self.var_zipcode.get(),
                                            self.var_country.get(), self.var_phone.get(), self.var_fax.get(), self.var_details.get(), self.var_product_id.get())  
                        conn.commit()

                        my_cursor.execute("UPDATE Suppliers\
                                            SET Company_Name = ?, Contact_Name = ?, Contact_Title = ?, Homepage = ?\
                                            WHERE Supplier_ID = ?",
                                            self.var_company_name.get(), self.var_contact_name.get(), self.var_contact_title.get(),
                                            self.var_homepage.get(), self.var_product_id.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Products\
                                            SET Product_Name = ?, Unit = ?, Unit_Price = ?, In_Stock = ?, On_Order = ?, Reorder_Level = ?, Discontinued = ?\
                                            WHERE Product_ID = ?",
                                            self.var_product_name.get(), self.var_unit.get(), self.var_unit_price.get(), self.var_in_stock.get(),
                                            self.var_on_order.get(), self.var_reorder_level.get(), self.var_discontinued.get(), self.var_product_id.get())
                        conn.commit()

                        self.fetch_data()
                        conn.close()

                        messagebox.showinfo("Update", "Product details have been updated successfully", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)  

    def Delete(self):
        Delete = messagebox.askyesno("Furniture Management Application", "Do you want to delete this product?", parent = self.root)
        if Delete > 0:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("DELETE FROM Products WHERE Product_ID = ?", self.var_product_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Categories WHERE Category_ID = ?", self.var_product_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Suppliers WHERE Supplier_ID = ?", self.var_product_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Supplier_Addresses WHERE Supplier_Address_ID = ?", self.var_product_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Supplier_Status WHERE Supplier_Status_ID = ?", self.var_product_id.get())
                        conn.commit()

                        self.fetch_data()
                        conn.close()
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
                        print(str(es))
        else:
                if not Delete:
                        return
        conn.commit()
        self.fetch_data()
        conn.close()

    def Reset(self):
        x = random.randint(1000,9999)
        self.var_product_id.set(str(x))
        self.var_product_name.set(""),
        self.var_category_name.set(""),
        self.var_description.set(""),
        self.var_unit.set(""),
        self.var_unit_price.set(""),
        self.var_in_stock.set(""),
        self.var_on_order.set(""),
        self.var_reorder_level.set(""),
        self.var_discontinued.set(""),
        self.var_company_name.set(""),
        self.var_contact_name.set(""),
        self.var_contact_title.set(""),
        self.var_homepage.set(""),
        self.var_address.set(""),
        self.var_city.set(""),
        self.var_state.set(""),
        self.var_zipcode.set(""),
        self.var_country.set(""),
        self.var_phone.set(""),
        self.var_fax.set(""),
        self.var_details.set(""),
        self.var_status.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Product_Win(root)
    root.mainloop()
