#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Nick M. (https://github.com/nickmasster)
# Copyright 2011-2013 Codernity (http://codernity.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""General index"""

import io
import os
import marshal
from typing import Any, Generator, Optional

from codernitydb3 import __version__


class IndexException(Exception):
    """General index exception"""


class IndexNotFoundException(IndexException):
    """Index not found"""


class ReindexException(IndexException):
    """Re-index related exception"""


# TODO should be a warning?
class TryReindexException(ReindexException):
    """Try re-index exception"""


class ElemNotFound(IndexException):
    """Index element not found"""


class DocIdNotFound(ElemNotFound):
    """Index primary key not found"""


class IndexConflict(IndexException):
    """Indices conflict occurred"""


class IndexPreconditionsException(IndexException):
    """Index pre-condition exception"""


# TODO add ABC
class Index:
    """Abstract class for database index"""

    __version__ = __version__

    STATUS_O = b'o'
    STATUS_U = b'u'
    STATUS_D = b'd'

    custom_header = ""  # : use it for imports required by your index

    def __init__(self, db_path: str, name: str) -> None:
        """
        Class constructor

        :param db_path: Path to database
        :type db_path: str
        :param name: Index name
        :type name: str
        """
        self.name = name
        self._start_ind = 500
        self.db_path = db_path
        self.buckets = None
        self._storage = None

    @property
    def opened(self) -> bool:
        """Is index opened?"""
        return self.buckets and not self.buckets.closed

    @property
    def storage(self):
        """Index storage"""
        return self._storage

    def open_index(self) -> None:
        """
        Open existing index

        :raise IndexException: Index doesn't exists
        """
        if not os.path.isfile(os.path.join(self.db_path, self.name + '_buck')):
            raise IndexException("Doesn't exists")
        self.buckets = io.open(os.path.join(self.db_path, self.name + "_buck"),
                               'r+b',
                               buffering=0)
        self._fix_params()
        self._open_storage()

    def _close(self) -> None:
        """
        Close index and storage files
        """
        self.buckets.close()
        self._storage.close()

    def close_index(self) -> None:
        """
        Close index
        """
        self.flush()
        self.fsync()
        self._close()

    def create_index(self) -> None:
        """
        Create new index
        """

    def _fix_params(self) -> None:
        """
        Load index configuration from file
        """
        self.buckets.seek(0)
        props = marshal.loads(self.buckets.read(self._start_ind))
        for key, val in props.items():
            self.__dict__[key] = val
        self.buckets.seek(0, 2)

    def _save_params(self, in_params: Optional[dict] = None) -> None:
        """
        Save index configuration into file

        :param in_params: Index configuration parameters
        :type in_params: dict

        :raise IndexException: Configuration is too large
        """
        self.buckets.seek(0)
        props = marshal.loads(self.buckets.read(self._start_ind))
        props.update(in_params)
        self.buckets.seek(0)
        data = marshal.dumps(props)
        if len(data) > self._start_ind:
            raise IndexException("To big props")
        self.buckets.write(data)
        self.flush()
        self.buckets.seek(0, 2)
        self.__dict__.update(props)

    def _open_storage(self, *args, **kwargs) -> None:
        """
        Open index storage
        """
        raise NotImplementedError

    def _create_storage(self, *args, **kwargs) -> None:
        """
        Create index storage
        """
        raise NotImplementedError

    def _destroy_storage(self, *args, **kwargs) -> None:
        """
        Destroy index storage
        """
        self._storage.destroy()

    def _find_key(self, key: bytes):
        """
        Find index key

        :param key: Index key
        :type key: bytes
        """
        raise NotImplementedError

    def update(self, doc_id: bytes, key: bytes, start: int, size: int) -> None:
        """
        Update exsting index element

        :param doc_id: Index primary key
        :type doc_id: bytes
        :param key: Index secondary key
        :type key: bytes
        :param start: Data record start position
        :type start: int
        :param size: Data record size
        :type size: int
        """
        raise NotImplementedError

    def insert(self, doc_id: bytes, key: bytes, start: int, size: int) -> None:
        """
        Insert new index element

        :param doc_id: Index primary key
        :type doc_id: bytes
        :param key: Index secondary key
        :type key: bytes
        :param start: Data record start position
        :type start: int
        :param size: Data record size
        :type size: int
        """
        raise NotImplementedError

    def get(self, key: str):
        """
        Get index element by key

        :param key: Index key
        :type key: str
        """
        raise NotImplementedError

    def get_many(self,
                 key: str,
                 start_from: Optional[int] = None,
                 limit: Optional[int] = 0):
        """
        Get multiple index elements by key

        :param key: Index key
        :type key: str
        :param start_from: Lookup start position
        :type start_from: int
        :param limit: Maximum number of indices to retrieve
        :type limit: int
        """
        raise NotImplementedError

    def all(self, start_pos: Optional[int] = 0) -> Generator:
        """
        Get all index elements

        :param start_from: Lookup start position
        :type start_from: int

        :return: List of index elements
        :rtype: Generator
        """
        raise NotImplementedError

    def delete(self,
               key: str,
               start: Optional[int] = 0,
               size: Optional[int] = 0):
        """
        Delete index element

        :param key: Index key
        :type key: str
        :param start: Data record start position
        :type start: int
        :param size: Data record size
        :type size: int
        """
        raise NotImplementedError

    def make_key_value(self, data: Any):
        """
        Build key & value

        :param data: Data record
        :type data: Any
        """
        raise NotImplementedError

    def make_key(self, data: Any):
        """
        Build key

        :param data: Data record
        :type data: Any
        """
        raise NotImplementedError

    def compact(self, *args, **kwargs) -> None:
        """
        Compact index
        """
        raise NotImplementedError

    def destroy(self, *args, **kwargs) -> None:
        """
        Destroy index
        """
        self._close()
        bucket_file = os.path.join(self.db_path, self.name + '_buck')
        os.unlink(bucket_file)
        self._destroy_storage()
        self._find_key.clear()

    def flush(self) -> None:
        """
        Flush index buffer into file
        """
        if self.opened:
            self.buckets.flush()
        self._storage.flush()

    def fsync(self) -> None:
        """
        Flush index file into disk
        """
        if self.opened:
            os.fsync(self.buckets.fileno())
        self._storage.fsync()

    def update_with_storage(self, doc_id: bytes, key: bytes, value: Any):
        """
        Update existing data record and it's index element

        :param doc_id: Index primary key
        :type doc_id: bytes
        :param key: Index secondary key
        :type key: bytes
        :param start: Data record
        :type start: Any
        """
        if value:
            start, size = self._storage.insert(value)
        else:
            start = 1
            size = 0
        return self.update(doc_id, key, start, size)

    def insert_with_storage(self, doc_id: bytes, key: bytes, value: Any):
        """
        Insert new data record and index element

        :param doc_id: Index primary key
        :type doc_id: bytes
        :param key: Index secondary key
        :type key: bytes
        :param start: Data record
        :type start: Any
        """
        if value:
            start, size = self._storage.insert(value)
        else:
            start = 1
            size = 0
        return self.insert(doc_id, key, start, size)
