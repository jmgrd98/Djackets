from django.urls import path, include
from product import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetails.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('products/search/', views.search),
]