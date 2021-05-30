import pytest

# strict - (строгость) значение False по умолчанию,  в выводе терминала  будет xfailed,
# если функция провалила тест и xpass,если прошла.
# при значении True в выводе терминала будет xfailed, если функция не прошла тест,
# но если фунцкция неожиданно прошла тест то будет fail
@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
