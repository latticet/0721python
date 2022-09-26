-- sql语句的默认排序 ：主键id升序
SELECT * FROM student;
SELECT * FROM student WHERE stu_name in ('张飞', '关羽', '袁术');

-- 按照年龄升序查询学生信息
SELECT * FROM student ORDER BY stu_age;
SELECT * FROM student ORDER BY stu_age ASC;

-- 按照年龄升序和id降序查询学生信息
SELECT * FROM student ORDER BY stu_age, stu_id DESC;

