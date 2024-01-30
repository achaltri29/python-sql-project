import mysql.connector as sql
con=sql.connect(host='localhost',user='root',password='Achal,123',database='school_manage')
cur=con.cursor()
cur.execute("use school_manage")

def add():
    print("Which type of data are you entering?")
    while True:
        b=input('''Student's personal info(p),
                   Student's academic info(a),
                   student's fees status(f),
                   bus service status(b) :''')
        if b in ['p','a','f','b']:
            break
        print("Invalid response,please try again")
    if b=='p':
        table="st_prsnl_info"
        roll_no=input("please provide the roll no. of student:")
        ini_name=input("please provide initial name of student:")
        DOB=input("Please provide birth date of student in YYYY-MM-DD format:")
        address=input("Please provide address of student:")
        Parent_phoneNo=input("Please provide valid phone number of one of the parent/guardian:")
        cur.execute(f"insert into {table} values({roll_no},'{ini_name}','{DOB}','{address}',{Parent_phoneNo})")
        print("Data saved!")

    elif b=='a':
        table="acad_per_info"
        roll_no=input("please provide the roll no. of student:")
        clas=input("Type class of the student:")
        division=input("Type division to allot:")
        pyp=input("previous year percentage:")
        pyg=input("previous year grades:")
        cur.execute(f"insert into {table} values({roll_no},'{clas}','{division}',{pyp},'{pyg}')")
        print("Data saved!")

    elif b=='f':
        table="sch_fee"
        roll_no=input("please provide the roll no. of student:")
        schf=input("school fees paid?:-(y/n)")
        busf=input("bus fees amount paid?:-(y/n)")
        if schf=='y':
            c="yes"
        else:
            c="no"
        if busf=="y":
            d="yes"
        else:
            d="no"
        cur.execute(f"insert into {table} values({roll_no},'{c}','{d}")
        print("Data saved")


    elif b=='b':
        table="bus_service"
        roll_no=input("please provide the roll no. of student:")
        bss=input("Type the student's bus status:-(y/n)")
        dis=input("Type the distance(in km):")
        if bss=="y":
            bss="yes"
        cur.execute(f"insert into {table} values({roll_no},'{bss}',{dis})")
        print("Data saved")



def remove():
    print("Which type of data do you want to remove?")
    while True:
        b=input('''Student's personal info(p),
                   Student's academic info(a),
                   student's fees status(f),
                   bus service status(b) :''')
        if b in ['p','a','f','b']:
            break
        print("Invalid response,please try again")
    if b=='p':
        table="st_prsnl_info"
    elif b=='a':
        table="acad_per_info"
    elif b=='f':
        table="sch_fee"
    elif b=='b':
        table="bus_service"

    roll_no=input("Type the roll number whose data you want to remove:")

    

def change():
    print("which type of data do you want to change?")
    while True:
        b=input('''Student's personal info(p),
                   Student's academic info(a),
                   student's fees status(f),
                   bus service status(b) :''')
        if b in ['p','a','f','b']:
            break
        print("Invalid response,please try again")

    r=input("Provide the roll number to change:")

    if b=='p':
        print("type s for no changes in column")
        inm=input("Type the student's new initial name:")
        bd=input("Type the student's new birth date in YYYY-MM-DD format:")
        ad=input("Type the student's new address:")
        ph=input("Type the student's parent's new phone number:")

        inmr=f"ini_name='{inm}'"
        bdr=f"DOB='{bd}'"
        adr=f"address='{ad}'"
        phr=f"Parent_phoneNo='{ph}'"

        inmx,bdx,adx=False,False,False

    if inm =="s":
        inmr=''
    else:
        inmx=True

    if bd =="s":
        bdr=''
    elif(bd!="s") and inmx:
        inmr= inmr + ","
    if bd !="s":
        bdx=True

    if ad =="s":
        adr=''
    elif(ad!="s") and bdx:
        bdr= bdr + ","
    if ad !="s":
        adx=True

    if ph =="s":
        phr=''
    elif(ph!="s") and adx:
        adr= adr + ","

    cur.execute("update st_prsnl_info set" + inmr + bdr + adr + phr + f"where roll_no={r}")
    print("Data changes!")

    if b=='a':
        clas=input("Type the student's new class:")
        division=input("Type the student's new division:")
        pyp=input("Type the new preyious year percentage of the student:")
        pyg=input("Type the new previous year grades of the student:")
        cur.execute(f"update acad_per_info set class='{clas}',division='{division}',pyp={pyp},pyg='{pyg}' where roll_no={r}")
        print("Data changes!")

    elif b=='f':
        sch=input("Type new school fees:")
        bus=input("Type new bus fees:")
        cur.execute(f"update sch_fee set sch='{sch}',bus='{bus}' where roll_no={r}")
        print("Data changes!")

    elif b=='b':
        bss=input("Type new bus service status-(yes/no):")
        dis=input("Type new distance-(yes/no):")
        cur.execute(f"update sch_fee set bss='{bss}',dist='{dis}' where roll_no={r}")



def display():
    print("What do you want to search?")
    b=input('''Student's roll number from initial name(1),
                   Student's personal info(2),
                   student's fees status(3),
                   bus service stauts(4),
                   student's academic info(5):''')
    if b=='1':
        nm=input("please type initial name of student:")
        cur.execute(f"select roll_no from st_prsnl_info where ini_name='{nm}'")
        a=cur.fetchone()
        print("roll number of student is",a)

    elif b=='2':
        a=input("Provide roll number of student:")
        cur.execute(f"select * from st_prsnl_info where roll_no={a}")
        d=cur.fetchone()
        print(d)

    elif b=='3':
        a=input("Provide roll number of student:")
        cur.execute(f"select * from sch_fee where roll_no={a}")
        d=cur.fetchone()
        print(d)

    elif b=='4':
        a=input("Provide roll number of student:")
        cur.execute(f"select * from bus_service where roll_no={a}")
        d=cur.fetchone()
        print(d)

    elif b=='5':
        a=input("Provide roll number of student:")
        cur.execute(f"select * from acad_per_info where roll_no={a}")
        d=cur.fetchone()
        print(d)

print("Welcome to School Management Program")
while True:
    print("Here are your actions to work with database:")
    print("Add,Remove,Change or Display data as a,r,c,d respectively")
    while True:
        a=input("Please mention your action as defined above(like a,r,c,d)")
        if a in ['a','r','c','d']:
            break
        print("Invalid response,please try again.")

    if a=='a':
        add()
    elif a=='r':
        remove()
    elif a=='c':
        change()
    elif a=='d':
        display()

    I=input("Do you want to run the software again?(y/n):")
    if I!="y":
        break

cur.execute("COMMIT")
con.close()
        
        

        

    
        

    
 
      
        
        
        
        

     



                       
                           
