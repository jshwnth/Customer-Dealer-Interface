import tkinter as tk
from tkinter import messagebox
import mysql.connector


#DATABASE INITIALIZATION AND TABLE CREATION-------------------------------------------------------------(KINDLY CHANGE THE USERNAME,PASSWORD,DATABASE NAME, ACCORDING TO YOUR SQL DATABASE CONFIGURATION)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="test"
)

mycursor = mydb.cursor()

#TABLE CREATION

mycursor.execute("CREATE TABLE IF NOT EXISTS electronics (id VARCHAR(255)  PRIMARY KEY, category VARCHAR(255), brand_name VARCHAR(255), dimensions VARCHAR(255), price VARCHAR(255), description VARCHAR(255), location VARCHAR(255), stock VARCHAR(255), dealer_name VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS automobiles (id VARCHAR(255)  PRIMARY KEY, category VARCHAR(255), brand_name VARCHAR(255), model VARCHAR(255), mileage VARCHAR(255), price VARCHAR(255), description VARCHAR(255), location VARCHAR(255), stock VARCHAR(255), dealer_name VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS books (id VARCHAR(255)  PRIMARY KEY, category VARCHAR(255), name VARCHAR(255), price VARCHAR(255), description VARCHAR(255), location VARCHAR(255), stock VARCHAR(255), dealer_name VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS movies (id VARCHAR(255)  PRIMARY KEY, category VARCHAR(255), name VARCHAR(255), price VARCHAR(255), description VARCHAR(255), location VARCHAR(255), stock VARCHAR(255), dealer_name VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS sports (id VARCHAR(255)  PRIMARY KEY, category VARCHAR(255), brand_name VARCHAR(255), dimensions VARCHAR(225), price VARCHAR(255), description VARCHAR(255), location VARCHAR(255), stock VARCHAR(255), dealer_name VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS login (id VARCHAR(255)  PRIMARY KEY, user_name VARCHAR(255), pwd VARCHAR(255), d_name VARCHAR(255))")

class dealer_delete_page:

    def __init__(self,root,tblname,dn):
        self.root=root
        self.tblname=tblname
        self.dn=dn
        self.initialize()


    def initialize(self):

        self.title=tk.Label(self.root,text="DELETE ENTRY")
        self.title.grid(columnspan=2,row=0)
              

        if self.tblname=="electronics":

            def confirm1():

                self.val0=self.addent0.get()
                
                print(self.val0)
                
                if self.val0=='' :
                    tk.messagebox.showinfo("Warning", "Please Fill Up The Box")

                               
                else:
                    idno=self.val0
                    mycursor.execute("DELETE FROM electronics WHERE id='%s'" % (idno))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entry deleted successfully")
                    

            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)
            

            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)

                      
            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm1)
            self.addbut.grid(columnspan=2,row=3,pady=20)



        if self.tblname=="automobiles":

            def confirm2():

                self.val0=self.addent0.get()
                
                print(self.val0)
                
                if self.val0=='' :
                    tk.messagebox.showinfo("Warning", "Please Fill Up The Box")

                               
                else:
                    idno=self.val0
                    mycursor.execute("DELETE FROM automobiles WHERE id='%s'" % (idno))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entry deleted successfully")
                    

            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)
            

            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)

                      
            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm1)
            self.addbut.grid(column=2,row=9)

 


        if self.tblname=="books":
               

               def confirm3():
                   self.val0=self.addent0.get()
                
                   print(self.val0)
                
                   if self.val0=='' :
                       tk.messagebox.showinfo("Warning", "Please Fill Up The Box")

                               
                   else:
                       idno=self.val0
                       mycursor.execute("DELETE FROM books WHERE id='%s'" % (idno))
                       tk.messagebox.showinfo("Success", "Entry deleted successfully")
                       

               self.addlab0=tk.Label(self.root,text="ID")
               self.addlab0.grid(column=0,row=1,pady=20)
            

               self.addent0=tk.Entry(self.root)
               self.addent0.grid(column=1,row=1,pady=20)

                      
               self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm1)
               self.addbut.grid(column=2,row=9)


                



        if self.tblname=="movies":

            def confirm4():

                self.val0=self.addent0.get()
                
                print(self.val0)
                
                if self.val0=='' :
                    tk.messagebox.showinfo("Warning", "Please Fill Up The Box")

                               
                else:
                    idno=self.val0
                    mycursor.execute("DELETE FROM movies WHERE id='%s'" % (idno))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entry deleted successfully")
                    
                    
            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)
            

            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)

                      
            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm1)
            self.addbut.grid(column=2,row=9)






        if self.tblname=="sports":

            def confirm5():

                self.val0=self.addent0.get()
                
                print(self.val0)
                
                if self.val0=='' :
                    tk.messagebox.showinfo("Warning", "Please Fill Up The Box")

                               
                else:
                    idno=self.val0
                    mycursor.execute("DELETE FROM sports WHERE id='%s'" % (idno))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entry deleted successfully")
                    

            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)
            

            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)

                      
            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm1)
            self.addbut.grid(column=2,row=9)
















