-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 10, 2020 at 04:48 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingmic`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `sno` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`sno`, `name`, `email`, `msg`, `date`) VALUES
(20, 'sumon', 'sumon@gmail.com', 'Cristiano is the best', '2020-06-04 21:49:35'),
(22, 'me', 'niloy@gmail.com', 'best of best', '2020-06-05 10:55:36');

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text DEFAULT NULL,
  `phone_num` int(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(1, 'sumon', 0, '24252552', '2020-06-01 17:44:40', 'firstpost@gmail.com'),
(2, 'sumonislam', 1714296673, 'I love You shairy', '2020-06-01 18:08:52', 'sumon@gmail.com'),
(4, 'sumon two', 171429667, 'I love You shairy', '2020-06-02 01:10:59', 'sumon2@gmail.com'),
(5, 'wr35t', 1714294667, 'wsrtwtw', '2020-06-02 02:46:05', 'sumon2qr@gmail.com'),
(6, 'gf4egt4', 2147483647, '2e2rffr', '2020-06-02 02:47:51', 'sum2on2qr@gmail.com'),
(7, 'md sumon', 2147483647, 'mist', '2020-06-02 02:50:26', 'sumon3255.sms@gmail.com'),
(8, 'yetyey', 25425, 'tgtwet', '2020-06-02 02:53:43', 'tetyeyt');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tag_line` varchar(15) NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tag_line`, `slug`, `content`, `img_file`, `date`) VALUES
(2, 'MY first Post', 'Learn something', 'second-post', 'Ccreative thoughts, new imaginations in form of device or method\".[1] Innovation is often also viewed as the application of better solutions that meet new requirements, unarticulated needs, or existing market needs.[2] Such innovation takes place through the provision of more-effective products, processes, services, technologies, or business models that are made available to markets, governments and society. An innovation is something original and more effective and, as a consequence, new, that \"breaks into\" the market or society.[3] Innovation is related to, but not the same as, invention,[4] as innovation is more apt to involve the practical implementation of an invention (ie new / improved ability) to make a meaningful impact in the market or society,[5] and not all innovations require an invention. Innovation often[quantify] manifests itself via the engineering process, when the problem being solved is of a technical or scientific nature. The opposite of innovation is exnovation.   ', 'about-bg.jpg', '2020-06-04 21:28:51'),
(13, 'My second post', 'Gain More Knowl', 'second-post', ' Knowledge is a familiarity, awareness, or understanding of someone or something, such as facts, information, descriptions, or skills, which is acquired through experience or education by perceiving, discovering, or learning.\r\n\r\nKnowledge can refer to a theoretical or practical understanding of a subject. It can be implicit (as with practical skill or expertise) or explicit (as with the theoretical understanding of a subject); it can be more or less formal or systematic.[1] In philosophy, the study of knowledge is called epistemology; the philosopher Plato famously defined knowledge as \"justified true belief\", though this definition is now thought by some analytic philosophers[citation needed] to be problematic because of the Gettier problems, while others defend the platonic definition.[2] However, several definitions of knowledge and theories to explain it exist.', 'about-bg.jpg', '2020-06-04 21:25:08'),
(16, 'Cristiano Ronaldo', 'Legend', 'cristiano', ' Cristiano Ronaldo is the first player to win the UEFA Champions League five \r\ntimes. He also holds the record for the most number of goals scored in Real \r\nMadrid\'s history. untill this day,he remains the only player in the history of\r\nLa Liga to score 30 or more goals in six consecutive seasons.', 'cris.jpg', '2020-06-04 23:21:03');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
