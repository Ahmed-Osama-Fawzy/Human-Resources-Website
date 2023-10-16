from django.shortcuts import render
from datetime import datetime
from .models import XUsers , Emplooyes , HRs , Vactions

# For Controlling Side

def index(request):
    return render(request,'Board.html',{'title':'Board Page' , 'User':'Public'})

def Main(request):
    return render(request,'main.html',{'title':'Main Page' , 'User':'Public'})

def Login(request):
    Username = request.POST.get("Username")
    Password = request.POST.get("Password")
    data = XUsers.objects.all()
    for One in data:
        if One.Username == Username and One.Password == Password:
            if One.Type == True:
                print("Manager")
                return render(request,'manager-home.html',{'title':'Manager Home Page' , 'User':'Owner'})
            else:
                print("HR")
                return render(request,'admin-home.html',{'title':'Admin Home Page' , 'User':'Admin'})
    return render(request,'login.html',{'title':'Login Page' , 'User':'Public'})

def ForgetPassword(request):
    return render(request,'forget-password.html',{'title':'Forget Password Page' , 'User':'Public'})

def OTP(request):
    return render(request,'OTP.html',{'title':'OTP Page' , 'User':'Public'})


# For Only Admin Side


def AdminHome(request):
    return render(request,'admin-home.html',{'title':'Admin Home Page' , 'User':'Admin'})

