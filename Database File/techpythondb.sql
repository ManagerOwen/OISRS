-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 22, 2024 at 08:47 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `techpythondb`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_customuser'),
(22, 'Can change user', 6, 'change_customuser'),
(23, 'Can delete user', 6, 'delete_customuser'),
(24, 'Can view user', 6, 'view_customuser'),
(25, 'Can add page', 7, 'add_page'),
(26, 'Can change page', 7, 'change_page'),
(27, 'Can delete page', 7, 'delete_page'),
(28, 'Can view page', 7, 'view_page'),
(29, 'Can add specialization', 8, 'add_specialization'),
(30, 'Can change specialization', 8, 'change_specialization'),
(31, 'Can delete specialization', 8, 'delete_specialization'),
(32, 'Can view specialization', 8, 'view_specialization'),
(33, 'Can add tech reg', 9, 'add_techreg'),
(34, 'Can change tech reg', 9, 'change_techreg'),
(35, 'Can delete tech reg', 9, 'delete_techreg'),
(36, 'Can view tech reg', 9, 'view_techreg'),
(37, 'Can add hire', 10, 'add_hire'),
(38, 'Can change hire', 10, 'change_hire'),
(39, 'Can delete hire', 10, 'delete_hire'),
(40, 'Can view hire', 10, 'view_hire');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-07-21 15:51:28.251808', '1', 'omisrs', 1, '[{\"added\": {}}]', 7, 1),
(2, '2024-07-21 15:51:40.500728', '1', 'Automotive', 1, '[{\"added\": {}}]', 8, 1),
(3, '2024-07-21 15:51:47.331817', '2', 'Engineering', 1, '[{\"added\": {}}]', 8, 1),
(4, '2024-07-21 15:51:53.244162', '3', 'Chemical', 1, '[{\"added\": {}}]', 8, 1),
(5, '2024-07-21 15:52:18.526939', '4', 'Biological', 1, '[{\"added\": {}}]', 8, 1),
(6, '2024-07-21 15:53:56.655231', '1', '  - 0782750750', 1, '[{\"added\": {}}]', 9, 1),
(7, '2024-07-21 15:54:05.596925', '1', 'Hire #4 - Chris', 1, '[{\"added\": {}}]', 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'tasapp', 'customuser'),
(10, 'tasapp', 'hire'),
(7, 'tasapp', 'page'),
(8, 'tasapp', 'specialization'),
(9, 'tasapp', 'techreg');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-07-19 07:47:18.622314'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-07-19 07:47:19.769492'),
(3, 'auth', '0001_initial', '2024-07-19 07:47:26.534659'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-07-19 07:47:28.445061'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-07-19 07:47:28.623404'),
(6, 'auth', '0004_alter_user_username_opts', '2024-07-19 07:47:28.843390'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-07-19 07:47:28.890446'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-07-19 07:47:28.933006'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-07-19 07:47:28.988646'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-07-19 07:47:29.036351'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-07-19 07:47:29.085774'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-07-19 07:47:29.797907'),
(13, 'auth', '0011_update_proxy_permissions', '2024-07-19 07:47:29.939131'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-07-19 07:47:29.987302'),
(15, 'tasapp', '0001_initial', '2024-07-19 07:47:51.549298'),
(16, 'admin', '0001_initial', '2024-07-19 07:47:57.314485'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-07-19 07:47:57.443011'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-07-19 07:47:57.670184'),
(19, 'sessions', '0001_initial', '2024-07-19 07:47:59.497318'),
(20, 'tasapp', '0002_alter_customuser_profile_pic_and_more', '2024-07-21 15:57:13.771458'),
(21, 'tasapp', '0003_rename_doctor_id_hire_tech_id_and_more', '2024-07-22 18:42:03.393917');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0a5luj0kvbesfibg2fexvbv72zl73os6', 'e30:1sVx2F:QlpoX8ZNTIHzp1M_nkhnwfcyfyUufTx7o_whzTc-070', '2024-08-05 17:41:19.388486'),
('0w7qvngdu9wn6wkgx65socfg3fuvdj82', 'e30:1sVx5r:-TSKdoT-OH8uKZtHKyXoWWkFSM3t8DF6L-Jp4Qopy6A', '2024-08-05 17:45:03.503202'),
('8pw0s365ivof22ykse3ojbkw4qilafmn', 'e30:1sVx3w:tdKzdXtYKHVdqn4zpy9sRSW1fHWTAZFFG8fNCkk8udI', '2024-08-05 17:43:04.867621'),
('ufpl49z8c0zxlld5k24uysud7pu61mqz', 'e30:1sVx39:QfttGQvx_WZ0eesMiAt-mQrWhA9FZsbQcwMacRQ0eyA', '2024-08-05 17:42:15.918220');

-- --------------------------------------------------------

--
-- Table structure for table `tasapp_customuser`
--

CREATE TABLE `tasapp_customuser` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(50) NOT NULL,
  `profile_pic` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tasapp_customuser`
--

INSERT INTO `tasapp_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `user_type`, `profile_pic`) VALUES
(1, 'pbkdf2_sha256$600000$FD2kEenFHWgfssf6QVmbem$3O8x2UPcD7oFvfxQC1B3rwZpBXH8JIh1SADyCpqW2TE=', '2024-07-22 18:19:42.967297', 1, 'owen', '', '', 'owen@owen.com', 1, 1, '2024-07-21 15:45:50.624977', '1', 'media/profile_pic/18U_Standing_Rack_Cabinet_MHplzTi.png'),
(2, 'pbkdf2_sha256$600000$LNeW4CacF9KgEWMphejeg8$9oubVnUsrWySjVEiAvYRCCXVP/LrWxSZ7iBT9UD657s=', '2024-07-22 18:46:05.308021', 0, 'test', 'test', 'testing', 'testuser@gmail.com', 0, 1, '2024-07-21 15:58:50.526303', '2', 'media/profile_pic/18U_Standing_Rack_Cabinet_MHplzTi.png');

-- --------------------------------------------------------

--
-- Table structure for table `tasapp_customuser_groups`
--

CREATE TABLE `tasapp_customuser_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tasapp_customuser_user_permissions`
--

CREATE TABLE `tasapp_customuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tasapp_hire`
--

CREATE TABLE `tasapp_hire` (
  `id` bigint(20) NOT NULL,
  `hirenumber` int(11) NOT NULL,
  `fullname` varchar(250) NOT NULL,
  `mobilenumber` varchar(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `date_of_hire` varchar(250) NOT NULL,
  `time_of_hire` varchar(250) NOT NULL,
  `additional_msg` longtext NOT NULL,
  `remark` varchar(250) NOT NULL,
  `status` varchar(200) NOT NULL,
  `prescription` longtext NOT NULL,
  `recommendedtest` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `tech_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tasapp_hire`
--

INSERT INTO `tasapp_hire` (`id`, `hirenumber`, `fullname`, `mobilenumber`, `email`, `date_of_hire`, `time_of_hire`, `additional_msg`, `remark`, `status`, `prescription`, `recommendedtest`, `created_at`, `updated_at`, `tech_id_id`) VALUES
(1, 4, 'Chris', '0782750750', 'chris@gmail.com', '19/07/2024', '6pm', 'afafdsfsd', 'werwr', 'ewrwre', 'ewrwer', 'werwer', '2024-07-21 15:54:05.595909', '2024-07-21 15:54:05.595909', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tasapp_page`
--

CREATE TABLE `tasapp_page` (
  `id` bigint(20) NOT NULL,
  `pagetitle` varchar(250) NOT NULL,
  `address` varchar(250) NOT NULL,
  `aboutus` longtext NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobilenumber` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tasapp_page`
--

INSERT INTO `tasapp_page` (`id`, `pagetitle`, `address`, `aboutus`, `email`, `mobilenumber`, `created_at`, `updated_at`) VALUES
(1, 'omisrs', 'banda', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pretium tincidunt mattis. Proin imperdiet, odio nec viverra cursus, dui arcu vestibulum odio, at dictum sapien felis vel ipsum. Suspendisse potenti. Nullam non sem et lorem consequat ultrices. Mauris nisl odio, porta non elementum ut, laoreet vitae sem. Aenean ultricies lorem libero, id posuere nibh aliquet ut. Cras ornare facilisis ligula vel tempus. Nullam non libero pulvinar, posuere arcu sed, vestibulum nisi. Ut mollis semper vestibulum. Aliquam porttitor nisi eu nibh consequat, non pretium massa consequat. Nunc malesuada, neque placerat feugiat consequat, nunc erat viverra libero, ut imperdiet nibh odio nec orci. In tristique dignissim auctor. Mauris sit amet tempus purus. Pellentesque euismod, magna et suscipit imperdiet, elit augue fringilla dolor, congue porta nisi mi at ex.', 'info@omisrs.com', 700700700, '2024-07-21 15:51:28.249552', '2024-07-21 15:51:28.249552');

-- --------------------------------------------------------

--
-- Table structure for table `tasapp_specialization`
--

CREATE TABLE `tasapp_specialization` (
  `id` bigint(20) NOT NULL,
  `sname` varchar(200) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tasapp_specialization`
--

INSERT INTO `tasapp_specialization` (`id`, `sname`, `created_at`, `updated_at`) VALUES
(1, 'Automotive', '2024-07-21 15:51:40.498440', '2024-07-21 15:51:40.498440'),
(2, 'Engineering', '2024-07-21 15:51:47.329597', '2024-07-21 15:51:47.329597'),
(3, 'Chemical', '2024-07-21 15:51:53.242167', '2024-07-21 15:51:53.242167'),
(4, 'Biological', '2024-07-21 15:52:18.525443', '2024-07-21 15:52:18.525443');

-- --------------------------------------------------------

--
-- Table structure for table `tasapp_techreg`
--

CREATE TABLE `tasapp_techreg` (
  `id` bigint(20) NOT NULL,
  `mobilenumber` varchar(11) NOT NULL,
  `regdate_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint(20) DEFAULT NULL,
  `specialization_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tasapp_techreg`
--

INSERT INTO `tasapp_techreg` (`id`, `mobilenumber`, `regdate_at`, `updated_at`, `admin_id`, `specialization_id_id`) VALUES
(1, '0782750750', '2024-07-21 15:53:56.651524', '2024-07-21 15:53:56.651524', 1, 1),
(2, '0782750000', '2024-07-21 15:58:52.087241', '2024-07-21 15:58:52.087241', 2, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_tasapp_customuser_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `tasapp_customuser`
--
ALTER TABLE `tasapp_customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `tasapp_customuser_groups`
--
ALTER TABLE `tasapp_customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tasapp_customuser_groups_customuser_id_group_id_e3017c75_uniq` (`customuser_id`,`group_id`),
  ADD KEY `tasapp_customuser_groups_group_id_2892936b_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `tasapp_customuser_user_permissions`
--
ALTER TABLE `tasapp_customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tasapp_customuser_user_p_customuser_id_permission_33c3d3e7_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `tasapp_customuser_us_permission_id_eb0d203b_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `tasapp_hire`
--
ALTER TABLE `tasapp_hire`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tasapp_hire_tech_id_id_510970c8_fk_tasapp_techreg_id` (`tech_id_id`);

--
-- Indexes for table `tasapp_page`
--
ALTER TABLE `tasapp_page`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tasapp_specialization`
--
ALTER TABLE `tasapp_specialization`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tasapp_techreg`
--
ALTER TABLE `tasapp_techreg`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `admin_id` (`admin_id`),
  ADD KEY `tasapp_techreg_specialization_id_id_48232fb2_fk_tasapp_sp` (`specialization_id_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `tasapp_customuser`
--
ALTER TABLE `tasapp_customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tasapp_customuser_groups`
--
ALTER TABLE `tasapp_customuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tasapp_customuser_user_permissions`
--
ALTER TABLE `tasapp_customuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tasapp_hire`
--
ALTER TABLE `tasapp_hire`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tasapp_page`
--
ALTER TABLE `tasapp_page`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tasapp_specialization`
--
ALTER TABLE `tasapp_specialization`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tasapp_techreg`
--
ALTER TABLE `tasapp_techreg`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_tasapp_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `tasapp_customuser` (`id`);

--
-- Constraints for table `tasapp_customuser_groups`
--
ALTER TABLE `tasapp_customuser_groups`
  ADD CONSTRAINT `tasapp_customuser_gr_customuser_id_e6ccabab_fk_tasapp_cu` FOREIGN KEY (`customuser_id`) REFERENCES `tasapp_customuser` (`id`),
  ADD CONSTRAINT `tasapp_customuser_groups_group_id_2892936b_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `tasapp_customuser_user_permissions`
--
ALTER TABLE `tasapp_customuser_user_permissions`
  ADD CONSTRAINT `tasapp_customuser_us_customuser_id_e4c4fd68_fk_tasapp_cu` FOREIGN KEY (`customuser_id`) REFERENCES `tasapp_customuser` (`id`),
  ADD CONSTRAINT `tasapp_customuser_us_permission_id_eb0d203b_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `tasapp_hire`
--
ALTER TABLE `tasapp_hire`
  ADD CONSTRAINT `tasapp_hire_tech_id_id_510970c8_fk_tasapp_techreg_id` FOREIGN KEY (`tech_id_id`) REFERENCES `tasapp_techreg` (`id`);

--
-- Constraints for table `tasapp_techreg`
--
ALTER TABLE `tasapp_techreg`
  ADD CONSTRAINT `tasapp_techreg_admin_id_adc74278_fk_tasapp_customuser_id` FOREIGN KEY (`admin_id`) REFERENCES `tasapp_customuser` (`id`),
  ADD CONSTRAINT `tasapp_techreg_specialization_id_id_48232fb2_fk_tasapp_sp` FOREIGN KEY (`specialization_id_id`) REFERENCES `tasapp_specialization` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
