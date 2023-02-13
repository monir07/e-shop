
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from shop.views import HomeView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home View
    path('', HomeView.as_view()),
    # custom authentication
    path('custom-auth/', include('custom_auth.urls')),
    # shop urls
    path('shop/', include('shop.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ADMIN PANEL HEADER AND TITLE TEXT CHANGE.
admin.site.site_header = "E-Shop Admin"
admin.site.site_title = "E-Shop Admin Portal"
admin.site.index_title = "Welcome to E-Shop Portal"