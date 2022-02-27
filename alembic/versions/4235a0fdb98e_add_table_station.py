"""add Table station

Revision ID: 4235a0fdb98e
Revises: f7c5d2dc0e4e
Create Date: 2022-02-27 15:08:04.527229

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4235a0fdb98e'
down_revision = 'f7c5d2dc0e4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('typestation',
    sa.Column('id_type_station', sa.Integer(), nullable=False),
    sa.Column('name_type_station', sa.String(), nullable=False),
    sa.Column('name_table_station', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id_type_station'),
    sa.UniqueConstraint('id_type_station')
    )
    op.create_table('station',
    sa.Column('id_station', sa.Integer(), nullable=False),
    sa.Column('name_station', sa.String(), nullable=False),
    sa.Column('city_station', sa.String(), nullable=True),
    sa.Column('ip_station', sa.String(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitube', sa.Float(), nullable=True),
    sa.Column('id_type_station', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_type_station'], ['typestation.id_type_station'], ),
    sa.PrimaryKeyConstraint('id_station'),
    sa.UniqueConstraint('id_station')
    )
    op.create_table('tablealarm',
    sa.Column('id_message', sa.Integer(), nullable=False),
    sa.Column('id_station', sa.Integer(), nullable=True),
    sa.Column('id_type_message', sa.Integer(), nullable=True),
    sa.Column('id_text_message', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_acknowledge', sa.Boolean(), nullable=True),
    sa.Column('date_active', sa.Date(), nullable=True),
    sa.Column('date_out', sa.Date(), nullable=True),
    sa.Column('date_acknowledge', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['id_station'], ['station.id_station'], ),
    sa.PrimaryKeyConstraint('id_message'),
    sa.UniqueConstraint('id_message')
    )
    op.drop_table('con')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('con',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('now_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='con_pkey'),
    sa.UniqueConstraint('id', name='con_id_key')
    )
    op.drop_table('tablealarm')
    op.drop_table('station')
    op.drop_table('typestation')
    # ### end Alembic commands ###