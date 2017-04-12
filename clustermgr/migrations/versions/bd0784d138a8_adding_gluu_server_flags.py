"""adding gluu_server flags

Revision ID: bd0784d138a8
Revises: 2c3888be67c0
Create Date: 2017-04-05 17:25:17.804352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd0784d138a8'
down_revision = '2c3888be67c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ldap_server', sa.Column('gluu_server', sa.Boolean(), nullable=True))
    op.add_column('ldap_server', sa.Column('gluu_version', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ldap_server', 'gluu_version')
    op.drop_column('ldap_server', 'gluu_server')
    # ### end Alembic commands ###