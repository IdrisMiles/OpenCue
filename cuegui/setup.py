#  Copyright (c) 2018 Sony Pictures Imageworks Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as fp:
    long_description = fp.read()

setup(
    name='cuegui',
    # TODO(cipriano) This version number should be dynamic. (b/121159512)
    version='0.1',
    description='The OpenCue management GUI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/imageworks/OpenCue',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cuegui=cuegui.__main__:main'
        ]
    },
)
