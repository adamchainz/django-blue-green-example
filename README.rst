django-blue-green-example
=========================

Reproducing the technique from `Smooth Database Changes in Blue-Green Deployments <https://fly.io/django-beats/smooth-database-changes-in-blue-green-deployments/>`__ by      Mariusz Felisiak.

Run:

.. code-block:: sh

    python3.11 -m venv .venv
    source .venv/bin/activate
    pip install 'django==4.2.*'
    python manage.py migrate

You’ll see this crash:

.. code-block:: console

    $ python manage.py migrate bookstore 0004
    Operations to perform:
      Target specific migration: 0004_remove_book_font_delete_font_from_db, from bookstore
    Running migrations:
      Applying bookstore.0004_remove_book_font_delete_font_from_db...Traceback (most recent call last):
      File "/.../manage.py", line 21, in <module>
        main()
      File "/.../manage.py", line 17, in main
        execute_from_command_line(sys.argv)
      File "/.../.venv/lib/python3.11/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
        utility.execute()
      File "/.../.venv/lib/python3.11/site-packages/django/core/management/__init__.py", line 436, in execute
        self.fetch_command(subcommand).run_from_argv(self.argv)
      File "/.../.venv/lib/python3.11/site-packages/django/core/management/base.py", line 412, in run_from_argv
        self.execute(*args, **cmd_options)
      File "/.../.venv/lib/python3.11/site-packages/django/core/management/base.py", line 458, in execute
        output = self.handle(*args, **options)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/.../.venv/lib/python3.11/site-packages/django/core/management/base.py", line 106, in wrapper
        res = handle_func(*args, **kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/.../.venv/lib/python3.11/site-packages/django/core/management/commands/migrate.py", line 356, in handle
        post_migrate_state = executor.migrate(
                             ^^^^^^^^^^^^^^^^^
      File "/.../.venv/lib/python3.11/site-packages/django/db/migrations/executor.py", line 135, in migrate
        state = self._migrate_all_forwards(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/.../.venv/lib/python3.11/site-packages/django/db/migrations/executor.py", line 167, in _migrate_all_forwards
        state = self.apply_migration(
                ^^^^^^^^^^^^^^^^^^^^^
      File "/.../.venv/lib/python3.11/site-packages/django/db/migrations/executor.py", line 252, in apply_migration
        state = migration.apply(state, schema_editor)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/.../.venv/lib/python3.11/site-packages/django/db/migrations/migration.py", line 132, in apply
        operation.database_forwards(
      File "/.../.venv/lib/python3.11/site-packages/django/db/migrations/operations/special.py", line 36, in database_forwards
        database_operation.state_forwards(app_label, to_state)
      File "/.../.venv/lib/python3.11/site-packages/django/db/migrations/operations/fields.py", line 165, in state_forwards
        state.remove_field(app_label, self.model_name_lower, self.name)
      File "/.../.venv/lib/python3.11/site-packages/django/db/migrations/state.py", line 258, in remove_field
        old_field = model_state.fields.pop(name)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    KeyError: 'font'

See branch ``fixed`` for a fixed version, using ``RunSQL`` to delete the field and table.
