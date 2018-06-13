from django.conf.urls import url
import kenyan_stores_scraper.views as scraper_views

app_name = "kenyan_stores_scraper"
urlpatterns = [
    url(r'^home/$', scraper_views.home, name="home"),
    url(r'^$',scraper_views.red,name="redirect"),
    url(r'^details/(?P<pk>\d+)/$',scraper_views.details,name="details"),
    url(r'^pdf/$',scraper_views.GeneratePdf.as_view(),name="pdf"),

]