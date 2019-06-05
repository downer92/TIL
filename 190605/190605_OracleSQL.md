190605 Oracle SQL



## REVIEW

#subquery : select문 내부에 정의된 select문(inner query, nested query)

- single row subquery - scalar subquery
- multiple row subquery - 2개 이상의 column값을 리턴한다. multiple column subquery
- correlated subquery : 서브쿼리가 메인쿼리의 컬럼을 참조해서 main query의 행수만큼 subquery가 반복적으로 수행하는 query
- subquery는 main query보다 먼저 수행하고, 1번 수행.

#Outer query(main query) : subquery를 감싸는 select문



#subquery가 올 수 있는 위치

```sql
select절
from절  --- inline view
where절 -- 연산자 오른쪽 (subquery)
having절 -- 연산자 오른쪽 (subquery)
order by절
```

- subquery를 where절이나 having절에 정의할 때 single row subquery는 single row operator(>,>=,<,<=,=,<>)와 함께 사용해야 하고 multiple row subquery는 multiple row operator(in, any>, any<, all>, all<)와 함께 사용해야 한다.

- subquery에는 모든 select절, 함수 등 제약없이 사용 가능하지만, order by절은 from절의 inline view에서만 허용됨.



#rownum: 결과행에 순차적인 번호를 발행해주는 내장 컬럼

- order by절 전에 발생되므로, order by 후에 rownum으로 순차적인 번호를 발행하려면 subquery를 사용.



#correlated subquery(상관관계 subquery)

```sql
select~
from table1 a
where column 연산자 (select~
					from table2
					where a.column = column2)
```

- exists, not exists: correlated subquery에서 존재 유무를 체크해주는 연산자



#with : 긴 query문에서 반복적으로 사용하는 subquery를 먼저 정의해서 재사용하기 위해 사용

```sql
with
별칭 as (subquery),
별칭 as (subquery),
별칭 as (subquery)
.......
별칭 as (subquery)
select~
from~
.....
```



#set operator : 서로 다른 select의 결과를 단일 결과집합으로 만들기 위해 쓰는 연산자

- 합집합 : union, union all
  - union : 각 select의 결과 행에서 중복된 행을 제외하기 위해 sorting
  - union all : append방식(첫 번째 select의 결과에다가 두번째 select의 결과를 추가하는)
- 교집합 : intersect
  - intersect : 각 select의 결과 행에서 중복된 행만 결과로 생성하기 위해 sorting해서 비교한다
- 차집합 : minus
  - minus : 첫번째 select의 결과에만 속한 행을 선택하기 위해 sorting해서 비교한다.

```sql
select~
from~
[where~]
[group by~]
[having ~]
union | union all | intersect | minus
select~
from~
[where~]
[group by~]
[having ~]; --※각 select문에서 컬럼개수와 컬럼타입이 일치해야 한다!!!
```

**※ **각 select문에서 컬럼개수와 컬럼타입이 일치해야 한다.

**※ **union all을 제외하면 결과는 첫번째 컬럼값을 기준으로 정렬된 결과가 리턴되므로 다른 컬럼으로 정렬하려면 order by절은 마지막 select문에만 허용된다.

```sql
-- 전체 사원의 급여 평균
-- 부서별 사원의 급여 평균
-- 부서와 직무별 사원의 급여 평균
```



#roll up : 소그룹간의 소계를 계산. n+1가지의 결과를 도출

```sql
select deptno, job
from emp
group by roll up;
-- (deptno, job), (deptno), () 3가지 결과 도출
```

#cube : n=2이상일 때 순서에 조심해야 한다.

```sql
select deptno, job, sal
from emp
group by cube;
-- (deptno, job, sal), (deptno, job), (deptno, sal), (job, sal), (deptno), (job), (sal), () 총 8가지 결과 도출.
```

#grouping sets : union all 등을 사용해 복잡하게 sql문장을 작성했던 것을 간단하게 한 문장으로 해결

```sql

```



----------------------------------------------------------------------------------------------------------------------------------------------------------



## Insert 문

새로운 데이터를 추가하려면 대상 테이블에 insert 권한 또는 테이블의 소유자여야 한다. 



```sql
insert into 테이블명 [(컬럼명, 컬럼명, ....)]
values (컬럼리스트의 순서대로 값...);
-- 새로 추가되는 행의 데이터로 일부 컬럼값만 정의할 경우, 필수 컬럼은 반드시 정의

--컬럼명이 생략될 경우
insert into 테이블명
values (테이블에 정의된 컬럼 순서대로 모든 값이 선언);
```



#에러유형

