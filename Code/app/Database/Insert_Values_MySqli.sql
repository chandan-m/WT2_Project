delete from Orders_Details;
delete from Orders;
delete from Wallet;
delete from Cart;
delete from Views;
delete from Reviews;
delete from Product;
delete from Category;
delete from Seller;
delete from Customer;
delete from Users;

insert into Users values('cust1','pass','c');
insert into Users values('cust2','pass','c');
insert into Users values('cust3','pass','c');
insert into Users values('cust4','pass','c');
insert into Users values('cust5','pass','c');
insert into Users values('cust6','pass','c');
insert into Users values('cust7','pass','c');
insert into Users values('cust8','pass','c');
insert into Users values('cust9','pass','c');
insert into Users values('cust10','pass','c');
insert into Users values('sell1','pass','s');
insert into Users values('sell2','pass','s');
insert into Users values('sell3','pass','s');
insert into Users values('sell4','pass','s');
insert into Users values('sell5','pass','s');


insert into Customer values(1,'Chinmay','Srinivasan','8060197641','chinmay@gmail.com','26/4, 1st Cross, Ganesha Block, 8th Main, Mahalakshmi Layout',560096,'cust1');
insert into Customer values(2,'Munni','Saxena','9367487772','munni@gmail.com','Konnankunte, Kanakapura Main Road',560062,'cust2');
insert into Customer values(3,'Abhishek','Ghosh','5786398295','abhishek@yahoo.com','Dr. Rajkumar Road, Rajajinagar 2nd Stage',560010,'cust3');
insert into Customer values(4,'Namita','Sarma','9157040001','namita@gmail.com','17 Cross, HSR Layout',560102,'cust4');
insert into Customer values(5,'Ruchi','Madan','6362857472','ruchi@yahoo.com','11/17, 1st Block, Jayanagar',560011,'cust5');
insert into Customer values(6,'Hira','Rastogi','9984933232','hira@gmail.com','2/4, Langford Garden Road, Richmond Town',560025,'cust6');
insert into Customer values(7,'Esha','Ray','7553957543','odlyzko@gmail.com','3, Kumara Krupa Road, Madhavanagar',560001,'cust7');
insert into Customer values(8,'Siddharth','Wable','8308951998','esha.ray@gmail.com','1/74, 26th Main, Jayanagar 9th Block',560011,'cust8');
insert into Customer values(9,'Krishna','Goyal','7197417607','krishna.goyal@yahoo.com','No. 803, HAL 2nd Stage, Indiranagar',560008,'cust9');
insert into Customer values(10,'Gowri','Rao','8896289549','gowri1224@google.com','6, Lady Curzon Road',560001,'cust10');

insert into Seller values(1,'Rajanna','Kopla','9980173388','barapparaju@gmail.com','banashankari 3rd stagre',560085,'sell1');
insert into Seller values(2,'Cina','John','9980176688','youcantseeme@hotmail.com','gorugunte palya',560052,'sell2');
insert into Seller values(3,'Bhimanna','Gowda','9900199007','theycallmebheems@yahoo.co.in','binnypet 4th cross eta mall',566098,'sell3');
insert into Seller values(4,'Shilpa','Shetty','9343785136','iamshilpa@icloud.com','kamakshipalya',560084,'sell4');
insert into Seller values(5,'Mani','Kanta','9060910358','theycallmekunt@rediff.com','JP Nagar',560069,'sell5');

insert into Category values(1,'Phones');
insert into Category values(2,'Electronics');
insert into Category values(3,'Books');
insert into Category values(4,'Fashion');
insert into Category values(5,'Furniture');

