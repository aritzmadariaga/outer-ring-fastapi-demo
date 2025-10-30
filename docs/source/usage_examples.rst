Usage Examples
==============

Here are some practical examples of how to use the API and services.

**Create a spacecraft (Python, using HTTPX):**

.. code-block:: python

   import httpx
   response = httpx.post(
       "http://localhost:8000/api/v1/spacecraft/",
       json={
           "registry_code": "OR-001",
           "name": "Outer Explorer",
           "manufacturer": "Deusto",
           "crew_capacity": 5,
           "max_delta_v": 12000,
           "operational": True
       }
   )
   print(response.json())

**Get all spacecrafts:**

.. code-block:: python

   response = httpx.get("http://localhost:8000/api/v1/spacecraft/")
   print(response.json())

You can add more examples for other endpoints or business logic here.
