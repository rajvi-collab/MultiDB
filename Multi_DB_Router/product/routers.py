"""Database Routing."""
import random


class ProductRouter(object):
    """Database Routing."""

    def db_for_read(self, model, **hints):
        """Attempt to read models."""
        db_list = ('data1_db', 'data2_db', 'data3_db', 'data4_db')
        if model._meta.app_label == 'product':
            return random.choice(db_list)
        return None

    def db_for_write(self, model, **hints):
        """Attempt to write  models."""
        if model._meta.app_label == 'product':
            return 'data1_db'
        return None
