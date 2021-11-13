-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 28-10-2021 a las 14:49:14
-- Versión del servidor: 8.0.27-0ubuntu0.20.04.1
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
-- Estructura de tabla para la tabla `denuncia`
--

CREATE TABLE `denuncia` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `category_id` int(11) NOT NULL,
  `created_at` date NOT NULL DEFAULT current_timestamp(),
  `closed_at` date DEFAULT NULL,
  `description` text NOT NULL,
  `coordenada_lat` varchar(200) NOT NULL,
  `coordenada_lng` varchar(200) NOT NULL,
  `operator_id` int(11) DEFAULT NULL,
  `denunciante_name` varchar(200) NOT NULL,
  `denunciante_last_name` varchar(200) DEFAULT NULL,
  `denunciante_phone` varchar(200) NOT NULL,
  `denunciante_email` varchar(200) NOT NULL,
  `seguimiento` text DEFAULT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'UNCONFIRMED'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denuncia_categoria`
--

CREATE TABLE `denuncia_categoria` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `denuncia_categoria`
--

INSERT INTO `denuncia_categoria` (`id`, `name`) VALUES
(1, 'calles'),
(2, 'alcantarillas'),
(3, 'desagües'),
(4, 'infraestructura');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `denuncia_seguimiento`
--

CREATE TABLE `denuncia_seguimiento` (
  `id` int(11) NOT NULL,
  `denuncia_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `created_at` date NOT NULL DEFAULT current_timestamp(),
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
-- Estructura de tabla para la tabla `Coordenadas`
--

CREATE TABLE `Coordenadas` (
  `id` int NOT NULL,
  `lat` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `lng` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

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
(27, 'recorrido_show'),
(28, 'zonas_index'),
(29, 'zonas_show'),
(30, 'zonas_import'),
(31, 'zonas_destroy'),
(32, 'denuncia_index'),
(33, 'denuncia_update'),
(34, 'denuncia_create'),
(35, 'denuncia_destroy');
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Punto_encuentro`
--

CREATE TABLE `Punto_encuentro` (
  `id` int NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `direccion` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `lat` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `lng` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `estado` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci COMMENT='Tabla para guardar los puntos de encuentro';

--
-- Volcado de datos para la tabla `Punto_encuentro`
--

INSERT INTO `Punto_encuentro` (`id`, `nombre`, `direccion`, `lat`, `lng`, `estado`, `telefono`, `email`) VALUES
(49, 'aaa', 'a', '-34.91591853170241', '-57.94755935668946', 'publicado', 'aaa', 'a@gmail.com'),
(50, 'f', 'f', '-34.917326130709455', '-57.9745101928711', 'despublicado', 'f', 'v@gmail.com');

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

--
-- Volcado de datos para la tabla `Recorrido`
--



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
(2, 27),
(1, 28),
(2, 28),
(1, 29),
(2, 29),
(1, 30),
(2, 30),
(2, 31),
(1, 32),
(1, 33),
(1, 34),
(2, 32),
(2, 33),
(2, 34),
(2, 35);
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
(17, 'admin@gmail.com', 'admin', 'pbkdf2:sha256:260000$8li21ZhHQatYCtTo$04ea4a5677e6ee78b16d21fd3dc4d349a646cc820f18c8c7fe0576db1decdbb8', 1, '2021-10-23 17:19:38', '2021-10-23 17:19:38', 'admin', 'admin'),
(18, 'ope@gmail.com', 'ope', 'pbkdf2:sha256:260000$2s4wfQpeAtSL56Z6$c0d8e6a7251d810d71617b9e42a322d821ca7a6d2babb7411fcc5b6c5ea48c56', 1, '2021-10-23 17:48:15', '2021-10-23 17:48:15', 'ope', 'ope');

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
(18, 1),
(1, 2),
(17, 2);



--
-- Estructura de tabla para la tabla `Zonas`
--
CREATE TABLE `Zonas` (
  `id` int NOT NULL,
  `codigo` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `estado` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `color` varchar(50) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `Zonas`
--

INSERT INTO `Zonas` (`id`, `codigo`, `nombre`, `estado`, `color`) VALUES
(1, '123aa', 'zonaa1', 'publicado', '#a40000'),
(2, '40058', '2ZONA', 'despublicado', '#a40000');
--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Configuracion`
--
ALTER TABLE `Configuracion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `denuncia`
--
ALTER TABLE `denuncia`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `denuncia_categoria`
--
ALTER TABLE `denuncia_categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `denuncia_seguimiento`
--
ALTER TABLE `denuncia_seguimiento`
  ADD PRIMARY KEY (`id`,`denuncia_id`),
  ADD KEY `denuncia_id` (`denuncia_id`);

--
-- Indices de la tabla `Coordenadas`
--
ALTER TABLE `Coordenadas`
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
-- Indices de la tabla `Zonas`
--
ALTER TABLE `Zonas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Configuracion`
--
ALTER TABLE `Configuracion`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `denuncia`
--
ALTER TABLE `denuncia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `denuncia_categoria`
--
ALTER TABLE `denuncia_categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `denuncia_seguimiento`
--
ALTER TABLE `denuncia_seguimiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


--
-- AUTO_INCREMENT de la tabla `Coordenadas`
--
ALTER TABLE `Coordenadas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Permiso`
--
ALTER TABLE `Permiso`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `Punto_encuentro`
--
ALTER TABLE `Punto_encuentro`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT de la tabla `Recorrido`
--
ALTER TABLE `Recorrido`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `Rol`
--
ALTER TABLE `Rol`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `Usuario`
--
ALTER TABLE `Usuario`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `Zonas`
--

ALTER TABLE `Zonas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

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