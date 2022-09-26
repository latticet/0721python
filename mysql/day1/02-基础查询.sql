-- 查询多个字段
SELECT stu_no, stu_name FROM student;
SELECT * FROM student;

-- 字段设置别名
SELECT stu_no as no, stu_name name FROM student;

-- 去重重复记录
SELECT DISTINCT class_id FROM student;