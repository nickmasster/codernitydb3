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
"""General storage"""

import struct
import marshal
from os import fsync
from abc import ABC
from typing import Any, Optional, Tuple, Union
from pathlib import Path

from codernitydb3 import __version__


class StorageException(Exception):
    """General storage exception"""


class StorageNotInitialized(StorageException):
    """Storage is not initialized yet"""


class IU_Storage(ABC):
    """Abstract class for database storage"""

    STATUS_C = b'c'
    STATUS_D = b'd'

    __version__ = __version__

    def __init__(self, db_path: Union[str, Path], name: Optional[str] = None):
        """
        Class constructor

        :param db_path: Path to database
        :type db_path: str or Path
        :param name: Storage name
        :type name: str
        """
        self._name = name or 'main'
        self._path = Path(db_path).joinpath('%s_stor' % self._name)
        self._fhd = None

    @property
    def name(self) -> str:
        """Storage name"""
        return self._name

    @property
    def path(self) -> Path:
        """Storage path"""
        return self._path

    @property
    def opened(self) -> bool:
        """Is strorage opened?"""
        return self._fhd and not self._fhd.closed

    def create(self) -> None:
        """
        Create new storage

        :raise StorageException: Storage already exists
        """
        if self._path.is_file():
            raise StorageException('storage already exists')
        with open(self._path, 'wb') as fhd:
            fhd.write(
                struct.pack('10s90s', self.__version__.encode('utf8'),
                            b'|||||'))
        self.open()

    def open(self) -> None:
        """
        Open existing storage

        :raise StorageException: Storage doesn't exists
        """
        if not self._path.is_file():
            raise StorageException("storage doesn't exists")
        self._fhd = open(self._path, 'r+b', buffering=0)
        self._fhd.seek(0, 2)

    def destroy(self) -> None:
        """
        Destroy storage
        """
        self.close()
        try:
            self._path.unlink()
        except FileNotFoundError:
            pass

    def close(self) -> None:
        """
        Close storage
        """
        if self.opened:
            self._fhd.close()

    # pylint: disable = R0201
    def _data_from(self, data: bytes) -> Any:
        """
        Unpack data from storage

        :param data: Packed data
        :type data: bytes

        :return: Unpacked data
        :rtype: Any
        """
        return marshal.loads(data)

    # pylint: disable = R0201
    def _data_to(self, data: Any) -> bytes:
        """
        Pack data into storage

        :param data: Unpacked data
        :type data: Any

        :return: Packed data
        :rtype: bytes
        """
        return marshal.dumps(data)

    def _save(self, data: Any) -> Tuple[int, int]:
        """
        Save data to storage

        :param data: Data to save
        :type data: Any

        :return: Data location and size in storage
        :rtype: Tuple[int, int]
        """
        if not self.opened:
            raise StorageNotInitialized
        self._fhd.seek(0, 2)
        start = self._fhd.tell()
        size = self._fhd.write(self._data_to(data))
        self.flush()
        return start, size

    def insert(self, data: Any) -> Tuple[int, int]:
        """
        Insert new data

        :param data: Data
        :type data: Any

        :return: Data start position and size in storage
        :rtype: Tuple[int, int]
        """
        return self._save(data)

    def update(self, data: Any) -> Tuple[int, int]:
        """
        Update existing data

        :param data: Data
        :type data: Any

        :return: Data location and size in storage
        :rtype: Tuple[int, int]
        """
        return self._save(data)

    def get(self,
            start: int,
            size: int,
            status: Optional[bytes] = None) -> Any:
        """
        Get data

        :param start: Data start position
        :type start: int
        :param size: Data size
        :type size: int
        :param status: Data status
        :type status: bytes

        :return: Data from storage
        :rtype: Any
        """
        # TODO probably `status` is unused
        status = status or self.STATUS_C
        if status == self.STATUS_D:
            return None
        # print(locals())
        self._fhd.seek(start)
        return self._data_from(self._fhd.read(size))

    def flush(self) -> None:
        """
        Flush storage buffer into file
        """
        if self.opened:
            self._fhd.flush()

    def fsync(self) -> None:
        """"
        Flush storage file into disk
        """
        if self.opened:
            fsync(self._fhd.fileno())


# classes for public use, done in this way because of
# generation static files with indexes (_index directory)


class Storage(IU_Storage):
    """General storage class for public use"""
