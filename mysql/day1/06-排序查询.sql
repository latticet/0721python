/*
SELECT 字段列表 FROM 表名 ORDER BY 字段1 [排序方式] , 字段2 [排序方式], 字段N [排序方式];
● 排序方式
  ○ ASC : 升序(默认值)
  ○ DESC: 降序
*/
-- sql语句的默认排序 ：主键id升序
SELECT * FROM student;
SELECT * FROM student WHERE stu_name in ('张飞', '关羽', '袁术');

-- 按照年龄升序查询学生信息
SELECT * FROM student ORDER BY stu_age;
SELECT * FROM student ORDER BY stu_age ASC;

-- 按照年龄升序和id降序查询学生信息
SELECT * FROM student ORDER BY stu_age, stu_id DESC;

