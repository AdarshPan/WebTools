from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 url(r'lo',views.DiagnoseXray,name="Diagnosis"),
 url(r'login/',views.loginView,name="login_view"),
 # url('<int:pk>/', views.prediction, name='gwen'),
url('', views.prediction, name='prediction'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)