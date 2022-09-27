-- alter table 从表 add [constraint 约束名字] foreign key (外键字段) references 主表(关联字段) [on delete {级别}] [on update {级别}]

ALTER TABLE student ADD FOREIGN KEY(class_id) 
REFERENCES class(class_id)


SHOW CREATE TABLE student;
/*
CREATE TABLE `student` (
  `stu_id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '学生id',
  `stu_no` char(10) NOT NULL COMMENT '学生学号',
  `stu_name` varchar(20) DEFAULT NULL COMMENT '学生姓名',
  `class_id` int(10) unsigned DEFAULT NULL COMMENT '班级id',
  `stu_age` tinyint(255) unsigned DEFAULT NULL COMMENT '学生年龄',
  PRIMARY KEY (`stu_id`),
  KEY `class_id` (`class_id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COMMENT='学生表'
*/