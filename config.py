CACHE_CONFIG = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

REQUIRE_AUTHENTICATION = [
    "user.change_password",
    "poll.create"
]

NO_AUTHENTICATION = [
    "user.create",
    "user.login"
]
