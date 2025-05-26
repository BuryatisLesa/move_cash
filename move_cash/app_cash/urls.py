
from django.urls import path
from app_cash.views import (
    MoveCashList,
    MoveCashDetail,
    MoveCashCreate,
    MoveCashUpdate,
    MoveCashDelete,
)
urlpatterns = [
    path("movecashs/", MoveCashList.as_view(), name="movecashs"),
    path("movecashs/<int:pk>/", MoveCashDetail.as_view(), name="movecashs_detatil"),
    path("movecashs/create/", MoveCashCreate.as_view(), name="movecashs_create"),
    path("movecashs/update/<int:pk>", MoveCashUpdate.as_view(), name="movecashs_update"),
    path("movecashs/delete/<int:pk>", MoveCashDelete.as_view(), name="movecashs_delete")
]