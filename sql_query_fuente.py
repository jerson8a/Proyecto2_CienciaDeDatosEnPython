DDL_QUERY = '''
CREATE TABLE IF NOT EXISTS ingresos_municipales(
    id_ingresos_municipales INT PRIMARY KEY,
    identificador INT,
    ejercicio INT,
    mes INT,
    region NVARCHAR(100),
    codigoEntidad INT,
    entidad NVARCHAR(100),
    codigoDepartamento INT,
    departamento NVARCHAR(100),
    codigoClase INT,
    clase NVARCHAR(100),
    codigoSeccion INT,
    seccion NVARCHAR(100),
    codigoGrupo INT,
    grupo NVARCHAR(100),
    codigoRecurso INT,
    recurso NVARCHAR(100),
    asignado DECIMAL(12,8),
    modificado DECIMAL(12,8),
    vigente DECIMAL(12,8),
    devengado DECIMAL(12,8),
    percibido DECIMAL(12,8)
)

'''