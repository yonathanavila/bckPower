-- Paso x: Alter foreign key constrain
ALTER TABLE at.resultados_scorings
ADD CONSTRAINT "FK_AT_Resultados_Scorings$EstaEnUna$AT_Ubicacion_Municipios"
FOREIGN KEY (id_scoring) REFERENCES at.scorings (id)
ON UPDATE CASCADE;

ALTER TABLE at.resultados_scorings
ADD CONSTRAINT "FK_AT_Resultados_Scorings$EstaEnUna$AT_Tipos_Resultados"
FOREIGN KEY (id_tipo_resultado) REFERENCES at.tipos_resultados (id)
ON UPDATE CASCADE;

-- Paso x: Alter primary key constrain
ALTER TABLE at.resultados_scorings
RENAME COLUMN "PK_09fe9ff3be190adc3bd3de588ef" TO "PK_AT_Resultados_Scorings_Id";

-- Paso x: Alter foreign key constrain
ALTER TABLE at.actividad_evento
ADD CONSTRAINT "FK_AT_Actividad_Evento$EstaEnUna$AT_Tipos_Visita"
FOREIGN KEY (id_tipo_visita) REFERENCES at.tipos_visita (id)
ON UPDATE CASCADE;


-- Paso x: Alter primary key constrain
ALTER TABLE at.resultados_scorings
RENAME COLUMN "" TO "PK_AT_Actividad_Evento_Id";

-- Paso x: Alter foreign key constrain
ALTER TABLE at.actividades
ADD CONSTRAINT "FK_AT_Actividades$EstaEnUna$AT_Proyectos"
FOREIGN KEY (id_proyecto) REFERENCES at.proyectos (id)
ON UPDATE CASCADE;

-- Paso x: Alter primary key constrain
ALTER TABLE at.actividades
RENAME COLUMN "PK_03490866fef1c23456f0e289d9c" TO "PK_AT_Actividades_Id";

-- Paso x: Alter foreign key constrain
ALTER TABLE at.actividades_areas
ADD CONSTRAINT "FK_AT_Actividades$EstaEnUna$AT_Proyectos"
FOREIGN KEY (id_area) REFERENCES grl.areas (id_area)
ON UPDATE CASCADE;

-- Paso x: Alter primary key constrain
ALTER TABLE at.actividades_areas
RENAME COLUMN "PK_03490866fef1c23456f0e289d9c" TO "PK_AT_Actividades_Areas_Id";
