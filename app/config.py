<<<<<<< HEAD:app/config.py
=======
CACHE_CONFIG = {
    "DEBUG": False,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

>>>>>>> 8ed14b17f7c065dd1e28e1598695b583af775934:config.py
REQUIRE_AUTHENTICATION = [
    "user.change_password",
    "poll.create",
    "poll.view_all"
]

NO_AUTHENTICATION = [
    "user.create",
    "user.login"
]
