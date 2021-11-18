from launch_darkly_client import LaunchDarklyClient


class UserFeatureFlags(dict):
    def __init__(self, client: LaunchDarklyClient, user):
        self._client = client
        self._user = user

    def __getitem__(self, key):
        if key in self.keys():
            return super().__getitem__(key)
        value = self._get_value_from_client(key)
        self.__setitem__(key, value)
        return value

    def _get_value_from_client(self, key):
        return self._client.get_variation(key, self._user, None)