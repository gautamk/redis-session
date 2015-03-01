__author__ = 'gautam'


class SessionManager:
    def __init__(self, redis_connection):
        """
        Create a new session manager
        :param redis_connection: redis.StrictRedis
        :return:
        """
        self.redis_connection = redis_connection

    def create_session(self, **kwargs):
        """
        Create a new session and return its id
        :param kwargs: attributes for the session
        :return: a string id
        """
        return None
