"""
JSON Reader - Reads test data and environment configuration from JSON files.
"""

import json
import os
import logging

logger = logging.getLogger(__name__)


class JSONReader:
    _cache = {}

    @classmethod
    def load(cls, filepath: str) -> dict:
        """
        Load a JSON file, using in-memory cache to avoid repeated disk reads.

        Args:
            filepath: Absolute or relative path to the JSON file.

        Returns:
            Parsed dict from JSON.
        """
        abs_path = os.path.abspath(filepath)
        if abs_path not in cls._cache:
            if not os.path.exists(abs_path):
                raise FileNotFoundError(f"JSON file not found: {abs_path}")
            with open(abs_path, "r", encoding="utf-8") as f:
                cls._cache[abs_path] = json.load(f)
            logger.debug(f"Loaded JSON from: {abs_path}")
        return cls._cache[abs_path]

    @classmethod
    def get(cls, filepath: str, key: str, default=None):
        """
        Get a specific key from a JSON file.

        Args:
            filepath: Path to JSON file.
            key: Top-level key to retrieve.
            default: Default value if key not found.

        Returns:
            Value associated with key.
        """
        data = cls.load(filepath)
        return data.get(key, default)

    @classmethod
    def clear_cache(cls):
        cls._cache.clear()
