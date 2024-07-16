from django.contrib import admin
from django.urls import path
from .import views,adminviews,tecviews,userviews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('login', views.LOGIN, name='login'),
    
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    # This is admin panel
    # path('Admin/AdminHome', adminviews.ADMINHOME, name='admin_home'),
    # path('Admin/Specialization', adminviews.SPECIALIZATION, name='add_specilizations'),
    # path('Admin/ManageSpecialization', adminviews.MANAGESPECIALIZATION, name='manage_specilizations'),
    # path('Admin/DeleteSpecialization/<str:id>', adminviews.DELETE_SPECIALIZATION, name='delete_specilizations'),
    # path('UpdateSpecialization/<str:id>', adminviews.UPDATE_SPECIALIZATION, name='update_specilizations'),
    # path('UPDATE_Specialization_DETAILS', adminviews.UPDATE_SPECIALIZATION_DETAILS, name='update_specilizations_details'),
    # path('Admin/TechList', adminviews.TechList, name='viewtechlist'),
    # path('Admin/ViewTechDetails/<str:id>', adminviews.ViewtechDetails, name='viewTechdetails'),
    # path('Admin/ViewTechHireList/<str:id>', adminviews.ViewtechHireList, name='viewTechhirelist'),
    # path('Admin/ViewCustomertDetails/<str:id>', adminviews.ViewCustomertDetails, name='viewcustomertdetails'),
    # path('SearchTech', adminviews.Search_Tech, name='search_tech'),

    # path('TechBetweenDateReport', adminviews.Tech_Between_Date_Report, name='tech_between_date_report'),

    # #Website Page
    #  path('Website/update', adminviews.WEBSITE_UPDATE, name='website_update'),
    #  path('UPDATE_WEBSITE_DETAILS', adminviews.UPDATE_WEBSITE_DETAILS, name='update_website_details'),

    # # This is Tech Panel
    path('techSignup/', tecviews.TECSIGNUP, name='techSignup'),
    # path('Tech/tecHome', tecviews.TECHHOME, name='Tech_home'),
    # path('Tech/ViewHire', tecviews.View_Hire, name='view_hire'),
    # path('TechCustomertHireDetails/<str:id>', tecviews.Customert_Hire_Details, name='customerthiredetails'),
    # path('HireDetailsRemark/Update', tecviews.Customert_Hire_Details_Remark, name='customert_hire_details_remark'),
    #  path('TechCustomertApprovedHire', tecviews.Customert_Approved_Hire, name='customertapprovedhire'),
    #  path('TechCustomertCancelledHire', tecviews.Customert_Cancelled_hire, name='customertcancelledhire'),
    #  path('TechCustomertNewHire', tecviews.Customert_New_hire, name='customertnewhire'),
    #  path('TechCustomertListApprovedHire', tecviews.Customert_List_Approved_Hire, name='customertlisthire'),
    #  path('TechHireList/<str:id>', tecviews.TechHireList, name='techhirelist'),
    #  path('CustomertHirePrescription', tecviews.Customert_Hire_Prescription, name='customerthireprescription'),
    #   path('CustomertHireCompleted', tecviews.Customert_Hire_Completed, name='customerthirecompleted'),
    #   path('SearchHire', tecviews.Search_Hire, name='search_hire'),
    #   path('BetweenDateReport', tecviews.Between_Date_Report, name='between_date_report'),

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
