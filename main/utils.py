def user_listing_path(instance , filename):
    return 'user_{0}/listingd/{1}'.format(instance.seller.user.id, filename)