"""new fields in user model

Revision ID: 8751f8c55802
Revises: bc4b5ca9fe43
Create Date: 2023-01-14 18:28:17.764299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8751f8c55802'
down_revision = 'bc4b5ca9fe43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
