"""empty message

Revision ID: 433b48036d0c
Revises: dcd782df6e70
Create Date: 2025-10-10 16:13:34.957357

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "433b48036d0c"
down_revision: Union[str, Sequence[str], None] = "dcd782df6e70"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users", sa.Column("vk_id", sa.BigInteger(), nullable=True))
    op.create_unique_constraint(op.f("uq_users_vk_id"), "users", ["vk_id"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f("uq_users_vk_id"), "users", type_="unique")
    op.drop_column("users", "vk_id")
