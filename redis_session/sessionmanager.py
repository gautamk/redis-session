import uuid

from redis_session.session import Session


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
        :return: an instance of the session object
        """
        session_id = uuid.uuid4()
        self.redis_connection.hmset(session_id, kwargs)
        return Session(session_id, kwargs)

