django-blue-green-example
=========================

Reproducing the technique from `Smooth Database Changes in Blue-Green Deployments <https://fly.io/django-beats/smooth-database-changes-in-blue-green-deployments/>`__ by      Mariusz Felisiak.

Run:

.. code-block:: sh

    python3.11 -m venv .venv
    source .venv/bin/activate
    pip install 'django==4.2.*'
    python manage.py migrate
