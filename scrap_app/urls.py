from django.urls import path
from scrap_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("sign_up/",views.Sign_up.as_view(),name="sign_up"),
    path("signin",views.Sign_in.as_view(),name="sign"),
    path("sign_out/",views.SignOutView.as_view(),name="sign_out"),
    path("profile_add/<int:pk>/",views.UserProfileView.as_view(),name="profile_add"),
    path("profile_list/",views.ProfileListView.as_view(),name="profile_list"),
    path("profile/<int:pk>/",views.ProfileView.as_view(),name="profile"),
    path("scrap/add/",views.ScrapAddView.as_view(),name="scrap_add"),
    path('scrap/list/',views.ScrapListView.as_view(),name="scrap_list"),
    path("scrap/edit/<int:pk>/",views.ScrapUpdateView.as_view(),name="scrap_update"),
    path("scrap/whislist/<int:pk>/",views.WishListView.as_view(),name="wish_list"),
    path("scrap/details/<int:pk>",views.ScrapDetailView.as_view(),name="scrap_details"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("bid/<int:pk>",views.BidAddView.as_view(),name="bid"),
    path("scrap/user/list/",views.UserProductsView.as_view(),name="userscrap"),
    path("scrap/user/wishlist/",views.WishView.as_view(),name="wish"),
    path("scrap/user/remove/<int:pk>/",views.ScrapdeleteView.as_view(),name="scrapremove"),
    path("scrap/user/cat/<int:pk>/",views.CatScrapview.as_view(),name="catscrap")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
