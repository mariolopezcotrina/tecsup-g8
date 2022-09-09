USE agenda;

-- En los ORM's (Django, SQLAlchemy, Prisma, TypeORM, Sequelize) aun no esta
-- contemplado la creacion de algo mas que fuesen tablas y relaciones.
-- No esta contemplado la creacion de Vistas (views), Procedimientos Almacenados
-- (store procedures), Funciones (Functions), Tablas de Expresion Comun
-- (Common Table Expressions), disparadores (Triggers) entre otros

CREATE VIEW listar_etiquetas_con_la_letra_A AS
SELECT * FROM importancias WHERE nombre LIKE '%a%';


SELECT * FROM listar_etiquetas_con_la_letra_A;