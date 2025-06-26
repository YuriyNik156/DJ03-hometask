from generalnews.conf import settings
from generalnews.conf.urls.static import static

from generalnews.contrib import admin
from generalnews.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
