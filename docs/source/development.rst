Development
===========

This section provides guidelines for contributing and developing in this project.

- **Testing:**

  .. code-block:: bash

     make test

- **Linting and formatting:**

  .. code-block:: bash

     make lint
     make format

- **Migrations:**

  .. code-block:: bash

     alembic revision --autogenerate -m "message"
     alembic upgrade head

- **Pre-commit hooks:**

  .. code-block:: bash

     pre-commit install

- **Documentation:**

  .. code-block:: bash

     make docs

See the README and CONTRIBUTING.md for more details.
