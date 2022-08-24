from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk
import random
import pyodbc
from tkinter import messagebox
from connection import Connect
class Loan_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Loan")
        self.root.geometry("1295x730+230+220")
        self.root.resizable(False, False)
#=================================================================Variables========================================================
        x = random.randint(1000,9999)

        self.var_loan_id = StringVar()
        self.var_loan_id.set(str(x))

        self.var_transaction_id = StringVar()


        self.var_lender_name = StringVar()

        self.var_loan_date_opened = StringVar()


        self.var_principal = StringVar()
        self.var_interest_rate = StringVar()
        self.var_duration = StringVar()
        self.var_phone_number = StringVar()
        self.var_email_address = StringVar()
        self.var_fax_number = StringVar()
        self.var_physical_address = StringVar()
        self.var_mailing_address = StringVar()
        self.var_loan_status = StringVar()

#=================================================================title========================================================
        lbl_title = Label(self.root, text = "ADD LOAN DETAILS", font = ("times new roman", 18, "bold"), bg = "black", fg = "gold")
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

#=================================================================Logo========================================================
        img2 = Image.open(r"Images\icon.jpg")
        img2 = img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image = self.photoimg2, bd = 0, relief = RIDGE)
        lblimg.place(x = 5, y = 2, width = 100, height = 50)

#=================================================================labelFrame========================================================
        labelframeleft = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Loan Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        labelframeleft.place(x = 5, y = 50, width = 425, height = 677)

