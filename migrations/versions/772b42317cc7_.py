"""empty message

Revision ID: 772b42317cc7
Revises: 111bb3098a0a
Create Date: 2016-08-26 13:48:21.133933

"""

# revision identifiers, used by Alembic.
revision = '772b42317cc7'
down_revision = '111bb3098a0a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pile', 'testmigration')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pile', sa.Column('testmigration', mysql.VARCHAR(length=255), nullable=True))
    ### end Alembic commands ###
