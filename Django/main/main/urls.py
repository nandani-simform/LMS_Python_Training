from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns



router = DefaultRouter()
router.register('studentapi', views.StudentViewSets, basename='student')
# router.register('studentapi', views.StudentModelViewSets, basename='student')



urlpatterns = [
    # path('stuinfo/<int:pk>', views.student_detail, name='student-detail'),
    # path('stuinfo/', views.student_detail_list, name='student-detail-list'),

    # # # CBV
    # path('studentapi/', views.StudentAPI.as_view() ),
    # path('studentapi/<int:pk>', views.StudentAPI.as_view()),
    
    #FBV
    # path('studentapi/', vie,
    # path('studentapi/<int:pk>', views.studenws.student_api )t_api ),

    # generic view 
    # path('studentapi/', views.LCStudent.as_view()),
    # path('studentapi/<int:pk>', views.RUDStudentRetrive.as_view()),

    # # concrete view
    # path('studentapi/', views.StudentListCreate.as_view()),
    # # path('studentapi/', views.StudentCreate.as_view()),
    # # path('studentapi/<int:pk>/', views.StudentRetrive.as_view()),
    # # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
    # # path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetriveUpdateDestroy.as_view()),


    # viewsets
    path('', include(router.urls)),

    path('admin/', admin.site.urls),

]

