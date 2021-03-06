"""empty message

Revision ID: 0100dd620883
Revises: 70b99dc57257
Create Date: 2021-11-21 13:29:34.631751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0100dd620883'
down_revision = '70b99dc57257'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brand_distribution',
    sa.Column('brand_id', sa.Integer(), nullable=False),
    sa.Column('distributor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['brands.id'], ),
    sa.ForeignKeyConstraint(['distributor_id'], ['distributors.id'], ),
    sa.PrimaryKeyConstraint('brand_id', 'distributor_id')
    )
    op.drop_table('brand_products')
    op.drop_table('brand_contractors')
    op.add_column('distributors', sa.Column('brand_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'distributors', 'brands', ['brand_id'], ['id'])
    op.add_column('products', sa.Column('brand_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'products', 'brands', ['brand_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'brand_id')
    op.drop_constraint(None, 'distributors', type_='foreignkey')
    op.drop_column('distributors', 'brand_id')
    op.create_table('brand_contractors',
    sa.Column('brand_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('distributor_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['brands.id'], name='brand_contractors_brand_id_fkey'),
    sa.ForeignKeyConstraint(['distributor_id'], ['distributors.id'], name='brand_contractors_distributor_id_fkey'),
    sa.PrimaryKeyConstraint('brand_id', 'distributor_id', name='brand_contractors_pkey')
    )
    op.create_table('brand_products',
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('brand_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['brands.id'], name='brand_products_brand_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='brand_products_product_id_fkey'),
    sa.PrimaryKeyConstraint('product_id', 'brand_id', name='brand_products_pkey')
    )
    op.drop_table('brand_distribution')
    # ### end Alembic commands ###
