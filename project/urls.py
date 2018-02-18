from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from home.views import home_view, venue_view, about_view
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from welcome.views import index, health
from django.http import HttpResponseRedirect

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', lambda r: HttpResponseRedirect('/aawedding/home/')),
    url(r'^health$', health),
    url(r'^aawedding/admin/', include(admin.site.urls)),
    url(r'^aawedding/home/$', home_view, name='home'),
    url(r'^aawedding/venue/$', login_required(venue_view), name='venue'),
    url(r'^aawedding/about/$', about_view, name='about'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
    url(r'aawedding/guest/', include('guest.urls')),
    url(r'aawedding/rsvp/', include('rsvp.urls')),
    #url(r'/', include('snowmaker.urls')),
    url(r'^', lambda r: HttpResponseRedirect('/aawedding/home/')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
