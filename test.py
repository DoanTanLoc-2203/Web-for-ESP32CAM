import MySQLManage as SQL
import json
# SQL.DeleteTable("product")
# SQL.CreateTable("product")
# SQL.InsertItem('product','Nitendo','Game','Nitendo Switch 3.0',10.99,6.99, 'https://game.haloshop.vn/image/cache/catalog/products/may-game/nintendo/nintendo-switch-2019-neon-00-700x700.jpg' ,5.0)
# SQL.InsertItem('product','TIMEWEAR','Watch','TIMEWEAR Commando Series Analog Digital Sports Watch for Men',3499.00,659.00, 'https://images-na.ssl-images-amazon.com/images/I/81qcmjX9TrL._UL1500_.jpg' ,5.0)
# SQL.InsertItem('product','RAWLINGS','Watch','Rawlings Coolflo T-Ball Helmet, Scarlet',31.12,28.53, 'https://images-na.ssl-images-amazon.com/images/I/41DNfMRaKtL._AC_.jpg' ,4.9)
info = SQL.SelectAll("product")