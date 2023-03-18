"""Autogenerated

Revision ID: 5202edc2bec7
Revises: 
Create Date: 2023-03-18 19:25:15.047545

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5202edc2bec7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('publication', sa.String(), nullable=True),
    sa.Column('pubdate', sa.DateTime(), nullable=True),
    sa.Column('authors', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('body', postgresql.ARRAY(sa.String(), dimensions=1), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles')
    # ### end Alembic commands ###
