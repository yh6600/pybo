"""empty message

Revision ID: 65a476adee1d
Revises: 378d074b469f
Create Date: 2023-12-22 11:31:05.808614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65a476adee1d'
down_revision = '378d074b469f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
