DROP DATABASE IF EXISTS ec;
CREATE DATABASE ec;


CREATE TABLE Users(
  Usersname varchar(15) PRIMARY KEY,
  Password varchar(30) NOT NULL,
  Type char(10)
);

CREATE TABLE Customer(
  Cust_id int PRIMARY KEY AUTO_INCREMENT,
  Fname varchar(20),
  Lname varchar(20),
  Ph_no char(10),
  E_mail varchar(50),
  Address varchar(100),
  Pin int,
  Usersname varchar(15) NOT NULL,
  FOREIGN KEY(Usersname) REFERENCES Users(Usersname) ON DELETE CASCADE
);

CREATE TABLE Seller(
  Seller_id int PRIMARY KEY AUTO_INCREMENT,
  Fname varchar(20),
  Lname varchar(20),
  Ph_no char(10),
  E_mail varchar(50),
  Address varchar(100),
  Pin int,
  Usersname varchar(15) NOT NULL,
  FOREIGN KEY(Usersname) REFERENCES Users(Usersname) ON DELETE CASCADE
);

CREATE TABLE Category(
  Category_id int PRIMARY KEY AUTO_INCREMENT,
  Name varchar(25)
);

CREATE TABLE Product(
  Prod_id int PRIMARY KEY AUTO_INCREMENT,
  Name varchar(100),
  Brand varchar(50),
  Price decimal(10,2),
  Discount decimal(5,2),
  Description varchar(500),
  Stock int,
  Category_id int NOT NULL,
  Seller_id int NOT NULL,
  FOREIGN KEY(Category_id) REFERENCES Category(Category_id) ON DELETE CASCADE,
  FOREIGN KEY(Seller_id) REFERENCES Seller(Seller_id) ON DELETE CASCADE
);

CREATE TABLE Reviews(
  Ratings int,
  Description varchar(200),
  Rdate datetime NOT NULL ,
  Cust_id int NOT NULL,
  Prod_id int NOT NULL,
  FOREIGN KEY(Cust_id) REFERENCES Customer(Cust_id) ON DELETE CASCADE,
  FOREIGN KEY(Prod_id) REFERENCES Product(Prod_id) ON DELETE CASCADE,
  UNIQUE(Cust_id,Prod_id)
);

CREATE TABLE Views(
  Likes int,
  Cust_id int NOT NULL,
  Prod_id int NOT NULL,
  FOREIGN KEY(Cust_id) REFERENCES Customer(Cust_id) ON DELETE CASCADE,
  FOREIGN KEY(Prod_id) REFERENCES Product(Prod_id) ON DELETE CASCADE,
  UNIQUE(Cust_id,Prod_id)
);

CREATE TABLE Cart(
  Quantity int,
  Amount decimal(10,2),
  Cust_id int NOT NULL,
  Prod_id int NOT NULL,
  FOREIGN KEY(Cust_id) REFERENCES Customer(Cust_id) ON DELETE CASCADE,
  FOREIGN KEY(Prod_id) REFERENCES Product(Prod_id) ON DELETE CASCADE,
  UNIQUE(Cust_id,Prod_id)
);

CREATE TABLE Wallet(
  Txn_id int PRIMARY KEY AUTO_INCREMENT,
  Amount decimal(10,2),
  Type char(2),
  Tdate datetime NOT NULL ,
  Cust_id int NOT NULL,
  FOREIGN KEY(Cust_id) REFERENCES Customer(Cust_id) ON DELETE CASCADE
);

CREATE TABLE Orders(
  Orders_id int PRIMARY KEY AUTO_INCREMENT,
  OrdersDate datetime NOT NULL ,
  Status varchar(20),
  N_items int,
  TotalAmt decimal(10,2),
  Cust_id int NOT NULL,
  Txn_id int NOT NULL UNIQUE,
  FOREIGN KEY(Cust_id) REFERENCES Customer(Cust_id) ON DELETE CASCADE,
  FOREIGN KEY(Txn_id) REFERENCES Wallet(Txn_id) ON DELETE CASCADE

);

CREATE TABLE Orders_Details(
  Quantity int,
  Amount decimal(10,2),
  Orders_id int NOT NULL,
  Prod_id int NOT NULL,
  FOREIGN KEY(Orders_id) REFERENCES Orders(Orders_id) ON DELETE CASCADE,
  FOREIGN KEY(Prod_id) REFERENCES Product(Prod_id) ON DELETE CASCADE,
  UNIQUE(Orders_id,Prod_id)
);