#------------#--------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#----------------------------------------------------------------
class dealer_update_page:

    def __init__(self,root,tblname,dn):
        self.root=root
        self.tblname=tblname
        self.dn=dn
        self.initialize()


    def initialize(self):

        self.title=tk.Label(self.root,text="UPDATE ENTRY")
        self.title.grid(columnspan=2,row=0)
              

        if self.tblname=="electronics":

            def confirm1():

                self.val0=self.addent0.get()
                self.val1=self.addent1.get()
                self.val2=self.addent2.get()
                self.val3=self.addent3.get()
                self.val4=self.addent4.get()
                self.val5=self.addent5.get()
                self.val6=self.addent6.get()
                self.val7=self.addent7.get()
                print(self.val0)
                
                if self.val0=='' or self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='' or self.val7=='' :
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                               
                else:
                    idno=self.val0
                    mycursor.execute("UPDATE electronics SET category='%s', brand_name='%s', dimensions='%s', price='%s', description='%s', location='%s', stock='%s', dealer_name='%s' WHERE id='%s'" % (self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,self.dn,idno))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entries updated successfully")
                    

            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)
            
            self.addlab1=tk.Label(self.root,text="category")
            self.addlab1.grid(column=0,row=2,pady=20)
        
            self.addlab2=tk.Label(self.root,text="Brand name")
            self.addlab2.grid(column=0,row=3,pady=20)

            self.addlab3=tk.Label(self.root,text="dimensions")
            self.addlab3.grid(column=0,row=4,pady=20)
            
            self.addlab4=tk.Label(self.root,text="price")
            self.addlab4.grid(column=0,row=5,pady=20)

            self.addlab5=tk.Label(self.root,text="description")
            self.addlab5.grid(column=0,row=6,pady=20)

            self.addlab6=tk.Label(self.root,text="location")
            self.addlab6.grid(column=0,row=7,pady=20)

            self.addlab7=tk.Label(self.root,text="stock quantity")
            self.addlab7.grid(column=0,row=8,pady=20)


            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)

            self.addent1=tk.Entry(self.root)
            self.addent1.grid(column=1,row=2,pady=20)

            self.addent2=tk.Entry(self.root)
            self.addent2.grid(column=1,row=3,pady=20)

            self.addent3=tk.Entry(self.root)
            self.addent3.grid(column=1,row=4,pady=20)
            
            self.addent4=tk.Entry(self.root)
            self.addent4.grid(column=1,row=5,pady=20)

            self.addent5=tk.Entry(self.root)
            self.addent5.grid(column=1,row=6,pady=20)

            self.addent6=tk.Entry(self.root)
            self.addent6.grid(column=1,row=7,pady=20)

            self.addent7=tk.Entry(self.root)
            self.addent7.grid(column=1,row=8,pady=20)
                      
            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm1)
            self.addbut.grid(columnspan=2,row=9)



        if self.tblname=="automobiles":

            def confirm2():

                self.val0=self.addent0.get()
                self.val1=self.addent1.get()
                self.val2=self.addent2.get()
                self.val3=self.addent3.get()
                self.val4=self.addent4.get()
                self.val5=self.addent5.get()
                self.val6=self.addent6.get()
                self.val7=self.addent7.get()
                self.val8=self.addent8.get()
                
                if self.val0=='' or self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='' or self.val7=='' or self.val8=='':
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                                  
                
                else:
                    idno=self.val0
                    mycursor.execute("UPDATE automobiles SET category='%s', brand_name='%s', model='%s', mileage='%s', price='%s', description='%s', location='%s', stock='%s', dealer_name='%s' WHERE id=%s" % (self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,self.val8,self.dn,idno))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entries updated successfully")
                    mycursor.commit()
                    

            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)

            
            self.addlab1=tk.Label(self.root,text="category")
            self.addlab1.grid(column=0,row=2,pady=20)
        
            self.addlab2=tk.Label(self.root,text="Brand name")
            self.addlab2.grid(column=0,row=3,pady=20)

            self.addlab3=tk.Label(self.root,text="model")
            self.addlab3.grid(column=0,row=4,pady=20)

            self.addlab4=tk.Label(self.root,text="mileage")
            self.addlab4.grid(column=0,row=5,pady=20)

            self.addlab5=tk.Label(self.root,text="price")
            self.addlab5.grid(column=0,row=6,pady=20)

            self.addlab6=tk.Label(self.root,text="description")
            self.addlab6.grid(column=0,row=7,pady=20)

            self.addlab7=tk.Label(self.root,text="location")
            self.addlab7.grid(column=0,row=8,pady=20)
            
            self.addlab8=tk.Label(self.root,text="stock quantity")
            self.addlab8.grid(column=0,row=9,pady=20)



            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)

            self.addent1=tk.Entry(self.root)
            self.addent1.grid(column=1,row=2,pady=20)

            self.addent2=tk.Entry(self.root)
            self.addent2.grid(column=1,row=3,pady=20)

            self.addent3=tk.Entry(self.root)
            self.addent3.grid(column=1,row=4,pady=20)
            
            self.addent4=tk.Entry(self.root)
            self.addent4.grid(column=1,row=5,pady=20)

            self.addent5=tk.Entry(self.root)
            self.addent5.grid(column=1,row=6,pady=20)

            self.addent6=tk.Entry(self.root)
            self.addent6.grid(column=1,row=7,pady=20)

            self.addent7=tk.Entry(self.root)
            self.addent7.grid(column=1,row=8,pady=20)

            self.addent8=tk.Entry(self.root)
            self.addent8.grid(column=1,row=9,pady=30)

            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm2)
            self.addbut.grid(columnspan=2,row=10)



        if self.tblname=="books":
               

               def confirm3():

                self.val0=self.addent0.get()
                self.val1=self.addent1.get()
                self.val2=self.addent2.get()
                self.val3=self.addent3.get()
                self.val4=self.addent4.get()
                self.val5=self.addent5.get()
                self.val6=self.addent6.get()
                
                
                if self.val0=='' or self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='' :
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                                               
                else:
                    idno=self.val0
                    mycursor.execute("UPDATE books SET category='%s', name='%s', price='%s', description='%s', location='%s', stock='%s', dealer_name='%s' WHERE id=%s" % (self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.dn,idno))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entries updated successfully")
                    


                self.addlab0=tk.Label(self.root,text="ID")
                self.addlab0.grid(column=0,row=1,pady=20)
            
                self.addlab1=tk.Label(self.root,text="category")
                self.addlab1.grid(column=0,row=2,pady=20)
        
                self.addlab2=tk.Label(self.root,text="name")
                self.addlab2.grid(column=0,row=3,pady=20)

                self.addlab3=tk.Label(self.root,text="price")
                self.addlab3.grid(column=0,row=4,pady=20)

                self.addlab4=tk.Label(self.root,text="description")
                self.addlab4.grid(column=0,row=5,pady=20)

                self.addlab5=tk.Label(self.root,text="location")
                self.addlab5.grid(column=0,row=6,pady=20)

                self.addlab6=tk.Label(self.root,text="stock")
                self.addlab6.grid(column=0,row=7,pady=20)


                
                self.addent0=tk.Entry(self.root)
                self.addent0.grid(column=1,row=1,pady=20)

            
                self.addent1=tk.Entry(self.root)
                self.addent1.grid(column=1,row=2,pady=20)

                self.addent2=tk.Entry(self.root)
                self.addent2.grid(column=1,row=3,pady=20)

                self.addent3=tk.Entry(self.root)
                self.addent3.grid(column=1,row=4,pady=20)
            
                self.addent4=tk.Entry(self.root)
                self.addent4.grid(column=1,row=5,pady=20)

                self.addent5=tk.Entry(self.root)
                self.addent5.grid(column=1,row=6,pady=20)

                self.addent6=tk.Entry(self.root)
                self.addent6.grid(column=1,row=7,pady=20)

                    
                self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm3)
                self.addbut.grid(columnspan=2,row=9)




        if self.tblname=="movies":

            def confirm4():

                self.val0=self.addent0.get()
                self.val1=self.addent1.get()
                self.val2=self.addent2.get()
                self.val3=self.addent3.get()
                self.val4=self.addent4.get()
                self.val5=self.addent5.get()
                self.val6=self.addent6.get()
                
                
                if self.val0=='' or self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='':
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                
                elif self.val3 and self.val6 not in '1234567890':
                    tk.messagebox.showinfo("Warning", "Incorrect Parameters passed")
                
                else:
                    idno=self.val0
                    mycursor.execute("UPDATE books SET category='%s', name='%s', price='%s', description='%s', location='%s', stock='%s', dealer_name='%s' WHERE id=%s" % (self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,idno))
                    tk.messagebox.showinfo("Success", "Entries updated successfully")
                    mycursor.commit()



            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)

            
            self.addlab1=tk.Label(self.root,text="category")
            self.addlab1.grid(column=0,row=2,pady=20)
        
            self.addlab2=tk.Label(self.root,text="name")
            self.addlab2.grid(column=0,row=3,pady=20)

            self.addlab3=tk.Label(self.root,text="price")
            self.addlab3.grid(column=0,row=4,pady=20)

            self.addlab4=tk.Label(self.root,text="description")
            self.addlab4.grid(column=0,row=5,pady=20)

            self.addlab5=tk.Label(self.root,text="location")
            self.addlab5.grid(column=0,row=6,pady=20)

            self.addlab6=tk.Label(self.root,text="stock")
            self.addlab6.grid(column=0,row=7,pady=20)



            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)

            
            self.addent1=tk.Entry(self.root)
            self.addent1.grid(column=1,row=2,pady=20)

            self.addent2=tk.Entry(self.root)
            self.addent2.grid(column=1,row=3,pady=20)

            self.addent3=tk.Entry(self.root)
            self.addent3.grid(column=1,row=4,pady=20)
            
            self.addent4=tk.Entry(self.root)
            self.addent4.grid(column=1,row=5,pady=20)

            self.addent5=tk.Entry(self.root)
            self.addent5.grid(column=1,row=6,pady=20)

            self.addent6=tk.Entry(self.root)
            self.addent6.grid(column=1,row=7,pady=20)

            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm4)
            self.addbut.grid(columnspan=2,row=8)




        if self.tblname=="sports":

            def confirm5():

                self.val0=self.addent0.get()
                self.val1=self.addent1.get()
                self.val2=self.addent2.get()
                self.val3=self.addent3.get()
                self.val4=self.addent4.get()
                self.val5=self.addent5.get()
                self.val6=self.addent6.get()
                self.val7=self.addent7.get()
                
                if self.val0=='' or self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='' or self.val7=='' :
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                                                
                else:
                  idno=self.val0
                  mycursor.execute("UPDATE electronics SET category='%s', brand_name='%s', dimensions='%s', price='%s', description='%s', location='%s', stock='%s', dealer_name='%s' WHERE id=%s" % (self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,self.dn,idno))
                  mydb.commit()
                  tk.messagebox.showinfo("Success", "Entries updated successfully")
                  



            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)
            
            self.addlab1=tk.Label(self.root,text="category")
            self.addlab1.grid(column=0,row=2,pady=20)
        
            self.addlab2=tk.Label(self.root,text="Brand name")
            self.addlab2.grid(column=0,row=3,pady=20)

            self.addlab3=tk.Label(self.root,text="dimensions")
            self.addlab3.grid(column=0,row=4,pady=20)

            self.addlab4=tk.Label(self.root,text="price")
            self.addlab4.grid(column=0,row=5,pady=20)

            self.addlab5=tk.Label(self.root,text="description")
            self.addlab5.grid(column=0,row=6,pady=20)

            self.addlab6=tk.Label(self.root,text="location")
            self.addlab6.grid(column=0,row=7,pady=20)

            self.addlab7=tk.Label(self.root,text="stock quantity")
            self.addlab7.grid(column=0,row=8,pady=20)

            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)

            
            self.addent1=tk.Entry(self.root)
            self.addent1.grid(column=1,row=2,pady=20)

            self.addent2=tk.Entry(self.root)
            self.addent2.grid(column=1,row=3,pady=20)

            self.addent3=tk.Entry(self.root)
            self.addent3.grid(column=1,row=4,pady=20)
            
            self.addent4=tk.Entry(self.root)
            self.addent4.grid(column=1,row=5,pady=20)

            self.addent5=tk.Entry(self.root)
            self.addent5.grid(column=1,row=6,pady=20)

            self.addent6=tk.Entry(self.root)
            self.addent6.grid(column=1,row=7,pady=20)

            self.addent7=tk.Entry(self.root)
            self.addent7.grid(column=1,row=8,pady=20)

            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm5)
            self.addbut.grid(columnspan=2,row=9)























