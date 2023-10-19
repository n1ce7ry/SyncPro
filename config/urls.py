from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("__debug__/", include("debug_toolbar.urls")),
    
    path('', include('dashboard.urls')),
    path('login/', include('authorization.urls')),
    path('tasks/', include('tasks.urls')),
    path('applications/', include('applications.urls')),
    path('clients/', include('clients.urls')),
    path('finance/', include('finance.urls')),
    path('settings/', include('settings.urls')),
]
