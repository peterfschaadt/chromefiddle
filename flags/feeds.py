from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from flags.models import Flag


class LatestMacFlagsFeed(Feed):
	"""
	Subscribe to RSS feed for latest Mac flags.
	"""
	title = "ChromeFiddle's latest experimental Mac flags"
	link = '/mac/feed'
	description = "Subscribe for updates on Chrome's latest experimental flags for Mac OS X"

	def items(self):
		# Display 20 latest flags
		return Flag.objects.filter(is_mac=True).order_by('-pub_date')[:20]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.description


class LatestWindowsFlagsFeed(Feed):
	"""
	Subscribe to RSS feed for latest Windows flags.
	"""
	title = "ChromeFiddle's latest experimental Windows flags"
	link = '/windows/feed'
	description = "Subscribe for updates on Chrome's latest experimental flags for Windows"

	def items(self):
		# Display 20 latest flags
		return Flag.objects.filter(is_windows=True).order_by('-pub_date')[:20]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.description


class LatestLinuxFlagsFeed(Feed):
	"""
	Subscribe to RSS feed for latest Linux flags.
	"""
	title = "ChromeFiddle's latest experimental Linux flags"
	link = '/linux/feed'
	description = "Subscribe for updates on Chrome's latest experimental flags for Linux"

	def items(self):
		# Display 20 latest flags
		return Flag.objects.filter(is_linux=True).order_by('-pub_date')[:20]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.description


class LatestChromeOsFlagsFeed(Feed):
	"""
	Subscribe to RSS feed for latest Chrome OS flags.
	"""
	title = "ChromeFiddle's latest experimental Chrome OS flags"
	link = '/chrome-os/feed'
	description = "Subscribe for updates on Chrome's latest experimental flags for Chrome OS"

	def items(self):
		# Display 20 latest flags
		return Flag.objects.filter(is_chrome_os=True).order_by('-pub_date')[:20]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.description


class LatestAndroidFlagsFeed(Feed):
	"""
	Subscribe to RSS feed for latest Android flags.
	"""
	title = "ChromeFiddle's latest experimental Android flags"
	link = '/android/feed'
	description = "Subscribe for updates on Chrome's latest experimental flags for Android"

	def items(self):
		# Display 20 latest flags
		return Flag.objects.filter(is_android=True).order_by('-pub_date')[:20]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.description


