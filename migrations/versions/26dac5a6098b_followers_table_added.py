"""followers table added

Revision ID: 26dac5a6098b
Revises: 8751f8c55802
Create Date: 2023-01-17 22:00:14.417024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26dac5a6098b'
down_revision = '8751f8c55802'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
