from django.urls import include, re_path
from certification import views 
 
urlpatterns = [ 
    re_path(r'^api/certifications$', views.certification_list),
    re_path(r'^api/certifications/(?P<pk>[0-9]+)$', views.certification_detail),
    # url(r'^api/certifications/published$', views.tutorial_list_published)
]