from django.urls import path,include
from . import views 


urlpatterns = [
    # path('login/',views.login_view,name = 'employee_login'),
    
    path('', views.employee_forms,name='employee_insert'),
    path('list/',views.employee_list,name='employee_list'),
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('<int:id>/', views.employee_forms,name= 'employee_update'),
]
