

drop table if exists company_sdhan

CREATE table company_sdhan
insert into company_sdhan select company_id, company_name from company

show CREATE table user_sdhan

drop table if exists company_sdhan

CREATE TABLE `company_sdhan` (
`company_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT 'company_id',
`company_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '업체명',
PRIMARY KEY ('company_id') USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8


alter table company_sdhan add primary key (company_id)

desc company_sdhan

