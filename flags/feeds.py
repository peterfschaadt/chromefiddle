from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from flags.models import Flag


class LatestFlagsFeed(Feed):
	"""
	Subscribe to RSS feed for latest flags.
	"""
	title = "ChromeFiddle's latest experimental flags"
	link = '/feeds'
	description = "Subscribe for updates on Chrome's latest experimental flags"

	def items(self):
		# Display 20 latest flags
		return Flag.objects.order_by('-pub_date')[:20]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.description
