import pytest

pytestmark = pytest.mark.frontend

@pytest.mark.extra
def test_another_mark():
    print('another mark from Hanna')