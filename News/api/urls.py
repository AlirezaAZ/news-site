from django.urls import path, include

app_name = 'app_api'

urlpatterns = [
    path('interface/', include('interface.urls')),
]
