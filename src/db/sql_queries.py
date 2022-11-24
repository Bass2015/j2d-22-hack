

DATABASE = {
    'port': 5430,
    'host': 'localhost',
    'username': 'bass',
    'name': 'j2d',
    'password': '1234'
}

CREATE = f"CREATE DATABASE {DATABASE['name']};"
GRANT = f"GRANT ALL PRIVILEGES ON DATABASE {DATABASE['name']} TO {DATABASE['username']};"
