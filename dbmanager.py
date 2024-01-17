from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import random


class MemberConnect:
    def __init__(self, root):
        self.root = root  # janela principal da GUI
        blank_space = " "
        self.root.title(202 * blank_space + "MySQL Connector")
        self.root.geometry("1360x700+0+0")

        # db variables
        MemID = StringVar()
        FirstName = StringVar()
        Surname = StringVar()
        Address = StringVar()
        POBox = StringVar()
        Gender = StringVar()
        MType = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Search = StringVar()
        MemIDBar = StringVar()

        # ========
        # FUNÇÕES
        # ========

        def addNew():
            if MemID.get() == "" or FirstName.get() == "" or Surname.get() == "":
                tkinter.messagebox.showerror(
                    "Error check input", "Enter correct member details"
                )
            else:
                sqlCon = pymysql.connect(
                    host="localhost", user="dsv", password="jld0856", database="members"
                )
                qry = f"INSERT INTO member VALUES('{MemID.get()}','{FirstName.get()}','{Surname.get()}','{Address.get()}','{POBox.get()}','{Gender.get()}','{Mobile.get()}','{Email.get()}','{MType.get()}')"

                cur = sqlCon.cursor()
                cur.execute(qry)
                sqlCon.commit()
                ShowRecord()
                sqlCon.close()
                tkinter.messagebox.showinfo(
                    "Data Entry Form", "Record entered successfully"
                )

        def ShowRecord():
            sqlCon = pymysql.connect(
                host="localhost", user="dsv", password="jld0856", database="members"
            )
            qry = "SELECT * FROM member"

            cur = sqlCon.cursor()
            cur.execute(qry)

            rs = cur.fetchall()

            if len(rs) != 0:
                self.member_records.delete(*self.member_records.get_children())
                for row in rs:
                    self.member_records.insert("", END, values=row)
                sqlCon.commit()
                sqlCon.close()

        def MembersInfo(ev):
            viewInfo = self.member_records.focus()
            learnerData = self.member_records.item(viewInfo)
            row = learnerData["values"]

            MemID.set(row[0])
            FirstName.set(row[1])
            Surname.set(row[2])
            Address.set(row[3])
            POBox.set(row[4])
            Gender.set(row[5])
            Mobile.set(row[6])
            Email.set(row[7])
            MType.set(row[8])

        def update():
            sqlCon = pymysql.connect(
                host="localhost", user="dsv", password="jld0856", database="members"
            )
            qry = f"UPDATE member SET firstname='{FirstName.get()}', surname='{Surname.get()}', address='{Address.get()}', pobox='{POBox.get()}', gender='{Gender.get()}', mobile='{Mobile.get()}', email='{Email.get()}',mtype='{MType.get()}' WHERE memid='{MemID.get()}'"

            cur = sqlCon.cursor()
            cur.execute(qry)

            sqlCon.commit()
            ShowRecord()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Data Entry Form", "Record Updated Successfully."
            )

        def deleteDB():
            sqlCon = pymysql.connect(
                host="localhost", user="dsv", password="jld0856", database="members"
            )
            qry = f"DELETE FROM member WHERE memid='{MemID.get()}'"

            cur = sqlCon.cursor()
            cur.execute(qry)

            sqlCon.commit()
            ShowRecord()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Data Entry Form", "Record DELETED Successfully."
            )

        def Reset():
            MemID.set("")
            FirstName.set("")
            Surname.set("")
            Address.set("")
            POBox.set("")
            Gender.set("")
            Mobile.set("")
            Email.set("")
            MType.set("")

        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Data Entry Form", "Confirm if you want to exit."
            )
            if iExit > 0:
                root.destroy()
                return

        def searchDG():
            try:
                sqlCon = pymysql.connect(
                    host="localhost", user="dsv", password="jld0856", database="members"
                )
                qry = f"SELECT * FROM member WHERE memid='{Search.get()}'"

                cur = sqlCon.cursor()
                cur.execute(qry)

                row = cur.fetchone()
                
                MemID.set(row[0])
                FirstName.set(row[1])
                Surname.set(row[2])
                Address.set(row[3])
                POBox.set(row[4])
                Gender.set(row[5])
                Mobile.set(row[6])
                Email.set(row[7])
                MType.set(row[8])

                sqlCon.commit()                

            except Exception as e:
                message = f"No such record.\nProblem: {e}"
                tkinter.messagebox.showinfo("Data Entry Form", message=message)
                Search.set("")
                Reset()

            sqlCon.close()
            Search.set("")


        # ====================
        # DEFININDO OS FRAMES
        # ====================
        #
        # Main Frame - Janela Principal
        MainFrame = Frame(
            self.root, bd=10, width=1350, height=700, relief=RIDGE, bg="cadetblue"
        )  # RIDGE = define efeito 3D do frame (FLAT, RAISED, SUNKEN, GROOVE)
        MainFrame.grid()

        # TitleFrame - Título
        TitleFrame = Frame(MainFrame, bd=7, width=1340, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)

        # SearchFrame - Pesquisa registros
        SearchFrame = Frame(
            MainFrame, bd=5, padx=5, width=1340, height=50, relief=RIDGE
        )
        SearchFrame.grid(row=1, column=0)

        # MidFrame
        MidFrame = Frame(MainFrame, bd=5, width=1340, height=500, relief=RIDGE)
        MidFrame.grid(row=2, column=0)

        # MembersDetailsFRM - Dados de um membro específico
        MembersDetailsFrm = Frame(
            MidFrame, bd=5, width=1340, height=100, padx=6, pady=4, relief=RIDGE
        )
        MembersDetailsFrm.grid(row=0, column=0)

        # TreeviewFrm - Lista de registros da base de dados
        TreeviewFrm = Frame(
            MidFrame, bd=5, width=1340, height=400, padx=2, relief=RIDGE
        )
        TreeviewFrm.grid(row=1, column=0)

        # ButtonFrame - Botões de ação
        ButtonFrame = Frame(
            MidFrame, bd=7, width=1340, height=50, bg="cadetblue", relief=RIDGE
        )
        ButtonFrame.grid(row=2, column=0)

        # ===============================
        # POPULANDO OS FRAMES
        # ===============================

        # TÍTULO
        # ------
        self.lblTitle = Label(
            TitleFrame, font=("arial", 40, "bold"), text="MySql Connection", bd=7
        )
        self.lblTitle.grid(row=0, column=0, padx=422)

        # MEMBROS (MembersDetailsFrm)
        # ---------------------------

        # MemID
        self.lblmemberID = Label(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            text="Member ID",
            bd=7,
            anchor="w",
            justify=LEFT,
        )
        self.lblmemberID.grid(row=0, column=0, sticky="W", padx=5)

        self.txtmemberID = Entry(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            width=36,
            textvariable=MemID,
            bd=7,
            justify=LEFT,
        )
        self.txtmemberID.grid(row=0, column=1)

        # FirstName
        self.lblFirstName = Label(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            text="First Name",
            bd=7,
            anchor="w",
            justify=LEFT,
        )
        self.lblFirstName.grid(row=1, column=0, sticky="W", padx=5)

        self.txtFirstName = Entry(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            width=36,
            textvariable=FirstName,
            bd=7,
            justify=LEFT,
        )
        self.txtFirstName.grid(row=1, column=1)

        # Surname
        self.lblSurname = Label(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            text="Surname",
            bd=7,
            anchor="w",
            justify=LEFT,
        )
        self.lblSurname.grid(row=2, column=0, sticky="W", padx=5)

        self.txtSurname = Entry(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            width=36,
            textvariable=Surname,
            bd=7,
            justify=LEFT,
        )
        self.txtSurname.grid(row=2, column=1)

        # Address
        self.lblAddress = Label(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            text="Address",
            bd=7,
            anchor="w",
            justify=LEFT,
        )
        self.lblAddress.grid(row=0, column=2, sticky="W", padx=5)

        self.txtAddress = Entry(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            width=36,
            textvariable=Address,
            bd=7,
            justify=LEFT,
        )
        self.txtAddress.grid(row=0, column=3)

        # Gender
        self.lblGender = Label(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            text="Gender",
            bd=7,
            anchor="w",
            justify=LEFT,
        )
        self.lblGender.grid(row=1, column=2, sticky="W", padx=5)

        self.txtGender = Entry(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            width=36,
            textvariable=Gender,
            bd=7,
            justify=LEFT,
        )
        self.txtGender.grid(row=1, column=3)

        # Mobile
        self.lblMobile = Label(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            text="Mobile",
            bd=7,
            anchor="w",
            justify=LEFT,
        )
        self.lblMobile.grid(row=2, column=2, sticky="W", padx=5)

        self.txtMobile = Entry(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            width=36,
            textvariable=Mobile,
            bd=7,
            justify=LEFT,
        )
        self.txtMobile.grid(row=2, column=3)

        # POBox
        self.lblPOBox = Label(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            text="POBox",
            bd=7,
            anchor="w",
            justify=LEFT,
        )
        self.lblPOBox.grid(row=0, column=4, sticky="W", padx=5)

        self.txtPOBox = Entry(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            width=35,
            textvariable=POBox,
            bd=5,
            justify=LEFT,
        )
        self.txtPOBox.grid(row=0, column=5)

        # Email
        self.lblEmail = Label(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            text="Email",
            bd=5,
            anchor="w",
            justify=LEFT,
        )
        self.lblEmail.grid(row=1, column=4, sticky="W", padx=5)

        self.txtEmail = Entry(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            width=35,
            textvariable=Email,
            bd=5,
            justify=LEFT,
        )
        self.txtEmail.grid(row=1, column=5)

        # MType
        self.lblType = Label(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            text="Type",
            bd=5,
            anchor="w",
            justify=LEFT,
        )
        self.lblType.grid(row=2, column=4, sticky="W", padx=5)

        self.cboType = ttk.Combobox(
            MembersDetailsFrm,
            font=("arial", 12, "bold"),
            width=33,
            textvariable=MType,
            state="readonly",
        )
        self.cboType["values"] = ("Member Type", "Annual Member", "Quartely", "Monthly")
        self.cboType.current(0)
        self.cboType.grid(row=2, column=5)

        # LISTA DE REGISTROS (TreeviewFrm)
        # --------------------------------

        scroll_y = Scrollbar(TreeviewFrm, orient="vertical")
        self.member_records = ttk.Treeview(
            TreeviewFrm,
            height=12,
            columns=(
                "memid",
                "firstname",
                "surname",
                "address",
                "pobox",
                "gender",
                "mobile",
                "email",
                "mtype",
            ),
            yscrollcommand=scroll_y.set,
        )
        scroll_y.pack(side=RIGHT, fill=Y)

        self.member_records.heading("memid", text="MemberID")
        self.member_records.heading("firstname", text="FirstName")
        self.member_records.heading("surname", text="Surname")
        self.member_records.heading("address", text="Address")
        self.member_records.heading("pobox", text="PO Box")
        self.member_records.heading("gender", text="Gender")
        self.member_records.heading("mobile", text="Mobile")
        self.member_records.heading("email", text="Email")
        self.member_records.heading("mtype", text="Member Type")

        self.member_records["show"] = "headings"

        self.member_records.column("memid", width=110)
        self.member_records.column("firstname", width=140)
        self.member_records.column("surname", width=140)
        self.member_records.column("address", width=212)
        self.member_records.column("pobox", width=120)
        self.member_records.column("gender", width=110)
        self.member_records.column("mobile", width=120)
        self.member_records.column("email", width=212)
        self.member_records.column("mtype", width=120)

        self.member_records.pack(fill=BOTH, expand=1)
        self.member_records.bind("<ButtonRelease-1>", MembersInfo)
        ShowRecord()

        # SearchFrm - Pesquisa
        self.lblBarCode = Label(
            SearchFrame, font=("arial", 12, "bold"), text="Bar Code"
        )
        self.lblBarCode.grid(row=0, column=0, sticky=W, padx=4)
        self.txtBarCode = Entry(
            SearchFrame,
            font=("CCode39", 13, "bold"),
            bd=5,
            width=28,
            justify="center",
            textvariable=MemIDBar,
        )
        self.txtBarCode.grid(row=0, column=1, padx=39)

        self.txtSearch = Entry(
            SearchFrame,
            font=("arial", 18, "bold"),
            bd=5,
            width=33,
            justify="right",
            textvariable=Search,
        )
        self.txtSearch.grid(row=0, column=2)

        self.btnSearch = Button(
            SearchFrame,
            pady=1,
            padx=29,
            bd=4,
            font=("arial", 16, "bold"),
            width=9,
            height=1,
            text="Search",
            bg="cadetblue",
            command=searchDG
        ).grid(row=0, column=3, padx=1)

        # ButtonFrame - Botões de ação (CRUD)
        self.btnAddNew = Button(
            ButtonFrame,
            pady=1,
            padx=23,
            bd=4,
            font=("arial", 16, "bold"),
            width=12,
            height=1,
            text="AddNew",
            command=addNew,
        ).grid(row=0, column=0, padx=1)
        self.btnShowRecord = Button(
            ButtonFrame,
            pady=1,
            padx=23,
            bd=4,
            font=("arial", 16, "bold"),
            width=12,
            height=1,
            text="Show Record",
            command=ShowRecord,
        ).grid(row=0, column=1, padx=1)
        self.btnUpdate = Button(
            ButtonFrame,
            pady=1,
            padx=23,
            bd=4,
            font=("arial", 16, "bold"),
            width=12,
            height=1,
            text="Update",
            command=update,
        ).grid(row=0, column=2, padx=1)
        self.btnDelete = Button(
            ButtonFrame,
            pady=1,
            padx=23,
            bd=4,
            font=("arial", 16, "bold"),
            width=12,
            height=1,
            text="Delete",
            command=deleteDB,
        ).grid(row=0, column=3, padx=1)
        self.btnReset = Button(
            ButtonFrame,
            pady=1,
            padx=23,
            bd=4,
            font=("arial", 16, "bold"),
            width=12,
            height=1,
            text="Reset",
            command=Reset,
        ).grid(row=0, column=4, padx=1)
        self.btnExit = Button(
            ButtonFrame,
            pady=1,
            padx=23,
            bd=4,
            font=("arial", 16, "bold"),
            width=12,
            height=1,
            text="Exit",
            command=iExit,
        ).grid(row=0, column=5, padx=1)


if __name__ == "__main__":
    root = Tk()
    application = MemberConnect(root)
    root.mainloop()
