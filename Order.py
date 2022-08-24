from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk
import random
import pyodbc
from tkinter import messagebox
from connection import Connect
class Order_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Order")
        self.root.geometry("1295x730+230+220")
        self.root.resizable(False, False)
#=================================================================Variables========================================================
        x = random.randint(1000,9999)

        self.var_Order_id = StringVar()
        self.var_Order_id.set(str(x))

        # self.var_Order_Item_id = StringVar()
        # self.var_Order_Item_id.set(str(x))

        self.var_customer_id = StringVar()
        # self.var_customer_id.set(str(x))

        self.var_product_id = StringVar()
        # self.var_product_id.set(str(x))

        # self.var_line_item_id = StringVar()
        # self.var_line_item_id.set(str(x))

        # self.var_invoice_id = StringVar()
        # self.var_invoice_id.set(str(x))

        self.var_product_quantity = StringVar()
        self.var_itemcost = StringVar()
        self.var_satisfaction_item = StringVar()
        self.var_order_detail = StringVar()
        self.var_order_date = StringVar()
        self.var_Discount = StringVar()
        self.var_Delivery_cost = StringVar()
        self.var_Invoice_date = StringVar()
        self.var_Invoice_detail = StringVar()
#=================================================================title========================================================
        lbl_title = Label(self.root, text = "ADD ORDER AND INVOICE DETAILS", font = ("times new roman", 18, "bold"), bg = "black", fg = "gold")
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

#=================================================================Logo========================================================
        img2 = Image.open(r"Images\icon.jpg")
        img2 = img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image = self.photoimg2, bd = 0, relief = RIDGE)
        lblimg.place(x = 5, y = 2, width = 100, height = 50)

#=================================================================labelFrame========================================================
        labelframeleft = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Order Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        labelframeleft.place(x = 5, y = 50, width = 425, height = 677)

