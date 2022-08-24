from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk
import random
import pyodbc
from tkinter import messagebox
from connection import Connect
class Payment_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Payment")
        self.root.geometry("1295x730+230+220")
        self.root.resizable(False, False)
#=================================================================Variables========================================================
        x = random.randint(1000,9999)

        self.var_Account_ID = StringVar()
        self.var_Account_ID.set(str(x))

        self.var_invoice_ID = StringVar()

        self.var_Account_Name = StringVar()
        self.var_Date_Account_Opened = StringVar()
        self.var_Status = StringVar()
        self.var_Payment_Date = StringVar()
        self.var_Payment_Amount = StringVar()
        self.var_Payment_Method = StringVar()
        self.var_Details = StringVar()

#=================================================================title========================================================
        lbl_title = Label(self.root, text = "ADD ACCOUNT AND TRANSACTION DETAILS", font = ("times new roman", 18, "bold"), bg = "black", fg = "gold")
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

#=================================================================Logo========================================================
        img2 = Image.open(r"Images\icon.jpg")
        img2 = img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image = self.photoimg2, bd = 0, relief = RIDGE)
        lblimg.place(x = 5, y = 2, width = 100, height = 50)

#=================================================================labelFrame========================================================
        labelframeleft = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Account and Transaction Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        labelframeleft.place(x = 5, y = 50, width = 425, height = 677)

