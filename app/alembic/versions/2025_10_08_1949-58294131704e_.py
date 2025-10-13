"""empty message

Revision ID: 58294131704e
Revises: 51807b8f22f5
Create Date: 2025-10-08 19:49:59.089842

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "58294131704e"
down_revision: Union[str, Sequence[str], None] = "51807b8f22f5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("scores", sa.Column("user_id", sa.Integer(), nullable=False))
    op.drop_constraint(op.f("fk_scores_user_owner_users"), "scores", type_="foreignkey")
    op.create_foreign_key(op.f("fk_scores_user_id_users"), "scores", "users", ["user_id"], ["id"])
    op.drop_column("scores", "user_owner")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "scores",
        sa.Column("user_owner", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(op.f("fk_scores_user_id_users"), "scores", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_scores_user_owner_users"),
        "scores",
        "users",
        ["user_owner"],
        ["id"],
    )
    op.drop_column("scores", "user_id")
