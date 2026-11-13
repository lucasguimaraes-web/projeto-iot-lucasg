-- Esquema padrão do banco ctiot — semana 3
--
-- Como root, uma única vez:
--   CREATE DATABASE ctiot CHARACTER SET utf8mb4;
--   CREATE USER 'ctiot_app'@'localhost' IDENTIFIED BY '<senha>';
--   GRANT SELECT, INSERT ON ctiot.* TO 'ctiot_app'@'localhost';
--
-- Depois:  mysql -u root -p ctiot < banco/schema.sql

CREATE TABLE IF NOT EXISTS dispositivos (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  nome       VARCHAR(50) NOT NULL UNIQUE,
  projeto    VARCHAR(30) NOT NULL,
  criado_em  TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS leituras (
  id              BIGINT AUTO_INCREMENT PRIMARY KEY,
  dispositivo_id  INT         NOT NULL,
  grandeza        VARCHAR(30) NOT NULL,
  valor           DOUBLE      NOT NULL,
  recebido_em     DATETIME(3) NOT NULL,
  FOREIGN KEY (dispositivo_id) REFERENCES dispositivos(id),
  INDEX idx_consulta (dispositivo_id, grandeza, recebido_em)
);
