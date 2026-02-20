from .models import Profile
from django.core.cache import cache
from django.conf import settings


class ProfileService:
    CACHE_TTL = 60 * 5

    @staticmethod
    def get_profile(user_id):
        key = f"profile:{user_id}"
        profile = cache.get(key)
        if profile is not None:
            return profile
        profile = Profile.objects.select_related('user').filter(user_id=user_id).first()
        cache.set(key, profile, ProfileService.CACHE_TTL)
        return profile

    @staticmethod
    def invalidate_profile_cache(user_id):
        cache.delete(f"profile:{user_id}")

