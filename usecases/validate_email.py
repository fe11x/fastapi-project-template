import logging

from dataclasses import dataclass
from enum import Enum, auto
from typing import Callable

from stories import story, arguments, Success, Result, Failure

from emails.validations import is_valid_email, is_valid_email_provider


logger = logging.getLogger(__name__)


@dataclass
class ValidateEmail:
    """
    Validate email address
    """
    @story
    @arguments('email')
    def validate(I):
        I.check_format
        I.check_provider
        I.check_availability

    def check_format(self, ctx):
        if is_valid_email(ctx.email):
            return Success()
        return Failure(self.Errors.invalid_format)

    def check_provider(self, ctx):
        if is_valid_email_provider(ctx.email):
            return Success()
        return Failure(self.Errors.invalid_provider)

    def check_availability(self, ctx):
        if self.does_email_exist(ctx.email):
            return Failure(self.Errors.not_available)
        return Success()

    def give_result(self, ctx):
        return Result(True)

    does_email_exist: Callable

    @validate.failures
    class Errors(Enum):
        invalid_format = auto()
        invalid_provider = auto()
        not_available = auto()
