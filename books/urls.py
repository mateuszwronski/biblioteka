from django.urls import path

from books.views import BookList, AuthorList, BookDetails

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('author/', AuthorList.as_view(), name='author_list'),
    path('<int:pk>/', BookDetails.as_view(), name='book_details'),
]
