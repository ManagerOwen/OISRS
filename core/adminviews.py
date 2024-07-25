from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from tasapp.models import Specialization,TechReg,Hire,Page,CustomUser
from django.contrib import messages
from datetime import datetime

@login_required(login_url='/')
def ADMINHOME(request):
    user = CustomUser.objects.all()
    tech_count = TechReg.objects.all().count
    specialization_count = Specialization.objects.all().count
    context = {
        'tech_count':tech_count,
        'user': user,
        'specialization_count':specialization_count,

    } 
    return render(request,'admin/adminhome.html',context)

@login_required(login_url='/')
def SPECIALIZATION(request):
    if request.method == "POST":
        specializationname = request.POST.get('specializationname')
        specialization =Specialization(
            sname=specializationname,
        )
        specialization.save()
        messages.success(request,'Specialization  Added Succeesfully!!!')
        return redirect("add_specilizations")
    return render(request,'admin/specialization.html')

@login_required(login_url='/')
def MANAGESPECIALIZATION(request):
    specialization = Specialization.objects.all()
    context = {'specialization':specialization,

    }
    return render(request,'admin/manage_specialization.html',context)

def DELETE_SPECIALIZATION(request,id):
    specialization = Specialization.objects.get(id=id)
    specialization.delete()
    messages.success(request,'Record Delete Succeesfully!!!')
    
    return redirect('manage_specilizations')

login_required(login_url='/')
def UPDATE_SPECIALIZATION(request,id):
    specialization = Specialization.objects.get(id=id)
    
    context = {
         'specialization':specialization,
    }

    return render(request,'admin/update_specialization.html',context)

login_required(login_url='/')

def UPDATE_SPECIALIZATION_DETAILS(request):
        if request.method == 'POST':
          sep_id = request.POST.get('sep_id')
          sname = request.POST.get('sname')
          sepcialization = Specialization.objects.get(id=sep_id) 
          sepcialization.sname = sname
          sepcialization.save()   
          messages.success(request,"Your specialization detail has been updated successfully")
          return redirect('manage_specilizations')
        return render(request, 'admin/update_specialization.html')

@login_required(login_url='/')
def TechList(request):
    techlist = TechReg.objects.all()
    context = {'techlist':techlist,

    }
    return render(request,'admin/tech-list.html',context)

def ViewTechDetails(request,id):
    techlist1=TechReg.objects.filter(id=id)
    context={'techlist1':techlist1

    }

    return render(request,'admin/tech-details.html',context)

def ViewTechHireList(request,id):
    customerdetails=Hire.objects.filter(tech_id=id)
    context={'customerdetails':customerdetails

    }

    return render(request,'admin/tech_hire_list.html',context)

def New_Hire(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    clientdetails = Hire.objects.filter(status='0',tech_id=tech_reg)
    context = {'clientdetails': clientdetails}
    return render(request, 'admin/new_hire.html', context)

def Approved_Hire(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    clientdetails = Hire.objects.filter(status='Approved',tech_id=tech_reg)
    context = {'clientdetails': clientdetails}
    return render(request, 'admin/approved_hire.html', context)

def Cancelled_Hire(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    clientdetails = Hire.objects.filter(status='Cancelled',tech_id=tech_reg)
    context = {'clientdetails': clientdetails}
    return render(request, 'admin/cancelled_hire.html', context)

def All_Hire(request):
    clientdetails = Hire.objects.all()
    context = {'clientdetails': clientdetails}
    return render(request, 'admin/all_hire.html', context)

def Completed_Hire(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    clientdetails = Hire.objects.filter(status='Completed',tech_id=tech_reg)
    context = {'clientdetails': clientdetails}
    return render(request, 'admin/completed_hire.html', context)

def Client_List(request):
    tech_admin = request.user
    tech_reg = TechReg.objects.get(admin=tech_admin)
    clientdetails = Hire.objects.filter(status='0',tech_id=tech_reg)
    context = {'clientdetails': clientdetails}
    return render(request, 'admin/client_list.html', context)

def ViewCustomerDetails(request,id):
    customerdetails=Hire.objects.filter(id=id)
    context={'customerdetails':customerdetails
    }
    return render(request,'admin/customer_hire_details.html',context)

def Search_Technician(request):
    if request.method == "GET":
        query = request.GET.get('query', '')
        if query:
            # Filter records where email or mobilenumber contains the query
            searchdoc = TechReg.objects.filter(mobilenumber__icontains=query) | TechReg.objects.filter(admin__first_name__icontains=query) |TechReg.objects.filter(admin__last_name__icontains=query)
            messages.info(request, "Search against " + query)
            return render(request, 'admin/search-tech.html', {'searchdoc': searchdoc, 'query': query})
        else:
            print("No Record Found")
            return render(request, 'admin/search-tech.html', {})

def Search_Hire(request):
    if request.method == "GET":
        query = request.GET.get('query', '')
        if query:
            # Filter records where email or mobilenumber contains the query
            searchdoc = TechReg.objects.filter(mobilenumber__icontains=query) | TechReg.objects.filter(admin__first_name__icontains=query) |TechReg.objects.filter(admin__last_name__icontains=query)
            messages.info(request, "Search against " + query)
            return render(request, 'admin/search-tech.html', {'searchdoc': searchdoc, 'query': query})
        else:
            print("No Record Found")
            return render(request, 'admin/search-tech.html', {})

def Tech_Between_Date_Report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    tech = []
    if start_date and end_date:
        # Validate the date inputs
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'admin/tech-between-date.html', {'tech': tech, 'error_message': 'Invalid date format'})

        # Filter visitors between the given date range
        tech = TechReg.objects.filter(regdate_at__range=(start_date, end_date))

    return render(request, 'admin/tech-between-date.html', {'tech': tech,'start_date':start_date,'end_date':end_date})


@login_required(login_url='/')
def WEBSITE_UPDATE(request):
    page = Page.objects.all()
    context = {"page":page,

    }
    return render(request,'admin/website.html',context)

@login_required(login_url='/')
def UPDATE_WEBSITE_DETAILS(request):
    if request.method == 'POST':
          web_id = request.POST.get('web_id')
          pagetitle = request.POST['pagetitle']
          address = request.POST['address']
          aboutus = request.POST['aboutus']
          email = request.POST['email']
          mobilenumber = request.POST['mobilenumber']
          page =Page.objects.get(id=web_id)
          page.pagetitle = pagetitle
          page.address = address
          page.aboutus = aboutus
          page.email = email
          page.mobilenumber = mobilenumber
          page.save()
          messages.success(request,"Your website detail has been updated successfully")
          return redirect('website_update')
    return render(request,'admin/website.html')

