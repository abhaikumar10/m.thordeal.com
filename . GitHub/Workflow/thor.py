#takes name,email and message and save it to text file
def save():
        f=open("information.txt","a+") #location of file
        name=input('enter name :')
        email=input("enter mail:")
        msg=input("enter message:")
        #creating file
        f.write("\n"+"Name- "+name+"  ")
        f.write("E-Mail- "+email+"  ")
        f.write("Message- "+msg)
        f.close()
