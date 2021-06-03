"""add table for study group

Revision ID: 3d93e73b4145
Revises: 0faa45dff513
Create Date: 2021-06-03 13:46:31.872161

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3d93e73b4145'
down_revision = '0faa45dff513'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('abbr', sa.String(length=7), nullable=False),
    sa.Column('name', sa.String(length=4), nullable=True),
    sa.Column('course', sa.SmallInteger(), nullable=True),
    sa.Column('number', sa.SmallInteger(), nullable=True),
    sa.Column('datetime_reg', sa.DateTime(), nullable=True),
    sa.Column('datetime_upd', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_class_datetime_reg'), 'class', ['datetime_reg'], unique=False)
    op.add_column('user', sa.Column('id_group', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'user', 'class', ['id_group'], ['id'])
    op.drop_column('user', 'group')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('group', mysql.VARCHAR(length=16), nullable=True))
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'id_group')
    op.drop_index(op.f('ix_class_datetime_reg'), table_name='class')
    op.drop_table('class')
    # ### end Alembic commands ###
