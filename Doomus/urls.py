"""Doomus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from MainDoomus.views import *
from usuari.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as autenticacion_views
from compo.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home$', home, name='home'),
    url(r'^quisom$', quisom, name='quisom'),
    url(r'^registrat$', registrat, name='registrat'),
    url(r'^descobreix$', descobreix, name='descobreix'),
    url(r'^penja$', novacompo, name='penja'),
    url(r'^entra', autenticacion_views.login, {'template_name':'entra.html'}, name='entra'),
    url(r'^sortir', autenticacion_views.logout, name='sortir'),
    url(r'^freestyle$', freestyle, name='freestyle'),
    url(r'^afegir/(?P<compo_id>[0-9]+)$', afegircompo, name='afegircompo')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)