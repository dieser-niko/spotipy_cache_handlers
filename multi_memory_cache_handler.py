class MultiMemoryCacheHandler(CacheHandler):
    """
    Allows multiple user tokens to be stored in memory as an instance
    attribute of this class. The token info will be lost when this
    instance is freed.
    """
    def __init__(self, token_info=None, key=None):
        """
        Parameters:
            * key: The key to the token info. Change it to get a different token_info.
            * token_info: The token info to store in memory. Can be None.
        """
        self.key = key
        self.token_info = {key: token_info}

    def get_cached_token(self):
        return self.token_info.get(key)

    def save_token_to_cache(self, token_info):
        self.token_info[key] = token_info

    def change_key(self, key):
        self.key = key
