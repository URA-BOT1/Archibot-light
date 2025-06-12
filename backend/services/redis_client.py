import os

try:
    import redis
except ImportError:  # pragma: no cover
    redis = None


def get_redis_client():
    """Return a Redis client using REDIS_URL or default local instance."""
    url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    if redis is None:
        return None
    return redis.from_url(url)
