Architecture
============

The project follows a clean architecture pattern, separating concerns into distinct layers:

- **API Layer:** Handles HTTP requests and responses (FastAPI).
- **Service Layer:** Contains business logic.
- **Repository Layer:** Manages data access and persistence (SQLAlchemy).
- **Schema Layer:** Data validation and serialization (Pydantic).
- **Core Layer:** Configuration and cross-cutting concerns.

.. note::
   You can add diagrams here using sphinxcontrib-mermaid or PlantUML for better visualization.

Example (Mermaid):

.. mermaid::

   graph TD;
     API-->Service;
     Service-->Repository;
     Repository-->DB[(Database)];
     Service-->Schema;
     API-->Schema;
     Core-->API;
     Core-->Service;
     Core-->Repository;
