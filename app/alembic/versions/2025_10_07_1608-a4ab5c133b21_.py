"""empty message

Revision ID: a4ab5c133b21
Revises: a844093a7679
Create Date: 2025-10-07 16:08:44.449018

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "a4ab5c133b21"
down_revision: Union[str, Sequence[str], None] = "a844093a7679"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users", sa.Column("username", sa.String(length=30), nullable=False))
    op.create_index(op.f("ix_users_username"), "users", ["username"], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_users_username"), table_name="users")
    op.drop_column("users", "username")