#=================================================================label and entries========================================================
# Loan ID        
        lblLoanID = Label(labelframeleft, text = "Loan ID", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblLoanID.grid(row = 0, column = 0, sticky = W)

        txtLoanID = ttk.Entry(labelframeleft, textvariable = self.var_loan_id, width = 23, font = ("times new roman", 13, "bold"), state = "readonly")
        txtLoanID.grid(row = 0, column = 1)

# Transaction ID
        lblTransactionID = Label(labelframeleft, text = "Transaction ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblTransactionID.grid(row = 1, column = 0, sticky = W)

        txtTransactionID = ttk.Entry(labelframeleft, textvariable = self.var_transaction_id, width = 23, font = ("times new roman", 13, "bold"))
        txtTransactionID.grid(row = 1, column = 1)

# Lender Name
        lblLenderName = Label(labelframeleft, text = "Lender Name:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblLenderName.grid(row = 2, column = 0, sticky = W)

        txtLenderName = ttk.Entry(labelframeleft, textvariable = self.var_lender_name, width = 23, font = ("times new roman", 13, "bold"))
        txtLenderName.grid(row = 2, column = 1)

# Loan Date Opened
        lblLoanDateOpened = Label(labelframeleft, text = "Loan Opened (mm/dd/yyyy):", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblLoanDateOpened.grid(row = 3, column = 0, sticky = W)

        txtLoanDateOpened = ttk.Entry(labelframeleft, textvariable = self.var_loan_date_opened, width = 23, font = ("times new roman", 13, "bold"))
        txtLoanDateOpened.grid(row = 3, column = 1)

# Principal
        lblPrincipal = Label(labelframeleft, text = "Principal:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblPrincipal.grid(row = 4, column = 0, sticky = W)

        txtPrincipal = ttk.Entry(labelframeleft, textvariable = self.var_principal, width = 23, font = ("times new roman", 13, "bold"))
        txtPrincipal.grid(row = 4, column = 1)

# Interest Rate
        lblInterestRate = Label(labelframeleft, text = "Interest Rate (%):", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblInterestRate.grid(row = 5, column = 0, sticky = W)

        combo_InterestRate = ttk.Combobox(labelframeleft, textvariable = self.var_interest_rate, font = ("times new roman", 12, "bold"), width = 24, state = "readonly")
        combo_InterestRate["value"] = ("0")
        combo_InterestRate.current(0)
        combo_InterestRate.grid(row = 5, column = 1)

# Duration
        lblDuration = Label(labelframeleft, text = "Duration:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDuration.grid(row = 6, column = 0, sticky = W)

        combo_Duration = ttk.Combobox(labelframeleft, textvariable = self.var_duration, font = ("times new roman", 12, "bold"), width = 24, state = "readonly")
        combo_Duration["value"] = ("12")
        combo_Duration.current(0)
        combo_Duration.grid(row = 6, column = 1)

# Lender Phone
        lblLenderPhone = Label(labelframeleft, text = "Lender Phone:", font = ("times new roman", 13, "bold"), padx = 2, pady = 6)
        lblLenderPhone.grid(row = 7, column = 0, sticky = W)

        txtLenderPhone = ttk.Entry(labelframeleft, textvariable = self.var_phone_number, width = 23, font = ("times new roman", 13, "bold"))
        txtLenderPhone.grid(row = 7, column = 1)

# Lender EmailAddress
        lblLenderEmailAddress = Label(labelframeleft, text = "Email Address:", font = ("times new roman", 13, "bold"), padx = 2, pady = 6)
        lblLenderEmailAddress.grid(row = 8, column = 0, sticky = W)

        txtLenderEmailAddress = ttk.Entry(labelframeleft, textvariable = self.var_email_address, width = 23, font = ("times new roman", 13, "bold"))
        txtLenderEmailAddress.grid(row = 8, column = 1)

# Fax
        lblFax = Label(labelframeleft, text = "Fax:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblFax.grid(row = 9, column = 0, sticky = W)

        txtFax = ttk.Entry(labelframeleft, textvariable = self.var_fax_number, width = 23, font = ("times new roman", 13, "bold"))
        txtFax.grid(row = 9, column = 1)

# Physical Address
        lblPhysicalAddress = Label(labelframeleft, text = "Physical Address:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblPhysicalAddress.grid(row = 10, column = 0, sticky = W)

        txtPhysicalAddress = ttk.Entry(labelframeleft, textvariable = self.var_physical_address, width = 23, font = ("times new roman", 13, "bold"))
        txtPhysicalAddress.grid(row = 10, column = 1)

# Mailing Address
        lblMailingAddress = Label(labelframeleft, text = "Mailing Address:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblMailingAddress.grid(row = 11, column = 0, sticky = W)

        txtMailingAddress = ttk.Entry(labelframeleft, textvariable = self.var_mailing_address, width = 23, font = ("times new roman", 13, "bold"))
        txtMailingAddress.grid(row = 11, column = 1)

# Loan Status
        lblLoanStatus = Label(labelframeleft, text = "Loan Status:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblLoanStatus.grid(row = 12, column = 0, sticky = W)

        combo_LoanStatus = ttk.Combobox(labelframeleft, textvariable = self.var_loan_status, font = ("times new roman", 12, "bold"), width = 24)
        combo_LoanStatus["value"] = ("Active", "Inactive")
        combo_LoanStatus.current(0)
        combo_LoanStatus.grid(row = 12, column = 1)

#=================================================================btns========================================================
        btn_frame = Frame(labelframeleft, bd = 2, relief = RIDGE)
        btn_frame.place(x = 0, y = 615, width = 412, height = 35)

        btnAdd = Button(btn_frame, text = "Add", command = self.add, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
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

        self.Lender_details_Table = ttk.Treeview(details_table, column = ("Loan ID", "Transaction ID", "Lender Name", "Loan Opened", "Principal",
                                                                        "Interest Rate", "Duration", "Monthly", "Lender Phone", "Fax", "Email Address",
                                                                        "Physical Address", "Mailing Address", "Loan Status"),
                                                                        xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Lender_details_Table.xview)
        scroll_y.config(command = self.Lender_details_Table.yview)

        self.Lender_details_Table.heading("Loan ID", text = "Loan ID")
        self.Lender_details_Table.heading("Transaction ID", text = "Transaction ID")
        self.Lender_details_Table.heading("Lender Name", text = "Lender Name")
        self.Lender_details_Table.heading("Loan Opened", text = "Loan Opened")
        self.Lender_details_Table.heading("Principal", text = "Principal")
        self.Lender_details_Table.heading("Interest Rate", text = "Interest Rate")
        self.Lender_details_Table.heading("Duration", text = "Duration")
        self.Lender_details_Table.heading("Monthly", text = "Monthly")
        self.Lender_details_Table.heading("Lender Phone", text = "Lender Phone")
        self.Lender_details_Table.heading("Fax", text = "Fax")
        self.Lender_details_Table.heading("Email Address", text = "Email Address")
        self.Lender_details_Table.heading("Physical Address", text = "Physical Address")
        self.Lender_details_Table.heading("Mailing Address", text = "Mailing Address")
        self.Lender_details_Table.heading("Loan Status", text = "Loan Status")

        self.Lender_details_Table["show"] = "headings"

        self.Lender_details_Table.column("Loan ID", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Transaction ID", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Lender Name", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Loan Opened", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Principal", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Interest Rate", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Duration", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Monthly", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Lender Phone", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Fax", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Email Address", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Physical Address", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Mailing Address", width = 100, anchor = CENTER)
        self.Lender_details_Table.column("Loan Status", width = 100, anchor = CENTER)

        self.Lender_details_Table.pack(fill = BOTH, expand = 1)
        self.Lender_details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

#=================================================================Commands========================================================  
    def add(self):
        if self.var_transaction_id.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("INSERT INTO Lender_Addresses (Address_ID, Physical_Address, Mailing_Address) VALUES (?, ?, ?)",
                                        self.var_loan_id.get(), self.var_physical_address.get(), self.var_mailing_address.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Lender_Contact (Lender_Contact_ID, Phone_Number, Email_Address, Fax_Number, Address_ID) VALUES (?, ?, ?, ?, ?)",
                                            self.var_loan_id.get(), self.var_phone_number.get(), self.var_email_address.get(),
                                            self.var_fax_number.get(), self.var_loan_id.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Loan_Status (Loan_Status_ID, Status) VALUES (?, ?)", self.var_loan_id.get(), self.var_loan_status.get())  
                        conn.commit()

                        my_cursor.execute("INSERT INTO Contracts (Contract_ID, Principal, Interest_Rate, Duration) VALUES (?, ?, ?, ?)",
                                            self.var_loan_id.get(), self.var_principal.get(), self.var_interest_rate.get(), self.var_duration.get())  
                        conn.commit()

                        my_cursor.execute("INSERT into Loan (Loan_ID, Transaction_ID, Lender_Name, Loan_Date_Open, Lender_Contact_ID, Contract_ID, Loan_Status_ID)\
                                            values (?, ?, ?, ?, ?, ?, ?)",
                                            self.var_loan_id.get(), self.var_transaction_id.get(), self.var_lender_name.get(), self.var_loan_date_opened.get(),
                                            self.var_loan_id.get(), self.var_loan_id.get(), self.var_loan_id.get())
                        conn.commit()
                        conn.close()
                        self.fetch_data()
                        self.Reset()
                        messagebox.showinfo("Success", "Loan has been added", parent = self.root)
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
     
    def fetch_data(self):
        try:
                conn = pyodbc.connect(Connect)
                print("Connection to MySQL DB successful")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Loan.Loan_ID, Loan.Transaction_ID, Loan.Lender_Name, Loan.Loan_Date_Open,\
		                                Contracts.Principal, Contracts.Interest_Rate, Contracts.Duration, Contracts.Monthly_Amount,\
		                                Lender_Contact.Phone_Number, Lender_Contact.Fax_Number, Lender_Contact.Email_Address,\
		                                Lender_Addresses.Physical_Address, Lender_Addresses.Mailing_Address,\
		                                Loan_Status.Status\
                                    FROM Lender_Contact\
                                    INNER JOIN Lender_Addresses ON Lender_Addresses.Address_ID = Lender_Contact.Address_ID\
                                    INNER JOIN Loan ON Lender_Contact.Lender_Contact_ID = Loan.Lender_Contact_ID\
                                    INNER JOIN Loan_Status ON Loan_Status.Loan_Status_ID = Loan.Loan_Status_ID\
                                    INNER JOIN Contracts ON Contracts.Contract_ID = Loan.Contract_ID")
                
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                        self.Lender_details_Table.delete(*self.Lender_details_Table.get_children())
                        for i in rows:
                                self.Lender_details_Table.insert("",END,values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]))
                        conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)

    def get_cursor(self, event = ""):
        cursor_row = self.Lender_details_Table.focus()
        content = self.Lender_details_Table.item(cursor_row)
        row = content["values"]

        self.var_loan_id.set(row[0])
        self.var_transaction_id.set(row[1])
        self.var_lender_name.set(row[2])
        self.var_loan_date_opened.set(row[3])
        self.var_principal.set(row[4])
        self.var_interest_rate.set(row[5])
        self.var_duration.set(row[6])
        self.var_phone_number.set(row[8])
        self.var_email_address.set(row[9])
        self.var_fax_number.set(row[10])
        self.var_physical_address.set(row[11])
        self.var_mailing_address.set(row[12])
        self.var_loan_status.set(row[13])

    def update(self):
        if self.var_transaction_id.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("UPDATE Loan_Status SET Status = ?\
                                        WHERE Loan_Status_ID = ?",
                                        self.var_loan_status.get(), self.var_loan_id.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Contracts SET Principal = ?, Interest_Rate = ?, Duration = ?\
                                        WHERE Contract_ID = ?",
                                        self.var_principal.get(), self.var_interest_rate.get(), self.var_duration.get(),
                                        self.var_loan_id.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Lender_Addresses SET Physical_Address = ?, Mailing_Address = ?\
                                        WHERE Address_ID = ?",
                                        self.var_physical_address.get(), self.var_mailing_address.get(), self.var_loan_id.get())  
                        conn.commit()

                        my_cursor.execute("UPDATE Lender_Contact SET Phone_Number = ?, Email_Address = ?, Fax_Number = ?\
                                        WHERE Lender_Contact_ID = ?",
                                        self.var_phone_number.get(), self.var_email_address.get(), self.var_fax_number.get(),
                                        self.var_loan_id.get())  
                        conn.commit()

                        my_cursor.execute("UPDATE Loan SET Transaction_ID = ?, Lender_Name = ?, Loan_Date_Open = ?\
                                        WHERE Loan_ID = ?",
                                        self.var_transaction_id.get(), self.var_lender_name.get(), self.var_loan_date_opened.get(),
                                        self.var_loan_id.get())
                        conn.commit()

                        conn.close()
                        self.fetch_data()
                        self.Reset()

                        messagebox.showinfo("Update", "Loan details have been updated successfully", parent = self.root)
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)  

    def Delete(self):
        Delete = messagebox.askyesno("Furniture Management Apllication", "Do you want to delete this loan?", parent = self.root)
        if Delete > 0:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("DELETE FROM Loan WHERE Loan_ID = ?", self.var_loan_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Loan_Status WHERE Loan_Status_ID = ?", self.var_loan_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Contracts WHERE Contract_ID = ?", self.var_loan_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Lender_Contact WHERE Lender_Contact_ID = ?", self.var_loan_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Lender_Addresses WHERE Address_ID = ?", self.var_loan_id.get())
                        conn.commit()

                        conn.close()
                        self.fetch_data()
                        self.Reset()

                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
        else:
                if not Delete:
                        return

    def Reset(self):
        x = random.randint(1000,9999)
        self.var_loan_id.set(str(x))
        self.var_transaction_id.set(""),
        self.var_lender_name.set(""),
        self.var_loan_date_opened.set(""),
        self.var_principal.set(""),
        self.var_interest_rate.set(""),
        self.var_duration.set(""),
        self.var_phone_number.set(""),
        self.var_email_address.set(""),
        self.var_fax_number.set(""),
        self.var_physical_address.set(""),
        self.var_mailing_address.set(""),
        self.var_loan_status.set("")
           
if __name__ == "__main__":
    root = Tk()
    obj = Loan_Win(root)
    root.mainloop()
