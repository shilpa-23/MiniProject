from django.conf.urls import url
from uploadfile import views


urlpatterns=[
    url('^$',views.upload,name="upload"),
    url('^down1',views.downl,name="dowe1"),



]