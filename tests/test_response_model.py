"""Unit tests for response model wrappers."""

from polarsteps_api.models.response import TripResponse, UserResponse


def test_trip_response_stores_model_error_without_printing(capsys):
    """Invalid successful trip payloads should not write to stdout."""
    response = TripResponse(data={"id": 123}, status_code=200, headers={})

    captured = capsys.readouterr()
    assert captured.out == ""
    assert response.trip is None
    assert response.model_error is not None


def test_user_response_stores_model_error_without_printing(capsys):
    """Invalid successful user payloads should not write to stdout."""
    response = UserResponse(data={"id": 123}, status_code=200, headers={})

    captured = capsys.readouterr()
    assert captured.out == ""
    assert response.user is None
    assert response.model_error is not None
