from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, AppointmentView, CategoryListView, \
   subscribe
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', cache_page(60)(PostsList.as_view()), name='news_list'),
   #path('<int:pk>/', cache_page(60*5)(PostDetail.as_view()), name='post_detail'), # добавим кэширование на детали товара. Раз в 10 минут товар будет записываться в кэш для экономии ресурсов.
   path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('make_appointment/', AppointmentView.as_view(), name='make_appointment'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]