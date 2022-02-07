from rest_framework.routers import DefaultRouter

from probe import views

router = DefaultRouter()
router.register(f'int', views.SomeView)

urlpatterns = []
urlpatterns += router.urls
