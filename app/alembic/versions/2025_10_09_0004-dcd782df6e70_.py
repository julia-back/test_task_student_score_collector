"""empty message

Revision ID: dcd782df6e70
Revises: 58294131704e
Create Date: 2025-10-09 00:04:14.997821

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "dcd782df6e70"
down_revision: Union[str, Sequence[str], None] = "58294131704e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column("users", "hashed_password", existing_type=sa.VARCHAR(), nullable=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column("users", "hashed_password", existing_type=sa.VARCHAR(), nullable=False)
