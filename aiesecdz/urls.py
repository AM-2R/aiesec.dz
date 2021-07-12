from . import views
from django.urls import path, include

committees = [
    path('AiA', views.AiA, name='AiA'),
    path('babez/', include('babez.urls')),
    path('benak', views.benak, name='benak'),
    path('blida', views.blida, name='blida'),
    path('cons', views.cons, name='cons'),
    path('oran', views.oran, name='oran'),
    path('ouargla', views.ouargla, name='ouargla'),

    
]

urlpatterns = [
    path('', views.index, name='index'),
    path('companies', views.companies, name='companies'),
    path('contact', views.contact, name='contact'),
    path('cookies', views.cookies, name='cookies'),
    path('gv', views.gv, name='gv'),
    path('ge', views.ge, name='ge'),
    path('gt', views.gt, name='gt'),
    path('host_family', views.host_family, name='host_family'),
    path('join_aiesec', views.join_aiesec, name='join_aiesec'),
    path('offices', views.offices, name='offices'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('y4gg', views.y4gg, name='y4gg'),
    path('ysf', views.ysf, name='ysf'),
    path('blog', views.blog, name='blog'),
    path('globalv', views.globalv, name='globalv'),
    
]+committees
