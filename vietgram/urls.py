from django.conf.urls import url
from django.contrib import admin
from users import views as user_views

urlpatterns = [
    url(
        regex=r'^$',
        view=user_views.index,
        name='index'
    ),
    url(
        regex=r'^login/$',
        view=user_views.login,
        name='login'
    ),
    url(
        regex=r'^explore/$',
        view=user_views.explore,
        name='explore'
    ),
    url(
        regex=r'^profile/$',
        view=user_views.profile,
        name='profile'
    ),
    url(r'^admin/', admin.site.urls),
]
