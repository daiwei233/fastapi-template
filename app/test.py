from pydantic.networks import PostgresDsn


class MysqlDsn(PostgresDsn):
    allowed_schemes = {'mysql+pymysql'}
    user_required = True


db = 'db'

a = MysqlDsn.build(
    scheme="mysql+pymysql",
    user="root",
    password="password",
    host="127.0.0.1:3306",
    path=f"/{db or ''}",
)

print(a)