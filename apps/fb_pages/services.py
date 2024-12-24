from facebook_business.api import FacebookAdsApi


def initialize_facebook_api(page):
    FacebookAdsApi.init(access_token=page.access_token)
