

drop table if exists company_sdhan

CREATE table company_sdhan
insert into company_sdhan select company_id, company_name from company

show CREATE table user_sdhan

drop table if exists company_sdhan

drop table if exists user_sdhan

CREATE table user_sdhan (
    login_id varchar(45) NOT NULL,
    user_name varchar(45) NOT NULL,
    company_id varchar(45) NOT NULL,
    PRIMARY KEY (user_sdhan)
)

alter table user_sdhan drop primary key
alter table company_sdhan drop primary key

alter table user_sdhan add primary key (login_id)

insert into user_sdhan select login_id, user_name, company_id from user

CREATE TABLE `company_sdhan` (
`company_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'company_id',
`company_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '업체명',
PRIMARY KEY ('company_id') USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8


alter table company_sdhan add primary key (company_id)

desc company_sdhan

alter table user_sdhan CHANGE company_name company_id varchar(100);

DELETE FROM company_sdhan WHERE company_id='';