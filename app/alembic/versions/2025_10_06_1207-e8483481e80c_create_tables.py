"""create tables

Revision ID: e8483481e80c
Revises:
Create Date: 2025-10-06 12:07:26.792902

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "e8483481e80c"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
