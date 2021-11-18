from singletoninstance import SingletonInstance
import ldclient
from ldclient import Config

class LaunchDarklyClient:
    def __init__(self, key):
        self._client = ldclient
        self._configure_client(key)

    def _configure_client(self, key):
        self._client.set_config(Config(key))
        if self._client.get().is_initialized():
            print("SDK successfully initialized!")
        else:
            print("SDK failed to initialize")
            exit()

    def get_variation(self, key, user, default=None):
        return self._client.get().variation(key, user, default)

    def get_close(self):
        return self._client.get().close()


class SingletonLaunchDarklyClient(LaunchDarklyClient, metaclass=SingletonInstance):
    pass
