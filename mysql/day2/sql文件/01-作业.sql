-- A. 查询卖的最贵的商品的名称
-- 1. 获取商品中最贵的价格
SELECT MAX(shop_price) FROM ecs_goods;
-- 2. 通过价格获取对应商品
SELECT goods_name FROM ecs_goods WHERE shop_price = 3010;
-- 测试：SELECT goods_name FROM ecs_goods ORDER BY shop_price DESC LIMIT 3;
-- 子查询
SELECT goods_name FROM ecs_goods WHERE shop_price = (SELECT MAX(shop_price) FROM ecs_goods);

-- B. 查询商品品牌为”仓品”的 所有商品名称和商品价格
-- 1. 通过品牌名获取品牌的id
SELECT brand_id FROM ecs_brand WHERE brand_name = '仓品';
-- 2. 通过品牌id获取商品信息
SELECT goods_name, shop_price FROM ecs_goods WHERE brand_id = 15;
-- 子查询
SELECT goods_name, shop_price FROM ecs_goods WHERE brand_id = (SELECT brand_id FROM ecs_brand WHERE brand_name = '仓品');

-- C. 查询商品品牌为”仓品”的 所有商品名称和商品价格 按照价格降序排列
SELECT goods_name, shop_price FROM ecs_goods WHERE brand_id = (SELECT brand_id FROM ecs_brand WHERE brand_name = '仓品') ORDER BY shop_price DESC;

-- D. 查询每个商品品牌的商品数量
SELECT brand_id, COUNT(*) FROM ecs_goods 
GROUP BY brand_id;

-- 内连接第一种方式
-- ecs_brand b ecs_goods g
SELECT b.brand_name, COUNT(*) FROM 
ecs_brand b, ecs_goods g
WHERE b.brand_id = g.brand_id
GROUP BY g.brand_id;

-- 内连接第二种方式
SELECT b.brand_name, COUNT(*) FROM 
ecs_brand b INNER JOIN ecs_goods g
ON b.brand_id = g.brand_id
GROUP BY g.brand_id;

-- E. 查询商品品牌对应的商品数量大于5的商品品牌名称
SELECT brand_id FROM ecs_goods GROUP BY brand_id HAVING
COUNT(*) > 5;

-- ecs_brand b ecs_goods g
SELECT b.brand_name FROM ecs_goods g, ecs_brand b 
WHERE b.brand_id = g.brand_id
GROUP BY g.brand_id HAVING
COUNT(*) > 5;








