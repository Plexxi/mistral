# Copyright 2016 OpenStack Foundation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Increase size of task_executions_v2.unique_key

Revision ID: 016
Revises: 015
Create Date: 2016-08-11 15:57:23.241734

"""

# revision identifiers, used by Alembic.
revision = '016'
down_revision = '015'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('task_executions_v2', 'unique_key', type_=sa.String(200))
