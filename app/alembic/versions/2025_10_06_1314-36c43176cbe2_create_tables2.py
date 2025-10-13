"""create tables2

Revision ID: 36c43176cbe2
Revises: e8483481e80c
Create Date: 2025-10-06 13:14:01.287974

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "36c43176cbe2"
down_revision: Union[str, Sequence[str], None] = "e8483481e80c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "scores",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("subject", sa.String(length=55), nullable=False),
        sa.Column("point", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("telegram_id", sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=True)
    op.create_index(op.f("ix_users_telegram_id"), "users", ["telegram_id"], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_users_telegram_id"), table_name="users")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
    op.drop_table("scores")
