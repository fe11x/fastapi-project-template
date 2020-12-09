import functools
from typing import Iterable
from uuid import UUID


# TODO: switch to `mappers` by contributing support for Pony ORM https://github.com/proofit404/mappers/issues/250


class MapperEntityMissing(BaseException):
    pass


def mapper(function=None, *, entity=None, config=None):
    """
    Handles conversion from ORM to domain entities
    """
    # TODO: add UT and document `config` usage
    if function is None:
        return functools.partial(mapper, entity=entity, config=config)

    if not entity:
        raise MapperEntityMissing

    config = config or {}

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        nonlocal entity, config

        entities = []
        results = function(*args, **kwargs)

        if results and not isinstance(results, Iterable):
            return _convert_from_orm(entity, results)

        for orm_object in results:
            entities.append(
                _convert_from_orm(entity, orm_object)
            )

        return entities

    def _convert_from_orm(entity, orm_object):
        if isinstance(orm_object, UUID):
            return entity(id=orm_object)

        _apply_config_mapping(orm_object)
        return entity.from_orm(orm_object)

    def _apply_config_mapping(object):
        nonlocal config

        for field, column in config.items():
            if hasattr(object, column):
                setattr(object, field, getattr(object, column))

    return wrapper
