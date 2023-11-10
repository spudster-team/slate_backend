from django.urls import path

from .views import UserView, UserAuthTokenView, QuestionView, ResponseView, get_all_tags, get_all_photo

urlpatterns = [
    path('user', UserView.as_view({"post": "create", "get": "retrieve", "delete": "destroy", "patch": "update"})),
    path('user/most-active', UserView.as_view({"get": "most_actif_user"})),
    path('user/auth', UserAuthTokenView.as_view()),
    path('question', QuestionView.as_view({"get": "list", "post": "create"})),
    path('question/<int:id>', QuestionView.as_view({"get": "retrieve", "patch": "update", "delete": "destroy"})),
    path('question/vote/<int:id>', QuestionView.as_view({"post": "voting"})),
    path('question/response/<int:id>', QuestionView.as_view({"post": "respond"})),
    path('response/<int:id>', ResponseView.as_view({"delete": "destroy", "put": "update"})),
    path('response/vote/<int:id>', ResponseView.as_view({"post": "voting"})),
    path('tags', get_all_tags),
    path('photos', get_all_photo)
]
