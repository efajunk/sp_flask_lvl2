"""added surname to author

Revision ID: b27207ed1e01
Revises: 0cab0aef4ee0
Create Date: 2021-09-06 19:48:35.999302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b27207ed1e01'
down_revision = '0cab0aef4ee0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('author_model', sa.Column('surname', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('author_model', 'surname')
    # ### end Alembic commands ###
