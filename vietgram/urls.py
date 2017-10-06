from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
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
    url(r'^admin/', admin.site.urls),
    url(
        regex=r'^(?P<username_from_url>.+)/$',
        view=user_views.profile,
        name='profile'
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
