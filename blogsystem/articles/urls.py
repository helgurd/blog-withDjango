from django.conf.urls import url
from . import views

app_name= 'articles' #this is only  space naming for not to conflict with other apps urls wich could have same name url
#you have to add app_name = ' articles' to the url  in article_list.html
urlpatterns = [
    url(r'^$',views.article_list,name= 'list'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name = 'detail')

]