```sql
insert into dept
values (150, 'HR', null); --error 컬럼 사이즈 초과

insert into dept
values (50, 'HR', null); --error deptno(PK)에 중복값 ...

insert into emp (empno, ename, deptno)
values (9000, 'Kim', 70); --deptno(FK)의 참조컬럼에 70번데이터가 존재하지 않음=>참조 무결성 제약조건

insert into emp (empno, ename, deptno, hiredate)
values (9000, 'Kim', 50, sysdate);

insert into emp (empno, ename, deptno, hiredate)
values (9001, 'Lee', 50, '19년3월2일'); --error 날짜 포맷에 맞지 않음

insert into emp (empno, ename, deptno, hiredate)
values (9001, 'Lee', 50, '19/03/02'); 
```



#테이블 복제하기(같은 구조를 갖지만 데이터는 복사하고 싶지 않을 때 사용하는 방법)

```sql
create table emp10
as select * 
   from emp
   where 1=2; --false 조건을 주기. 검색된 row가 없어질 것. 그러면 이 테이블은 구조만 생성됨!           
              --테이블 구조만 복제! CTAS
desc emp10
select * from emp10;
```



#subquery로 행수 추가하기

```sql
insert into emp10
select * from emp where deptno = 10;
-- values절 대신 subquery를 선언하면 subquery의 결과 행수만큼 추가된다.

insert into emp10 (empno, ename, deptno, sal)
select empno, job, hiredate, mgr
from emp where deptno = 20;
--subquery에서 insert에 선언된 컬럼개수나 타입과 일치하지 않으면 error가 발생!
--컬럼개수나 컬럼타입이 맞아야 한다는 점에 주의하자!
```





## UPDATE문

:  테이블에 이미 존재하는 행의 데이터를 수정할 때 컬럼단위로 수정한다.

```sql
update 테이블명
set 컬렴명 = new 컬럼값 [, 컬럼명=new컬럼값, ...];
--테이블의 모든 데이터의 변경컬럼값을 단일 값으로 변경
--ex)
select * from emp10;
update emp10
set sal = 1; --전체 sal열의 값이 1로 바뀜
--메모리에서만 저장이 된 데이터이기 때문에 
rollback; --수행했던 작업 취소되는데 table을 생성한 이후에 수행된 작업이 전부 취소됨


update 테이블명
set 컬렴명 = new 컬럼값 [, 컬럼명=new컬럼값, ...];
where 조건;
--where 조건에 해당하는 데이터를 변경컬럼값으로 변경


select empno, ename, deptno, sal
from emp;

update emp
set sal = 1
where deptno = 30;

select empno, ename, deptno, sal
from emp
where deptno = 30;
```



#에러 발생 유형

```sql
update dept
set deptno = 100
where dname = 'IT'; --error, 컬럼size 초과

update dept
set deptno = 40
where dname = 'IT'; --error, 중복값

update emp
set deptno = 60
where empno = 7788; --error 참조무결성제약조건 오류
```



#subquery의 사용

```sql
--SMITH사원의 급여를 KING사원의 급여와 동일하도록 변경하세요.
update emp
set sal = (select sal
             from emp
             where ename ='KING')
where ename = 'SMITH';
             
select ename, sal
from emp
where ename = 'SMITH';


--KING사원과 동일한 부서에 근무하는 KING을 제외한 다른 사원의 급여를 20%인상 수정하라.	
update emp
set sal = (select sal*1.2
           from (select deptno
                 from emp
                 where ename='KING'))
where ename <> 'KING';
```



#Table생성하기

```sql
create table customer (
custid number(7),
custname varchar2(15),
point number(5) default 1000 --default키워드를 사용해서 기본값 주기.
);

desc customer
select*from customer;

insert into customer (custid, custname)
values (990301, 'Kim');

select*from customer;
```



## DELETE문

```sql
delete from 테이블명; --전체행 삭제
delete 테이블명; --오라클에서는 from절 생략 가능
--ex)
select * from emp;
delete from emp;
select * from emp;
rollback;

delete from 테이블명 where 조건; --조건을 만족하는 행만 삭제
--ex)
delete from emp where deptno = 30;
select * from emp;
rollback;


delete from 테이블명 where 컬럼 연산자 (subquery);


--문> ADAMS 사원과 동일한 직무를 담당하는 사원 삭제(ADAMS를 제외하고)
select * from emp;

delete
from emp
where job = (select job
             from emp
             where ename = 'ADAMS')
and ename <> 'ADAMS';
rollback;

select * from emp;
```



## MERGE문

: Insert Update Delete를 한번에 수행할 수 있음. ETL작업에 많이 사용된다

