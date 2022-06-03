CACHE_CONFIG = {
    "DEBUG": True,
    "CACHE_TYPE": "flask_caching.contrib.uwsgicache.UWSGICache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

REQUIRE_AUTHENTICATION = [
    "user.change_password",
    "poll.create",
    "poll.view_all"
]

NO_AUTHENTICATION = [
    "user.create",
    "user.login"
]
