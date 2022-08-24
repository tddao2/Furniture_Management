from tkinter import *
from PIL import Image, ImageTk  #pip install pillow
from tkinter import ttk
import random
import pyodbc
from tkinter import messagebox
from connection import Connect
class Employee_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee")
        self.root.geometry("1295x850+230+220")
        self.root.resizable(False, False)
#=================================================================Variables========================================================
        x = random.randint(1000,9999)

        self.var_employee_id = StringVar()
        self.var_employee_id.set(str(x))

        self.var_employee_address_id = StringVar()
        self.var_employee_address_id.set(str(x))

        self.var_store_id = StringVar()
        self.var_store_id.set(str(x))

        self.var_job_title_id = StringVar()
        self.var_job_title_id.set(str(x))

        self.var_employee_status_id = StringVar()
        self.var_employee_status_id.set(str(x))

        self.var_first_name = StringVar()
        self.var_last_name = StringVar()
        self.var_date_of_birth = StringVar()
        self.var_email_address = StringVar()
        self.var_phone_number = StringVar()
        self.var_job_title = StringVar()
        self.var_job_title_description = StringVar()
        self.var_current_status = StringVar()
        self.var_street = StringVar()
        self.var_city = StringVar()
        self.var_state = StringVar()
        self.var_zip_code = StringVar()
        self.var_country = StringVar()
        self.var_details = StringVar()
        self.var_location = StringVar()
#=================================================================title========================================================
        lbl_title = Label(self.root, text = "ADD EMPLOYEE DETAILS", font = ("times new roman", 18, "bold"), bg = "black", fg = "gold")
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

#=================================================================Logo========================================================
        img2 = Image.open(r"Images\icon.jpg")
        img2 = img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image = self.photoimg2, bd = 0, relief = RIDGE)
        lblimg.place(x = 5, y = 2, width = 100, height = 50)

#=================================================================labelFrame========================================================
        labelframeleft = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Employee Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        labelframeleft.place(x = 5, y = 50, width = 425, height = 793)

