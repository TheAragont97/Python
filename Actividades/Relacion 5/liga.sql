-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-05-2020 a las 02:05:26
-- Versión del servidor: 10.4.8-MariaDB
-- Versión de PHP: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `liga`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipo`
--

CREATE TABLE `equipo` (
  `cod_equipo` int(2) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `estadio` varchar(30) NOT NULL,
  `aforo` float NOT NULL,
  `fundacion` date NOT NULL,
  `ciudad` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `equipo`
--

INSERT INTO `equipo` (`cod_equipo`, `nombre`, `estadio`, `aforo`, `fundacion`, `ciudad`) VALUES
(3, 'Mirandes', 'Miranda', 5000, '1939-01-01', 'Miranda del Ebro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `goles`
--

CREATE TABLE `goles` (
  `cod_gol` int(3) NOT NULL,
  `cod_partido` int(2) NOT NULL,
  `momento_gol` int(3) DEFAULT NULL,
  `descripcion` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `goles`
--

INSERT INTO `goles` (`cod_gol`, `cod_partido`, `momento_gol`, `descripcion`) VALUES
(8, 6, 99, 'cabeza');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugador`
--

CREATE TABLE `jugador` (
  `cod_jugador` int(3) NOT NULL,
  `cod_equipo` int(2) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `fecha_nac` date NOT NULL,
  `posicion` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `jugador`
--

INSERT INTO `jugador` (`cod_jugador`, `cod_equipo`, `nombre`, `fecha_nac`, `posicion`) VALUES
(4, 3, 'Raúl', '1998-01-01', 'Portero');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partidos`
--

CREATE TABLE `partidos` (
  `cod_partido` int(2) NOT NULL,
  `cod_equipo` int(2) NOT NULL,
  `fecha` date NOT NULL,
  `gol_casa` int(2) NOT NULL,
  `gol_fuera` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `partidos`
--

INSERT INTO `partidos` (`cod_partido`, `cod_equipo`, `fecha`, `gol_casa`, `gol_fuera`) VALUES
(6, 3, '1999-01-01', 5, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presidente`
--

CREATE TABLE `presidente` (
  `dni` varchar(9) NOT NULL,
  `cod_equipo` int(2) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellidos` varchar(20) NOT NULL,
  `fec_nacimiento` date NOT NULL,
  `ano_presidente` date NOT NULL,
  `nom_equipo` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `presidente`
--

INSERT INTO `presidente` (`dni`, `cod_equipo`, `nombre`, `apellidos`, `fec_nacimiento`, `ano_presidente`, `nom_equipo`) VALUES
('12345678H', 3, 'Paco', 'Gonzales', '1987-01-01', '2000-01-01', 'Mirandes');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipo`
--
ALTER TABLE `equipo`
  ADD PRIMARY KEY (`cod_equipo`);

--
-- Indices de la tabla `goles`
--
ALTER TABLE `goles`
  ADD PRIMARY KEY (`cod_gol`),
  ADD KEY `cod_partido` (`cod_partido`);

--
-- Indices de la tabla `jugador`
--
ALTER TABLE `jugador`
  ADD PRIMARY KEY (`cod_jugador`),
  ADD KEY `cod_equipo` (`cod_equipo`);

--
-- Indices de la tabla `partidos`
--
ALTER TABLE `partidos`
  ADD PRIMARY KEY (`cod_partido`),
  ADD KEY `cod_equipo` (`cod_equipo`);

--
-- Indices de la tabla `presidente`
--
ALTER TABLE `presidente`
  ADD PRIMARY KEY (`dni`),
  ADD KEY `cod_equipo` (`cod_equipo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipo`
--
ALTER TABLE `equipo`
  MODIFY `cod_equipo` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `goles`
--
ALTER TABLE `goles`
  MODIFY `cod_gol` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `jugador`
--
ALTER TABLE `jugador`
  MODIFY `cod_jugador` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `partidos`
--
ALTER TABLE `partidos`
  MODIFY `cod_partido` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `goles`
--
ALTER TABLE `goles`
  ADD CONSTRAINT `goles_ibfk_1` FOREIGN KEY (`cod_partido`) REFERENCES `partidos` (`cod_partido`);

--
-- Filtros para la tabla `jugador`
--
ALTER TABLE `jugador`
  ADD CONSTRAINT `jugador_ibfk_1` FOREIGN KEY (`cod_equipo`) REFERENCES `equipo` (`cod_equipo`);

--
-- Filtros para la tabla `partidos`
--
ALTER TABLE `partidos`
  ADD CONSTRAINT `partidos_ibfk_1` FOREIGN KEY (`cod_equipo`) REFERENCES `equipo` (`cod_equipo`);

--
-- Filtros para la tabla `presidente`
--
ALTER TABLE `presidente`
  ADD CONSTRAINT `presidente_ibfk_1` FOREIGN KEY (`cod_equipo`) REFERENCES `equipo` (`cod_equipo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
