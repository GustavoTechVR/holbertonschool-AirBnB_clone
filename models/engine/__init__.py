#!/usr/bin/python3
"""
Empty module for engine package
"""
from models.engine.file_storage import FileStorage
# Create a unique FileStorage instance for the application
storage = FileStorage()
storage.reload()
