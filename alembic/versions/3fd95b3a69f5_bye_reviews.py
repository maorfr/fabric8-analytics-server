"""bye reviews

Revision ID: 3fd95b3a69f5
Revises: 49c27b67936f
Create Date: 2016-06-17 06:56:52.333454

"""

# revision identifiers, used by Alembic.
revision = '3fd95b3a69f5'
down_revision = '49c27b67936f'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('approved', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('comment', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('epv', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], name='review_user_fkey'),
    sa.PrimaryKeyConstraint('id', name='review_pkey')
    )
    ### end Alembic commands ###
