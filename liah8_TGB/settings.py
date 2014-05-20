# Scrapy settings for liah8_TGB project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'liah8_TGB'

SPIDER_MODULES = ['liah8_TGB.spiders']
NEWSPIDER_MODULE = 'liah8_TGB.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'liah8_TGB (+http://www.yourdomain.com)'
DOWNLOAD_DELAY = 0.5
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS_PER_IP = 2
