from rest_framework.throttling import UserRateThrottle

class ReviewCreateAPI(UserRateThrottle):
    scope = 'review-create'


class ReviewListCreateAPI(UserRateThrottle):
    scope = 'review-list-create'