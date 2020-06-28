"""create waypoints and scenarios tables

Revision ID: 49d0898c4802
Revises: 
Create Date: 2020-06-29 00:25:55.663316

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '49d0898c4802'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('isim_scenarios',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('notes', sa.VARCHAR(length=255), nullable=True),
    sa.Column('last_update', sqlite.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('isim_waypoints',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=10), nullable=True),
    sa.Column('lat', sa.FLOAT(precision=10), nullable=True),
    sa.Column('lon', sa.FLOAT(precision=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('isim_waypoints')
    op.drop_table('isim_scenarios')
    # ### end Alembic commands ###
