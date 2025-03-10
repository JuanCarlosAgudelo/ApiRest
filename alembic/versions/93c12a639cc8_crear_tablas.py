"""Crear tablas

Revision ID: 93c12a639cc8
Revises: 
Create Date: 2025-03-05 08:39:06.337904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93c12a639cc8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('computadores',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('referencia', sa.String(), nullable=False),
    sa.Column('marca', sa.String(), nullable=False),
    sa.Column('cpu', sa.String(), nullable=False),
    sa.Column('ram', sa.Integer(), nullable=False),
    sa.Column('almacenamiento', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_computadores_referencia'), 'computadores', ['referencia'], unique=True)
    op.create_table('almacen',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('referencia_comp', sa.String(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['referencia_comp'], ['computadores.referencia'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('referencia_comp')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('almacen')
    op.drop_index(op.f('ix_computadores_referencia'), table_name='computadores')
    op.drop_table('computadores')
    # ### end Alembic commands ###
