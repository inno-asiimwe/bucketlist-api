"""empty message

Revision ID: af67c803c17f
Revises: 
Create Date: 2017-10-21 01:06:40.460003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af67c803c17f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=256), nullable=False),
    sa.Column('lastname', sa.String(length=256), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('bucketlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('bucketlist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bucketlist_id'], ['bucketlists.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('bucketlists')
    op.drop_table('users')
    op.drop_table('blacklist_token')
    # ### end Alembic commands ###