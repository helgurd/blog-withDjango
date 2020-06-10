
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^about/$',views.about ),
    url(r'^$',views.homepage),
    url(r'^contactme/$',views.contactme),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)