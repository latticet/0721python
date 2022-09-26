-- SELECT 字段列表 FROM 表名 LIMIT 起始索引, 查询记录数;   
-- 查询前3个学生的信息
SELECT * FROM student limit 3;
SELECT * FROM student limit 0, 3;

-- 查询后3个学生的信息
SELECT * FROM student ORDER BY stu_id DESC limit 3;
SELECT * FROM student LIMIT 2, 3;

-- 分页实现原理
SELECT * FROM student LIMIT 4, 2;
-- 每页显示条数(m)
-- 当前页    LIMIT
--   1       0, 2
--   2       2, 2
--   3       4, 2 
--   4       (4-1) * 2, 2
--   n       (当前页-1) * 每页显示条数

