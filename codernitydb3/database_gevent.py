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

from codernitydb3.database_safe_shared import SafeDatabase
from codernitydb3.env import cdb_environment

try:
    from gevent.lock import RLock
except ImportError:
    raise NotImplementedError

cdb_environment['mode'] = "gevent"
cdb_environment['rlock_obj'] = RLock


class GeventDatabase(SafeDatabase):
    pass
