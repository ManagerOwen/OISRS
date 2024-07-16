from django.shortcuts import render,redirect,HttpResponse
from tasapp.models import Tech Reg,Specialization,CustomUser,Hire,Page
import random
from datetime import datetime
from django.contrib import messages
def USERBASE(request):
    
    return render(request, 'userbase.html',context)

def Index(request):
    techview = TechReg.objects.all()
    page = Page.objects.all()

    context = {'techview': techview,
    'page':page,
    }
    return render(request, 'index.html',context)




def create_hire(request):
    techview = TechReg.objects.all()
    page = Page.objects.all()

    if request.method == "POST":
        hirenumber = random.randint(100000000, 999999999)
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        mobilenumber = request.POST.get('mobilenumber')
        date_of_hire = request.POST.get('date_of_hire')
        time_of_hire = request.POST.get('time_of_hire')
        tech_id = request.POST.get('tech_id')
        additional_msg = request.POST.get('additional_msg')

        # Retrieve the TechReg instance using the tech_id
        doc_instance = TechReg.objects.get(id=tech_id)

        # Validate that date_of_hire is greater than today's date
        try:
            hire_date = datetime.strptime(date_of_hire, '%Y-%m-%d').date()
            today_date = datetime.now().date()

            if hire_date <= today_date:
                # If the hire date is not in the future, display an error message
                messages.error(request, "Please select a date in the future for your hire")
                return redirect('hire')  # Redirect back to the hire page
        except ValueError:
            # Handle invalid date format error
            messages.error(request, "Invalid date format")
            return redirect('hire')  # Redirect back to the hire page

        # Create a new Hire instance with the provided data
        hiredetails = Hire.objects.create(
            hirenumber=hirenumber,
            fullname=fullname,
            email=email,
            mobilenumber=mobilenumber,
            date_of_hire=date_of_hire,
            time_of_hire=time_of_hire,
            tech_id=doc_instance,
            additional_msg=additional_msg
        )

        # Display a success message
        messages.success(request, "Your Hire Request Has Been Sent. We Will Contact You Soon")

        return redirect('hire')

    context = {'techview': techview,
    'page':page}
    return render(request, 'hire.html', context)


def User_Search_Hire(request):
    page = Page.objects.all()
    
    if request.method == "GET":
        query = request.GET.get('query', '')
        if query:
            # Filter records where fullname or Hire Number contains the query
            customer = Hire.objects.filter(fullname__icontains=query) | Hire.objects.filter(hirenumber__icontains=query)
            messages.info(request, "Search against " + query)
            context = {'customer': customer, 'query': query, 'page': page}
            return render(request, 'search-hire.html', context)
        else:
            print("No Record Found")
            context = {'page': page}
            return render(request, 'search-hire.html', context)
    
    # If the request method is not GET
    context = {'page': page}
    return render(request, 'search-hire.html', context)
def View_Hire_Details(request,id):
    page = Page.objects.all()
    customerdetails=Hire.objects.filter(id=id)
    context={'customerdetails':customerdetails,
    'page': page

    }

    return render(request,'user_hire-details.html',context)




