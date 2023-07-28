"""Django wait command for postgresql connection"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    """
    Django command to wait for postgresql connection

    """

    def handle(self, *args, **options):
        """Entrypoint for command"""

        self.stdout.write("Waiting for postgresql connection")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(
                    "Database connection unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS(
            'Database connection established'))
