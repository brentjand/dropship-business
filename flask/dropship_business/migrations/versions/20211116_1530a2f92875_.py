"""empty message

Revision ID: 1530a2f92875
Revises: 290e90d4853d
Create Date: 2021-11-16 11:03:58.817155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1530a2f92875'
down_revision = '290e90d4853d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('account_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'customers', 'accounts', ['account_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customers', type_='foreignkey')
    op.drop_column('customers', 'account_id')
    # ### end Alembic commands ###