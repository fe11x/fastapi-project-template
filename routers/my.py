from pydantic.main import BaseModel
from fastapi import APIRouter, HTTPException, Header

from implemented import ValidateEmail

router = APIRouter()


"""
Current User actions
"""


class Email(BaseModel):
    email: str


class EmailValidationResult(BaseModel):
    is_valid: bool = True
    reason: str = 'available'


@router.post("/email/validate", response_model=EmailValidationResult)
def validate_email(request: Email):
    """
    Updates or validates an email address for an anonymous user

    Example query that can trigger this endpoint:

        {
          validateEmail(email: "evgeny@dispostable.com") {
            is_valid
            reason
          }
        }
    """
    email = request.email
    result = ValidateEmail.validate.run(email=email)

    if result.is_success:
        return EmailValidationResult()

    for reason in ValidateEmail.validate.failures:
        if result.failed_because(reason):
            return EmailValidationResult(is_valid=False, reason=reason.name)

    return EmailValidationResult(is_valid=False, reason='unknown')
