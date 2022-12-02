from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, AppointmentView, CategoryListView, subscribe


urlpatterns = [
   path('', PostsList.as_view(), name='news_list'),
   path('<int:pk>', PostDetail.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('make_appointment/', AppointmentView.as_view(), name='make_appointment'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]