"""empty message

Revision ID: 2debe9c54e79
Revises: 6b2679a00a1e
Create Date: 2025-03-05 16:18:57.891840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2debe9c54e79'
down_revision: Union[str, None] = '6b2679a00a1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
