"""add superuser

Revision ID: 0a3b130ba11e
Revises: 401db8381531
Create Date: 2024-07-09 09:18:10.667944

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Boolean
from app.core.security import get_password_hash

# revision identifiers, used by Alembic.
revision = '0a3b130ba11e'
down_revision = '401db8381531'
branch_labels = None
depends_on = None


def upgrade():
    # Define the user table with appropriate columns
    user_table = table(
        'user',
        column('id', sa.Integer),
        column('email', String),
        column('hashed_password', String),
        column('is_superuser', Boolean),
        column('is_active', Boolean),
    )

    # Insert the superuser
    op.bulk_insert(
        user_table,
        [{
            'email': 'devops@hng.tech',
            'hashed_password': get_password_hash('devops11'),
            'is_superuser': True,
            'is_active': True,
        }]
    )


def downgrade():
    # Delete the superuser
    op.execute(
        "DELETE FROM user WHERE email='devops@hng.tech'"
    )
