from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EmployeeView, EmployeeCreate, EmployeeDetailsView, ProjectView,\
    ProjectCreate, ProjectDetailsView, ClientView, ClientCreate, ClientDetailsView, AddEmployeeToProject,\
    AddProjectToClient, ClientUpdateView
from rest_framework.authtoken import views


urlpatterns = {
    url(r'^employees/$', EmployeeView.as_view(), name='get'),
    url(r'^employees/create$', EmployeeCreate.as_view(), name='add'),
    url(r'^employees/(?P<pk>[0-9]+)/$', EmployeeDetailsView.as_view(), name='details'),

    url(r'^projects/$', ProjectView.as_view(), name='get'),
    url(r'^projects/create$', ProjectCreate.as_view(), name='add'),
    url(r'^projects/(?P<pk>[0-9]+)/$', ProjectDetailsView.as_view(), name='details'),
    url(r'^projects/(?P<pk>[0-9]+)/employee$', AddEmployeeToProject.as_view(), name='add_employee'),

    url(r'^clients/$', ClientView.as_view(), name='get'),
    url(r'^clients/create$', ClientCreate.as_view(), name='add'),
    url(r'^clients/(?P<pk>[0-9]+)/$', ClientDetailsView.as_view(), name='details'),
    url(r'^clients/(?P<pk>[0-9]+)/update$', ClientUpdateView.as_view(), name='details'),
    url(r'^clients/(?P<pk>[0-9]+)/project$', AddProjectToClient.as_view(), name='add_employee'),


    # Request to get auth token, POST username and Password
    url(r'^api-token-auth/', views.obtain_auth_token)

}

urlpatterns = format_suffix_patterns(urlpatterns)