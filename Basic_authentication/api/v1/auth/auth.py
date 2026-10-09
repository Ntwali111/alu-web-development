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
        """ Return True if path requires authentication, else False
        """
        if path is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path = path + '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return None, header handling will be added later
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return None, user lookup will be added later
        """
        return None
