# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dumbo.lib import PrimaryMapper, SecondaryMapper


class opt(object):

    def __init__(self, name, value):
        self.opt = (name, value)

    def __call__(self, func):
        if hasattr(func, 'opts'):
            func.opts.append(self.opt)
        else:
            func.opts = [self.opt]
        return func


def primary(mapper):
    return PrimaryMapper(mapper)

def secondary(mapper):
    return SecondaryMapper(mapper)
