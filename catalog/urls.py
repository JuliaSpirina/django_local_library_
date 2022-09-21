
# from . import views
# from django.urls import path
# from django.conf.urls import url
#
# urlpatterns = [
#     url('', views.index, name='index'),
#     url(r'^$', views.index, name='index'),
#     url(r'^books/$', views.BookListView.as_view(), name='books'),
#     url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
#     # url(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
#     # url(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),
# ]
# # urlpatterns += [
# #     path('catalog/', include('catalog.urls')),
#
# # ]

from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),

    re_path(r'^$', views.index, name='index'),
    re_path(r'^author/$', views.AuthorListView.as_view(), name='authors'),

    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    # re_path(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
    # re_path(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),
]

urlpatterns += [
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    re_path(r'^allbooks/$', views.LoanedBooksByLibrarianListView.as_view(), name='all-borrowed'),
]

urlpatterns += [
    re_path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    re_path(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    re_path(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    re_path(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]

urlpatterns += [
    re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    re_path(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book_update'),
    re_path(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book_delete'),
]