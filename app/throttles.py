import time
from django.core.cache import cache
from rest_framework.throttling import BaseThrottle


class RedisRateThrottle(BaseThrottle):
    """
    Custom Redis-based throttling.
    Allows N requests per duration (seconds).
    """
    rate = 5        # max requests
    duration = 60   # time window (in seconds)

    def get_cache_key(self, request):
        """
        Unique key per user (if authenticated) or IP (if anonymous).
        """
        if request.user.is_authenticated:
            return f"throttle:user:{request.user.id}"
        return f"throttle:ip:{self.get_ident(request)}"

    def allow_request(self, request, view):
        """
        Check if request is allowed under the rate limit.
        """
        cache_key = self.get_cache_key(request)
        timestamps = cache.get(cache_key, [])

        now = time.time()
        # Keep only requests within time window
        timestamps = [ts for ts in timestamps if now - ts < self.duration]

        if len(timestamps) >= self.rate:
            return False  # Block request

        # Add this request
        timestamps.append(now)
        cache.set(cache_key, timestamps, timeout=self.duration)
        return True

    def wait(self):
        """
        Time client should wait before next request is allowed.
        """
        return self.duration
