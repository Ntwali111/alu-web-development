#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Template class for all authentication systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Return False, path checking will be added later
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Return None, header handling will be added later
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return None, user lookup will be added later
        """
        return None