insert into Product values(1,'Apple iPhone X','Apple',100000.0,10.0,'iPhone X features a 5.8-inch Super Retina display with HDR and True Tone. An all-screen design and a surgical-grade stainless steel band. Charges wirelessly. Resists water and dust. 12MP dual cameras with dual optical image stabilization. TrueDepth camera with Portrait mode and Portrait Lighting. Face ID lets you unlock and use Apple Pay with just a glance. Powered by the A11 Bionic chip, iPhone X supports augmented reality experiences in games and apps. ',50,1,1);
insert into Product values(2,'Apple iPhone 8','Apple',70000.0,25.0,'iPhone 8 features an all-glass design and an aerospace-grade aluminum band. Charges wirelessly. Resists water and dust. 4.7-inch Retina HD display with True Tone. 12MP camera with an advanced image signal processor. Powered by the A11 Bionic chip.',50,1,1);
insert into Product values(3,'Apple iPhone XS Max','Apple',150000.0,5.0,'iPhone XS Max features a 6.5-inch Super Retina display with custom-built OLED panels for an HDR display that provides the industry s best color accuracy, true blacks, and remarkable brightness. Advanced Face ID lets you securely unlock your iPhone, log in to apps, and pay with just a glance.',50,1,1);
insert into Product values(4,'Samsung Galaxy S9','Samsung',60000.0,0.0,'Super Speed Dual Pixel Camera Infinity Display: edge-to-edge immersive screen, enhancing your entertainment experience IP68 rating: withstands splashes, spills, and rain so it can take a dip, worry-free Fast Wireless Charging',50,1,1);
insert into Product values(5,'Samsung Galaxy Note9','Samsung',70000.0,0.0,'Galaxy Note has always put powerful technology in the hands of those who demand more. Now, the all new Galaxy Note9 surpass',50,1,1);
insert into Product values(6,'Samsung Galaxy S8','Samsung',40000.0,20.0,'Explore a world of endless possibilities with the Samsung Galaxy S8. Featuring the innovative Infinity Display, this smartphone offers a smooth, curved surface without sharp angles.',50,1,1);
insert into Product values(7,'OnePlus 6T','OnePlus',40000.0,0.0,'Unlock the speed with the new OnePlus 6T. Featuring our largest display ever and a resilient glass back, the OnePlus 6T was crafted with care and purpose.',50,1,1);
insert into Product values(8,'OnePlus 6','OnePlus',35000.0,0.0,'The Phone comes with a large 3300 mAh battery to support its 6.28 inch screen with Optic AMOLED display having a resolution of 1080 x 2280 at 402 ppi. The screen is also protected by a durable Scratch Resistant glass. OnePlus 6 boasts of dual primary camera of 16 + 20 MP megapixel and 16 megapixel front Camera.',50,1,1);
insert into Product values(9,'OnePlus 5T','OnePlus',30000.0,0.0,'OnePlus 5T is powered by an octa-core Qualcomm Snapdragon 835 processor that features 4 cores clocked at 2.45GHz and 4 cores clocked at 1.9GHz. It comes with 6GB of RAM. The OnePlus 5T runs Android 7.1.1 and is powered by a 3,300mAh non-removable battery. The OnePlus 5T supports Dash Charge fast charging.',50,1,1);
insert into Product values(10,'Sony DSC-H300 Point','Sony',13990.0,10.0,'The High zoom camera Sony Cyber-shot H300, with a powerful 35x optical zoom, brings your subject to you for beautiful, precise pictures. A 20.1MP sensor, HD video and creative features, let you capture detailed images and movies with ease.',50,2,2);
insert into Product values(11,'Canon EOS 1300D','Canon',25490.0,0.0,'The EOS 1300D packs in all the fun of photography, which is why we recommend it to users looking for their very first EOS DSLR camera. It uses an 18-megapixel APS-C size sensor and the DIGIC 4+ image processor - which even professional photographers recognize as high performance with core features',50,2,2);
insert into Product values(12,'Nikon D5300','Nikon',47990.0,40.0,'The Nikon D5300 is an ideal camera for advanced novices and those who want to get the most out of their photography sessions. Featuring a 24.2 megapixel DX-format CMOS sensor with EXPEED image processor, the D5300 shoots rich images with precise colour reproduction and sharp details. ',50,2,2);
insert into Product values(13,'Seagate 1 TB Wired External Hard Disk Drive','Seagate',4499.0,30.0,'1 TB PORTABLE SLIM HARD DRIVE USB 3.0',100,2,2);
insert into Product values(14,'Mi LED Smart TV 4A','Mi',22999.0,0.0,'The Mi LED TV 4A PRO dons features such as Full HD and HDR display, 64-bit Quad-core processor, DTS-HD audio, Google Voice Search, ultra-bright resolution, built-in Chromecast and Play Store',20,2,2);
insert into Product values(15,'LG Smart 80cm','LG',21999.0,0.0,'The secret behind LG TV s life-like color and wide viewing angle is the panel. Just as the quality of the beans determines the quality of the coffee, the quality of the panel determines the quality of the TV.',20,2,2);
insert into Product values(16,'Apple Watch Series 3','Apple',30900.0,0.0,'Low and high heart rate notifications. Emergency SOS. New Breathe watch faces. Automatic workout detection. New yoga and hiking workouts. Advanced features for runners like cadence and pace alerts. New head-to-head competitions.',50,2,2);
insert into Product values(17,'Inside the C - Suite','Harper Business',248.0,15.0,'21 Lessons from Top Management to Get Your Way in Business and in Life',100,3,3);
insert into Product values(18,'How to Lead Others','Bloomdsbury USA',323.0,15.0,'How to Lead Others aims to convey the basics of leadership in a way that is concise, relevant and practical by breaking down leadership into eight simple lessons',100,3,3);
insert into Product values(19,'Triple Dueces','Page Publishing Inc',639.0,0.0,'Triple Deuces goes deep inside the fences and walls of our jails and prisons to provide the reader with an unvarnished reality of how and why things happen ...',100,3,3);
insert into Product values(20,'The Da Vinci Code','Random House India',236.0,15.0,'The Da Vinci Code is a 2003 mystery thriller novel by Dan Brown. It follows "symbologist" Robert Langdon and cryptologist Sophie Neveu after a murder in the Louvre Museum in Paris causes them to become involved in a battle between the Priory of Sion and Opus Dei over the possibility of Jesus Christ having been a companion to Mary Magdalene.',100,3,3);
insert into Product values(21,'ALCHEMIST','HarperCollins',209.0,0.0,'The Alchemist by Paulo Coelho continues to change the lives of its readers forever. With more than two million copies sold around the world, The Alchemist has established itself as a modern classic, universally admired.',100,3,3);
insert into Product values(22,'Breaking India','Amaryllis',635.0,0.0,'Breaking India: Western Interventions in Dravidian and Dalit Faultlines is a book written by Rajiv Malhotra and Aravindan Neelakandan',100,3,3);
insert into Product values(23,'Top Notch Solid Men Henley Black T-Shirt','Henley',329.0,0.0,'You look Cool, Smart & Charming with the new collection of Top Notch Henely Neck T- Shirts.Top Notch belongs to Rajdhani Cotton which is One Of The Leading Brand For T Shirts, and provides you with the best quality Casual Shirt & T shirts.',20,4,4);
insert into Product values(24,'Peter England University Printed Men Polo Neck Mul','Peter England',479.0,0.0,'Make an exquisite style statement over the weekend with this printed green T-shirt from Peter England Casuals.',20,4,4);
insert into Product values(25,'Flying Machine Regular Mens Blue Jeans','Flying Machine',1899.0,0.0,'Fit: Regular. Fabric: COTTON. Mid Rise Jeans. Clean Look, Mid Rise',20,4,4);
insert into Product values(26,'Sara Self Design Fashion Poly Silk Saree','Saraa',449.0,0.0,'Saree Fabric : Ploy Silk, Saree Blouse Fabric : Poly Silk , Saree Work : Woven , Saree Blouse Work : Woven',10,4,4);
insert into Product values(27,'trendyfrog Women Checkered Casual Multicolor Shirt','trendyfrog',385.0,0.0,'Fabric: Cotton. Regular Fit, Full Sleeve. Pattern: Checkered',30,4,4);
insert into Product values(28,'Lee Skinny Womens Black Jeans','Lee',899.0,0.0,'With uber-comfy fits, trendiest of styles, cool features and endless choices, Lee is a fashion trove of urban clothing. ',20,4,4);
insert into Product values(29,'RoyalOak Milan Glass 4 Seater Dining Set','Royal Oak',11499.0,10.0,'A contemporary design that bodes well with most dining room themes, this Royal Oak dining set s table and chairs has sturdy metal legs. The four-seater dining set is compact in size and would snugly fit in small spaces. The chairs have an ergonomic design and foam on the backrest',10,5,5);
insert into Product values(30,'Nilkamal Baron Solid Wood Coffe Table','Nilkamal',2749.0,0.0,'Making provisions for elegant placement and storage space, the dark brown colored coffee table from the hub of Nilkamal is wide enough to spread out your dining accessories on. Crafted from a high quality material, it is going to last for years to come.',20,5,5);
insert into Product values(31,'Furn Central Metal Open Book Shelf','Furn',1499.0,0.0,'Metal Open Book Shelf, 5 Shelves, W x H x D: 52 cm x 144 cm x 31 cm (1 ft 8 in x 4 ft 8 in x 1 ft), DIY(Do-It-Yourself)',10,5,5);
insert into Product values(32,'Flipkart Perfect Homes Sirena TV Entertainment Unit','Flipkart',6999.0,0.0,'This TV unit is made of 100% safe European Standard Particle Board Engineered wood, with reduced formaldehyde emissions. The material used in this unit is laminated from all sides to give it full protection from moisture and other external factors.',40,5,5);
insert into Product values(33,'DZYN Furnitures Leatherette Office Executive Chair','DYZN',3999.0,0.0,'Premium Executive Chair with equisite finish. One touch Tilt-&-Lock Mechanism with Pressure Hydraulic. Dimensions: Height: 33" Length:22" Depth: 22" .',80,5,5);
insert into Product values(34,'Flipkart Perfect Homes Porto Fabric 4 Seater Sofa','Flipkart',24999.0,50.0,'Polycotton, Right Facing, Filling Material: Foam. W x H x D: 243 cm x 74 cm x 167 cm (7 ft 11 in x 2 ft 5 in x 5 ft 5 in). DIY - Basic assembly to be done with simple tools, comes with instructions',10,5,5);