#--------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#--------------------------------------------------------------------------------------------------------------
class dealer_add_page:

    def __init__(self,root,tblname,dn):
        self.root=root
        self.tblname=tblname
        self.dn=dn
        self.initialize()
        
        


    def initialize(self):

        self.title=tk.Label(self.root,text="ADD ENTRY")
        self.title.grid(columnspan=2,row=0)
              

        if self.tblname=="electronics":

            def confirm1():

                self.val0=self.addent0.get()
                self.val1=self.addent1.get()
                self.val2=self.addent2.get()
                self.val3=self.addent3.get()
                self.val4=self.addent4.get()
                self.val5=self.addent5.get()
                self.val6=self.addent6.get()
                self.val7=self.addent7.get()
                
                if self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='' or self.val7=='' :
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                
                
                else:
                    mycursor.execute("INSERT INTO electronics (id, category, brand_name, dimensions, price, description, location, stock, dealer_name) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (self.val0,self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,self.dn))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entries added successfully")
                    


            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)
            
            self.addlab1=tk.Label(self.root,text="category")
            self.addlab1.grid(column=0,row=2,pady=20)
        
            self.addlab2=tk.Label(self.root,text="Brand name")
            self.addlab2.grid(column=0,row=3,pady=20)

            self.addlab3=tk.Label(self.root,text="dimensions")
            self.addlab3.grid(column=0,row=4,pady=20)

            self.addlab4=tk.Label(self.root,text="price")
            self.addlab4.grid(column=0,row=5,pady=20)

            self.addlab5=tk.Label(self.root,text="description")
            self.addlab5.grid(column=0,row=6,pady=20)

            self.addlab6=tk.Label(self.root,text="location")
            self.addlab6.grid(column=0,row=7,pady=20)

            self.addlab7=tk.Label(self.root,text="stock quantity")
            self.addlab7.grid(column=0,row=8,pady=20)

            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)


            self.addent1=tk.Entry(self.root)
            self.addent1.grid(column=1,row=2,pady=20)

            self.addent2=tk.Entry(self.root)
            self.addent2.grid(column=1,row=3,pady=20)

            self.addent3=tk.Entry(self.root)
            self.addent3.grid(column=1,row=4,pady=20)
            
            self.addent4=tk.Entry(self.root)
            self.addent4.grid(column=1,row=5,pady=20)

            self.addent5=tk.Entry(self.root)
            self.addent5.grid(column=1,row=6,pady=20)

            self.addent6=tk.Entry(self.root)
            self.addent6.grid(column=1,row=7,pady=20)

            self.addent7=tk.Entry(self.root)
            self.addent7.grid(column=1,row=8,pady=20)
            
            

            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm1)
            self.addbut.grid(columnspan=2,row=9)
            

            
                

            
          

        if self.tblname=="automobiles":

            def confirm2():

                self.val0=self.addent0.get()
                self.val1=self.addent1.get()
                self.val2=self.addent2.get()
                self.val3=self.addent3.get()
                self.val4=self.addent4.get()
                self.val5=self.addent5.get()
                self.val6=self.addent6.get()
                self.val7=self.addent7.get()
                self.val8=self.addent8.get()
                
                if self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='' or self.val7=='' or self.val8=='':
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                                   
                
                else:
                    mycursor.execute("INSERT INTO automobiles (id,category, brand_name, model, mileage, price, description, location, stock, dealer_name) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (self.val0,self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,self.val8,self.dn))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entries added successfully")
                    mycursor.commit()



            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)
            
            self.addlab1=tk.Label(self.root,text="category")
            self.addlab1.grid(column=0,row=2,pady=20)
        
            self.addlab2=tk.Label(self.root,text="Brand name")
            self.addlab2.grid(column=0,row=3,pady=20)

            self.addlab3=tk.Label(self.root,text="model")
            self.addlab3.grid(column=0,row=4,pady=20)

            self.addlab4=tk.Label(self.root,text="mileage")
            self.addlab4.grid(column=0,row=5,pady=20)

            self.addlab5=tk.Label(self.root,text="price")
            self.addlab5.grid(column=0,row=6,pady=20)

            self.addlab6=tk.Label(self.root,text="description")
            self.addlab6.grid(column=0,row=7,pady=20)

            self.addlab7=tk.Label(self.root,text="location")
            self.addlab7.grid(column=0,row=8,pady=20)
            
            self.addlab8=tk.Label(self.root,text="location")
            self.addlab8.grid(column=0,row=9,pady=20)

            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)



            self.addent1=tk.Entry(self.root)
            self.addent1.grid(column=1,row=2,pady=20)

            self.addent2=tk.Entry(self.root)
            self.addent2.grid(column=1,row=3,pady=20)

            self.addent3=tk.Entry(self.root)
            self.addent3.grid(column=1,row=4,pady=20)
            
            self.addent4=tk.Entry(self.root)
            self.addent4.grid(column=1,row=5,pady=20)

            self.addent5=tk.Entry(self.root)
            self.addent5.grid(column=1,row=6,pady=20)

            self.addent6=tk.Entry(self.root)
            self.addent6.grid(column=1,row=7,pady=20)

            self.addent7=tk.Entry(self.root)
            self.addent7.grid(column=1,row=8,pady=20)

            self.addent8=tk.Entry(self.root)
            self.addent8.grid(column=1,row=9,pady=30)

            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm2)
            self.addbut.grid(columnspan=2,row=10)




        if self.tblname=="books":

            def confirm3():

                self.val0=self.addent0.get()
                self.val1=self.addent1.get()
                self.val2=self.addent2.get()
                self.val3=self.addent3.get()
                self.val4=self.addent4.get()
                self.val5=self.addent5.get()
                self.val6=self.addent6.get()
                
                
                if self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='' :
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                                                
                else:
                    mycursor.execute("INSERT INTO books (id,category, name, price, description, location, stock, dealer_name) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.dn))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entries added successfully")
                    


            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)

            
            self.addlab1=tk.Label(self.root,text="category")
            self.addlab1.grid(column=0,row=2,pady=20)
        
            self.addlab2=tk.Label(self.root,text="name")
            self.addlab2.grid(column=0,row=3,pady=20)

            self.addlab3=tk.Label(self.root,text="price")
            self.addlab3.grid(column=0,row=4,pady=20)

            self.addlab4=tk.Label(self.root,text="description")
            self.addlab4.grid(column=0,row=5,pady=20)

            self.addlab5=tk.Label(self.root,text="location")
            self.addlab5.grid(column=0,row=6,pady=20)

            self.addlab6=tk.Label(self.root,text="stock")
            self.addlab6.grid(column=0,row=7,pady=20)

            self.addlab7=tk.Label(self.root,text="dealer name")
            self.addlab7.grid(column=0,row=8,pady=20)

            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)


            
            self.addent1=tk.Entry(self.root)
            self.addent1.grid(column=1,row=2,pady=20)

            self.addent2=tk.Entry(self.root)
            self.addent2.grid(column=1,row=3,pady=20)

            self.addent3=tk.Entry(self.root)
            self.addent3.grid(column=1,row=4,pady=20)
            
            self.addent4=tk.Entry(self.root)
            self.addent4.grid(column=1,row=5,pady=20)

            self.addent5=tk.Entry(self.root)
            self.addent5.grid(column=1,row=6,pady=20)

            self.addent6=tk.Entry(self.root)
            self.addent6.grid(column=1,row=7,pady=20)

            self.addent7=tk.Entry(self.root)
            self.addent7.grid(column=1,row=8,pady=20)

            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm3)
            self.addbut.grid(columnspan=2,row=9)

     


        if self.tblname=="movies":

            def confirm4():

                self.val0=self.addent0.get()
                self.val1=self.addent1.get()
                self.val2=self.addent2.get()
                self.val3=self.addent3.get()
                self.val4=self.addent4.get()
                self.val5=self.addent5.get()
                self.val6=self.addent6.get()
                
                
                if self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='':
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                
                elif self.val3 and self.val6 not in '1234567890':
                    tk.messagebox.showinfo("Warning", "Incorrect Parameters passed")
                
                else:
                    mycursor.execute("INSERT INTO movies (id,category, name, price, description, location, stock, dealer_name) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.dn))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entries added successfully")
                    


            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)

            self.addlab1=tk.Label(self.root,text="category")
            self.addlab1.grid(column=0,row=2,pady=20)
        
            self.addlab2=tk.Label(self.root,text="name")
            self.addlab2.grid(column=0,row=3,pady=20)

            self.addlab3=tk.Label(self.root,text="price")
            self.addlab3.grid(column=0,row=4,pady=20)

            self.addlab4=tk.Label(self.root,text="description")
            self.addlab4.grid(column=0,row=5,pady=20)

            self.addlab5=tk.Label(self.root,text="location")
            self.addlab5.grid(column=0,row=6,pady=20)

            self.addlab6=tk.Label(self.root,text="stock")
            self.addlab6.grid(column=0,row=7,pady=20)


            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)


            
            self.addent1=tk.Entry(self.root)
            self.addent1.grid(column=1,row=2,pady=20)

            self.addent2=tk.Entry(self.root)
            self.addent2.grid(column=1,row=3,pady=20)

            self.addent3=tk.Entry(self.root)
            self.addent3.grid(column=1,row=4,pady=20)
            
            self.addent4=tk.Entry(self.root)
            self.addent4.grid(column=1,row=5,pady=20)

            self.addent5=tk.Entry(self.root)
            self.addent5.grid(column=1,row=6,pady=20)

            self.addent6=tk.Entry(self.root)
            self.addent6.grid(column=1,row=7,pady=20)

            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm4)
            self.addbut.grid(columnspan=2,row=8)

      

            

        if self.tblname=="sports":

            def confirm5():

                self.val0=self.addent0.get()
                self.val1=self.addent1.get()
                self.val2=self.addent2.get()
                self.val3=self.addent3.get()
                self.val4=self.addent4.get()
                self.val5=self.addent5.get()
                self.val6=self.addent6.get()
                self.val7=self.addent7.get()
                
                if self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='' or self.val7=='' :
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")

                
                elif self.val4 and self.val6 not in '1234567890':
                    tk.messagebox.showinfo("Warning", "Incorrect Parameters passed")
                
                else:
                    mycursor.execute("INSERT INTO sports (id,category, brand_name, dimensions, price, description, location, stock, dealer_name) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (self.val0,self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,self.dn))
                    mydb.commit()
                    tk.messagebox.showinfo("Success", "Entries added successfully")


            self.addlab0=tk.Label(self.root,text="ID")
            self.addlab0.grid(column=0,row=1,pady=20)

            
            self.addlab1=tk.Label(self.root,text="category")
            self.addlab1.grid(column=0,row=2,pady=20)
        
            self.addlab2=tk.Label(self.root,text="Brand name")
            self.addlab2.grid(column=0,row=3,pady=20)

            self.addlab3=tk.Label(self.root,text="dimensions")
            self.addlab3.grid(column=0,row=4,pady=20)

            self.addlab4=tk.Label(self.root,text="price")
            self.addlab4.grid(column=0,row=5,pady=20)

            self.addlab5=tk.Label(self.root,text="description")
            self.addlab5.grid(column=0,row=6,pady=20)

            self.addlab6=tk.Label(self.root,text="location")
            self.addlab6.grid(column=0,row=7,pady=20)

            self.addlab7=tk.Label(self.root,text="stock quantity")
            self.addlab7.grid(column=0,row=8,pady=20)

            self.addent0=tk.Entry(self.root)
            self.addent0.grid(column=1,row=1,pady=20)

            self.addent1=tk.Entry(self.root)
            self.addent1.grid(column=1,row=2,pady=20)

            self.addent2=tk.Entry(self.root)
            self.addent2.grid(column=1,row=3,pady=20)

            self.addent3=tk.Entry(self.root)
            self.addent3.grid(column=1,row=4,pady=20)
            
            self.addent4=tk.Entry(self.root)
            self.addent4.grid(column=1,row=5,pady=20)

            self.addent5=tk.Entry(self.root)
            self.addent5.grid(column=1,row=6,pady=20)

            self.addent6=tk.Entry(self.root)
            self.addent6.grid(column=1,row=7,pady=20)

            self.addent7=tk.Entry(self.root)
            self.addent7.grid(column=1,row=8,pady=20)

            self.addbut=tk.Button(self.root,text="CONFIRM",command=confirm5)
            self.addbut.grid(columnspan=2,row=9)

            
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------          






#------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#--------------
class dealer_main_page:

    def __init__(self,root,dn):
        self.root=root
        self.dn=dn
        self.initialize()
        

    def change(self,*args):
        self.tblname=self.var.get()
        a=self.var.get()
    
        

    def addpagefun(self):
        dealeradd=tk.Tk()
        app=dealer_add_page(dealeradd,self.tblname,self.dn)
        dealeradd.mainloop()

    def updatepagefun(self):
        dealerupdate=tk.Tk()
        app=dealer_update_page(dealerupdate,self.tblname,self.dn)
        dealerupdate.mainloop()

    def deletepagefun(self):
        dealerdelete=tk.Tk()
        app=dealer_delete_page(dealerdelete,self.tblname,self.dn)
        dealerdelete.mainloop()
              
           
 
  
    def initialize(self):

        #title
        self.title=tk.Label(self.root,text="WELCOME DEALER!",font=("Times New Roman",26))
        self.title.grid(columnspan=2,row=0)

        #title
        self.title=tk.Label(self.root,text="Select table ")
        self.title.grid(column=0,row=1,pady=30)
        
        #options drop down
        self.optionslist=["electronics","automobiles","books","movies","sports"]
        self.var=tk.StringVar(self.root)
        self.var.trace("w",self.change)
        self.optionmenu=tk.OptionMenu(self.root,self.var,self.optionslist[0],self.optionslist[1],self.optionslist[2],self.optionslist[3],self.optionslist[4])
        self.optionmenu.grid(column=1,row=1,pady=30)
        

        #add label and button

        self.but5=tk.Button(self.root,text="ADD",command=self.addpagefun)
        self.but5.grid(column=0,row=2,padx=30)
     
        #update label and button
        
        self.but6=tk.Button(self.root,text="UPDATE",command=self.updatepagefun)
        self.but6.grid(column=1,row=2,padx=30)

        #delete label and button

        self.but7=tk.Button(self.root,text="DELETE",command=self.deletepagefun)
        self.but7.grid(column=2,row=2,padx=30)


#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------       





class customer_main_page:

    def __init__(self,root,myresult,val1):
        self.root=root
        self.myresult=myresult
        self.val1=val1# use for if loop
        
        self.initialize()
        
    def initialize(self):
        self.txtbox=tk.Text(self.root,height=50,width=50)
        self.txtbox.grid(column=0,row=0)

        if self.val1=='electronics':
            for x in self.myresult:
                self.txtbox.insert(tk.INSERT,"\n Name:  %s \n Size: %s \n Price: %s \n Description: %s \n Contact details:  %s \n Dealer name:  %s  \n" % (x[2],x[3],x[4],x[5],x[6],x[8]))
          

        elif self.val1=='automobiles':
            for x in self.myresult:
                self.txtbox.insert(tk.INSERT,"\n Name: %s \n Model: %s \n Mileage: %s \n Price: %s \n Description: %s \n Contact details: %s \n Dealer name:  %s  \n" % (x[2],x[3],x[4],x[5],x[6],x[8],x[8]))
            
         
        elif self.val1=='books':
            for x in self.myresult:
                self.txtbox.insert(tk.INSERT,"\n Name:  %s  \n Price:  %s \n Description:  %s \n Contact details:  %s \n Dealer name:  %s  \n" % (x[2],x[3],x[4],x[5],x[7]))
            
         
        elif self.val1=='movies':
            for x in self.myresult:
                self.txtbox.insert(tk.INSERT,"\n Name:  %s  \n Price:  %s \n Description:  %s \n Contact details:  %s \n Dealer name:  %s  \n" % (x[2],x[3],x[4],x[5],x[7]))
         
                 
        elif self.val1=='electronics':
            for x in self.myresult:
                self.txtbox.insert(tk.INSERT,"\n Name:  %s \n Price: %s \n Size: %s \n Description: %s \n Contact details:  %s \n Dealer name:  %s  \n" % (x[2],x[3],x[4],x[5],x[6],x[8]))
          
        





        
    
#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------#-------------  



class main:

    def __init__(self,root):
        self.root=root
        self.initialize()

    def initialize(self):
        self.title=tk.Label(self.root,text="CUSTOMER DEALER INTERFACE",font=("Times New Roman",26))
        self.title.grid(columnspan=2,row=0)


        def customerclick():

                    
            def submit_click():#retrives txt from entry and validates with database and opens new tkinter window
                self.val1 = self.ent1.get()
                self.val2 = self.ent2.get()
                
                if self.val1 == '' or self.val2 == '':
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        
                else:
                    if self.val1=='automobiles' or self.val1=='electronics' or self.val1=='sports' or self.val1=='movies' or self.val1=='books' :
                        mycursor.execute("SELECT * FROM %s WHERE category='%s'" %(self.val1,self.val2))
                        myresult = mycursor.fetchall()
                        c=tk.Tk()
                        app=customer_main_page(c,myresult,self.val1)
                        c.mainloop()
                        
                                                
                    else:
                        tk.messagebox.showinfo("Warning", "Category not found")
                   
                 
            self.lab1=tk.Label(text="MAIN CATEGORY")
            self.lab1.grid(column=0,row=2,pady=30)
            
            self.lab2=tk.Label(text="SUB CATEGORY")
            self.lab2.grid(column=0,row=3,pady=30)

            self.but3=tk.Button(text="SUBMIT",command=submit_click)
            self.but3.grid(columnspan=2,row=4,pady=30)

            self.ent1=tk.Entry()
            self.ent1.grid(column=1,row=2,pady=30)
            
            self.ent2=tk.Entry()
            self.ent2.grid(column=1,row=3,pady=30)
           
    
        self.but1=tk.Button(self.root,text="customer",height=5,width=10)
        self.but1.grid(column=0,row=1)
        

        def dealerclick():

                    
            def submit_click():#retrives txt from entry and validates with database and opens new tkinter window
                self.val1 = self.ent1.get()
                self.val2 = self.ent2.get()
                if self.val1 == '' or self.val2 == '':
                    tk.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        
                else:
                    mycursor.execute("SELECT * FROM login")
                    myresult = mycursor.fetchall()
                    flag=0
                    for x in myresult:
                        if self.val1 and self.val2 in x:
                            flag=-1
                            dn=x[3]
                    if flag==-1:
                        dealer=tk.Tk()
                        app=dealer_main_page(dealer,dn)
                        dealer.mainloop()

                    else:
                        tk.messagebox.showinfo("Warning", "Creditinals not found")
                   
                 
            self.lab1=tk.Label(text="USERNAME")
            self.lab1.grid(column=0,row=2,pady=30)
            
            self.lab2=tk.Label(text="PASSWORD")
            self.lab2.grid(column=0,row=3,pady=30)

            self.but3=tk.Button(text="SUBMIT",command=submit_click)
            self.but3.grid(columnspan=2,row=4,pady=30)

            self.ent1=tk.Entry()
            self.ent1.grid(column=1,row=2,pady=30)
            
            self.ent2=tk.Entry()
            self.ent2.grid(column=1,row=3,pady=30)
           
    
        self.but1=tk.Button(self.root,text="customer",height=5,width=10,command=customerclick)#calls customer click
        self.but1.grid(column=0,row=1,padx=30)
        self.but2=tk.Button(self.root,text="dealer",height=5,width=10,command=dealerclick)#calls dealer click and initializes space for username and password
        self.but2.grid(column=1,row=1,padx=30)
        


x=tk.Tk()
app=main(x)
x.mainloop()
