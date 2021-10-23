-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 23-10-2021 a las 16:16:58
-- Versión del servidor: 8.0.26-0ubuntu0.20.04.2
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyS`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administra_punto`
--

CREATE TABLE `administra_punto` (
  `id_usuario` int NOT NULL,
  `id_punto_encuentro` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Configuracion`
--

CREATE TABLE `Configuracion` (
  `id` int NOT NULL,
  `color1Privada` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `color2Privada` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `color3Privada` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `color1Publica` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `color2Publica` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `color3Publica` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `maxElementos` int NOT NULL,
  `criterio_orden` varchar(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `sitio_en_mantenimiento` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `Configuracion`
--

INSERT INTO `Configuracion` (`id`, `color1Privada`, `color2Privada`, `color3Privada`, `color1Publica`, `color2Publica`, `color3Publica`, `maxElementos`, `criterio_orden`, `sitio_en_mantenimiento`) VALUES
(2, '#a40000', '#4e9a06', '#75507b', '#C8F2D2', '#C7F1D1', '#C6FFD3', 4, 'Alfabetico', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Permiso`
--

CREATE TABLE `Permiso` (
  `id` int NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci COMMENT='Tabla para guardar los permisos del sistema';

--
-- Volcado de datos para la tabla `Permiso`
--

INSERT INTO `Permiso` (`id`, `nombre`) VALUES
(1, 'punto_encuentro_index'),
(2, 'punto_encuentro_new'),
(3, 'punto_encuentro_destroy'),
(4, 'punto_encuentro_update'),
(5, 'punto_encuentro_show'),
(6, 'usuario_index'),
(8, 'usuario_new'),
(9, 'usuario_destroy'),
(10, 'usuario_update'),
(11, 'usuario_show'),
(12, 'rol_index'),
(13, 'rol_new'),
(14, 'rol_destroy'),
(15, 'rol_update'),
(16, 'rol_show'),
(17, 'permiso_index'),
(18, 'permiso_new'),
(19, 'permiso_destroy'),
(20, 'permiso_update'),
(21, 'permiso_show'),
(22, 'configuracion_update'),
(23, 'recorrido_index'),
(24, 'recorrido_new'),
(25, 'recorrido_destroy'),
(26, 'recorrido_update'),
(27, 'recorrido_show');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Punto_encuentro`
--

CREATE TABLE `Punto_encuentro` (
  `id` int NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `direccion` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `coordenadas` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `estado` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci COMMENT='Tabla para guardar los puntos de encuentro';

--
-- Volcado de datos para la tabla `Punto_encuentro`
--

INSERT INTO `Punto_encuentro` (`id`, `nombre`, `direccion`, `coordenadas`, `estado`, `telefono`, `email`) VALUES
(22, 'zzzz', 'zzzzzz', 'zzzzz', 'publicado', 'zzzzzzzz', 'z@gmail.com'),
(26, 'hdsh', 'dfhs', 'dfh', 'publicado', 'dfhdfh', 'agshad@gmail.com'),
(27, 'c', 'c', 'c', 'publicado', 'c', 'aaa@gmail.com'),
(30, 'bb', 'b', 'bbb', 'despublicado', 'bb', 'bb@gmail.com'),
(31, 'nnn', 'nnn', 'nnn', 'publicado', 'nnn', 'n@gmail.com'),
(32, 'g', 'gg', 'gg', 'publicado', 'ggg', 'gas@thth.com'),
(34, 'vvv', 'vvv', 'vvv', 'publicado', 'v', 'v@gmail.com'),
(35, 'aaa', 'asasas', 'aaaa', 'despublicado', 'aaa', 'agsh@gmail.com'),
(36, 'd', 'sgsg', 'sgds', 'despublicado', 'dasf', 'a@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Recorrido`
--

CREATE TABLE `Recorrido` (
  `id` int NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `lat` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `lng` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `estado` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Rol`
--

CREATE TABLE `Rol` (
  `id` int NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci COMMENT='Tabla para guardar los roles del sistema';

--
-- Volcado de datos para la tabla `Rol`
--

INSERT INTO `Rol` (`id`, `nombre`) VALUES
(1, 'operador/a'),
(2, 'administrador/a');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol_tiene_permiso`
--

CREATE TABLE `rol_tiene_permiso` (
  `rol_id` int NOT NULL,
  `permiso_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci COMMENT='tabla de la relacion entre rol y permiso';

--
-- Volcado de datos para la tabla `rol_tiene_permiso`
--

INSERT INTO `rol_tiene_permiso` (`rol_id`, `permiso_id`) VALUES
(1, 1),
(2, 1),
(1, 2),
(2, 2),
(2, 3),
(1, 4),
(2, 4),
(1, 5),
(2, 5),
(2, 6),
(2, 8),
(2, 9),
(2, 10),
(2, 11),
(2, 12),
(2, 13),
(2, 14),
(2, 15),
(2, 16),
(2, 17),
(2, 18),
(2, 19),
(2, 20),
(2, 21),
(2, 22),
(1, 23),
(2, 23),
(1, 24),
(2, 24),
(2, 25),
(1, 26),
(2, 26),
(1, 27),
(2, 27);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Usuario`
--

CREATE TABLE `Usuario` (
  `id` int NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `updated_at` datetime NOT NULL,
  `created_at` datetime NOT NULL,
  `first_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `last_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci COMMENT='Tabla para almacenar los usuarios registrados en la pagina';

--
-- Volcado de datos para la tabla `Usuario`
--

INSERT INTO `Usuario` (`id`, `email`, `username`, `password`, `activo`, `updated_at`, `created_at`, `first_name`, `last_name`) VALUES
(1, 'gastonciancio@gmail.com', 'gciancio', 'pbkdf2:sha256:260000$5VWrriAIKIIziY9Z$e28f7c2af21cf06cb2011e86ff23c5900a886d6e6e4083fb079f8910ce1365fa', 1, '2021-10-17 14:55:53', '2021-10-13 16:39:57', 'gaston', 'ciancio'),
(13, 'a@gmail.com', 'a', 'pbkdf2:sha256:260000$CDiXyD3EauZPWaD1$6537c7497da55e60077a85d816fc32f7a94e1f422dc45a9d095f84fc58dad4cb', 1, '2021-10-17 15:24:06', '2021-10-17 13:21:22', 'aaaa', 'a'),
(14, 'bb@gmail.com', 'bb', 'pbkdf2:sha256:260000$YUUo7wF8blWWkXKG$265cfc6c671379305d4167c985344ace2d46177265f81dd5a708da342af8a5ad', 1, '2021-10-17 13:26:02', '2021-10-17 13:26:02', 'b', 'b'),
(15, 'c@gmail.com', 'c', 'pbkdf2:sha256:260000$SBNB6yH9rL9AtaoJ$65a2ece9ce85d31b7d386387baeb051aec0cdb9c94bad59c8b22c82ae24e2b5a', 1, '2021-10-17 13:34:27', '2021-10-17 13:26:32', 'c', 'ciancio'),
(16, 'v@gmail.com', 'v', 'pbkdf2:sha256:260000$KBRbQw16OhTV59FJ$44ae635d50c7b034abcc312b1f0d992c5a3cda2f9840fd26b7bf4c46ecd9d29a', 1, '2021-10-17 13:53:10', '2021-10-17 13:53:10', 'v', 'v');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_tiene_rol`
--

CREATE TABLE `usuario_tiene_rol` (
  `usuario_id` int NOT NULL,
  `rol_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci COMMENT='tabla de la relacion entre usuario y rol';

--
-- Volcado de datos para la tabla `usuario_tiene_rol`
--

INSERT INTO `usuario_tiene_rol` (`usuario_id`, `rol_id`) VALUES
(1, 1),
(13, 1),
(14, 1),
(15, 1),
(16, 1),
(1, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Configuracion`
--
ALTER TABLE `Configuracion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Permiso`
--
ALTER TABLE `Permiso`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Punto_encuentro`
--
ALTER TABLE `Punto_encuentro`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Recorrido`
--
ALTER TABLE `Recorrido`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Rol`
--
ALTER TABLE `Rol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rol_tiene_permiso`
--
ALTER TABLE `rol_tiene_permiso`
  ADD PRIMARY KEY (`rol_id`,`permiso_id`),
  ADD KEY `FK_permisoID` (`permiso_id`);

--
-- Indices de la tabla `Usuario`
--
ALTER TABLE `Usuario`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario_tiene_rol`
--
ALTER TABLE `usuario_tiene_rol`
  ADD PRIMARY KEY (`usuario_id`,`rol_id`),
  ADD KEY `FK_rolID` (`rol_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Configuracion`
--
ALTER TABLE `Configuracion`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `Permiso`
--
ALTER TABLE `Permiso`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `Punto_encuentro`
--
ALTER TABLE `Punto_encuentro`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `Recorrido`
--
ALTER TABLE `Recorrido`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Rol`
--
ALTER TABLE `Rol`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `Usuario`
--
ALTER TABLE `Usuario`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `rol_tiene_permiso`
--
ALTER TABLE `rol_tiene_permiso`
  ADD CONSTRAINT `FK_permisoID` FOREIGN KEY (`permiso_id`) REFERENCES `Permiso` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `foraingKeyRolID` FOREIGN KEY (`rol_id`) REFERENCES `Rol` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Filtros para la tabla `usuario_tiene_rol`
--
ALTER TABLE `usuario_tiene_rol`
  ADD CONSTRAINT `FK_rolID` FOREIGN KEY (`rol_id`) REFERENCES `Rol` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `FK_usuID` FOREIGN KEY (`usuario_id`) REFERENCES `Usuario` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;