```sql
merge into 대상테이블 t --alias 지정
using 소스테이블 s
on t.pk컬럼 = s.pk컬럼
when matched then --'Row가 존재하면'의 의미
update set t.컬럼=s.컬럼,.....
[delete where 조건]
when not matched then
insert (t.컬럼, t.컬럼, ...)
values (s.컬럼, s.컬럼, ...);

--문> emp테이블로부터 30번 부서 사원정보를 emp30 테이블로 복제하시오. 30번부서 사원은 직무와 급여를 update하고 급여가 2500이상이면 삭제하시오. 10, 20번 부서 사원은 사원번호와 이름과 부서번호만 입력하시오.
merge into emp30 a
using emp b
on a.empno = b.empno
when matched then
    update set a.job = b.job, a.sal = b.sal
    delete where a.sal > 2500
when not matched then
    insert (a.empno, a.ename, a.deptno)
    values (b.empno, b.ename, b.deptno);	
```



**#Transaction** : Unit of Work (분리되어 수행될 수 없는 하나의 작업 단위)

ACID - 원자성, 일관성, 격리성, 영속성

DB관점의 Transaction은 변경(DML, DDL, DCL 등 데이터베이스의 변경을 의미)이 포함되면 select는 transaction으로 포함되지 않고



#Transaction 단위

- 1개 이상의 DML들로 구성 - 명시적 commit, rollback

- 1개의 DDL - auto commit;

- 1개의 DCL - auto commit;

- 수행중인 DML 트랜잭션의 세션이 비정상종료하면 oracle server는 rollback한다.

- 수행중인 DML 트랜잭션을 정상종료(exit;)하면 oracle server는 commit한다.

- 읽기 일관성 - select하는 user들이 변경중인 user 작업이 종료될 때까지 기다리지 않고, 변경 작업하려는 user들은 select하는 user들이 검색을 종료할 때까지 기다릴 필요 없이 변경 작업중인 user들은 변경중인 값을 조회 결과로 볼 수 있고, 변경 작업중이 아닌 user들은 DB에 저장된(commit된) 데이터 값을 조회 결과로 볼 수 있도록  한다.

- 오라클 서버는 읽기 일관성을 위해서 Lock, undo segment 등을 지원한다.

```sql
create table test (num  number(2));
insert into test values (1);
insert into test values (2);
savepoint a;
insert into test values (3);
insert into test values (4);
savepoint b;
insert into test values (5);
insert into test values (6);
select * from test;
rollback to savepoint b;
```



Table : row + column. 물리적 데이터 저장. Heap, IOT, partition

View : table의 Data에 대한 Window. 물리적 Data 없음, 논리적 Table. select문으로 정의. 

1)보안을 위해서, 2)복잡한 query문을 간결하게 하기 위해서 사용





## Window 함수



**#RANK :**  특정 컬럼에 대한 순위를 구하는 함수로서 동일한 값에 대해서 동일한 순위를 가지며, 동일한 순위의 수만큼 다음 순위는 건너뛴다.  **동일한 순위가 많으면 그 수를 반영해서 그 다음순위가 정해지는 것**

```sql
--emp 테이블에서 사원이름, 직무, 급여 데이터와 전체 사원의 급여가 높은 순서와 JOB별로 급여가 높은 순서 출력하시오
select ename, job, sal, rank() over(order by sal desc) sal_rank,
       rank() over (partition by job order by sal desc) job_rank
from emp;
```



**#DENSE_RANK :** 특정 컬럼에 대한 순위를 구하는 함수로서 동일한 순위 다음의 순위는 동일 순위의 수와 상관없이 1 증가된 값을 돌려준다**. 동일한 순위가 아무리 많아도 그 다음순위는 +1되는 것**

```sql
select ename, job, sal, dense_rank() over(order by sal desc) sal_dense_rank,
       rank() over (partition by job order by sal desc) job__dense_rank
from emp;
```



**#ROW_NUMBER :** 특정 컬럼에 대한 순위를 구하는 함수로서 동일한 값이라도 고유한 순위를 부여한다 (동일한 순위를 배제하기 위해 unique한 순위를 oracle의 경우 rowid가 적은 행이 먼저 나온다.)  PARTITION내의 ROW들에 순서대로 UNIQUE한 일련번호를 부여한다.

```sql
select ename, job, sal,
       dense_rank() over (order by sal desc) sal_rank,
       rank() over (order by sal desc) sal_rank2,
       row_number() over (order by sal desc) sal_rank2
from emp;
```



#**SUM** **함수: 파티션별로 윈도우의 합을 구할 수 있다.**

