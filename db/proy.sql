-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-10-2021 a las 15:01:08
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proys`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administra_punto`
--

CREATE TABLE `administra_punto` (
  `id_usuario` int(11) NOT NULL,
  `id_punto_encuentro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `configuracion`
--

CREATE TABLE `configuracion` (
  `id` int(11) NOT NULL,
  `color1Privada` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `color2Privada` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `color3Privada` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `color1Publica` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `color2Publica` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `color3Publica` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `maxElementos` int(11) NOT NULL,
  `criterio_orden` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `sitio_en_mantenimiento` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `configuracion`
--

INSERT INTO `configuracion` (`id`, `color1Privada`, `color2Privada`, `color3Privada`, `color1Publica`, `color2Publica`, `color3Publica`, `maxElementos`, `criterio_orden`, `sitio_en_mantenimiento`) VALUES
(2, '#a40000', '#4e9a06', '#75507b', '#C8F2D2', '#C7F1D1', '#C6FFD3', 4, 'Alfabetico', 0);

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
  `coordenates` text DEFAULT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'UNCONFIRMED',
  `operator_id` int(11) NOT NULL,
  `denunciante_name` varchar(200) NOT NULL,
  `denunciante_last_name` varchar(200) DEFAULT NULL,
  `denunciante_phone` varchar(200) NOT NULL,
  `denunciante_email` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `denuncia`
--

INSERT INTO `denuncia` (`id`, `title`, `category_id`, `created_at`, `closed_at`, `description`, `coordenates`, `status`, `operator_id`, `denunciante_name`, `denunciante_last_name`, `denunciante_phone`, `denunciante_email`) VALUES
(1, 'Alcantarilla defectuosa frente a Teatro Argentino', 1, '2021-10-24', '2021-10-24', 'Hay una alcantarilla defectuosa. Not much to say. Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus voluptas culpa soluta quibusdam non veritatis eligendi neque, maxime dolores, animi illum distinctio. Sunt explicabo modi vel saepe? Accusantium, vero voluptates? Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus vero ipsam impedit officiis doloribus delectus consequuntur. Sapiente mollitia, unde aliquid nam distinctio praesentium nemo aspernatur voluptas facilis? Consectetur, id earum! Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus quasi ipsa nobis nesciunt nulla, ab voluptatibus sapiente perferendis amet harum atque, voluptate numquam quaerat. Minima soluta iure maiores vitae animi.', '33.4444, -66.000', 'IN_PROGRESS', 18, 'Juan', 'Perez', '2215555555', 'juanperez@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permiso`
--

CREATE TABLE `permiso` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='Tabla para guardar los permisos del sistema';

--
-- Volcado de datos para la tabla `permiso`
--

INSERT INTO `permiso` (`id`, `nombre`) VALUES
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
(29, 'denuncia_index'),
(30, 'denuncia_update');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `punto_encuentro`
--

CREATE TABLE `punto_encuentro` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `direccion` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `coordenadas` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `estado` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='Tabla para guardar los puntos de encuentro';

--
-- Volcado de datos para la tabla `punto_encuentro`
--

INSERT INTO `punto_encuentro` (`id`, `nombre`, `direccion`, `coordenadas`, `estado`, `telefono`, `email`) VALUES
(22, 'zzzz', 'zzzzzz', 'zzzzz', 'publicado', 'zzzzzzzz', 'z@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recorrido`
--

CREATE TABLE `recorrido` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `lat` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `lng` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `estado` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `recorrido`
--

INSERT INTO `recorrido` (`id`, `nombre`, `descripcion`, `lat`, `lng`, `estado`) VALUES
(6, 'hdsh', 'h', 'h', 'h', 'despublicado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='Tabla para guardar los roles del sistema';

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id`, `nombre`) VALUES
(1, 'operador/a'),
(2, 'administrador/a');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol_tiene_permiso`
--

CREATE TABLE `rol_tiene_permiso` (
  `rol_id` int(11) NOT NULL,
  `permiso_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='tabla de la relacion entre rol y permiso';

--
-- Volcado de datos para la tabla `rol_tiene_permiso`
--

INSERT INTO `rol_tiene_permiso` (`rol_id`, `permiso_id`) VALUES
(1, 1),
(1, 2),
(1, 4),
(1, 5),
(1, 23),
(1, 24),
(1, 26),
(1, 27),
(1, 29),
(1, 30),
(2, 1),
(2, 2),
(2, 3),
(2, 4),
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
(2, 23),
(2, 24),
(2, 25),
(2, 26),
(2, 27),
(2, 29),
(2, 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `email` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `username` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `updated_at` datetime NOT NULL,
  `created_at` datetime NOT NULL,
  `first_name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `last_name` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='Tabla para almacenar los usuarios registrados en la pagina';

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `email`, `username`, `password`, `activo`, `updated_at`, `created_at`, `first_name`, `last_name`) VALUES
(1, 'gastonciancio@gmail.com', 'gciancio', 'pbkdf2:sha256:260000$5VWrriAIKIIziY9Z$e28f7c2af21cf06cb2011e86ff23c5900a886d6e6e4083fb079f8910ce1365fa', 1, '2021-10-17 14:55:53', '2021-10-13 16:39:57', 'gaston', 'ciancio'),
(17, 'admin@gmail.com', 'admin', 'pbkdf2:sha256:260000$8li21ZhHQatYCtTo$04ea4a5677e6ee78b16d21fd3dc4d349a646cc820f18c8c7fe0576db1decdbb8', 1, '2021-10-23 17:19:38', '2021-10-23 17:19:38', 'admin', 'admin'),
(18, 'ope@gmail.com', 'ope', 'pbkdf2:sha256:260000$2s4wfQpeAtSL56Z6$c0d8e6a7251d810d71617b9e42a322d821ca7a6d2babb7411fcc5b6c5ea48c56', 1, '2021-10-23 17:48:15', '2021-10-23 17:48:15', 'ope', 'ope');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_tiene_rol`
--

CREATE TABLE `usuario_tiene_rol` (
  `usuario_id` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci COMMENT='tabla de la relacion entre usuario y rol';

--
-- Volcado de datos para la tabla `usuario_tiene_rol`
--

INSERT INTO `usuario_tiene_rol` (`usuario_id`, `rol_id`) VALUES
(1, 1),
(1, 2),
(17, 2),
(18, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `configuracion`
--
ALTER TABLE `configuracion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `denuncia`
--
ALTER TABLE `denuncia`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `permiso`
--
ALTER TABLE `permiso`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `punto_encuentro`
--
ALTER TABLE `punto_encuentro`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `recorrido`
--
ALTER TABLE `recorrido`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rol_tiene_permiso`
--
ALTER TABLE `rol_tiene_permiso`
  ADD PRIMARY KEY (`rol_id`,`permiso_id`),
  ADD KEY `FK_permisoID` (`permiso_id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
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
-- AUTO_INCREMENT de la tabla `configuracion`
--
ALTER TABLE `configuracion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `denuncia`
--
ALTER TABLE `denuncia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `permiso`
--
ALTER TABLE `permiso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `punto_encuentro`
--
ALTER TABLE `punto_encuentro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `recorrido`
--
ALTER TABLE `recorrido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `rol_tiene_permiso`
--
ALTER TABLE `rol_tiene_permiso`
  ADD CONSTRAINT `FK_permisoID` FOREIGN KEY (`permiso_id`) REFERENCES `permiso` (`id`),
  ADD CONSTRAINT `foraingKeyRolID` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`);

--
-- Filtros para la tabla `usuario_tiene_rol`
--
ALTER TABLE `usuario_tiene_rol`
  ADD CONSTRAINT `FK_rolID` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`),
  ADD CONSTRAINT `FK_usuID` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
