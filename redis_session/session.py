__author__ = 'gautam'


class Session:
    def __init__(self, session_id, session_data):
        self.session_id = session_id
        self.session_data = session_data

    def get(self, key, default=None):
        """
        Get data from the session,
        Note this doesn't actually fetch data,
        it merely is a convenience method to retrieve previously cached data
        :param key:
        :return: value
        """
        return self.session_data.get(key, default)