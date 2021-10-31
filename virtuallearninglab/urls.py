from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.apps import apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include("Components.student.urls")),
    path('courses', include("Components.courses.urls")),
    path('', include("Components.home.urls")),
    path('profile/', include("Components.profile.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin_panel/', include('Components.admin_panel.urls')),
    path("student/discussion_board/", include('Components.discussion_board.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('quiz/', include("Components.quiz.urls")),
    path('i18n/', include('django.conf.urls.i18n')),
    path('shop/', include(apps.get_app_config('oscar').urls[0])),
    path('shop/checkout/paypal/', include('paypal.express.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)