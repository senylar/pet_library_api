import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

# Класс для хранения состояния (любых данных) передающихся между тестами
class SharedData():
    def __init__(self, db):
        self.session = db  # сохраняем сессию к базе данных

    def get_session(self):
        return self.session

# Создание фикстуры для базы данных
@pytest.fixture(scope="class")
def fixture_create_db(request):
    engine = create_engine("sqlite:///:memory:")  # Используем БД в памяти
    SessionLocal = sessionmaker(bind=engine)

    session = SessionLocal()

    session.execute(text("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)"))
    # Передаём сессию в тест
    request.cls.testdata = SharedData(session)

    yield session

    session.close()  # Очистка после теста

@pytest.mark.usefixtures("fixture_create_db")
class TestSuite():
    def test_check_record(self):
        print("Start test")
        # Используем фикстуру db_session
        session = self.testdata.get_session()
        session.execute(text("INSERT INTO test (id, name) VALUES (1, 'Alice')"))
        result = session.execute(text("SELECT * FROM test")).fetchall()  # Извлекаем все записи
        assert len(result) == 1  # Проверяем, что добавлена одна запись
        assert result[0][1] == 'Alice'  # Проверяем, что имя записи — 'Alice'
    def test_count_records(self):
        session = self.testdata.get_session()
        # Добавляем три записи в таблицу
        session.execute(text("INSERT INTO test (id, name) VALUES (2, 'Bob')"))
        session.execute(text("INSERT INTO test (id, name) VALUES (3, 'Charlie')"))
        session.execute(text("INSERT INTO test (id, name) VALUES (4, 'David')"))

        # Проверяем количество записей в таблице
        result = session.execute(text("SELECT * FROM test")).fetchall()
        assert len(result) == 3

x = """	1.	API — общее понятие, которое может включать в себя любые способы взаимодействия между программами.
	2.	HTTP-запрос — это конкретная реализация транспортного уровня (часто используемая в веб-приложениях).
	3.	REST API — это один из возможных стилей проектирования веб-API, основанный на семантике HTTP и принципах REST."""