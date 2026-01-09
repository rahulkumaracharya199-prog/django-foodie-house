from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from foodie.views import home, productView
from foodie.admin_views import dashboard, manageCategory, manageProduct
from foodie.auth_views import signup, loginView, logoutView

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path("", home, name="homepage"),
    path("products/<int:product_id>/", productView, name="viewProduct"),

    # admin routes

    path("admin/", dashboard, name="admindashboard"),
    path("admin/manageCategory", manageCategory, name="manageCategory"),
    path("admin/manageProduct", manageProduct, name="manageProduct"),

    # auth routes can be added here

    path("accounts/signup/", signup, name="signup"),
    path("accounts/login/", loginView, name="login"),
    path("accounts/logout/", logoutView, name="logout"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
