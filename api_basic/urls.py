from django.urls import path, include
# from .views import ArticleList, ArticleDetail
# from .views import article_list, article_detail
# from .views import GenericArticleList, GenericArticleDetail
from rest_framework.routers import DefaultRouter
# from .views import ArticleViewSet
# from .views import GenericViewSetArticle
from .views import GenericModelViewSet

router = DefaultRouter()
# router.register(r'article', ArticleViewSet, basename='article')
# router.register(r'article', GenericViewSetArticle, basename='article')
router.register(r'article', GenericModelViewSet, basename='article')


urlpatterns = [
    path('viewset/', include(router.urls))
    # path('article/', ArticleList.as_view()),
    # path('article/<int:pk>/', ArticleDetail.as_view()),
    # path('article/', article_list),
    # path('article/<int:pk>/', article_detail),
    # path('generic/article', GenericArticleList.as_view()),
    # path('generic/article/<int:pk>', GenericArticleDetail.as_view())

]
