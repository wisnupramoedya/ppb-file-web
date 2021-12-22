"""add presence model

Revision ID: 4d0b3f04becb
Revises: 
Create Date: 2021-12-22 10:09:53.842864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d0b3f04becb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('presence',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=55), nullable=True),
    sa.Column('nik', sa.String(length=16), nullable=True),
    sa.Column('image_profile', sa.String(length=255), nullable=True),
    sa.Column('image_ktp', sa.String(length=255), nullable=True),
    sa.Column('image_face', sa.String(length=255), nullable=True),
    sa.Column('image_mask', sa.String(length=255), nullable=True),
    sa.Column('mask', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_presence_name'), 'presence', ['name'], unique=False)
    op.create_index(op.f('ix_presence_nik'), 'presence', ['nik'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_presence_nik'), table_name='presence')
    op.drop_index(op.f('ix_presence_name'), table_name='presence')
    op.drop_table('presence')
    # ### end Alembic commands ###