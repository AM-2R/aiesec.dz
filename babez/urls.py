from django.urls import path
from .views import home_page, algiers, local_committee

urlpatterns = [
    path('', home_page, name="babez"),
    path('algiers/', algiers, name="algiers"),
    path('lc/', local_committee, name='lc'),
]