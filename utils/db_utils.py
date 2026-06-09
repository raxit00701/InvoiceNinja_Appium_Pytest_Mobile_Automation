import logging
import mysql.connector
from mysql.connector import Error

logger = logging.getLogger(__name__)

# ---------------------------------------------------------
# DB Config
# ---------------------------------------------------------

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "ninja",
    "password": "ninja",
    "database": "ninja",
    "port": 3307,
}


class DBUtils:

    def __init__(self):

        self.connection = None

    # ---------------------------------------------------------
    # Connect
    # ---------------------------------------------------------

    def connect(self):

        try:

            self.connection = mysql.connector.connect(
                **DB_CONFIG, autocommit=True, connection_timeout=30
            )

            logger.info("Connected to database.")

        except Error as e:

            logger.error(f"Database connection failed: {e}")

            raise

    # ---------------------------------------------------------
    # Disconnect
    # ---------------------------------------------------------

    def disconnect(self):

        try:

            if self.connection and self.connection.is_connected():

                self.connection.close()

                logger.info("Disconnected from database.")

        except Error as e:

            logger.warning(f"Database disconnect warning: {e}")

    # ---------------------------------------------------------
    # Ensure Active Connection
    # ---------------------------------------------------------

    def ensure_connection(self):

        try:

            if self.connection is None:

                logger.warning("DB connection missing. Reconnecting...")

                self.connect()

            elif not self.connection.is_connected():

                logger.warning("DB connection lost. Reconnecting...")

                self.connect()

            else:

                # IMPORTANT
                self.connection.ping(reconnect=True, attempts=3, delay=2)

        except Error as e:

            logger.warning(f"DB ping failed. Reconnecting... {e}")

            self.connect()

    # ---------------------------------------------------------
    # Fetch Multiple Rows
    # ---------------------------------------------------------

    def fetch(self, query: str, params: tuple = None) -> list:

        self.ensure_connection()

        cursor = self.connection.cursor(dictionary=True)

        try:

            cursor.execute(query, params or ())

            results = cursor.fetchall()

            return results

        except Error as e:

            logger.error(f"Query failed: {e}")

            return []

        finally:

            cursor.close()

    # ---------------------------------------------------------
    # Fetch Single Row
    # ---------------------------------------------------------

    def fetch_one(self, query: str, params: tuple = None) -> dict | None:

        self.ensure_connection()

        cursor = self.connection.cursor(dictionary=True)

        try:

            cursor.execute(query, params or ())

            result = cursor.fetchone()

            return result

        except Error as e:

            logger.error(f"Query failed: {e}")

            return None

        finally:

            cursor.close()
