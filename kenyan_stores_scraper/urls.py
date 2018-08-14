from django.conf.urls import url
import kenyan_stores_scraper.views as scraper_views
from django.contrib.auth.views import login

app_name = "kenyan_stores_scraper"
urlpatterns = [
    url(r'^home/$', scraper_views.home, name="home"),
    url(r'^$',scraper_views.red,name="redirect"),
    url(r'^details/(?P<pk>\d+)/$',scraper_views.details,name="details"),
    # url(r'^pdf/$',scraper_views.GeneratePdf.as_view(),name="pdf"),
    url(r'^account/login',login,{'template_name': 'accounts/login.html'},name='login'),
    url(r'^account/logout$',scraper_views.logout_view,name='logout'),
    url(r'^account/register$',scraper_views.registration_view,name='register'),
    url(r'^products/tracked$',scraper_views.tracking_views,name="tracking"),
    url(r'^delete/(?P<id>\d+)/$',scraper_views.delete_product,name="delete_product"),
    url(r'^addtotracked/(?P<prod_id>\d+)',scraper_views.add_to_tracked,name='add_to_tracked'),
    url(r'^pdf/(?P<pk>\d+)/$',scraper_views.generate_pdf,name="generatepdf"),
    url(r'^report/$',scraper_views.reportgenerator,name="report"),


]