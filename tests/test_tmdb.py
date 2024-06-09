import pytest


from unittest.mock import Mock
import tmdb_client


def test_get_single_movie_cast(monkeypatch):
    mock_movie_cast = ["Actor1", "Actor2"]

    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = mock_movie_cast
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)

    movie_cast = tmdb_client.get_single_movie_cast("dummy")

    assert movie_cast == mock_movie_cast


def test_get_single_movie(monkeypatch):
    mock_movie_details = "dummy details"

    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = mock_movie_details
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)

    movie_details = tmdb_client.get_single_movie("dummy")

    assert movie_details == mock_movie_details

def test_get_movie_images(monkeypatch):
    mock_movie_images = ["dummy1", "dummy2"]

    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = mock_movie_images
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)

    movie_images = tmdb_client.get_movie_images("dummy")

    assert movie_images == mock_movie_images

def test_get_single_movie_cast(monkeypatch):
    mock_movie_cast = ["Actor1", "Actor2"]

    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = mock_movie_cast
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)

    movie_cast = tmdb_client.get_single_movie_cast("dummy")

    assert movie_cast == mock_movie_cast