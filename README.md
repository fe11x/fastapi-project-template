# Python back-end

## Environment setup

[Install poetry and dependencies](https://python-poetry.org/docs/):

```shell script
pip3 install poetry
poetry install
```

## Activating virtualenv

```shell script
poetry shell
```

## Testing

You can run all tests with pytest.

To run only unit tests, exclude bdd folder:

```shell script
pytest --ignore bdd
```

To run only integration scenarios, only run on the bdd folder:

```shell script
pytest bdd
```

## Managing dependencies

If you need to add a new dependency run:

```shell script
poetry add <package>
```

If you want to update `poetry.lock` run:

```shell script
poetry update
```