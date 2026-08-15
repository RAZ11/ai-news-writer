"""add updated_at column

Revision ID: 566a6bf2b94f
Revises: 6f8f5f842473
Create Date: 2026-08-15 21:26:20.669673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '566a6bf2b94f'
down_revision: Union[str, Sequence[str], None] = '6f8f5f842473'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column(
        "news_articles",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=True
        )
    )

def downgrade() -> None:
    op.drop_column(
        "news_articles",
        "updated_at"
    )