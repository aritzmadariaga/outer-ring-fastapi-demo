Installation
============

To install and run the project locally or in Docker:

**Docker (recommended):**

.. code-block:: bash

   docker compose build --no-cache
   docker compose up

**Local (with Python 3.12+):**

.. code-block:: bash

   uv pip install --system '.[dev]'
   uvicorn app.main:app --reload

For more details, see the README.md.
