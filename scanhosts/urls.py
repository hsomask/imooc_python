from django.urls import path, include

import scanhosts.views

urlpatterns = [
    path('user_info', scanhosts.views.user_info),
    path('getInfos', scanhosts.views.user_history)
]
