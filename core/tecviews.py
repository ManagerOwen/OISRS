from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from tasapp.models import TechReg,Specialization,CustomUser,Hire
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime


def TECSIGNUP(request):
    specialization = Specialization.objects.all()
    if request.method == "POST":
        pic = request.FILES.get('pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobno = request.POST.get('mobno')
        specialization_id = request.POST.get('specialization_id')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email already exist')
            return redirect('techSignup')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exist')
            return redirect('techSignup')
        else:
            user = CustomUser(
               first_name=first_name,
               last_name=last_name,
               username=username,
               email=email,
               user_type=2,
               profile_pic = pic,
            )
            user.set_password(password)
            user.save()
            spid =Specialization.objects.get(id=specialization_id)
            tech = TechReg(
                admin = user,
                
                mobilenumber = mobno,
                specialization_id = spid,
                
            )
            tech.save()            
            messages.success(request,'Signup Successfully')
            return redirect('tecSignup')
    
    context = {
        'specialization':specialization
    }

    return render(request,'tec/tecreg.html',context)

@login_required(login_url='/')
def TECHHOME(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    allaptcount = Hire.objects.filter(tech_id=tech_reg).count
    newaptcount = Hire.objects.filter(status='0',tech_id=tech_reg).count
    appaptcount = Hire.objects.filter(status='Approved',tech_id=tech_reg).count
    canaptcount = Hire.objects.filter(status='Cancelled',tech_id=tech_reg).count
    comaptcount = Hire.objects.filter(status='Completed',tech_id=tech_reg).count
    context = {
        'newaptcount':newaptcount,
        'allaptcount':allaptcount,
        'appaptcount':appaptcount,
        'canaptcount':canaptcount,
        'comaptcount':comaptcount        


    }
    return render(request,'tec/techome.html',context)



def View_Hire(request):
    try:
        tech_admin = request.user
        tech_reg = TechReg.objects.get(admin=tech_admin)
        view_Hire = Hire.objects.filter(tech_id=tech_reg)
        

        # Pagination
        paginator = Paginator(view_Hire, 5)  # Show 10 Hire per page
        page = request.GET.get('page')
        try:
            view_Hire = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            view_Hire = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            view_Hire = paginator.page(paginator.num_pages)

        context = {'view_Hire': view_Hire}
    except Exception as e:
        # Handle exceptions, such as database errors, gracefully
        context = {'error_message': str(e)}

    return render(request, 'tec/view_Hire.html', context)


def Customer_Hire_Details(request,id):
    customerdetails=Hire.objects.filter(id=id)
    context={'customerdetails':customerdetails

    }

    return render(request,'tec/customer_Hire_details.html',context)


def Customer_Hire_Details_Remark(request):
    if request.method == 'POST':
        customer_id = request.POST.get('pat_id')
        remark = request.POST['remark']
        status = request.POST['status']
        customeraptdet = Hire.objects.get(id=customer_id)
        customeraptdet.remark = remark
        customeraptdet.status = status
        customeraptdet.save()
        messages.success(request,"Status Update successfully")
        return redirect('view_Hire')
    context ={
        
    }
    return render(request,'tec/view_Hire.html',context)

def Customer_Approved_Hire(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    customerdetails1 = Hire.objects.filter(status='Approved',tech_id=tech_reg)
    context = {'customerdetails1': customerdetails1}
    return render(request, 'tec/customer_app_Hire.html', context)

def Customer_Cancelled_Hire(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    customerdetails1 = Hire.objects.filter(status='Cancelled',tech_id=tech_reg)
    context = {'customerdetails1': customerdetails1}
    return render(request, 'tec/customer_app_Hire.html', context)

def Customer_New_Hire(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    customerdetails1 = Hire.objects.filter(status='0',tech_id=tech_reg)
    context = {'customerdetails1': customerdetails1}
    return render(request, 'tec/customer_app_Hire.html', context)

def Customer_List_Approved_Hire(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    customerdetails1 = Hire.objects.filter(status='Approved',tech_id=tech_reg)
    context = {'customerdetails1': customerdetails1}
    return render(request, 'tec/customer_list_app_Hire.html', context)

def TechHireList(request,id):
    customerdetails=Hire.objects.filter(id=id)
    context={'customerdetails':customerdetails

    }

    return render(request,'tec/tech_Hire_list_details.html',context)

def Customer_Hire_Prescription(request):
    if request.method == 'POST':
        customer_id = request.POST.get('pat_id')
        prescription = request.POST['prescription']
        recommendedtest = request.POST['recommendedtest']
        status = request.POST['status']
        customeraptdet = Hire.objects.get(id=customer_id)
        customeraptdet.prescription = prescription
        customeraptdet.recommendedtest = recommendedtest
        customeraptdet.status = status
        customeraptdet.save()
        messages.success(request,"Status Update successfully")
        return redirect('view_Hire')
    context={}
    return render(request,'tec/customer_list_app_Hire.html',context)


def Customer_Hire_Completed(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    customerdetails1 = Hire.objects.filter(status='Completed',tech_id=tech_reg)
    context = {'customerdetails1': customerdetails1}
    return render(request, 'tec/customer_list_app_Hire.html', context)

def Search_Hire(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    if request.method == "GET":
        query = request.GET.get('query', '')
        if query:
            # Filter records where fullname or Hire Number contains the query
            customer = Hire.objects.filter(fullname__icontains=query) | Hire.objects.filter(hirenumber__icontains=query) & Hire.objects.filter(tech_id=tech_reg)
            messages.success(request, "Search against " + query)
            return render(request, 'tec/search-Hire.html', {'customer': customer, 'query': query})
        else:
            print("No Record Found")
            return render(request, 'tec/search-Hire.html', {})

def Between_Date_Report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    customer = []
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)

    if start_date and end_date:
        # Validate the date inputs
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'tec/between-dates-report.html', {'error_message': 'Invalid date format'})

        # Filter Hire between the given date range
        customer = Hire.objects.filter(created_at__range=(start_date, end_date)) & Hire.objects.filter(tech_id=tech_reg)

    return render(request, 'tec/between-dates-report.html', {'customer': customer,'start_date':start_date,'end_date':end_date})
