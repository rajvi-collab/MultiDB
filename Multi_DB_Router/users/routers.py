"""Router for the  User."""


class UsersRouter(object):
    """Routes are define for this app."""

    def db_for_read(self, model, **hints):
        """Send all read operations on Example app models to `example_db`."""
        if model._meta.app_label == 'users':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """Send all write operations on Example app models to `example_db`."""
        if model._meta.app_label == 'users':
            return 'default'
        return None
