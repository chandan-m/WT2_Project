--Simple Queries

--1. Name of customers ending with a
select fname from customer where fname like '%a' ;

--2. search for a product
select * from product where name like '%Sam%';

--3. Get all the product names and prices in a category.
select name,price from product where category_id=2;
select count(*) from product where category_id=2;

--4. No of likes and dislikes for a product
select count(*) as Likes from views where likes=1 and prod_id=14;
select count(*) as Dislikes from views where likes=0 and prod_id=14;

select prod_id,count(*) as Likes from views where likes=1 group by prod_id;
select prod_id,count(*) as Dislikes from views where likes=0 group by prod_id;

--5. Find all products on discount
select name,price,discount from product where discount>0;

--6. Wallet Balance
select sum(amount) from wallet where cust_id=1;
select customer.cust_id,fname,sum(amount) as Balance from Customer,Wallet where customer.cust_id=wallet.cust_id group by customer.cust_id;
--Wallet transaction history
select * from wallet where cust_id=1;

--7. Get avg ratings for each product.
select avg(ratings) from reviews where prod_id=1;
select p.prod_id,name,avg(ratings) as Avg_Ratings from product as p,reviews where p.prod_id=reviews.prod_id group by p.prod_id ;

--8. Get qty sold of a product.
select sum(quantity) as qty_sold  from orders_details where prod_id=23;

--9. Get the cart total.
select sum(amount) as total_amt,sum(quantity) as total_qty from cart where cust_id=2;

--10. All products in category phones in a price range of 20k-60k 
select name, price from product where price between 20000.00 and 60000.00 and category_id=1 order by price  ;

--11. Select all Products sold by a seller
select prod_id,name,price,stock from product where seller_id=3;


-- Complex Queries

--1. Find first time customers
select cust_id,fname,lname,ph_no
from customer
where cust_id NOT IN (select distinct cust_id from orders);

--2. Select the latest review for a product
select * from reviews
where rdate = (select max(rdate) from reviews where prod_id=1) and prod_id=1;

--3. Select all the pending orders of a seller
--All orders of a seller
select p.prod_id,p.name,o.orders_id,o.status,od.quantity,od.amount,o.OrdersDate
from product as p,orders_details as od,orders as o
where od.orders_id=o.orders_id and od.prod_id=p.prod_id and (od.prod_id in (select prod_id from product where seller_id=1))
order by o.OrdersDate;
--Only Pending orders of a Seller
select p.prod_id,p.name,o.orders_id,o.status,od.quantity,od.amount,o.OrdersDate
from product as p,orders_details as od,orders as o
where od.orders_id=o.orders_id and od.prod_id=p.prod_id and o.status='Pending' and od.prod_id in (select prod_id from product where seller_id=2)
order by o.OrdersDate;

--4. Select name,id, and cart total of all customers with items in cart.
select c.cust_id,c.fname,c.lname,sum(cart.amount) as Cart_Total,sum(cart.Quantity) as No_of_items
from customer as c,cart
where c.cust_id=cart.cust_id
group by cart.cust_id,c.cust_id
order by c.cust_id;

--5. Get the contents of cart of a customer.
select p.prod_id,p.name,p.price,p.discount,c.quantity,c.amount as total_amt
from product as p,cart as c
where p.prod_id=c.prod_id and c.cust_id=1;

--6. Get Order details for a particular order.
select p.prod_id,p.name,p.brand,s.fname as Seller_Name,od.quantity,od.amount
from product as p,orders as o,orders_details as od,seller as s
where p.prod_id=od.prod_id and od.orders_id=o.orders_id and s.seller_id=p.seller_id and o.orders_id=4;

--7. Get Details about order and customer for all pending orders shipped by a shipper
select o.orders_id,o.OrdersDate,o.n_items,c.fname,c.lname,c.ph_no,c.address,c.pin,c.e_mail
from orders as o join customer as c on o.cust_id=c.cust_id
where o.shipper_id=1 and o.status='Pending'
order by o.OrdersDate;

--8. Get all producta a customer has liked.
select prod_id,name,brand,price,discount
from product
where prod_id in(select prod_id from views where likes=1 and cust_id=9)
order by name;

--9. all products in a particular category in the cart
select p.prod_id,p.name,sum(c.quantity) as Total_Quantity 
from cart as c,product as p
where p.prod_id=c.prod_id and p.category_id=1
group by p.prod_id
order by p.prod_id;

--10. highest rated product in each category
select p.prod_id,p.name,p.category_id
from product as p,reviews as r
where p.prod_id=r.prod_id
group by p.category_id
having r.ratings=max(r.ratings);


--Order History
select o.orders_id,p.prod_id,p.name,p.brand,od.quantity,od.amount
from product as p,orders as o,orders_details as od,seller as s
where p.prod_id=od.prod_id and od.orders_id=o.orders_id and s.seller_id=p.seller_id and o.cust_id=4;

--Bill
select cust_id,ordersdate,n_items,totalamt from orders where orders_id=4;