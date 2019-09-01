# from .views import tweet_detail_view, tweet_list_view
from .views import TweetDetailView, TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView
from django.conf.urls import url
from django.views.generic.base import RedirectView
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',RedirectView.as_view(url="/")),
    url(r'^search/$', TweetListView.as_view(), name='list'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete', TweetDeleteView.as_view(), name='delete'),
]
