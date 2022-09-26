-- 分组查询 SELECT 字段列表 FROM 表名 GROUP BY 分组字段名
-- 使用class_id进行分组
SELECT class_id FROM student GROUP BY class_id;

-- 聚合函数配合group by 使用
-- 查询每个班级的人数
SELECT class_id,COUNT(*) FROM student GROUP BY class_id;

-- 查询每个班级的年龄总数
SELECT class_id,SUM(stu_age) FROM student GROUP BY class_id;

-- 查询每个班级的平均年龄
SELECT class_id,AVG(stu_age) FROM student GROUP BY class_id;

-- GROUP_CONCAT配合 GROUP BY 使用
-- 查询每个班级的学生姓名
SELECT class_id, GROUP_CONCAT(stu_name) FROM student GROUP BY class_id;

-- HAVING 配合 GROUP BY使用
-- 查询平均年龄大于30的班级
SELECT class_id, AVG(stu_age) FROM student GROUP BY class_id HAVING AVG(stu_age) > 30;





