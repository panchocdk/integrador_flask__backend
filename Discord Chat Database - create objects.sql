CREATE DATABASE discord_chat;
USE discord_chat;

CREATE TABLE user_status(
		status_id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
        status_name VARCHAR(50) NOT NULL UNIQUE) Engine=InnoDB;
        
CREATE TABLE user_roles(
		role_id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
        role_name VARCHAR(50) NOT NULL UNIQUE) Engine=InnoDB;
        
CREATE TABLE users(
		user_id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
        user_name VARCHAR(50) NOT NULL,
        email VARCHAR(75) NOT NULL,
        first_name VARCHAR(75) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        password VARCHAR(30) NOT NULL,
        profile_image VARCHAR(100),
        date_of_birth DATE NOT NULL,
        status_id INT,
        role_id INT,
        CONSTRAINT fk_users_status_id FOREIGN KEY (status_id) REFERENCES user_status(status_id),
		CONSTRAINT fk_users_role_id FOREIGN KEY (role_id) REFERENCES user_roles(role_id)) Engine=InnoDB;
        
CREATE TABLE servers(
		server_id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
        server_name VARCHAR(30) NOT NULL,
        description VARCHAR(255),
        icon_image VARCHAR(100)) Engine=InnoDB;
        
CREATE TABLE user_servers(
		id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        server_id INT NOT NULL,
        creator BOOLEAN NOT NULL,
        CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id),
        CONSTRAINT fk_server_id FOREIGN KEY (server_id) REFERENCES servers(server_id)) Engine=InnoDB;
        
CREATE TABLE channels(
		channel_id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
        channel_name VARCHAR(100) NOT NULL,
        server_id INT NOT NULL,
        description VARCHAR(255),
        CONSTRAINT fk_sserver_id FOREIGN KEY (server_id) REFERENCES servers(server_id)) Engine=InnoDB;
        
CREATE TABLE chats(
		chat_id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
        channel_id INT NOT NULL,
        user_id INT NOT NULL,
        chat_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        message TEXT NOT NULL,
        CONSTRAINT fk_uuser_id FOREIGN KEY (user_id) REFERENCES users(user_id),
        CONSTRAINT fk_cchannel_id FOREIGN KEY (channel_id) REFERENCES channels(channel_id)) Engine=InnoDB;