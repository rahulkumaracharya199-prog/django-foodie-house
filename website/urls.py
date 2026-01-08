from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from foodie.views import home, productView
from foodie.admin_views import dashboard, manageCategory, manageProduct

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path("", home),
    path("products/<int:product_id>/", productView, name="viewProduct"),

    # admin routes

    path("admin/", dashboard, name="admindashboard"),
    path("admin/manageCategory", manageCategory, name="manageCategory"),
    path("admin/manageProduct", manageProduct, name="manageProduct")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
