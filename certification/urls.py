from django.conf.urls import url 
from certification import views 
 
urlpatterns = [ 
    url(r'^api/certifications$', views.certification_list),
    url(r'^api/certifications/(?P<pk>[0-9]+)$', views.certification_detail),
    # url(r'^api/certifications/published$', views.tutorial_list_published)
]