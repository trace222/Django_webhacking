from django.urls import path
from . import views

app_name='test1'
urlpatterns = [
    path('',views.UrlInput),
    path('index',views.index,name='home'), #index 사이트 이름을 home 으로 지정한건가보군
    path('board',views.board,name="board"),
    path('writeboard',views.writeboard,name="writeboard"),
    path('writemanage',views.writemanage,name="writemanage"),
    path('deleteboard',views.deleteboard,name="deleteboard"),
    #path('vulnerable/<user>/results',views.results),
    path('main',views.vulnervle_main),
    path('result',views.result),
    path('crawling_result',views.crawling_result),
    path('solve',views.solve),
    path('login',views.login)
]
