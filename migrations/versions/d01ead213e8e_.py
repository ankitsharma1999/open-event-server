"""empty message

Revision ID: d01ead213e8e
Revises: 291bb44bb014
Create Date: 2016-07-31 10:08:38.145030

"""

# revision identifiers, used by Alembic.
revision = 'd01ead213e8e'
down_revision = '291bb44bb014'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tax',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('tax_name', sa.String(), nullable=False),
    sa.Column('tax_rate', sa.Float(), nullable=False),
    sa.Column('tax_id', sa.String(), nullable=False),
    sa.Column('send_invoice', sa.Boolean(), nullable=True),
    sa.Column('registered_company', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip', sa.Integer(), nullable=True),
    sa.Column('invoice_footer', sa.String(), nullable=True),
    sa.Column('tax_include_in_price', sa.Boolean(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tax')
    ### end Alembic commands ###