from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^show$', views.show.as_view(), name='showCD'),
    url(r'^add$', views.input.as_view(), name='addCD'),
    #url(r'^delete', views.delete.as_view(), name='delCD'),
)