#=================================================================label and entries========================================================
# Order ID        
        lblOrderID = Label(labelframeleft, text = "Order ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblOrderID.grid(row = 0, column = 0, sticky = W)

        entry_ref = ttk.Entry(labelframeleft, textvariable = self.var_Order_id, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        entry_ref.grid(row = 0, column = 1)

# Customer ID
        lblCustomerID = Label(labelframeleft, text = "Customer ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblCustomerID.grid(row = 1, column = 0, sticky = W)

        txtCustomerID = ttk.Entry(labelframeleft, textvariable = self.var_customer_id, width = 25, font = ("times new roman", 13, "bold"))
        txtCustomerID.grid(row = 1, column = 1)

# Product ID
        lblProductID = Label(labelframeleft, text = "Product ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblProductID.grid(row = 2, column = 0, sticky = W)

        txtProductID = ttk.Entry(labelframeleft, textvariable = self.var_product_id, width = 25, font = ("times new roman", 13, "bold"))
        txtProductID.grid(row = 2, column = 1)

# Price
        lblItemCost = Label(labelframeleft, text = "Price($):", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblItemCost.grid(row = 3, column = 0, sticky = W)

        txtItemCost = ttk.Entry(labelframeleft, textvariable = self.var_itemcost, width = 25, font = ("times new roman", 13, "bold"))
        txtItemCost.grid(row = 3, column = 1)

# Product Quantity
        lblProductQuantity = Label(labelframeleft, text = "Product Quantity:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblProductQuantity.grid(row = 4, column = 0, sticky = W)

        combo_ProductQuantity = ttk.Combobox(labelframeleft, textvariable = self.var_product_quantity, font = ("times new roman", 12, "bold"), width = 26)
        combo_ProductQuantity["value"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        combo_ProductQuantity.current(0)
        combo_ProductQuantity.grid(row = 4, column = 1)

# Satisfaction Item
        lblSatisfactionItem = Label(labelframeleft, text = "Satisfaction Item:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblSatisfactionItem.grid(row = 5, column = 0, sticky = W)

        combo_SatisfactionItem = ttk.Combobox(labelframeleft, textvariable = self.var_satisfaction_item, font = ("times new roman", 12, "bold"), width = 26)
        combo_SatisfactionItem["value"] = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        combo_SatisfactionItem.current(0)
        combo_SatisfactionItem.grid(row = 5, column = 1)

# Other Order Detail
        lblOtherOrderDetail = Label(labelframeleft, text = "Order Detail:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblOtherOrderDetail.grid(row = 6, column = 0, sticky = W)

        txtOtherOrderDetail = ttk.Entry(labelframeleft, textvariable = self.var_order_detail, width = 25, font = ("times new roman", 13, "bold"))
        txtOtherOrderDetail.grid(row = 6, column = 1)
# Order Date
        lblOrderDate = Label(labelframeleft, text = "Order Date:", font = ("times new roman", 13, "bold"), padx = 2, pady = 6)
        lblOrderDate.grid(row = 7, column = 0, sticky = W)

        txtCity = ttk.Entry(labelframeleft, textvariable = self.var_order_date, width = 25, font = ("times new roman", 13, "bold"))
        txtCity.grid(row = 7, column = 1)

# Delivery Cost
        lblDeliveryCost = Label(labelframeleft, text = "Delivery Cost($):", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDeliveryCost.grid(row = 8, column = 0, sticky = W)

        combo_Discount = ttk.Combobox(labelframeleft, textvariable = self.var_Delivery_cost, font = ("times new roman", 12, "bold"), width = 26)
        combo_Discount["value"] = ("0", "119", "419")
        combo_Discount.current(0)
        combo_Discount.grid(row = 8, column = 1)

# Invoice Details
        lblInvoiceDetails = Label(labelframeleft, text = "Invoice Details:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblInvoiceDetails.grid(row = 9, column = 0, sticky = W)

        txtInvoiceDetails = ttk.Entry(labelframeleft, textvariable = self.var_Invoice_detail, width = 25, font = ("times new roman", 13, "bold"))
        txtInvoiceDetails.grid(row = 9, column = 1)

# Invoice Date
        lblInvoiceDate = Label(labelframeleft, text = "Invoice Date:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblInvoiceDate.grid(row = 10, column = 0, sticky = W)

        txtInvoiceDate = ttk.Entry(labelframeleft, textvariable = self.var_Invoice_date, width = 25, font = ("times new roman", 13, "bold"))
        txtInvoiceDate.grid(row = 10, column = 1)

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

        self.Order_details_Table = ttk.Treeview(details_table, column = ("Invoice ID", "Customer ID", "Product ID", "Price", "Quantity", "Satisfaction Item",
                                                                        "Order Detail", "Order Date", "Delivery Cost", "Total Amount", "Invoice Details", "Invoice Date"),
                                                                        xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Order_details_Table.xview)
        scroll_y.config(command = self.Order_details_Table.yview)

        self.Order_details_Table.heading("Invoice ID", text = "Invoice ID")
        self.Order_details_Table.heading("Customer ID", text = "Customer ID")
        self.Order_details_Table.heading("Product ID", text = "Product ID")
        self.Order_details_Table.heading("Price", text = "Price")
        self.Order_details_Table.heading("Quantity", text = "Quantity")
        self.Order_details_Table.heading("Satisfaction Item", text = "Satisfaction Item")
        self.Order_details_Table.heading("Order Detail", text = "Order Detail")
        self.Order_details_Table.heading("Order Date", text = "Order Date")
        self.Order_details_Table.heading("Delivery Cost", text = "Delivery Cost")
        self.Order_details_Table.heading("Total Amount", text = "Total Amount")
        self.Order_details_Table.heading("Invoice Details", text = "Invoice Details")
        self.Order_details_Table.heading("Invoice Date", text = "Invoice Date")

        self.Order_details_Table["show"] = "headings"

        self.Order_details_Table.column("Invoice ID", width = 100, anchor = CENTER)
        self.Order_details_Table.column("Customer ID", width = 100, anchor = CENTER)
        self.Order_details_Table.column("Product ID", width = 100, anchor = CENTER)
        self.Order_details_Table.column("Price", width = 100, anchor = CENTER)
        self.Order_details_Table.column("Quantity", width = 100, anchor = CENTER)
        self.Order_details_Table.column("Satisfaction Item", width = 100, anchor = CENTER)
        self.Order_details_Table.column("Order Detail", width = 100, anchor = CENTER)
        self.Order_details_Table.column("Order Date", width = 100, anchor = CENTER)
        self.Order_details_Table.column("Delivery Cost", width = 100, anchor = CENTER)
        self.Order_details_Table.column("Total Amount", width = 100, anchor = CENTER)
        self.Order_details_Table.column("Invoice Details", width = 100, anchor = CENTER)
        self.Order_details_Table.column("Invoice Date", width = 100, anchor = CENTER)

        self.Order_details_Table.pack(fill = BOTH, expand = 1)
        self.Order_details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

#=================================================================Commands========================================================  
    def add(self):
        if self.var_customer_id.get() == "" or self.var_product_id.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("INSERT INTO Order_Line_Items (Line_Item_ID, Satisfaction_Item) VALUES (?, ?)", self.var_Order_id.get(), self.var_satisfaction_item.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Order_Items (Order_Item_ID, Product_ID, Item_Cost, Line_Item_ID, Product_Quantity, Order_Details) VALUES (?, ?, ?, ?, ?, ?)",
                                            self.var_Order_id.get(), self.var_product_id.get(), self.var_itemcost.get(), self.var_Order_id.get(), self.var_product_quantity.get(), self.var_order_detail.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Orders (Order_ID, Order_Item_ID, Customer_ID, Order_Date) VALUES (?, ?, ?, ?)",
                                        self.var_Order_id.get(), self.var_Order_id.get(), self.var_customer_id.get(), self.var_order_date.get())  
                        conn.commit()

                        my_cursor.execute("INSERT into Invoices (Invoice_ID, Invoice_Date, Order_ID, Delivery_Cost, Invoice_Details)\
                                            values (?, ?, ?, ?, ?)",
                                            self.var_Order_id.get(), self.var_Invoice_date.get(), self.var_Order_id.get(), self.var_Delivery_cost.get(), self.var_Invoice_detail.get())
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Order has been added", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
                        print(es)
     
    def fetch_data(self):
        try:
                conn = pyodbc.connect(Connect)
                print("Connection to MySQL DB successful")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Orders.Order_ID, Customers.Customer_ID, Products.Product_ID, Order_Items.Item_Cost, Order_Items.Product_Quantity,\
		                        Order_Line_Items.Satisfaction_Item, Order_Items.Order_Details, Orders.Order_Date, Invoices.Delivery_Cost,\
		                        Round((((Order_Items.Item_Cost * Order_Items.Product_Quantity + Invoices.Delivery_Cost) * 0.0825) + (Order_Items.Item_Cost * Order_Items.Product_Quantity + Invoices.Delivery_Cost)),2) as TotalAmount, Invoices.Invoice_Details, Invoices.Invoice_Date\
                                FROM Products\
                                INNER JOIN Order_Items ON Order_Items.Product_ID = Products.Product_ID\
                                INNER JOIN Order_Line_Items ON Order_Items.Line_Item_ID = Order_Line_Items.Line_Item_ID\
                                INNER JOIN Orders ON Orders.Order_Item_ID = Order_Items.Order_Item_ID\
                                INNER JOIN Invoices ON Invoices.Order_ID = Orders.Order_ID\
                                INNER JOIN Customers ON Customers.Customer_ID = Orders.Customer_ID")
                
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                        self.Order_details_Table.delete(*self.Order_details_Table.get_children())
                        for i in rows:
                                self.Order_details_Table.insert("",END,values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]))
                        conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)

    def get_cursor(self, event = ""):
        cursor_row = self.Order_details_Table.focus()
        content = self.Order_details_Table.item(cursor_row)
        row = content["values"]

        self.var_Order_id.set(row[0])
        self.var_customer_id.set(row[1])
        self.var_product_id.set(row[2])
        self.var_itemcost.set(row[3])
        self.var_product_quantity.set(row[4])
        self.var_satisfaction_item.set(row[5])
        self.var_order_detail.set(row[6])
        self.var_order_date.set(row[7])
        self.var_Delivery_cost.set(row[8])
        self.var_Invoice_detail.set(row[10])
        self.var_Invoice_date.set(row[11])

    def update(self):
        if self.var_customer_id.get() == "" or self.var_product_id.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("UPDATE Order_Line_Items SET Satisfaction_Item = ?\
                                        WHERE Line_Item_ID = ?",
                                        self.var_satisfaction_item.get(), self.var_Order_id.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Order_Items SET Product_ID = ?, Item_Cost = ?, Line_Item_ID = ?, Product_Quantity = ?, Order_Details = ?\
                                        WHERE Order_Item_ID = ?",
                                        self.var_product_id.get(), self.var_itemcost.get(), self.var_Order_id.get(),
                                        self.var_product_quantity.get(), self.var_order_detail.get(), self.var_Order_id.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Orders SET Order_Item_ID = ?, Customer_ID = ?, Order_Date = ?\
                                        WHERE Order_ID = ?",
                                        self.var_Order_id.get(), self.var_customer_id.get(), self.var_order_date.get(), self.var_Order_id.get())  
                        conn.commit()

                        my_cursor.execute("UPDATE Invoices SET Invoice_Date = ?, Order_ID = ?, Delivery_Cost = ?, Invoice_Details = ?\
                                        WHERE Invoice_ID = ?",
                                        self.var_Invoice_date.get(), self.var_Order_id.get(), self.var_Delivery_cost.get(),
                                        self.var_Invoice_detail.get(), self.var_Order_id.get())
                        conn.commit()

                        self.fetch_data()
                        conn.close()

                        messagebox.showinfo("Update", "Order details have been updated successfully", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)  

    def Delete(self):
        Delete = messagebox.askyesno("Furniture Management Apllication", "Do you want to delete this order?", parent = self.root)
        if Delete > 0:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("DELETE FROM Invoices WHERE Invoice_ID = ?", self.var_Order_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Orders WHERE Order_ID = ?", self.var_Order_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Order_Items WHERE Order_Item_ID = ?", self.var_Order_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Order_Line_Items WHERE Line_Item_ID = ?", self.var_Order_id.get())
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
        self.var_Order_id.set(str(x))
        self.var_customer_id.set(""),
        self.var_product_id.set(""),
        self.var_product_quantity.set(""),
        self.var_itemcost.set(""),
        self.var_satisfaction_item.set(""),
        self.var_order_detail.set(""),
        self.var_order_date.set(""),
        self.var_Discount.set(""),
        self.var_Delivery_cost.set(""),
        self.var_Invoice_date.set(""),
        self.var_Invoice_detail.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Order_Win(root)
    root.mainloop()
