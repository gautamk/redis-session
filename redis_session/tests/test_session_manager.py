import unittest

from mock import patch
from mockredis import mock_redis_client

from redis_session.sessionmanager import SessionManager


__author__ = 'gautam'


class TestSessionManager(unittest.TestCase):
    @patch('redis.Redis', mock_redis_client)
    def setUp(self):
        self.redis_connection = mock_redis_client()
        self.session_manager = SessionManager(self.redis_connection)

    def tearDown(self):
        pass

    def test_create_session(self):
        session = self.session_manager.create_session(email="john.doe@email.com")
        self.assertIsNotNone(session.session_id)
        session_data = self.redis_connection.get(session.session_id)
        self.assertIsNotNone(session_data)


class TestSession(TestSessionManager):
    def setUp(self):
        super(TestSession, self).setUp()
        self.data = {
            "email": "john.doe@email.com"
        }
        self.session = self.session_manager.create_session(**self.data)

    def test_session_get_valid_item(self):
        self.assertEqual(self.session.get("email"), self.data["email"])

    def test_session_get_invalid_item(self):
        self.assertIsNone(self.session.get("invalid"))

    def test_session_get_default_item(self):
        self.assertTrue(self.session.get("invalid", True))



