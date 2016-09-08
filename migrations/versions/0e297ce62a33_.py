"""empty message

Revision ID: 0e297ce62a33
Revises: 772b42317cc7
Create Date: 2016-08-26 13:53:56.501165

"""

# revision identifiers, used by Alembic.
revision = '0e297ce62a33'
down_revision = '772b42317cc7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pile', sa.Column('upgrade_status', sa.SmallInteger(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pile', 'upgrade_status')
    ### end Alembic commands ###