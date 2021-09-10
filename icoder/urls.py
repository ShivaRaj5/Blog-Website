from django.conf.urls import include
from django.contrib import admin
from django.urls import path
admin.site.site_header="iCoder Admin"
admin.site.site_title="iCoder"
admin.site.index_title="Welcome to iCoder admin panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls'))
]