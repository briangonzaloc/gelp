from django.conf.urls import url

from .views import ImportDataView

importer_urls = [
	url('', ImportDataView.as_view(), name='importer-data')
]