#=================================================================label and entries========================================================
# Account ID        
        lblAccountID = Label(labelframeleft, text = "Account ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblAccountID.grid(row = 0, column = 0, sticky = W)

        txtAccountID = ttk.Entry(labelframeleft, textvariable = self.var_Account_ID, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtAccountID.grid(row = 0, column = 1)

# Account Name
        lblAccountName = Label(labelframeleft, text = "Account Name:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblAccountName.grid(row = 1, column = 0, sticky = W)

        txtAccountName = ttk.Entry(labelframeleft, textvariable = self.var_Account_Name, width = 25, font = ("times new roman", 13, "bold"))
        txtAccountName.grid(row = 1, column = 1)

# Account Opened Date
        lblDateOpened = Label(labelframeleft, text = "Date Opened:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDateOpened.grid(row = 2, column = 0, sticky = W)

        txtDateOpened = ttk.Entry(labelframeleft, textvariable = self.var_Date_Account_Opened, width = 25, font = ("times new roman", 13, "bold"))
        txtDateOpened.grid(row = 2, column = 1)

# Account_Status
        lblAccountStatus = Label(labelframeleft, text = "Account Status:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblAccountStatus.grid(row = 3, column = 0, sticky = W)

        combo_AccountStatus = ttk.Combobox(labelframeleft, textvariable = self.var_Status, font = ("times new roman", 12, "bold"), width = 26)
        combo_AccountStatus["value"] = ("Active", "Inactive")
        combo_AccountStatus.current(0)
        combo_AccountStatus.grid(row = 3, column = 1)

# Invoice ID
        lblInvoiceID = Label(labelframeleft, text = "Invoice ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblInvoiceID.grid(row = 4, column = 0, sticky = W)

        txtInvoiceID = ttk.Entry(labelframeleft, textvariable = self.var_invoice_ID, width = 25, font = ("times new roman", 13, "bold"))
        txtInvoiceID.grid(row = 4, column = 1)

# Payment Date
        lblPaymentDate = Label(labelframeleft, text = "Payment Date:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblPaymentDate.grid(row = 5, column = 0, sticky = W)

        txtPaymentDate = ttk.Entry(labelframeleft, textvariable = self.var_Payment_Date, width = 25, font = ("times new roman", 13, "bold"))
        txtPaymentDate.grid(row = 5, column = 1)
# Amount
        lblAmount = Label(labelframeleft, text = "Amount:", font = ("times new roman", 13, "bold"), padx = 2, pady = 6)
        lblAmount.grid(row = 6, column = 0, sticky = W)

        txtAmount = ttk.Entry(labelframeleft, textvariable = self.var_Payment_Amount, width = 25, font = ("times new roman", 13, "bold"))
        txtAmount.grid(row = 6, column = 1)

# Payment Method
        lblPaymentMethod = Label(labelframeleft, text = "Payment Method:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblPaymentMethod.grid(row = 7, column = 0, sticky = W)

        combo_PaymentMethod = ttk.Combobox(labelframeleft, textvariable = self.var_Payment_Method, font = ("times new roman", 12, "bold"), width = 26)
        combo_PaymentMethod["value"] = ("Credit/Debit", "Cash", "Check", "Financing")
        combo_PaymentMethod.current(0)
        combo_PaymentMethod.grid(row = 7, column = 1)

# Details
        lblDetails = Label(labelframeleft, text = "Details:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDetails.grid(row = 8, column = 0, sticky = W)

        txtDetails = ttk.Entry(labelframeleft, textvariable = self.var_Details, width = 25, font = ("times new roman", 13, "bold"))
        txtDetails.grid(row = 8, column = 1)

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

        self.Payment_details_Table = ttk.Treeview(details_table, column = ("Transaction ID", "Account Name", "Date Opened", "Status",
                                                                        "Invoice ID", "Payment Date", "Amount", "Methods", "Details"),
                                                                        xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Payment_details_Table.xview)
        scroll_y.config(command = self.Payment_details_Table.yview)

        self.Payment_details_Table.heading("Transaction ID", text = "Transaction ID")
        self.Payment_details_Table.heading("Account Name", text = "Account Name")
        self.Payment_details_Table.heading("Date Opened", text = "Date Opened")
        self.Payment_details_Table.heading("Status", text = "Status")
        self.Payment_details_Table.heading("Invoice ID", text = "Invoice ID")
        self.Payment_details_Table.heading("Payment Date", text = "Payment Date")
        self.Payment_details_Table.heading("Amount", text = "Amount")
        self.Payment_details_Table.heading("Methods", text = "Methods")
        self.Payment_details_Table.heading("Details", text = "Details")

        self.Payment_details_Table["show"] = "headings"

        self.Payment_details_Table.column("Transaction ID", width = 100, anchor = CENTER)
        self.Payment_details_Table.column("Account Name", width = 100, anchor = CENTER)
        self.Payment_details_Table.column("Date Opened", width = 100, anchor = CENTER)
        self.Payment_details_Table.column("Status", width = 100, anchor = CENTER)
        self.Payment_details_Table.column("Invoice ID", width = 100, anchor = CENTER)
        self.Payment_details_Table.column("Payment Date", width = 100, anchor = CENTER)
        self.Payment_details_Table.column("Amount", width = 100, anchor = CENTER)
        self.Payment_details_Table.column("Methods", width = 100, anchor = CENTER)
        self.Payment_details_Table.column("Details", width = 100, anchor = CENTER)

        self.Payment_details_Table.pack(fill = BOTH, expand = 1)
        self.Payment_details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

#=================================================================Commands========================================================  
    def add(self):
        if self.var_Account_Name.get() == "" or self.var_invoice_ID.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("INSERT INTO Account_Status (Account_Status_ID, Status) VALUES (?, ?)", self.var_Account_ID.get(), self.var_Status.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Accounts (Account_ID, Date_Account_Opened, Account_Name, Account_Status_ID) VALUES (?, ?, ?, ?)",
                                            self.var_Account_ID.get(), self.var_Date_Account_Opened.get(),
                                            self.var_Account_Name.get(), self.var_Account_ID.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Payments (Payment_ID, Payment_Date, Payment_Amount, Payment_Method) VALUES (?, ?, ?, ?)",
                                        self.var_Account_ID.get(), self.var_Payment_Date.get(), self.var_Payment_Amount.get(), self.var_Payment_Method.get())  
                        conn.commit()

                        my_cursor.execute("INSERT into Transactions (Transaction_ID, Account_ID, Invoice_ID, Payment_ID, Transaction_Date, Details)\
                                            values (?, ?, ?, ?, ?, ?)",
                                            self.var_Account_ID.get(), self.var_Account_ID.get(), self.var_invoice_ID.get(),
                                            self.var_Account_ID.get(), self.var_Payment_Date.get(), self.var_Details.get())
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Payment has been added", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
                        print(es)
     
    def fetch_data(self):
        try:
                conn = pyodbc.connect(Connect)
                print("Connection to MySQL DB successful")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Accounts.Account_ID, Accounts.Account_Name, Accounts.Date_Account_Opened,\
		                                Account_Status.Status,\
		                                Transactions.Invoice_ID,\
		                                Payments.Payment_Date, Payments.Payment_Amount, Payments.Payment_Method, Transactions.Details FROM Transactions\
                                    INNER JOIN Accounts ON Accounts.Account_ID = Transactions.Account_ID\
                                    INNER JOIN Account_Status ON Accounts.Account_Status_ID = Account_Status.Account_Status_ID\
                                    INNER JOIN Payments ON Transactions.Payment_ID = Payments.Payment_ID")
                
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.Payment_details_Table.delete(*self.Payment_details_Table.get_children())
                    for i in rows:
                        self.Payment_details_Table.insert("",END,values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
                        conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)

    def get_cursor(self, event = ""):
        cursor_row = self.Payment_details_Table.focus()
        content = self.Payment_details_Table.item(cursor_row)
        row = content["values"]

        self.var_Account_ID.set(row[0])
        self.var_Account_Name.set(row[1])
        self.var_Date_Account_Opened.set(row[2])
        self.var_Status.set(row[3])
        self.var_invoice_ID.set(row[4])
        self.var_Payment_Date.set(row[5])
        self.var_Payment_Amount.set(row[6])
        self.var_Payment_Method.set(row[7])
        self.var_Details.set(row[8])

    def update(self):
        if self.var_Account_Name.get() == "" or self.var_invoice_ID.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("UPDATE Account_Status SET Status = ?\
                                        WHERE Account_Status_ID = ?",
                                        self.var_Status.get(), self.var_Account_ID.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Accounts SET Date_Account_Opened = ?, Account_Name = ?\
                                        WHERE Account_ID = ?",
                                        self.var_Date_Account_Opened.get(), self.var_Account_Name.get(), self.var_Account_ID.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Payments SET Payment_Date = ?, Payment_Amount = ?, Payment_Method = ?\
                                        WHERE Payment_ID = ?",
                                        self.var_Payment_Date.get(), self.var_Payment_Amount.get(), self.var_Payment_Method.get(), self.var_Account_ID.get())  
                        conn.commit()

                        my_cursor.execute("UPDATE Transactions SET Invoice_ID = ?, Transaction_Date = ?\
                                        WHERE Transaction_ID = ?",
                                        self.var_invoice_ID.get(), self.var_Payment_Date.get(), self.var_Account_ID.get())
                                      
                        conn.commit()

                        self.fetch_data()
                        conn.close()

                        messagebox.showinfo("Update", "Payment details have been updated successfully", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)  

    def Delete(self):
        Delete = messagebox.askyesno("Furniture Management Apllication", "Do you want to delete this payment?", parent = self.root)
        if Delete > 0:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("DELETE FROM Transactions WHERE Transaction_ID = ?", self.var_Account_ID.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Payments WHERE Payment_ID = ?", self.var_Account_ID.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Accounts WHERE Account_ID = ?", self.var_Account_ID.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Account_Status WHERE Account_Status_ID = ?", self.var_Account_ID.get())
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
        self.var_Account_ID.set(str(x))
        self.var_Account_Name.set(""),
        self.var_Date_Account_Opened.set(""),
        self.var_Status.set(""),
        self.var_invoice_ID.set(""),
        self.var_Payment_Date.set(""),
        self.var_Payment_Amount.set(""),
        self.var_Payment_Method.set(""),
        self.var_Details.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Payment_Win(root)
    root.mainloop()