```sql
select ename, mgr, sal, sum(sal) over (partition by mgr order by sal asc) sums
from emp;
```



**#RANGE  UNBOUNDED PRECEDING :** 현재 행을 기준으로 파티션 내의 첫번째 행까지의 범위를 지정한다.

```sql
select ename, mgr, sal, sum(sal) over (partition by mgr order by sal
                                       range unbounded proceeding)
from emp; --값 기준

select ename, mgr, sal, sum(sal) over (partition by mgr order by sal
                                       rows between current row and unbounded proceeding)
from emp; --행 기준
```



**#MAX** : 함수를 이용해 파티션별로 윈도우의 최대값을 구할 수 있다.

**#MIN** : 함수를 이용해 파티션별로 윈도우의 최소값을 구할 수 있다.



**#ROWS  BETWEEN 1 PRECEDING AND 1 FOLLOWING** **:** 현재 행을 기준으로 파티션 내에서 앞의 한 건, 현재 행, 뒤의 한 건을 범위로 지정한다.

```sql
select ename, mgr, sal,
	   first_value(sal) over (partition by mgr order by sal),
	   last_value(sal) over (partition by mgr order by sal
       range between current row and unbounded following)
from emp;
```



**#LAG :**  파티션별 윈도우에서 이전 몇 번째 행의 값을 가져올 수 있다.

```sql
select ename, hiredate, sal,
	   lag(sal) over (order by hiredate),
	   lag(sal, 2, 0) over (order by hiredate)
from emp;
```

- LAG 함수는 3개의 argument까지 사용할 수 있는데, 두번째 인자는 몇 번째 앞의 행을 가져올 지 결정하는 것이고 (default 1), 세번째 인자는 파티션의 첫번째 행의 경우 가져올 데이터가 없어 NULL값이 들어오는데 이 경우 다른 값으로 바꾸어 줄 수 있다.



**#LEAD :**  파티션별 윈도우에서 이후 몇 번째 행의 값을 가져올 수 있다 .

```sql
select ename, hiredate, sal,
	   lead(sal) over (order by hiredate),
	   lead(sal, 2, 0) over (order by hiredate)
from emp;
```

- LEAD 함수는 3개의 argument까지 사용할 수 있는데, 두번째 인자는 몇 번째 앞의 행을 가져올 지 결정하는 것이고 (default 1), 세번째 인자는 파티션의 첫번째 행의 경우 가져올 데이터가 없어 NULL값이 들어오는데 이 경우 다른 값으로 바꾸어 줄 수 있다.





## 객체

테이블을 생성하려면 create table 시스템 권한이 있어야 한다.

tablespace (data container) 저장소에 quota가 할당돼 있어야 한다.  



**#table 또는 컬럼 이름 규칙** 

- 영문자 또는 _, $, #로 시작
- 두 번째 문자부터 숫자 허용
- 키워드 안됨
- schema : 서로 연관된 table, index 등의 객체를 그룹핑하는 논리적 개념. 객체명을 재사용할 수 있는 namespace의 역할을 한다. 오라클은 user명을 schema명으로 사용한다. 
- schema내에서 중복된 이름 사용 불가
- 길이 제한 30자
- DB이름 길이 제한 8자



**#컬럼타입** 

- char : 고정길이 문자열 ~2000byte
- varchar2 : 가변길이 문자열 ~4000byte
- number(p, s)
- date 
- timestamp : date타입 확장, 1/10^9의 정밀한 초값 저장
- timestamp with timezone
- interval year to month
- interval day to second
- rowid
- CLOB(character large object) ~4G
- raw : binary 형식의 값 저장. ex) 지문, 증명사진 ~2000byte
- BLOB(binary large object) ~4G
- BFILE : read only 가능한 file을 DB외부에 운영체제의 폴더에 저장, TX처리 불가능



## 제약조건

```sql
create table 테이블명 (
컬럼명 컬럼타입(size)
컬럼명 컬럼타입(size) [default값]
컬럼명 컬럼타입(size) [제약조건] --컬럼레벨에서의 제약조건
.......
[제약조건] --table레벨에서의 제약조건
)
[................] ;
```

- 제약조건 constraint : table의 DML 수행시 규칙
  - primary key
  - not null
  - unique key
  - foreign key
  - check

