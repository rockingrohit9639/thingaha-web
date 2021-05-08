"""empty message

Revision ID: 4de71d9ca1f6
Revises: 1e9c73166fb0
Create Date: 2021-05-08 18:10:34.796329

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4de71d9ca1f6'
down_revision = '1e9c73166fb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('addresses', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('addresses', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    op.add_column('attendances', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('attendances', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    op.add_column('donations', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('donations', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    op.alter_column('donations', 'paid_at',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)
    op.add_column('extrafunds', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('extrafunds', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    op.add_column('schools', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('schools', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    op.add_column('students', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('students', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    op.add_column('transfers', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('transfers', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    op.add_column('users', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('transfers', 'updated_at')
    op.drop_column('transfers', 'created_at')
    op.drop_column('students', 'updated_at')
    op.drop_column('students', 'created_at')
    op.drop_column('schools', 'updated_at')
    op.drop_column('schools', 'created_at')
    op.drop_column('extrafunds', 'updated_at')
    op.drop_column('extrafunds', 'created_at')
    op.alter_column('donations', 'paid_at',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.drop_column('donations', 'updated_at')
    op.drop_column('donations', 'created_at')
    op.drop_column('attendances', 'updated_at')
    op.drop_column('attendances', 'created_at')
    op.drop_column('addresses', 'updated_at')
    op.drop_column('addresses', 'created_at')
    # ### end Alembic commands ###
