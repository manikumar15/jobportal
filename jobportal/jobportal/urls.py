from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.views.static import serve
from jobapp import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/',views.register),
    url(r'^loginview/',views.loginview),
    url(r'^login_in/',views.login_in),
    url(r'^aboutus/',views.aboutus),
    url(r'^jobpages/',views.jobpages),
    url(r'^jobs/',views.jobs),
    url(r'^apply_job/',views.apply_job),
    url(r'^$', views.search),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)