insert into Reviews values(5,'The Best Device ! All i need is my Iphone.','2018-11-08',1,1);
insert into Reviews values(4,'Awesome phone with small disappointments','2018-08-12',2,1);
insert into Reviews values(5,'Apple have done a great job from maximizing the display to increasing the battery capacity','2018-11-14',3,2);
insert into Reviews values(3,'Didnt like battery life.','2018-08-30',4,4);
insert into Reviews values(4,'One of the best entry-level DSLR. Suitable for those who are newly starting photography.','2018-05-25',1,11);
insert into Reviews values(3,'Good slim external HDD, but slow like a snail.','2018-07-30',3,13);
insert into Reviews values(1,'Poor TV with no quality control','2019-01-22',5,14);
insert into Reviews values(5,'One of the best murder mystery novels I have read ever','2018-01-25',6,20);
insert into Reviews values(5,'Terrific purchase','2017-07-27',7,27);
insert into Reviews values(5,'nice unit. overall we all liked it.','2018-07-09',8,32);

insert into Views values(0,1,21);
insert into Views values(1,9,14);
insert into Views values(0,9,26);
insert into Views values(1,8,4);
insert into Views values(1,3,5);
insert into Views values(1,6,4);
insert into Views values(1,7,21);
insert into Views values(1,5,7);
insert into Views values(0,4,14);
insert into Views values(1,9,16);

