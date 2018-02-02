from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from home.views import home_view
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from welcome.views import index, health
from django.http import HttpResponseRedirect

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', lambda r: HttpResponseRedirect('home/')),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', home_view, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
    url(r'guest/', include('guest.urls')),
    url(r'rsvp/', include('rsvp.urls')),
    #url(r'/', include('snowmaker.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
