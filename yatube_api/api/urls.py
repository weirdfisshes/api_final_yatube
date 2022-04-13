from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import PostViewSet, GroupViewSet, CommentsViewSet, FollowViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)
router.register('follow', FollowViewSet, basename='follows')
urlpatterns = [
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
