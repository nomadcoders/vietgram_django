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
    url(r'^admin/', admin.site.urls),
]
