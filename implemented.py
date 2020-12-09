"""
Implemented use cases with dependencies injected

- https://proofit404.github.io/dependencies/
- https://dry-python.org/static/slides/ddd-toolkit-3.html
- https://github.com/dry-python/bookshelf
- https://github.com/Alma-CFAO/PyApiFirstDemo
"""
from dependencies import Injector
from dependencies import Package

usecases = Package("usecases")
repositories = Package("repositories")


class ValidateEmail(Injector):
    validate = usecases.ValidateEmail.validate
    does_email_exist = repositories.does_email_exist
