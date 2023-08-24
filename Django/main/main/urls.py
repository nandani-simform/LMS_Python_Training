from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('stuinfo/<int:pk>', views.student_detail, name='student-detail'),
    path('stuinfo/', views.student_detail_list, name='student-detail-list'),
    # path('studentapi/', views.StudentAPI.as_view() , name='student-api'),
    
    path('studentapi/', views.hello ),
    path('admin/', admin.site.urls),
]
 