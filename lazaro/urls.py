"""lazaro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from control_personal import views
from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)


docs_schema_view = get_swagger_view(title='Lazaro API')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    # -------------------------------------------------------------------------------------------
    # API REST
    # -------------------------------------------------------------------------------------------
    url(r'^api/v2/', include(router.urls)),
    url(r'^docs/', docs_schema_view),
    # -------------------------------------------------------------------------------------------
]