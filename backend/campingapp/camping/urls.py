from django.urls import path
from campingapp.camping.views import detail, post, update, delete

app_name = "camping"
urlpatterns = [
    path("<int:camping_info_id>/", detail, name="detail"),
    path("update/<int:camping_info_id>/", update, name="update"),
    path("delete/<int:camping_info_id>/", delete, name="delete"),
    path("post/", post, name="post"),
]
