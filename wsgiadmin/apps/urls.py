from django.conf.urls import patterns, url
from wsgiadmin.apps.views import AppsListView, AppParametersView, AppDetailView, AppCreateView, DbCreateView, DbUpdateView, FtpAccessCreateView, FtpAccessUpdateView

urlpatterns = patterns('',
       url(r'^list/$', AppsListView.as_view(), name="apps_list"),
       url(r'^detail/(?P<app_id>\d+)/$', AppDetailView.as_view(), name="app_detail"),
       url(r'^rm/$', "wsgiadmin.apps.views.app_rm", name="app_rm"),
       url(r'^reinstall/$', "wsgiadmin.apps.views.app_reinstall", name="app_reinstall"),
       url(r'^restart/$', "wsgiadmin.apps.views.app_restart", name="app_restart"),
       url(r'^db/add/$', DbCreateView.as_view(), name="db_add"),
       url(r'^db/update/(?P<pk>\d+)/$', DbUpdateView.as_view(), name="db_update"),
       url(r'^db/rm/$', "wsgiadmin.apps.views.db_rm", name="db_rm"),
       url(r'^ftp/add/$', FtpAccessCreateView.as_view(), name="ftp_add"),
       url(r'^ftp/update/(?P<pk>\d+)/$', FtpAccessUpdateView.as_view(), name="ftp_update"),
       url(r'^ftp/rm/$', "wsgiadmin.apps.views.ftp_rm", name="ftp_rm"),
       url(r'^add_static/$', AppCreateView.as_view(app_type="static"), name="app_add_static"),
       url(r'^add_php/$', AppCreateView.as_view(app_type="php"), name="app_add_php"),
       url(r'^add_phpfpm/$', AppCreateView.as_view(app_type="phpfpm"), name="app_add_phpfpm"),
       url(r'^add_python/$', AppCreateView.as_view(app_type="python"), name="app_add_python"),
       url(r'^add_gunicorn/$', AppCreateView.as_view(app_type="gunicorn"), name="app_add_gunicorn"),
       url(r'^add_native/$', AppCreateView.as_view(app_type="native"), name="app_add_native"),
       url(r'^add_proxy/$', AppCreateView.as_view(app_type="proxy"), name="app_add_proxy"),
       url(r'^add_node/$', AppCreateView.as_view(app_type="node"), name="app_add_node"),
       url(r'^set_static/(?P<app_id>\d+)/$', AppParametersView.as_view(app_type="static"), name="app_params_static"),
       url(r'^set_php/(?P<app_id>\d+)/$', AppParametersView.as_view(app_type="php"), name="app_params_php"),
       url(r'^set_phpfpm/(?P<app_id>\d+)/$', AppParametersView.as_view(app_type="phpfpm"), name="app_params_phpfpm"),
       url(r'^set_python/(?P<app_id>\d+)/$', AppParametersView.as_view(app_type="python"), name="app_params_python"),
       url(r'^set_gunicorn/(?P<app_id>\d+)/$', AppParametersView.as_view(app_type="gunicorn"), name="app_params_gunicorn"),
       url(r'^set_native/(?P<app_id>\d+)/$', AppParametersView.as_view(app_type="native"), name="app_params_native"),
       url(r'^set_proxy/(?P<app_id>\d+)/$', AppParametersView.as_view(app_type="proxy"), name="app_params_proxy"),
       url(r'^set_node/(?P<app_id>\d+)/$', AppParametersView.as_view(app_type="node"), name="app_params_node"),
)
