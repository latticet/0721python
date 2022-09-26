/*
SELECT 字段列表 FROM 表A ... 
UNION [ ALL ]
SELECT 字段列表 FROM 表B ....;
*/

-- 查询年龄大于18和小于18的学生信息
SELECT * FROM student WHERE stu_age > 18
UNION ALL
SELECT * FROM student WHERE stu_age < 18;

-- 查询student表的stu_no和stu_name
-- 查询class表的class_name和class_room
SELECT stu_no, stu_name FROM student
UNION ALL
SELECT class_name, class_room FROM class;

-- UNION 单字段去重
-- 查询id大于等于4的数据和id小于等于3的学生信息
SELECT stu_age FROM student WHERE stu_id >= 4
UNION
SELECT stu_age FROM student WHERE stu_id <= 3;


-- UNION ALL 不去重
-- 查询id大于等于4的数据和id小于等于3的学生信息
SELECT stu_age FROM student WHERE stu_id >= 4
UNION All
SELECT stu_age FROM student WHERE stu_id <= 3;




