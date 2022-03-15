-- 테이블 삭제
drop table if exists user_sdhan

CREATE table company_sdhan
insert into company_sdhan2 select company_id, company_name from company

show CREATE table user_sdhan

show CREATE table company_sdhan

drop table if exists company_sdhan

drop table if exists user_sdhan

CREATE table user_sdhan (
    login_id varchar(45) NOT NULL,
    user_name varchar(45) NOT NULL,
    company_id varchar(45) NOT NULL,
    PRIMARY KEY (login_id)
)
insert into user_sdhan select login_id, user_name, company_id from user

CREATE table company_sdhan (
    company_id varchar(45) NOT NULL,
    company_name varchar(45) NOT NULL,
    PRIMARY KEY (company_id)
)
insert into company_sdhan select company_id, company_name from company

alter table user_sdhan drop primary key
alter table company_sdhan drop primary key

alter table user_sdhan add primary key (login_id)
alter table company_sdhan add primary key (company_id)

insert into user_sdhan select login_id, user_name, company_id from user

CREATE TABLE company_sdhan3 (
company_id varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'company_id',
company_name varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '업체명',
PRIMARY KEY (company_id) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8

alter table company_sdhan add primary key (company_id)

desc user_sdhan

select * from user_sdhan

select * from company

desc company_sdhan

alter table user_sdhan CHANGE company_name company_id varchar(100);

DELETE FROM user_sdhan WHERE login_id like ""


select company_name
from company_sdhan AS c
INNER JOIN user_sdhan AS u ON c.company_id = u.company_id;

select company_name
from company_sdhan
INNER JOIN user_sdhan ON company_sdhan.company_id = user_sdhan.company_id;

ALTER TABLE user_sdhan CHARACTER SET utf8 COLLATE utf8_general_ci;
