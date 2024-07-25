from django.contrib import admin
from django.urls import path
from .import views,adminviews,tecviews,userviews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('login', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    # This is admin panel
    path('Admin/admin', adminviews.ADMINHOME, name='admin_home'),
    path('Admin/specialization', adminviews.SPECIALIZATION, name='add_specilizations'),
    path('Admin/manageSpecialization', adminviews.MANAGESPECIALIZATION, name='manage_specilizations'),
    path('Admin/deleteSpecialization/<str:id>', adminviews.DELETE_SPECIALIZATION, name='delete_specilizations'),
    path('Admin/update_specialization/<str:id>', adminviews.UPDATE_SPECIALIZATION, name='update_specilizations'),
    path('Admin/update_specialization_detials', adminviews.UPDATE_SPECIALIZATION_DETAILS, name='update_specilizations_details'),
    path('Admin/technicians', adminviews.TechList, name='technician_list'),
    path('Admin/view_tech_details/<str:id>', adminviews.ViewTechDetails, name='view_tech_details'),
    path('Admin/view_tech_hire_list/<str:id>', adminviews.ViewTechHireList, name='viewTechhirelist'),
    path('Admin/view_customert_details/<str:id>', adminviews.ViewCustomerDetails, name='viewcustomertdetails'),
    path('Admin/newhire', adminviews.New_Hire, name='new_hire'),
    path('Admin/approvedhire', adminviews.Approved_Hire, name='approved_hire'),
    path('Admin/cancelledhire', adminviews.Cancelled_Hire, name='cancelled_hire'),
    path('Admin/allhire', adminviews.All_Hire, name='all_hire'),
    path('Admin/completedhire', adminviews.Completed_Hire, name='completed_hire'),
    path('Admin/bdhirereport', adminviews.Tech_Between_Date_Report, name='bd_hire_report'),
    path('Admin/searchtechnician', adminviews.Search_Technician, name='search_technician'),
    path('Admin/website_update', adminviews.WEBSITE_UPDATE, name='website_update'),
    path('Admin/update_website_details', adminviews.UPDATE_WEBSITE_DETAILS, name='update_website_details'),

    # # This is Technician Panel
    path('dashboard/signup/', tecviews.TECSIGNUP, name='techSignup'),
    path('dashboard/home', tecviews.TECHHOME, name='tech_home'),
    path('dashboard/view_hire', tecviews.View_Hire, name='view_hire'),
    path('dashboard/tech_hire_details/<str:id>', tecviews.Tech_Hire_Details, name='techdetails'),
    path('dashboard/Remark_Update', tecviews.Tech_Hire_Details_Remark, name='tech_hire_details_remark'),
    path('dashboard/new', tecviews.Tech_New_Hire, name='newhire'),
    path('dashboard/approved', tecviews.Tech_Approved_Hire, name='approvedhire'),
    path('dashboard/cancelled', tecviews.Tech_Cancelled_Hire, name='cancelledhire'),
    path('dashboard/all_hire', tecviews.Tech_All_Hire, name='allhire'),
    path('dashboard/clients', tecviews.All_Clients, name='clientlist'),
    path('dashboard/completed', tecviews.Tech_Hire_Completed, name='completedhire'),
    path('dashboard/tech_hire_list/<str:id>', tecviews.TechHireList, name='techhirelist'),
    path('dashboard/tech_hire_description', tecviews.Tech_Hire_Description, name='techhiredescription'),
    path('dashboard/search_hire', tecviews.Search_Hire, name='search_hire'),
    path('dashboard/tech_between_date_report', tecviews.Between_Date_Report, name='between_date_report'),

    #This is User Panel
    path('userbase/', userviews.USERBASE, name='userbase'),
    path('', userviews.Index, name='index'),
    path('userhire/', userviews.create_hire, name='hire'),
    path('User_SearchHire', userviews.User_Search_Hire, name='user_search_hire'),
    path('ViewHireDetails/<str:id>/', userviews.View_Hire_Details, name='viewhiredetails'),
    #profile path
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),
    path('Password', views.CHANGE_PASSWORD, name='change_password')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