insert into Cart values(1,90000.0,1,1);
insert into Cart values(1,40000.0,2,7);
insert into Cart values(2,6298.6,1,13);
insert into Cart values(7,2303.0,3,23);
insert into Cart values(5,1054.0,4,17);
insert into Cart values(1,12499.5,2,34);
insert into Cart values(3,5697.0,5,25);
insert into Cart values(1,6999.0,7,32);
insert into Cart values(1,22999.0,8,14);
insert into Cart values(1,70000.0,6,5);

INSERT INTO `wallet` (`Txn_id`, `Amount`, `Type`, `Tdate`, `Cust_id`) VALUES
(1, '100000.00', 'Cr', '2019-02-12 00:00:00', 1),
(2, '50000.00', 'Cr', '2019-02-13 00:00:00', 2),
(3, '40000.00', 'Cr', '2019-02-14 00:00:00', 3),
(4, '2000.00', 'Cr', '2019-02-15 00:00:00', 4),
(5, '100000.00', 'Cr', '2019-02-13 00:00:00', 5),
(6, '-90000.00', 'Dr', '2019-03-05 00:00:00', 1),
(7, '-29215.60', 'Dr', '2019-03-06 00:00:00', 2),
(8, '-40000.00', 'Dr', '2019-03-07 00:00:00', 3),
(9, '-1388.20', 'Dr', '2019-03-08 00:00:00', 4),
(10, '-12499.50', 'Dr', '2019-03-09 00:00:00', 5);

INSERT INTO `orders` (`Orders_id`, `OrdersDate`, `Status`, `N_items`, `TotalAmt`, `Cust_id`, `Txn_id`) VALUES
(1, '2020-04-14 02:00:00', 'Delivered', 1, '90000.00', 1, 1),
(2, '2020-04-06 00:00:00', 'Pending', 3, '29215.60', 2, 2),
(3, '2020-04-07 00:00:00', 'Delivered', 1, '40000.00', 3, 3),
(4, '2020-04-08 00:00:00', 'Delivered', 5, '1388.20', 4, 4),
(5, '2020-04-09 00:00:00', 'Pending', 1, '12499.50', 5, 5),
(6, '2020-04-02 00:00:00', 'Delivered', 1, '90000.00', 1, 6),
(7, '2020-04-14 00:00:00', 'Pending', 3, '29215.60', 2, 7),
(8, '2020-04-11 00:00:00', 'Delivered', 1, '40000.00', 3, 8),
(9, '2020-04-04 00:00:00', 'Delivered', 5, '1388.20', 4, 9),
(10, '2020-04-03 00:00:00', 'Pending', 1, '12499.50', 5, 10);

INSERT INTO `orders_details` (`Quantity`, `Amount`, `Orders_id`, `Prod_id`) VALUES
(16, '90000.00', 1, 1),
(26, '421.60', 2, 2),
(14, '28794.00', 2, 3),
(16, '40000.00', 3, 7),
(29, '401.20', 4, 6),
(36, '987.00', 4, 9),
(33, '12499.50', 5, 5),
(26, '90000.00', 6, 1),
(34, '987.00', 6, 5),
(27, '12499.50', 7, 4),
(19, '28794.00', 7, 8),
(21, '421.60', 8, 2),
(36, '40000.00', 9, 7),
(26, '401.20', 10, 4);