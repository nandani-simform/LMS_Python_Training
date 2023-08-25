from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    # path('stuinfo/<int:pk>', views.student_detail, name='student-detail'),
    # path('stuinfo/', views.student_detail_list, name='student-detail-list'),

    # # CBV
    # path('studentapi/', views.StudentAPI.as_view() ),
    # path('studentapi/<int:pk>', views.StudentAPI.as_view()),
    
    #FBV
    # path('studentapi/', views.student_api ),
    # path('studentapi/<int:pk>', views.student_api ),

    # generic view 
    # path('studentapi/', views.LCStudent.as_view()),
    # path('studentapi/<int:pk>', views.RUDStudentRetrive.as_view()),

    # concrete view
    path('studentapi/', views.StudentListCreate.as_view()),
    # path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrive.as_view()),
    # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetriveUpdateDestroy.as_view()),


    path('admin/', admin.site.urls),

]
 
