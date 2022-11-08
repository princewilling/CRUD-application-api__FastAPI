"""create posts table

Revision ID: 8f2e292fcd83
Revises: 
Create Date: 2022-11-08 16:38:38.091824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f2e292fcd83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('post', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('post  ')
    pass
