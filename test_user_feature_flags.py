from unittest.mock import patch, MagicMock

from launch_darkly_client import LaunchDarklyClient
from user_feature_flags import UserFeatureFlags


def test_constructor():
    flags = UserFeatureFlags(None, None)
    assert isinstance(flags, UserFeatureFlags)
    assert isinstance(flags, dict)


def test_get_item_returns_stored_value_if_present():
    expected = "bar"
    flags = UserFeatureFlags(None, None)
    with patch.dict(flags, {"foo": expected}, clear=True):
        actual = flags["foo"]
    assert actual == expected


def test_get_item_loads_calls_client_on_cache_miss():
    with patch.object(LaunchDarklyClient, '_configure_client', return_value=None):
        client = LaunchDarklyClient(None)
    client.get_variation = MagicMock(return_value="Value From LD")
    flags = UserFeatureFlags(client, None)

    actual = flags["foo"]
    client.get_variation.assert_called_with("foo", None, None)


def test_get_item_stores_client_result_for_future_use():
    with patch.object(LaunchDarklyClient, '_configure_client', return_value=None):
        client = LaunchDarklyClient(None)
    client.get_variation = MagicMock(return_value="Value From LD")
    flags = UserFeatureFlags(client, None)

    firstCall = flags["foo"]
    secondCall = flags["foo"]
    client.get_variation.assert_called_once_with("foo", None, None)
