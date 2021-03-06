"""empty message

Revision ID: 6f6872f9d32b
Revises: f71c64add923
Create Date: 2021-11-16 09:03:48.602913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f6872f9d32b'
down_revision = 'f71c64add923'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contracted_brands', sa.Column('distributor_id', sa.Integer(), nullable=False))
    op.drop_constraint('contracted_brands_product_id_fkey', 'contracted_brands', type_='foreignkey')
    op.create_foreign_key(None, 'contracted_brands', 'distributors', ['distributor_id'], ['id'])
    op.drop_column('contracted_brands', 'product_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contracted_brands', sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'contracted_brands', type_='foreignkey')
    op.create_foreign_key('contracted_brands_product_id_fkey', 'contracted_brands', 'products', ['product_id'], ['id'])
    op.drop_column('contracted_brands', 'distributor_id')
    # ### end Alembic commands ###
