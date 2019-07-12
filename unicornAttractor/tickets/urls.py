from django.urls import path
from django.conf.urls import url
from .views import tracker, create_ticket, ticket_details, upvote_comment, upvote_ticket

urlpatterns = [
    path('', tracker, name='tracker'),
    path('new-ticket/<ticket_type>/', create_ticket, name='new_ticket'),
    url(r'^(?P<pk>\d+)/$', ticket_details, name='ticket_details'),
    url(r'^upvote_comment/(?P<pk>\d+)/(?P<ticket_id>\d+)$', upvote_comment, name='upvote_comment'),
    url(r'^upvote_ticket/(?P<pk>\d+)/$', upvote_ticket, name='upvote_ticket'),
]