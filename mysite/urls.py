from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^', include('myblog.urls')),
    url(r'^login/$',
        login,
        {'template_name': 'login.html'},
        name="login"),
    url(r'^logout/$',
        logout,
        {'next_page': '/'},
        name="logout"),
    url(r'^admin/', include(admin.site.urls)),
]
