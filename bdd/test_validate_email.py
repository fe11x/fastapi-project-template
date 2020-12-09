import pytest
from pytest_bdd import scenarios, given, when, then, parsers


scenarios('features/validate_email.feature')


@pytest.fixture
def context():
    return {}


@given(parsers.cfparse("there's no user with email {email}"))
def make_sure_no_user_with_email(email, context):
    from repositories.user import does_email_exist, delete_user_by_email
    if does_email_exist(email):
        delete_user_by_email(email)


@when(parsers.cfparse("a user tries to check if {email} is a valid email"))
def validate_email(email, context):
    from routers.my import validate_email, Email, EmailValidationResult
    result: EmailValidationResult = validate_email(request=Email(email=email))
    context['result'] = result.is_valid


@then(parsers.cfparse("the result is {result}"))
def check_result(result, context):
    assert str(context['result']) == result
