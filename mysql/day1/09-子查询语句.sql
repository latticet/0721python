-- 标量子查询
-- 查询1班的学生信息
-- 1. 通过班级名称查询班级id
SELECT class_id FROM class WHERE class_name = '1班';
-- 2. 通过班级id查询学生信息
SELECT * FROM student WHERE class_id = 1;
-- 子查询
SELECT * FROM student WHERE class_id = (SELECT class_id FROM class WHERE class_name = '2班');

-- 列子查询（子查询结果为一列）
-- 查询1班和2班所有学生信息
-- 1.通过班级名称查询班级id
SELECT class_id FROM class WHERE class_name = '1班' OR class_name = '2班';
-- 2.通过班级id查询对应学生
SELECT * FROM student WHERE class_id = 1 or class_id = 2;
SELECT * FROM student WHERE class_id in (1, 2);
-- 子查询
SELECT * FROM student WHERE class_id IN (SELECT class_id FROM class WHERE class_name = '1班' OR class_name = '2班');

-- 行子查询（子查询结果为一行）
-- 查询class_id=1这个班级最大的人,年龄最大的人
-- 1. 利用班级id查询出这个班最大年龄
SELECT MAX(stu_age), class_id FROM student WHERE class_id = 1;
-- 2. 利用年龄和class_id查出对应学生
SELECT * FROM student WHERE stu_age = 32 AND class_id = 1;
-- 子查询
SELECT * FROM student WHERE (stu_age,class_id) = (SELECT MAX(stu_age), class_id FROM student WHERE class_id = 1);


-- 表子查询（子查询结果为多行多列）
-- 1. 查询stu_id小于等于6的所有学生
SELECT * FROM student WHERE stu_id <= 6;
-- 2.查询年龄大于30的学生信息
SELECT * from (SELECT * FROM student WHERE stu_id <= 6) new_student
WHERE stu_age > 30;