import sys, datetime, pyttsx3, mysql.connector as sql
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)
def daysfinder(today,day_took):
    difference = today-day_took
    no_of_days = difference.days
    return no_of_days

conn=sql.connect(host="localhost",user="root",passwd="Pavitra@01",database="agro_fertilizers")
if conn.is_connected():
    engine.say("successfully connected")
    engine.runAndWait()
c=conn.cursor()
print("Agro-Fertilizer Shop Management System")
print("1.login")
print("2.Exit")
engine.say("Welcome to Beeralingeshwara Agro-Fertilizers")
engine.runAndWait()
choice=int(input("Enter your choice: "))

if choice==1:
    user_name=input("Enter your user name=")
    password=input("Enter your password=")
    today=datetime.date.today()
    print(today)
    date=int(str(today)[0:4]+str(today)[5:7]+str(today)[8:])
    while user_name=="Manohar" and password=="Pavitra@01":
        print("1}.Add customer details")
        print("2}.Update debt clearance Customer_details")
        print("3}.Update Product Details")
        print("4}.Add product details")
        print("5}.New worker details")
        print("6}.To see all the paid customers details")
        print("7}.TO see all the Debt maintaining customer's details")
        print("8}.To see all products details")
        print("9}.To see all workers details")
        print("10}.To see one of the customer's details")
        print("11}.To see one of the product's details")
        print("12}.To see one of the worker's details")
        print("13}.To add a new product into Stocks")
        print("14}.To see Stocks")
        print("15}.Chart Representation for Stocks")
        print("16}.Daywise Business Statistics")
        print("17}.Monthwise Business Statistics")
        print("18}.Yearwise Business Statistics")
        print("19}.To exit")
        choice=int(input("enter your choice= "))
        if choice==1:
            cust_name=input("Customer Name: ")
            phone_no=int(input("Customer's Phone Number: "))
            items_count=int(input("Enter the count of Distinct Products Customer desired: "))
            pay_details=int(input("Enter 1 if cash else press any other numeric for debt:"))
            if pay_details==1:
                for i in range(items_count):
                    product_name=input("Enter the Product Name: ")
                    product_count=int(input("Enter the number of items: "))
                    u="select cash_price from Product_details where Product_name={}".format(product_name)
                    c.execute(u)
                    v=c.fetchall()[0][0]
                    cost=v
                    for i in range(product_count):
                        t="insert into cash_paid_customer_details values({},{},{},{},{})".format(cust_name,phone_no,product_name,cost,date)
                        c.execute(t)
                        conn.commit()
                    print("Data updated Successfully")
                    z="select quantity from stocks where Product_name={}".format(product_name)
                    c.execute(z)
                    mn=c.fetchall()[0][0]
                    mn-=product_count
                    c.execute("update stocks set quantity ={} where product_name={}".format(mn,product_name))
                    conn.commit()
                print("Successful!!!")
            else:
                for i in range(items_count):
                    product_name=input("Enter the Product Name: ")
                    product_count=int(input("Enter the number of items: "))
                    u="select debt_price from Product_details where Product_name={}".format(product_name)
                    c.execute(u)
                    v=c.fetchall()[0][0]
                    cost=v
                    for i in range(product_count):
                        t="insert into customer_details values({},{},{},{},{})".format(cust_name,phone_no,product_name,cost,date)
                        c.execute(t)
                        conn.commit()
                    z="select quantity from stocks where Product_name={}".format(product_name)
                    c.execute(z)
                    mn=c.fetchall()[0][0]
                    mn-=product_count
                    c.execute("update stocks set quantity ={} where product_name={}".format(mn,product_name))
                    conn.commit()
                    print("Data updated Successfully")
                print("Successful!!!")
        elif choice==2:
            cust_name=input("Customer Name: ")
            phone_no=int(input("Customer's Phone Number: "))
            product_name='"Debt Clearance"'
            u="select sum(cost) from Customer_details where customer_name={}".format(cust_name)
            c.execute(u)
            v=c.fetchall()[0][0]
            cost=v
            print(cost)
            t="insert into cash_paid_customer_details values({},{},{},{},{})".format(cust_name,phone_no,product_name,cost,date)
            c.execute(t)
            conn.commit()
            print("Successful")
            r="update customer_details set cost = 0 where customer_name={} and Phone_no={}".format(cust_name,phone_no)
            c.execute(r)
            conn.commit()
            print("Data updated Successfully")
        elif choice==3:
            product_name=input("Enter the Product_name: ")
            cash_price= int(input("Enter the Cash Price of the Product: "))
            debt_price= int(input("Enter the Debt Price of the Product: "))
            t="update product_details set cash_price = {} and Debt_price = {} where produc_name = {}".format(product_name,cash_price,debt_price)
            try:
                c.execute(t)
                conn.commit()
                print("Data Updated Successfully")
            except:
                print("!!!!!!No Records regarding the Product you asked Kindly verify!!!!!!")
        elif choice==4:
            product_name=input("Enter the Product_name: ")
            cash_price= int(input("Enter the Cash Price of the Product: "))
            debt_price= int(input("Enter the Debt Price of the Product: "))
            t="insert into product_details values({},{},{})".format(product_name,cash_price,debt_price)
            c.execute(t)
            conn.commit()
            print("Data updated Successfully")
        elif choice==5:
            name=input("enter his/her name=")
            work=input("enter job =")
            age=int(input("enter your  age="))
            salary=int(input("enter salary="))
            no =int(input("enter your  phone number="))
            sql_insert="insert into worker_details values({},{},{},{},{})".format(name,work,age,salary,no)
            c.execute(sql_insert)
            conn.commit()
            print("Data updated")
        elif choice==6:
            c.execute("select*from cash_paid_customer_details Order by Customer_name,date")
            record=c.fetchall()
            for i in record:
                print(i)
        elif choice==7:
            c.execute("select * from customer_details order by customer_name")
            v=c.fetchall()
            for i in v:
                print(i)
        elif choice==8:
            c.execute("select*from product_details")
            record=c.fetchall()
            for i in record:
                print(i)
        elif choice==9:
            c.execute("select*from worker_details")
            record=c.fetchall()
            for i in record:
                print(i)
        elif choice==10:
            a=input("Enter his/her name: ")
            b=int(input("Enter Phone no: "))
            r1=float(input("Enter rate of interest: "))
            r=r1/365
            t='select*from customer_details where customer_name={} and phone_no={}'.format(a,b)
            c.execute(t)
            v=c.fetchall()
            l=[]
            if v:
                global count
                count = 0
                for i in v:
                    count+=1
                    print(i)
                    l.append(i)
                _debt=[]
                for i in range(count):
                    a=daysfinder(today,l[i][4])
                    _debt.append((l[i][3])*a*r/100)
                engine.say(sum(_debt))
                engine.runAndWait()
                print(sum(_debt))
            else:
                engine.say("No Records")
                engine.runAndWait()
                print("No Records!!!!")
            
            
        elif choice==11:
            a=input("enter your product_name")
            t='select*from product_details where product_name={}'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(i)
        elif choice==12:
            a=input('enter your name')
            t='select*from worker_details where worker_name={}'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(i)
        elif choice==13:
            product_name=input("Enter the Product Name: ")
            quantity=int(input("Enter the Quantity kg/units: "))
            t="insert into stocks values({},{})".format(product_name,quantity)
            c.execute(t)
            conn.commit()
            print("Data updation Successful")
        elif choice==14:
            t="select* from stocks"
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(i)
        elif choice==15:
            import matplotlib.pyplot as plt
            t="Select*from stocks"
            c.execute(t)
            Items=c.fetchall()
            Names=[]
            Values=[]
            for i in Items:
                Names.append(i[0])
                Values.append(i[1])
            colors=['red','yellow','black','brown','pink','green','indigo','purple','white','orange']
            plt.pie(Values,labels=Names,colors=colors)
            plt.title("Manohar Grocery store")
            plt.show()
        elif choice==16:
            t="Select Date,month(date),year(date),sum(cost) from customer_details group by year(date),month(date),Date"
            c.execute(t)
            business=c.fetchall()
            for i in business:
                print(i)
            t="Select Date,month(date),year(date),sum(cost) from cash_paid_customer_details group by year(date),month(date),Date"
            c.execute(t)
            business=c.fetchall()
            for i in business:
                print(i)
        elif choice==17:
            t="select Year(date),month(Date),sum(cost) from customer_details group by year(date),month(date)"
            c.execute(t)
            business=c.fetchall()
            for i in business:
                print(i)
            t="select Year(date),month(Date),sum(cost) from cash_paid_customer_details group by year(date),month(date)"
            c.execute(t)
            business=c.fetchall()
            for i in business:
                print(i)
        elif choice==18:
            t="Select Year(date),sum(cost) from customer_details group by year(date)"
            c.execute(t)
            business=c.fetchall()
            for i in business:
                print(i)
            t="Select Year(date),sum(cost) from cash_paid_customer_details group by year(date)"
            c.execute(t)
            business=c.fetchall()
            for i in business:
                print(i)
        elif choice==19:
            print("logout Successful")
            sys.exit()
    else:
        print('!!!!!Wrong Password, Entry Restricted!!!!')
        print("Please Try Again")
        sys.exit()
        
            
if choice==2:
    sys.exit()