#=================================================================label and entries========================================================
# Employee ID        
        lblEmployeeID = Label(labelframeleft, text = "Employee ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblEmployeeID.grid(row = 0, column = 0, sticky = W)

        txtEmployeeID = ttk.Entry(labelframeleft, textvariable = self.var_employee_id, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtEmployeeID.grid(row = 0, column = 1)

# FirstName
        lblFirstName = Label(labelframeleft, text = "First Name:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblFirstName.grid(row = 1, column = 0, sticky = W)

        txtFirstName = ttk.Entry(labelframeleft, textvariable = self.var_first_name, width = 25, font = ("times new roman", 13, "bold"))
        txtFirstName.grid(row = 1, column = 1)

# LastName
        lblLastname = Label(labelframeleft, text = "Last Name:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblLastname.grid(row = 2, column = 0, sticky = W)

        txtLastname = ttk.Entry(labelframeleft, textvariable = self.var_last_name, width = 25, font = ("times new roman", 13, "bold"))
        txtLastname.grid(row = 2, column = 1)

# Date of Birth
        lblDateofBirth = Label(labelframeleft, text = "Date of Birth:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblDateofBirth.grid(row = 3, column = 0, sticky = W)

        txtDateofBirth = ttk.Entry(labelframeleft, textvariable = self.var_date_of_birth, width = 25, font = ("times new roman", 13, "bold"))
        txtDateofBirth.grid(row = 3, column = 1)

# Email Address
        lblEmailAddress = Label(labelframeleft, text = "Email Address:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblEmailAddress.grid(row = 4, column = 0, sticky = W)

        txtEmailAddress = ttk.Entry(labelframeleft, textvariable = self.var_email_address, width = 25, font = ("times new roman", 13, "bold"))
        txtEmailAddress.grid(row = 4, column = 1)

# Phone Number
        lblPhoneNumber = Label(labelframeleft, text = "Phone Number:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblPhoneNumber.grid(row = 5, column = 0, sticky = W)

        txtPhoneNumber = ttk.Entry(labelframeleft, textvariable = self.var_phone_number, width = 25, font = ("times new roman", 13, "bold"))
        txtPhoneNumber.grid(row = 5, column = 1)

# Employee Address ID
        lblEmployeeAddressID = Label(labelframeleft, text = "Employee Address ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblEmployeeAddressID.grid(row = 6, column = 0, sticky = W)

        txtEmployeeAddressID = ttk.Entry(labelframeleft, textvariable = self.var_employee_address_id, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtEmployeeAddressID.grid(row = 6, column = 1)

# Street
        lblStreet = Label(labelframeleft, text = "Street:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblStreet.grid(row = 7, column = 0, sticky = W)

        txtStreet = ttk.Entry(labelframeleft, textvariable = self.var_street, width = 25, font = ("times new roman", 13, "bold"))
        txtStreet.grid(row = 7, column = 1)

# City
        lblCity = Label(labelframeleft, text = "City:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblCity.grid(row = 8, column = 0, sticky = W)

        txtCity = ttk.Entry(labelframeleft, textvariable = self.var_city, width = 25, font = ("times new roman", 13, "bold"))
        txtCity.grid(row = 8, column = 1)

# State
        lblState = Label(labelframeleft, text = "State:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblState.grid(row = 9, column = 0, sticky = W)

        txtState = ttk.Entry(labelframeleft, textvariable = self.var_state, width = 25, font = ("times new roman", 13, "bold"))
        txtState.grid(row = 9, column = 1)

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

# Details
        lblDetails = Label(labelframeleft, text = "Details:", font = ("times new roman", 13, "bold"), padx = 2, pady = 6)
        lblDetails.grid(row = 12, column = 0, sticky = W)

        txtDetails = ttk.Entry(labelframeleft, textvariable = self.var_details, width = 25, font = ("times new roman", 13, "bold"))
        txtDetails.grid(row = 12, column = 1)
# Store ID
        lblStoreID = Label(labelframeleft, text = "Store ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblStoreID.grid(row = 13, column = 0, sticky = W)

        txtStoreID = ttk.Entry(labelframeleft, textvariable = self.var_store_id, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtStoreID.grid(row = 13, column = 1)

# Location
        lblLocation = Label(labelframeleft, text = "Location:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblLocation.grid(row = 14, column = 0, sticky = W)

        combo_Location = ttk.Combobox(labelframeleft, textvariable = self.var_location, font = ("times new roman", 12, "bold"), width = 26, state = "readonly")
        combo_Location["value"] = ("SouthWest", "NorthWest", "NorthEast", "SouthEast")
        combo_Location.current(0)
        combo_Location.grid(row = 14, column = 1)

# Job title ID
        lblJobtitleID = Label(labelframeleft, text = "Job title ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblJobtitleID.grid(row = 15, column = 0, sticky = W)

        txtJobtitleID = ttk.Entry(labelframeleft, textvariable = self.var_job_title_id, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtJobtitleID.grid(row = 15, column = 1)

# Job title
        lblJobtitle = Label(labelframeleft, text = "Job title:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblJobtitle.grid(row = 16, column = 0, sticky = W)

        combo_Jobtitle = ttk.Combobox(labelframeleft, textvariable = self.var_job_title, font = ("times new roman", 12, "bold"), width = 26, state = "readonly")
        combo_Jobtitle["value"] = ("Salesperson", "Manager", "Deliver", "Cashier", "Custodian")
        combo_Jobtitle.current(0)
        combo_Jobtitle.grid(row = 16, column = 1)

# Job Description
        lblJobDescription = Label(labelframeleft, text = "Job Description:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblJobDescription.grid(row = 17, column = 0, sticky = W)

        txtJobDescription = ttk.Entry(labelframeleft, textvariable = self.var_job_title_description, width = 25, font = ("times new roman", 13, "bold"))
        txtJobDescription.grid(row = 17, column = 1)

# Employee Status ID
        lblEmployeeStatusID = Label(labelframeleft, text = "Employee Status ID:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblEmployeeStatusID.grid(row = 18, column = 0, sticky = W)

        txtEmployeeStatusID = ttk.Entry(labelframeleft, textvariable = self.var_employee_status_id, width = 25, font = ("times new roman", 13, "bold"), state = "readonly")
        txtEmployeeStatusID.grid(row = 18, column = 1)

# Current Status
        lblStatus = Label(labelframeleft, text = "Status:", font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        lblStatus.grid(row = 19, column = 0, sticky = W)

        combo_Status = ttk.Combobox(labelframeleft, textvariable = self.var_current_status, font = ("times new roman", 12, "bold"), width = 26, state = "readonly")
        combo_Status["value"] = ("Active", "Inactive")
        combo_Status.current(0)
        combo_Status.grid(row = 19, column = 1)

#=================================================================btns========================================================
        btn_frame = Frame(labelframeleft, bd = 2, relief = RIDGE)
        btn_frame.place(x = 0, y = 730, width = 412, height = 35)

        btnAdd = Button(btn_frame, text = "Add", command = self.add_employee, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnAdd.grid(row = 0, column = 0, padx = 1)

        btnUpadate = Button(btn_frame, text = "Update", command = self.update, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnUpadate.grid(row = 0, column = 1, padx = 1)

        btnDelete = Button(btn_frame, text = "Delete", command = self.Delete, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnDelete.grid(row = 0, column = 2, padx = 1)

        btnReset = Button(btn_frame, text = "Reset", command = self.Reset, font = ("times new roman", 11, "bold"), bg = "black", fg = "gold", width = 10)
        btnReset.grid(row = 0, column = 3, padx = 1)

#=================================================================table Frame View========================================================
        Table_Frame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details", font = ("times new roman", 12, "bold"), padx = 2, fg = "blue")
        Table_Frame.place(x = 435, y = 50, width = 860, height = 793)

#=================================================================Show data table========================================================        
        details_table = Frame(Table_Frame, bd = 2, relief = RIDGE)
        details_table.place(x = 0, y = 0, width = 860, height = 770)

        scroll_x = ttk.Scrollbar(details_table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient = VERTICAL)

        self.Employee_details_Table = ttk.Treeview(details_table, column = ("ID", "First Name", "Last Name", "DOB", "Email", "Phone", "Position", "Description", "Store Location", "Status",
                                                                        "Street", "City", "State", "ZipCode", "Country", "Details"),
                                                                        xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Employee_details_Table.xview)
        scroll_y.config(command = self.Employee_details_Table.yview)

        self.Employee_details_Table.heading("ID", text = "ID")
        self.Employee_details_Table.heading("First Name", text = "First Name")
        self.Employee_details_Table.heading("Last Name", text = "Last Name")
        self.Employee_details_Table.heading("DOB", text = "DOB")
        self.Employee_details_Table.heading("Email", text = "Email")
        self.Employee_details_Table.heading("Phone", text = "Phone")
        self.Employee_details_Table.heading("Position", text = "Position")
        self.Employee_details_Table.heading("Description", text = "Description")
        self.Employee_details_Table.heading("Store Location", text = "Store Location")
        self.Employee_details_Table.heading("Status", text = "Status")
        self.Employee_details_Table.heading("Street", text = "Street")
        self.Employee_details_Table.heading("City", text = "City")
        self.Employee_details_Table.heading("State", text = "State")
        self.Employee_details_Table.heading("ZipCode", text = "ZipCode")
        self.Employee_details_Table.heading("Country", text = "Country")
        self.Employee_details_Table.heading("Details", text = "Details")

        self.Employee_details_Table["show"] = "headings"

        self.Employee_details_Table.column("ID", width = 40, anchor = CENTER)
        self.Employee_details_Table.column("First Name", width = 70, anchor = CENTER)
        self.Employee_details_Table.column("Last Name", width = 70, anchor = CENTER)
        self.Employee_details_Table.column("DOB", width = 70, anchor = CENTER)
        self.Employee_details_Table.column("Email", width = 210, anchor = CENTER)
        self.Employee_details_Table.column("Phone", width = 70, anchor = CENTER)
        self.Employee_details_Table.column("Position", width = 70, anchor = CENTER)
        self.Employee_details_Table.column("Description", width = 130, anchor = CENTER)
        self.Employee_details_Table.column("Store Location", width = 90, anchor = CENTER)
        self.Employee_details_Table.column("Status", width = 50, anchor = CENTER)
        self.Employee_details_Table.column("Street", width = 180, anchor = CENTER)
        self.Employee_details_Table.column("City", width = 60, anchor = CENTER)
        self.Employee_details_Table.column("State", width = 50, anchor = CENTER)
        self.Employee_details_Table.column("ZipCode", width = 60, anchor = CENTER)
        self.Employee_details_Table.column("Country", width = 60, anchor = CENTER)
        self.Employee_details_Table.column("Details", width = 130, anchor = CENTER)

        self.Employee_details_Table.pack(fill = BOTH, expand = 1)
        self.Employee_details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_employee(self):
        if self.var_first_name.get() == "" or self.var_last_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("INSERT INTO Employee_Status (Employee_Status_ID, Current_Status)\
                                                VALUES (?, ?)",
                                                self.var_employee_status_id.get(), self.var_current_status.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Job_Titles (Job_Title_ID, Job_Title, Job_Title_Description)\
                                                VALUES (?, ?, ?)",
                                                self.var_job_title_id.get(), self.var_job_title.get(), self.var_job_title_description.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Store_Location (Store_ID, Location)\
                                                VALUES (?, ?)",
                                                self.var_store_id.get(), self.var_location.get())  
                        conn.commit()

                        my_cursor.execute("INSERT INTO Employee_Addresses (Employee_Address_ID, Street, City, State, ZipCode, Country, Details)\
                                                VALUES (?, ?, ?, ?, ?, ?, ?)",
                                                self.var_employee_address_id.get(), self.var_street.get(), self.var_city.get(), self.var_state.get(),
                                                self.var_zip_code.get(), self.var_country.get(), self.var_details.get())
                        conn.commit()

                        my_cursor.execute("INSERT INTO Employees (Employee_ID, First_Name, Last_Name, Date_Of_Birth, Email_Address, Phone_Number, Employee_Address_ID, Store_ID, Job_Title_ID, Employee_Status_ID)\
                                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                                self.var_employee_id.get(), self.var_first_name.get(), self.var_last_name.get(), self.var_date_of_birth.get(), self.var_email_address.get(),
                                                self.var_phone_number.get(), self.var_employee_address_id.get(), self.var_store_id.get(), self.var_job_title_id.get(), self.var_employee_status_id.get())
                        conn.commit()
                        
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "A employee has been added", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
    
    def fetch_data(self):
        try:
                conn = pyodbc.connect(Connect)
                print("Connection to MySQL DB successful")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Employees.Employee_ID, Employees.First_Name, Employees.Last_Name, Employees.Date_Of_Birth, Employees.Email_Address, Employees.Phone_Number,\
		                                Job_Titles.Job_Title, Job_Titles.Job_Title_Description,\
		                                Store_Location.Location,\
		                                Employee_Status.Current_Status,\
		                                Employee_Addresses.Street, Employee_Addresses.City, Employee_Addresses.State, Employee_Addresses.ZipCode, Employee_Addresses.Country, Employee_Addresses.Details\
                                FROM Employees\
                                INNER JOIN Job_Titles ON Job_Titles.Job_Title_ID = Employees.Job_Title_ID\
                                INNER JOIN Store_Location ON Store_Location.Store_ID = Employees.Store_ID\
                                INNER JOIN Employee_Status ON Employee_Status.Employee_Status_ID = Employees.Employee_Status_ID\
                                INNER JOIN Employee_Addresses ON Employee_Addresses.Employee_Address_ID = Employees.Employee_Address_ID\
                                ORDER BY Employees.Employee_ID")
                
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                        self.Employee_details_Table.delete(*self.Employee_details_Table.get_children())
                        for i in rows:
                                self.Employee_details_Table.insert("",END,values = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]))
                        conn.commit()
                conn.close()
        except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)

    def get_cursor(self, event = ""):
        cursor_row = self.Employee_details_Table.focus()
        content = self.Employee_details_Table.item(cursor_row)
        row = content["values"]
        self.var_employee_id.set(row[0])
        self.var_first_name.set(row[1])
        self.var_last_name.set(row[2])
        self.var_date_of_birth.set(row[3])
        self.var_email_address.set(row[4])
        self.var_phone_number.set(row[5])
        self.var_job_title.set(row[6])
        self.var_job_title_description.set(row[7])
        self.var_location.set(row[8])
        self.var_current_status.set(row[9])
        self.var_street.set(row[10])
        self.var_city.set(row[11])
        self.var_state.set(row[12])
        self.var_zip_code.set(row[13])
        self.var_country.set(row[14])
        self.var_details.set(row[15])

    def update(self):
        if self.var_first_name.get() == "" or self.var_last_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("UPDATE Employee_Status SET Current_Status = ?\
                                        WHERE Employee_Status_ID = ?",
                                        self.var_current_status.get(), self.var_employee_id.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Employee_Addresses SET Street = ?, City = ?, State = ?, ZipCode = ?, Country = ?, Details = ?\
                                        WHERE Employee_Address_ID = ?",
                                        self.var_street.get(), self.var_city.get(), self.var_state.get(),
                                        self.var_zip_code.get(), self.var_country.get(), self.var_details.get(), self.var_employee_id.get())
                        conn.commit()

                        my_cursor.execute("UPDATE Store_Location SET Location = ?\
                                        WHERE Store_ID = ?",
                                        self.var_location.get(), self.var_employee_id.get())  
                        conn.commit()

                        my_cursor.execute("UPDATE Job_Titles SET Job_Title = ?, Job_Title_Description = ?\
                                        WHERE Job_Title_ID = ?",
                                        self.var_job_title.get(), self.var_job_title_description.get(), self.var_employee_id.get())  
                        conn.commit()

                        my_cursor.execute("UPDATE Employees SET First_Name = ?, Last_Name = ?, Date_Of_Birth = ?, Email_Address = ?, Phone_Number = ?\
                                        WHERE Employee_ID = ?",
                                        self.var_first_name.get(), self.var_last_name.get(), self.var_date_of_birth.get(),
                                        self.var_email_address.get(), self.var_phone_number.get(), self.var_employee_id.get())
                        conn.commit()

                        self.fetch_data()
                        conn.close()

                        messagebox.showinfo("Update", "Employee details has been updated successfully", parent = self.root)
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)  

    def Delete(self):
        Delete = messagebox.askyesno("Furniture Management Application", "Do you want to delete this employee?", parent = self.root)
        if Delete > 0:
                try:
                        conn = pyodbc.connect(Connect)
                        print("Connection to MySQL DB successful")
                        my_cursor = conn.cursor()

                        my_cursor.execute("DELETE FROM Employees WHERE Employee_ID = ?", self.var_employee_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Employee_Addresses WHERE Employee_Address_ID = ?", self.var_employee_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Store_Location WHERE Store_ID = ?", self.var_employee_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Job_Titles WHERE Job_Title_ID = ?", self.var_employee_id.get())
                        conn.commit()

                        my_cursor.execute("DELETE FROM Employee_Status WHERE Employee_Status_ID = ?", self.var_employee_id.get())
                        conn.commit()

                        self.fetch_data()
                        conn.close()
                        self.Reset()
                except Exception as es:
                        messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent = self.root)
        else:
                if not Delete:
                        return
        conn.commit()
        self.fetch_data()
        conn.close()

    def Reset(self):
        x = random.randint(1000,9999)
        self.var_employee_id.set(str(x))
        self.var_employee_address_id.set(str(x))
        self.var_store_id.set(str(x))
        self.var_job_title_id.set(str(x))
        self.var_employee_status_id.set(str(x))
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        self.var_date_of_birth.set(""),
        self.var_email_address.set(""),
        self.var_phone_number.set(""),
        self.var_job_title.set(""),
        self.var_job_title_description.set(""),
        self.var_current_status.set(""),
        self.var_street.set(""),
        self.var_city.set(""),
        self.var_state.set(""),
        self.var_zip_code.set(""),
        self.var_country.set(""),
        self.var_details.set(""),
        self.var_location.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Employee_Win(root)
    root.mainloop()
