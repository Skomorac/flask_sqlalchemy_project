"""Remove bio from User model

Revision ID: 3455932e7b36
Revises: f5aec3ad61f6
Create Date: 2024-06-01 10:38:01.220062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3455932e7b36'
down_revision = 'f5aec3ad61f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('bio')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', sa.VARCHAR(length=200), nullable=True))

    # ### end Alembic commands ###