def AddEmploee(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        Mobile = request.POST.get("Mobile")
        Address = request.POST.get("Address")
        Email = request.POST.get("Email")
        Salary = request.POST.get("Salary")
        Birthdate = request.POST.get("Birthdate")
        Department = request.POST.get("Department")
        Gender = request.POST.get("Gender")
        Mstatue = request.POST.get("Mstatue")
        Insert = Emplooyes(Username=Username,Mobile=Mobile,Address=Address,Email=Email,Birthdate=Birthdate,Salary=Salary,Department=Department,Gender=Gender,Mstatue=Mstatue)
        Insert.save()
    return render(request,'add-emploee.html',{'title':'Add Emploee Page' , 'User':'Admin'})

def UpdateEmploee(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        Mobile = request.POST.get("Mobile")
        Address = request.POST.get("Address")
        Email = request.POST.get("Email")
        Salary = request.POST.get("Salary")
        Birthdate = request.POST.get("Birthdate")
        Gender = request.POST.get("Gender")
        Mstatue = request.POST.get("Mstatue")
        Department = request.POST.get("Department")
        Update = Emplooyes
        if Mobile:
            Update.objects.filter(Username=Username).update(Mobile=Mobile)
        if Department:
            Update.objects.filter(Username=Username).update(Department=Department)
        if Address:
            Update.objects.filter(Username=Username).update(Mobile=Mobile)
        if Email:
            Update.objects.filter(Username=Username).update(Email=Email)
        if Salary:
            Update.objects.filter(Username=Username).update(Salary=Salary)
        if Birthdate:
            Update.objects.filter(Username=Username).update(Birthdate=Birthdate)
        if Gender:
            Update.objects.filter(Username=Username).update(Gender=Gender)
        if Mstatue:
            Update.objects.filter(Username=Username).update(Mstatue=Mstatue)
    return render(request,'update-emploee.html',{'title':'Update Emploee Page' , 'User':'Admin'})

def RemoveEmploee(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        Emplooyes.objects.filter(Username=Username).delete()
    return render(request,'remove-emploee.html',{'title':'Remove Emploee Page' , 'User':'Admin'})

def OrderVaction(request):
    if request.method  == "POST":
        EmployeeUsername = request.POST.get("EmployeeUsername")
        EmployeeDepartment = request.POST.get("EmployeeDepartment")
        Startdate = request.POST.get("Startdate")
        Enddate = request.POST.get("Enddate")
        Reason = request.POST.get("Reason")
        if Emplooyes.objects.filter(Username=EmployeeUsername)[0].AviVacdays > 0:
            Insert = Vactions(EmployeeUsername=EmployeeUsername,EmployeeDepartment=EmployeeDepartment,Startdate=Startdate,Enddate=Enddate,Reason=Reason)
            Insert.save() 
        elif HRs.objects.filter(Username=EmployeeUsername)[0].AviVacdays > 0:
            Insert = Vactions(EmployeeUsername=EmployeeUsername,EmployeeDepartment=EmployeeDepartment,Startdate=Startdate,Enddate=Enddate,Reason=Reason)
            Insert.save()    
    return render(request,'order-vaction.html',{'title':'Order Vaction Page' , 'User':'Admin'})


# For Only Owner Side


def ManagerHome(request):
    return render(request,'manager-home.html',{'title':'Manager Home Page' , 'User':'Owner'})

def AcceptionVactions(request):
    if request.method == 'POST':
        Id = request.POST.get("Id")
        Aboveness = request.POST.get("Aboveness")
        if Aboveness == 'Above':
            Vactions.objects.filter(id=Id).update(Statues='Aboved')
            Username = Vactions.objects.filter(id=Id)[0].EmployeeUsername
            if Emplooyes.objects.filter(Username=Username):
                Num = Emplooyes.objects.filter(Username=Username)[0].AviVacdays
                Emplooyes.objects.filter(Username=Username).update(AviVacdays=Num-1)
                print(Num)
            else:
                Num = HRs.objects.filter(Username=Username)[0].AviVacdays
                HRs.objects.filter(Username=Username).update(AviVacdays=Num-1)
                print(Num)
        else:
            Vactions.objects.filter(id=Id).update(Statues='Rejected')
    data = Vactions.objects.all()
    return render(request,'acception-vactions.html',{'title':'Acception Vactions Page' , 'User':'Owner','data':data})

def AddHR(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        Mobile = request.POST.get("Mobile")
        Address = request.POST.get("Address")
        Email = request.POST.get("Email")
        Salary = request.POST.get("Salary")
        Birthdate = request.POST.get("Birthdate")
        Gender = request.POST.get("Gender")
        Mstatue = request.POST.get("Mstatue")
        SInsert = XUsers(Username=Username,Password=Password,Type=False)
        Insert = HRs(Username=Username,Password=Password,Mobile=Mobile,Address=Address,Email=Email,Birthdate=Birthdate,Salary=Salary,Gender=Gender,Mstatue=Mstatue)
        SInsert.save()
        Insert.save()
    return render(request,'add-hr.html',{'title':'Add HR Page' , 'User':'Owner'})

def UpdateHR(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        Mobile = request.POST.get("Mobile")
        Address = request.POST.get("Address")
        Email = request.POST.get("Email")
        Salary = request.POST.get("Salary")
        Birthdate = request.POST.get("Birthdate")
        Gender = request.POST.get("Gender")
        Mstatue = request.POST.get("Mstatue")
        Update = HRs
        if Mobile:
            Update.objects.filter(Username=Username).update(Mobile=Mobile)
        if Address:
            Update.objects.filter(Username=Username).update(Mobile=Mobile)
        if Email:
            Update.objects.filter(Username=Username).update(Email=Email)
        if Salary:
            Update.objects.filter(Username=Username).update(Salary=Salary)
        if Birthdate:
            Update.objects.filter(Username=Username).update(Birthdate=Birthdate)
        if Gender:
            Update.objects.filter(Username=Username).update(Gender=Gender)
        if Mstatue:
            Update.objects.filter(Username=Username).update(Mstatue=Mstatue)
    return render(request,'update-hr.html',{'title':'Update HR Page' , 'User':'Owner'})

def RemoveHR(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        HRs.objects.filter(Username=Username).delete()
        XUsers.objects.filter(Username=Username).delete()
    return render(request,'remove-hr.html',{'title':'Remove HR Page' , 'User':'Owner'})

def ShowHRs(request):
    if request.method  == "POST":
        Action = request.POST.get("Action")
        Id = request.POST.get("Id")
        if Action == 'Modify':
            pass
        elif Action == 'Remove':
            pass
        else:
            pass
    data = HRs.objects.all()
    return render(request,'show-hrs.html',{'title':'Show HRs Page' , 'User':'Owner','data':data})

# For Both Owner & HR Employee

def ShowEmploees(request):
    if request.method  == "POST":
        Action = request.POST.get("Action")
        Id = request.POST.get("Id")
        if Action == 'Modify':
            pass
        elif Action == 'Remove':
            pass
        else:
            pass
    data = Emplooyes.objects.all()
    return render(request,'show-emploees.html',{'title':'Show Emploees Page' , 'User':'Public','data':data})

def ModifyPassword(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        OldPassword = request.POST.get("Oldpass")
        NewPassword = request.POST.get("Newpass")
        RenewPassword = request.POST.get("Renewpass")
        data = XUsers.objects.all()
        for One in data:
            if One.Username == Username and One.Password == OldPassword:
                if NewPassword == RenewPassword:
                    Insert = XUsers.objects.filter(Username=Username).update(Password=NewPassword)
                    Type = XUsers.objects.filter(Username=Username)[0].Type
                    if Type == False:
                        Insert = HRs.objects.filter(Username=Username).update(Password=NewPassword)
    return render(request,'modify-password.html',{'title':'Modify Password Page' , 'User':'Public'})

def ShowVactions(request):
    data = Vactions.objects.all()
    return render(request,'show-vactions.html',{'title':'Show Vactions Page' , 'User':'Public','data':data})