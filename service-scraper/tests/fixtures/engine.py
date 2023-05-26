import pytest
from sqlalchemy import create_mock_engine


@pytest.fixture(name="engine", autouse=True)
def engine(monkeypatch):
    def get_engine():
        return create_mock_engine("postgresql://", lambda x: x)

    monkeypatch.setattr("core.database.get_db_engine", get_engine)
