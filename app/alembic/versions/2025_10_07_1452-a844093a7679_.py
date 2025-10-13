"""empty message

Revision ID: a844093a7679
Revises: ccb104f7fbbd
Create Date: 2025-10-07 14:52:14.001955

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "a844093a7679"
down_revision: Union[str, Sequence[str], None] = "ccb104f7fbbd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column("users", "telegram_id", existing_type=sa.BIGINT(), nullable=True)
    op.drop_index(op.f("ix_users_telegram_id"), table_name="users")
    op.create_unique_constraint(None, "users", ["telegram_id"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, "users", type_="unique")
    op.create_index(op.f("ix_users_telegram_id"), "users", ["telegram_id"], unique=True)
    op.alter_column("users", "telegram_id", existing_type=sa.BIGINT(), nullable=False)
