from rest_framework.routers import DefaultRouter

from .views import PostModelViewSet, CommentModelViewSet, VoteModelViewSet

router = DefaultRouter()

router.register(r'post-modelset', PostModelViewSet, basename='post')
router.register(r'vote-modelset', VoteModelViewSet, basename='vote')
router.register(r'comment-modelset', CommentModelViewSet, basename='comment')

urlpatterns = router.urls
