from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'home/',views.Index,name='index'),
    url(r'^register/',views.Register,name="register"),
    url(r'^login/',views.user_login,name="login"),
    url(r'^playgame/',views.playgame.as_view(),name="playgame"),
    url(r'^post/(?P<username>[-\w]+)/$',views.Post.as_view(),name='post'),
    # url(r'^playgame2/',views.playgame2.as_view(),name="playgame2"),
    url(r'^insidepageonlyforme/',views.insidepage,name='insidepage'),
    url(r'^comment/(?P<username>[-\w]+)/(?P<title_slug>[-\w]+)/$',views.Comments_Create.as_view(),name='comments_creates'),
    url(r'ListenMusicByCtg/',views.MusicList.as_view(),name='music'),
    url(r'musicuploadby/(?P<username>[-\w]+)/',views.MusicCreate.as_view(),name="upload"),
    url(r'music_search/',views.MusicSearch,name='music_search'),
    url(r'logout/',views.LogoutView,name='logout'),
    url(r'dedication/',views.Dedicate,name='dedicate')






]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)