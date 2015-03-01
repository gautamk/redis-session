import unittest
from mock import patch
from mockredis import mock_redis_client
from redis import Redis
from redis_session.sessionmanager import SessionManager

__author__ = 'gautam'


class TestSession(unittest.TestCase):
    @patch('redis.Redis', mock_redis_client)
    def setUp(self):
        self.redis_connection = Redis()
        self.session_manager = SessionManager(self.redis_connection)

    def tearDown(self):
        pass


    def test_create_session(self):
        session_id = self.session_manager.create_session()
        self.assertIsNotNone(session_id)


