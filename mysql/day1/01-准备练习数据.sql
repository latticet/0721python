-- 学生表
create table student(
stu_id int unsigned not null primary key auto_increment comment '学生id',
stu_no char(10) not null unique key comment '学生学号',
stu_name varchar(20) comment '学生姓名',
class_id int unsigned comment '班级id'
)engine=innodb default charset=utf8 comment='学生表';


-- 班级表
create table class(
class_id int unsigned not null primary key auto_increment comment '班级id',
class_name varchar(20) comment '班级名称',
class_room char(3) comment '班级教室'
)engine=innodb default charset=utf8 comment='班级表';


-- 添加数据
insert into student values(null, 'itsrc-001', '曹操', 1);
insert into student values(null, 'itsrc-002', '袁绍', 1);
insert into student values(null, 'itsrc-003', '袁术', 1);
insert into class values(1, '1班', '601');

insert into student values(null, 'itsrc-011', '刘备', 2);
insert into student values(null, 'itsrc-012', '关羽', 2);
insert into student values(null, 'itsrc-013', '张飞', 2);
insert into class values(2, '2班', '602');