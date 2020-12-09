from pytest import fixture

from implemented import ValidateEmail


@fixture
def story():
    return ValidateEmail.let(does_email_exist=lambda x: False)


def test_validate_email_good(story):
    validation = story.validate.run(email='lenny@gmail.com')
    assert validation.is_success


def test_validate_email_good_with_special_symbols(story):
    validation = story.validate.run(email='lenny+_.-kravitz@gmail.com')
    assert validation.is_success


def test_validate_invalid_email(story):
    validation = story.validate.run(email='lenny@.com')
    assert validation.is_failure
    assert validation.failed_because(story.validate.failures.invalid_format)


def test_validate_invalid_provider(story):
    validation = story.validate.run(email='lenny@dispostable.com')
    assert validation.is_failure
    assert validation.failed_because(story.validate.failures.invalid_provider)

    validation = story.validate.run(email='lenny@fakemail.net')
    assert validation.is_failure
    assert validation.failed_because(story.validate.failures.invalid_provider)


def test_validate_unavailable(story):
    story = ValidateEmail.let(does_email_exist=lambda x: True)
    validation = story.validate.run(email='user@gmail.com')
    assert validation.is_failure
    assert validation.failed_because(story.validate.failures.not_available)
