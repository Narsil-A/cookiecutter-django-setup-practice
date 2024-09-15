import pytest

from cookiecutte_django_practice_with_docker.users.models import User
from cookiecutte_django_practice_with_docker.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()
