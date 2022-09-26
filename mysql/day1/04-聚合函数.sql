-- count 获取记录
-- 查询学生总数
SELECT count(*) FROM student;

-- sum 求所有学生的总年龄
SELECT SUM(stu_age) FROM student;
-- 查询大于18的所有学生的总年龄
SELECT SUM(stu_age) FROM student WHERE stu_age > 18;

-- MAX 求最大值
-- 求最大年龄
SELECT MAX(stu_age) FROM student;

-- avg 求平均值
-- 求学生的平均年龄
SELECT AVG(stu_age) FROM student;