```sql
create table userinfo
(userid varchar2(10) not null,
 username varchar2(15) constraint userinfo_nn not null,
 age number(30));
 desc userinfo
 
 desc userinfo
 insert into userinfo
 values('tester1', '테스터1', 20);
 insert into userinfo (username, age)
 values ('테스터1', 20); --error: not null 제약조건 에러
 select * from userinfo;
 
 select constraint_name, constraint_type
 from user_constraints
 where table_name = 'USERINFO';
 
insert into userinfo (userid, age)
 values ('tester2', 20); --error
 alter table userinfo disable constraint userinfo_nn; --제약조건 비활성화
 insert into userinfo (userid, age)
 values ('tester2', 20); --돌아감
 select * from userinfo;
 
 drop table userinfo;
 select * from userinfo;
 desc userinfo
 
 select constraint_name, constraint_type
 from user_constraints
 where table_name = 'USERINFO'; --제약조건 함께 사라짐
 
 select * from recyclebin;
 flashback table userinfo to before drop;

 select constraint_name, constraint_type
 from user_constraints
 where table_name = 'USERINFO'; --제약조건 함께 복원됨. but 이름은 원본 이름이 아님
 
 drop table userinfo purge;create table;
```



**#unique 제약조건**

```sql
create table userinfo
(userid varchar2(10) constraint userinfo_uk unique,
 username varchar2(15),
 age number(30));
 desc userinfo
 
 desc userinfo
 insert into userinfo
 values('tester1', '테스터1', 20);
 insert into userinfo (username, age)
 values ('테스터2', 25);  --userid는 null?
 insert into userinfo (username, age)
 values ('테스터3', 30);  --userid는 null?
 insert into userinfo
 values('tester1', '테스터5', 35);  --error
 select * from userinfo;
 
 select constraint_name, constraint_type
 from user_constraints
 where table_name = 'USERINFO';
 
 select index_name, uniqueness
 from user_indexes
 where table_name = 'USERINFO';
--oracle server는 unique제약조건이 선언된 컬럼에 자동으로 unique index를 생성

alter table userinfo disable constraint userinfo_uk;
select index_name, uniqueness
from user_indexes
where table_name = 'USERINFO';
--제약조건 비활성화 하면 인덱스 자동삭제

alter table userinfo enable constraint userinfo_uk;

select index_name, uniqueness
from user_indexes
where table_name = 'USERINFO';
--index 다시 자동생성
```



**#primary key 제약조건** 

- primary key = not null + unique
- 다른 제약조건은 하나의 테이블에 여러개 선언 가능하지만 primary key 제약조건은 하나만 선언 가능하다.

```sql
create table userinfo
(userid varchar2(10) constraint userinfo_pk primary key,
 username varchar2(15),
 age number(30));
 desc userinfo
 
 desc userinfo
 insert into userinfo
 values('tester1', '테스터1', 20);
 insert into userinfo (username, age)
 values ('테스터2', 25);  --error
 insert into userinfo
 values('tester1', '테스터5', 35);  --error
 select * from userinfo;
```



**#check 제약조건**

```sql
create table userinfo(
userid  varchar2(10),
username  varchar2(15),
gender  char(1) constraint userinfo_ck  check (gender in ('F', 'M')),
age  number(2) check (age > 0 and age < 100)
);

select constraint_name, constraint_type, search_condition
from user_constraints
where table_name='USERINFO';

insert into userinfo  values ('a001', 'an', 'f', 20);  --error: 체크 제약조건 위배
insert into userinfo  values ('a001', 'an', 'w', 20); --error: 체크 제약조건 위배
insert into userinfo  values ('a001', 'an', null, 20);   --null허용
insert into userinfo  values ('a002', 'choi', 'M', 0); --error: 체크 제약조건 위배
insert into userinfo  values ('a002', 'choi', 'M', 100); --error: 체크 제약조건 위배
insert into userinfo  values ('a002', 'choi', 'M', 25);  --ok
```



#CTAS이용해서 테이블 구조만 복제, 테이블 구조+데이터 복제 가능

```sql
create table 테이블이름
as
	(subquery);

create table emp20
as select empno, ename, deptno, sal*12
   from emp
   where deptno=20; --error
   
create table emp20
as select empno, ename, deptno, sal*12 salary
   from emp
   where deptno=20;
   
create table emp20 (empid, name, deptid, salary)
as select empno, ename, deptno, sal*12
   from emp
   where deptno=20;
```



#삭제한 테이블 Recyclebin에서 복원하기!

```sql
create table copy_dept
as select * from dept;
desc copy_dept
select * from copy_dept;

drop table copy_dept;
desc copy_dept
select * from copy_dept;
select tname from tab; ---BIN$~~~~~~~이름의 테이블
select * from user_recyclebin;
select * from "BIN$jE5ZlX/ISWi8jHRlYNnQmw==$0";
flashback table copy_dept to before drop; --복원하기
select * from user_recyclebin;
select tname from tab;
desc copy_dept
select * from copy_dept;
```













