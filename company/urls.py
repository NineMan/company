from django.contrib import admin
from django.urls import path, include

from company.yasg import urlpattern as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', include('staff.urls')),  # new
]

urlpatterns += doc_urls
