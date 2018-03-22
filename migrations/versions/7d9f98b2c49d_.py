"""empty message

Revision ID: 7d9f98b2c49d
Revises: 
Create Date: 2018-03-22 04:03:38.292196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d9f98b2c49d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('gender', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('biography', sa.Text(length=300), nullable=False),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.Column('created_on', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('userid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
