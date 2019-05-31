# 190530_Oracle SQL



## I. DB관련 개념

**#Database란?**

특정 기업이나 조직 또는 개인이 필요에 의해 논리적으로 연관된 데이터를 모아 일정한 형태로 저장해 놓은 것

비지니스 목적으로 transaction 처리를 위해서 여러 유저들이 공유하는 데이터  집합



**#DBMS(Database Management System)**

: 데이터베이스 관리 프로그램으로 DBMS를 이용하여 데이터 입력, 수정, 삭제 등의 기능을 제공한다.



**#DBMS의 역사**

계층형=>망형=>관계형=>객체관계형=>클러스터로 구성



**#Database 특징**

- 통합된 데이터: 데이터의 중복을 최소화하여 중복으로 인한 데이터 불일치

- 저장된 데이터: 디스크, 테이프 같은 컴퓨터 저장장치에 저장된 데이터

- 운영 데이터: 업무를 위한 검색을 할 목적으로 저장된 데이터

- 공용 데이터: 동시 공유. 

- 실시간 접근성

-  지속적인 변화

- 내용에 따른 참조



**#기존 파일 시스템의 문제점**

- 데이터를 파일 단위로 저장하므로 중복 가능

- 데이터의 중복 저장으로 일관성이 결여됨

-  데이터 정의와 프로그램의 독립성 유지 불가능

- 관리 기능 보통

- 프로그램 개발 생산성 나쁨



**#DBMS 장점**

-  DBMS를 이용해 데이터를 공유하기 때문에 중복 가능성이 낮음

-  중복 제거로 데이터의 일관성이 유지됨

- 데이터 정의와 프로그램의 독립성 유지 가능
- 데이터 복구, 보안, 동시성 제어, 데이터 관리 기능 등을 수행
- 짧은 시간에 큰 프로그램을 개발할 수 있음
- 데이터 무결성 유지, 데이터 표준 준수 용이



**#데이터베이스 사용자 그룹**

- 일반 사용자
- 응용프로그래머
- SQL 사용자
- DBA



**#데이터베이스의 유형**

- Busineess(or User) Data
- Meta Data





데이터베이스에 저장되는 데이터의 기본 단위는 Record(Row)라고 함.

다대다 참조관계가 가능하다.

DBMS에 저장되는 데이터는 고정된 구조, 정형 Schema구조를 가짐. 





## II. SQL

: 구조적인 지리언어

Table = Entity(Record 집합)



**#명령어**

- DML (select(선택), insert(추가), update(수정), delete(삭제), merge(병합))

- DDL (create(생성), alter(변경), drop(삭제), rename, truncate )

- TCL (commit, rollback, savepoint)

- DCL (grant, revoke)



**Transaction**: 분리돼서 수행될 수 없는 작업 단위. 

- **Unit of work**(원자성: 트랜잭션이 지녀야 할 성질의 하나. 시스템의 어떤 상황 하에서도 한 트랜잭션에 대한 모든 연산들의 결과가 데이터 베이스에 모두 반영되든가 아니면 전혀 반응되지 않아야 함을 의미하는 성질)



유저는 함수. 함수의 결과를 볼 때 from dual 사용. 오라클만!

identified by OOO: 패스워드 정하기

account unlock; 



```sql
-- sqlplus를 실행시키고 관리자 계정으로 접속해서 sample계정 비밀번호 설정하고, 잠긴 계정을 풉니다.
C:\Users\student>sqlplus / as sysdba

SQL*Plus: Release 11.2.0.1.0 Production on 목 5월 30 10:20:16 2019

Copyright (c) 1982, 2010, Oracle.  All rights reserved.


다음에 접속됨:
Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - 64bit Pro
With the Partitioning, OLAP, Data Mining and Real Application Testing

SQL> select user from dual;

USER
------------------------------
SYS

SQL> alter user scott
  2  identified by oracle   --비밀번호 설정
  3  account unlock;

사용자가 변경되었습니다.

SQL> alter user hr
  2  identified by oracle
  3  account unlock;

사용자가 변경되었습니다.


```

C:\app\student\product\11.2.0\dbhome_1\NETWORK\ADMIN // 홈주소

services.msc

host: 빠져나오기

lsnrctl start,stop,status

Dedicated Server Mode: 1대1로 맵핑이 되는 모드

리스너는 커넥션만 담당

이후 셀렉트 요청은  메모리가 받음..?

select 검색column명

 from 대상table



비지니스를 목적으로 필요한 데이터: Business Data, User Data

DBMS가 데이터베이스를 관리하는 데에 필요한 메타정보: User, table, 칼럼, 권한정보 등. =>Data Dictionary Data

IO의 단위는 블락단위

SQL은 목적지, 즉 내가 필요로 하는 데이터만 지정을 해주면 됨. 그러면 마치 네비게이션이 길을 안내해주듯 알아서 데이터를 찾아서 결과를 리턴해줌. 그래서 SQL은 선언적, 결과 중심의 언어라고 한다. 그에 비해 일반 프로그래밍 언어는 절차적 언어(과정을 기준으로 함)라고 한다.



**#검색방법**

- Projection검색: 1 Table, 컬럼기준검색

- Selection검색1 Table,  Raw기준검색

- Join 검색: 2개 이상의 Table, 공통속성(컬럼)값 기준으로 일치할 때 Raw 결합해서 검색



**#명령어**

- SQL> conn hr / oracle
- SQL> select * from employees
- SQL> conn scott / oracle
- SQL> select tname from tab; // 메타정보로 테이블 목록 확인
- SQL> select * from emp; // 테이블의 모든 데이터 조회

```sql
conn scott/oracle
describe emp			--테이블 구조 조회
desc dept
```





- sqlplus 툴: sql 실행, 결과 보여주는 환경 제공

- sqlplus 툴 명령어: ;(세미콜론) 없이 사용 가능, 4글자까지 명령어 축약 사용 가능

- sql문은 명령어 축약 불가, 반드시 세미콜론(;)으로 종료



char(1) ~2000byte: char()타입은 디폴트가 1이고 2000바이트크기에 해당하는 문자 데이터까지 저장가능

varchar(2) ~4000byte: varchar()타입은 디폴트가 2고 4000바이트크기에 해당하는 문자 데이터까지 저장가능

number타입: binary형식으로 정수, 실수



```sql
select sysdate from dual; --시스템 현재 시간을 리턴하는 함수

--세션에 설정된 기본 날짜 출력 형식은 RR/MM/DD입니다.
SQL> select sysdate from dual;   

SYSDATE
--------
19/05/30

--세션의 날짜 출력 형식을 변경 
SQL> alter session set nls_date_format ='YYYY/MM/DD HH24:MI:SS';

세션이 변경되었습니다.

SQL> select sysdate from dual;

SYSDATE
-------------------
2019/05/30 11:23:08

SQL> exit;  --db disconnection, 세션 종료
 


--세션을 종료한 후에 다시 시작하면 세션의 기본 날짜 출력 형식으로 변경된다.

C:\Users\student>sqlplus scott/oracle

SQL> select sysdate from dual;   

SYSDATE
--------
19/05/30
```

```sql

```

meta 정보가 저장된 oracle data dictionary view는

user_tables : 특정 user 소유의 테이블 목록 확인

all)tables : 특정 user 소유 + 권한을 받은 테이블 목록 확인

dba_tables: DB의 모든 테이블 목록 확인(DBA 권한으로만 확인 가능)



desc user_tables

select table_name from user_tables;  (user_tables의 별칭은 tab)

=

desc tab

select tname from tab;



```sql
desc user_tables
select table_name from user_tables; --user_tables의 별칭은 tab

desc tab
select tname from tab;

select table_name from all_tables;
select table_name from dba_tables; --오류 발생

conn / as sysdba --연결
select table_name from dba_tables;

```

select table_name from all_tables;

select table_name from dba_tables; --오류 발생

- sql문장의 키워드와 테이블명, 컬럼명 등은 대소문자 구별 안합니다. but, 대체적으로 clause는 대문자로

- 컬럼값은 대소문자 구별합니다.



```sql
select * from emp; --null은 값이 없는 것

--조회할 컬럼을 지정한 것. 조회할 컬럼의 순서는 테이블에 정의된 컬럼순서에 맞추지 않아도 된다.
select ename, sal, job, deptno from emp; 
select distinct deptno from emp; --hashing방식 사용해서 중복값을 제거=>사원이 포함된 부서번호 종류만 리턴
select deptno, distinct job from emp; --error: distinct는 중간에 쓸 수 없음! 모든 컬럼의 맨 앞에만 사용해야 한다.
select distinct deptno, job from emp; --2개의 컬럼값이 일치하면 결과집합에서 제거하고 일치하지 않을 때만 결과집합에 포함
```

- `INTEGER` : a positive or negative whole number
- `TEXT`: a text string
- `DATE`:  the date formatted as YYYY-MM-DD for the year, month, and day
- `REAL`:  a decimal value 



## II.1  Expression(표현식)

: 컬럼에 연산자 값을 적용하는 것

expresion  [as]  alas(별칭=>Column title Rename)

- **number**타입 컬럼은 산술연산 : + , - , * , /

- **char/varachar2** 타입 컬럼은 문자열을 결합: ||

- **date** 타입 컬럼: date+n, date-n, date-date, date+-1/n



```sql
select sal+100, sal-100, sal*2, sal/100
from emp;

select sal, comm, (sal+comm)*2
from emp; 
--데이터가 추가될때 입력되지 않는 컬럼값은 null이다.
--null은 아직 값이 없다 , 0도 아니고, ''도 아니다.
--null은 산술연산 수행 결과는 항상 null이다.
--null을 포함하는 컬럼들은 null아닌 값으로 변환 후에 산술연산을 수행해야 한다.
--모든 DBMS에서는 null아닌 값으로 변환해주는 내장 함수를 제공한다.
--nvl(column, null일때리턴값)

select sal, comm, (sal+nvl(comm, 0))*2 as salary
from emp; --컬럼 헤딩에 salary가 대문자로 나옴.

select sal, comm, (sal+nvl(comm, 0))*2 as "Salary" --큰따옴표로 감싸서 대소문자 구별 가능!
from emp; 

select sal, comm, (sal+nvl(comm, 0))*2 "Total Salary" 
--공백도 큰따옴표로 감싸야 하고 as는 생략 가능!
from emp; 

select ename|| ' works as ' ||job
from emp; --상수 문자열을 ' '로 감싸서 보기 좋게 출력할 수 있다.

select '''A''' --'자체가 출력 시작과 끝 의미 가져서 이렇게 표기하지만 가독성이 떨어짐
from dual;

select q'['A']'
from dual; --quotator사용해서 가독성을 쉽게!

desc dual
select * from dual; --단순 계산 결과, 함수 결과, 문자 데이터 출력 등을 할 때에만 사용!

--Quiz
select 10||10 from dual; --1010출력: 연산자가 ||이니까 oracle서버가 정수10을 문자열로 자동으로 환산해서 산출한 것
select '10'+'10' from dual; --20출력. 연산자가 +니까 문자열이 정수로 형변환돼서 산출된 것

select sysdate+1, sysdate-1 from dual; --날짜와 산술연산하는 정수는 Number of Days이다.

select sysdate-hiredate from emp; --기간이 리턴

select sysdate_hiredate from emp; --error

alter session set nls_date_format='YYYY-MM-DD HH24:MI:SS'; --날짜 설정 원래대로 바꾸기
select sysdate, sysdate+1/24, sysdate+5/1440 from dual;--n/24는 시간, n/1440은 분
```



**#주의사항**

- 문자, 날짜 데이터는 반드시 ' '를 사용해서 표현, 처리
- 날짜 데이터 세션에 설정된 포맷 형식하고 일치해야 한다.('RR/MM/DD')
- select~ from절이 필수적이다.
- 단순계산 결과, 함수 결과, 문자 데이터 출력 등은 dual테이블을 사용한다.



## II.2  SELECT문

select	검색 칼럼 리스트, 표현식 	from (데이터가 저장돼 있는)테이블명

where	조건 ;  => 칼럼   비교연산자   값

```sql
--부서번호 30번인 사원 검색
select ename, deptno
from emp
where deptno=30;

--직무가 ANALYST인 사원 검색
select ename, job
from emp
where job='ANALYST';

--급여가 3000이상인 사원 검색
select ename, sal
from emp
where sal>=3000; 

--87년1월1일 이후에 입사한 사원 이름 검색
alter session set nls_date_format='RR/MM/DD';
select ename, hiredate
from emp
where hiredate>='87/01/01';

--커미션이 있는 사원/ 커미션이 없는 사원
select ename, comm
from emp
where comm != null;
select ename, comm
from emp
where comm = null; --null은 비교연산자를 사용 못함! 대신 is null, is not null연산자를 사용!

select ename, comm
from emp
where comm is null;

select ename, comm
from emp
where comm is not null;

--월급이 3000이상 5000이하인 사원 검색(3000포함, 5000포함)
select ename, sal
from emp
where sal>=3000 and sal<=5000; --논리연산자로는 and, or, not 사용 가능

select ename, sal
from emp
where sal between 3000 and 5000; --범위연산자 "between 하한값 and 상한값"도 사용가능

--직무가 clerk 또는 analyst인 사원 검색
select ename, job
from emp
where job='CLERK' or job='ANALYST';

select ename, job
from emp
where job in('CLERK', 'ANALYST'); --in리스트 연산자: in(값, 값, 값,...)

--이름의 두번째 글자가 'D'인 사원 검색
select ename
from emp
where ename like '_D%';

--이름의 마지막 글자가 'N'인 사원 검색
select ename
from emp
where ename like '%N';

--81년도에 입사한 사원 검색
alter session set nls_date_format='RR/MM/DD';
select ename, hiredate
from emp
where hiredate > '80/12/31' and hiredate < '82/01/01';

alter session set nls_date_format='RR/MM/DD';
select ename, hiredate
from emp
where hiredate between '81/01/01' and '81/12/31';

--업무가 PRESIDENT이고 급여가 1500 이상이거나 업무가 SALESMAN인 사원의 사원번호, 이름, 업무, 급여를 출력해라.
select empno, ename, job, sal
from emp
where job='PRESIDENT' and sal>=1500 or job='SALESMAN';
--논리연산자의 우선순위는 NOT, AND, OR순이다.

```

empno 사번/ ename 이름/ job 직무/ hiredate 입사날짜/ 

comm 커미션/ deptno 부서번호/ sal 급여/ mgr 관리자번호



**#연산자 종류들**

- null은 비교연산자를 사용할 수 없다. 대신 is null, is not null연산자를 이용한다.
- ~이상 ~이하는 범위연산자 "between 하한값 and  상한값" 연산자를 사용할 수 있다.
- in 리스트 연산자: in(값, 값, 값,.....)
- character pattern matching 연산자: like '%, _'
  - %는 문자종류는 모든 문자, 개수는 0~M
  - _는 문자종류는 모든 문자, 개수는 1을 의미한다.
- 논리연산자의 우선순위는 NOT, AND, OR순이다.



## II. 3  절

select~

from~

[where 필터 조건]   --[ ]가 붙은 건 생략해도 된다는 것!

[group by 컬럼]

[having 조건]

[order by   정렬기준컬럼   정렬방식]   --  asc(오름차순=default), desc(내림차순)

- order by 절에는 컬럼 표현식, 별칭, 컬럼 포지션은 사용할 수 없다.

```sql
--월급의 오름차순으로 사원 정보 출력
select ename, job, sal
from emp
order by sal; --오름차순은 default라 생략 가능

--사원들의 사번, 이름, 부서번호, 월급, 커미션, 연봉(sal+comm*12)의 결과 연봉의 내림차순으로 출력
select empno, ename, deptno, sal, comm, sal+nvl(comm, 0)*12 as 연봉
--nvl(comm, 0)은 comm이라는 컬럼에서 null값이 있으면 그 null값은 0으로 처리해준다는 함수
from emp
order by 6 desc; -- 6은 6번째 컬럼(연봉)을 의미. 연봉이라고 적어줘도 됨. 

--사원들의 사번, 이름, 부서번호, 월급, 커미션, 연봉(sal+comm*12)의 결과 부서번호로 오름차순 정렬하고 연봉의 내림차순으로 출력
select empno, ename, deptno, sal, comm, (sal+nvl(comm,0))*12 as 연봉
from emp
order by 3 asc, 6 desc;

---------------------------------------연습문제-----------------------------------------
--1번: EMP테이블의 모든 자료 출력
select * from emp;

--2번: EMP테이블에서 사원번호, 이름, 급여, 담당업무 출력
select empno, ename, sal, job from emp; 

--3번: 모든 사원의 급여를 $300 증가시키기 위해 덧셈 연산자를 사용하고 결과에 SAL+300을 조회
select ename, sal+300 as sal from emp; 

--4번: EMP 테이블에서 사원번호, 이름, 급여보너스를 출력
select empno, ename,comm from emp; 

--5번: EMP 테이블에서 ENAME를 NAME로 SAL을 SALARY로 출력
select ename as NAME, sal as SALARY from emp; 

--6번: EMP 테이블에서 ENAME를 Name로 SAL*12를 Annual Salary 로 출력
select ename as "Name", sal*12 as "Salary" from emp; 

--7번: EMP 테이블에서 ENAME를 '성 명'으로, SAL를 ‘급 여'로  출력
select ename as "'성 명'", sal as "'급 여'" from emp; 

--8번: EMP 테이블에서 이름과 업무를 연결하여 출력
select ename || ' ' ||  job as "이름과 직업" from emp;

--9번: EMP 테이블에서 이름과 업무를 "King is a PRESIDENT" 형식으로 출력
select ename || ' is a ' || job from emp; --9번

--10번:  EMP 테이블에서 이름과 연봉을 "KING: 1 Year salary = 60000" 형식으로 출력
select ename || ': 1 Year salary = ' || sal from emp; 

--11번: EMP 테이블에서 JOB을 모두 출력
select job from emp; 

--12번: EMP 테이블에서 담당하고 있는 업무의 종류를 출력
select distinct job from emp; 

--13번: EMP 테이블이 부서번호를 중복 값을 제거해서 조회
select distinct deptno from emp; 

--14번: 부서별로 담당하는 업무를 한번씩 출력
select distinct deptno, job from emp; 

--15번: EMP 테이블에서 사원번호, 이름, rowid를 조회
select empno, ename, rowid from emp; 
--rowid는 논리적인 주소! 이 논리적인 주소를 oracle이 물리적인 주소와 맵핑해서 찾는 것

--17번: EMP 테이블에서 급여가 3000 이상인 사원의 사원번호, 이름, 담당업무, 급여를 출력
select empno, ename, job, sal from emp
where sal>=3000;

--18번: 담당업무가 Manager인 사원의 정보를 사원번호, 성명, 담당업무, 급여, 부서번호를 출력
select empno, ename, job, sal, deptno from emp
where job = 'MANAGER'; 

--19번: 1982년 1월 1일 이후에 입사한 사원의 사원번호, 성명, 담당업무, 급여, 입사일자, 부서번호를 출력
select empno, ename, job, sal, hiredate, deptno from emp
where hiredate>'82/01/01'; 

--20번: 급여가 1300에서 1700사이의 사원의 성명, 담당업무, 급여, 부서 번호를 출력
select ename, job, sal, deptno from emp
where sal between 1300 and 1700; 

--21번: 사원번호가 7902, 7788, 7566인 사원의 사원번호, 성명, 담당업무, 급여, 입사일자를 출력
select empno, ename, job, sal, hiredate from emp
where empno in (7902, 7788, 7566); 

--22번: 입사일자가 82년도에 입사한 사원의 사번, 성명, 당당업무, 급여, 입사일자, 부서번호를 출력
select empno, ename, job, sal, hiredate, deptno from emp
where hiredate between '82/01/01' and '82/12/31'; 

--23번: 이름의 첫 글자가 'M'인 사원의 이름, 급여 조회
select ename, sal from emp
where ename like 'M%'; 

--24번: 이름의 두 번째 글자가 ‘L'인 사원의 이름,업무를 조회
select ename, job from emp
where ename like '_L%'; --24번

--25번: 보너스가 NULL인 사원의 사원번호, 성명, 담당업무, 급여, 입사일자, 부서번호를 출력
select empno, ename, job, sal, hiredate, deptno from emp
where comm is null; 

--26번: 급여가 1100 이상이고 JOB이 Manager인 사원의 사원번호, 성명, 담당업무, 급여, 입사일자, 부서번호를 출력
select empno, ename, job, sal, hiredate, deptno from emp
where sal>=1100 and job='MANAGER'; 

```



## II.4   함수

SQL- 조건처리: (함수)

반복처리=>   테이블의 Db단위 반복처리

​					   명시적 for X, while X

​					    exception 처리 x 

데이터베이스에서 함수의 역할: SQL을 더 강력하게 사용할 수 있도록 보조한다.



- predefine 함수: 데이터베이스에서 미리 제공해주는 함수(ex: nvl, sysdate, user, ...)

- custom 함수 (PL/SQL): 사용자정의 함수



- 단일행 함수: DB의 함수가 반드시 1개의 결과 리턴. Character, Number, Date, null처리, Conversion(형변환) 함수 등이 있다.
  - nvl(A, B) 함수 : null값을 실제 값으로 변환하는 함수로 모든 데이터 타입에 사용 가능하며 데이터 유형이 일치해야 한다. A컬럼에서 null값을 찾아 null값에 B를 채우고 이 때 A가 숫자형이면 B도 동일한 숫자형 데이터 타입으로 대체해야 한다. 

- 복수행 함수(그룹 함수): 테이블의 전체 Raw 혹은 grouping된 Raw가 인풋으로 들어가서 1개의 결과 리턴



- Numeric Function

```sql
select initcap(ename), lower(ename), upper(ename)
from emp; --initcap: 첫글자만 대문자로, lower: 전부 소문자로, upper: 전부 대문자로

select length('korea') length('대한민국')
from dual; --length: 글자 수

select lengthb('korea') lengthb('대한민국')
from dual; --length: 바이트 수

select concat(concat(ename, ' is '), job)
from emp; --concat함수 안에 concat함수를 nested하면 nested된 함수부터 처리

select substr('today is 2015년 4월 26일', 1, 5),
	   substr('today is 2015년 4월 26일', 10, 5),
	   substr('today is 2015년 4월 26일', 15),
	   substr('today is 2015년 4월 26일', -3, 2)
	   from dual;
	   
select instr('korea is wonderful', 'o'),
       instr('korea is wonderful', 'o', 1, 2),
       instr('korea is wonderful', 'o', 9),
       instr('korea is wonderful', 'x')
       from dual;


-- lpad: left padding, rpad: right padding. 문자열로 변환, 문자열 전체 길이내에 왼쪽 공백에 특정 문자를 padding
select ename, sal, lpad(sal, 10, '*') from emp;
--sal 왼쪽 공백에 *을 채워서 10자리 수를 만든다.
select ename, sal, rpad(sal, 10, '*') from emp;
--sal 오른쪽 공백에 *을 채워서 10자리 수를 만든다.


-- ltrim, rtrim 함수
select length('  hello  '), length(trim('   hello   '))
from dual;  --trim은 공백 제거

select trim('H' from 'Hello wonderful'), trim('l' from 'Hello wonderful')
from dual; --trim('A' from 'B')는 B에서 A를 제거한다.

select ltrim('Hello wonderful', 'He'), rtrim('Hello wonderful', 'ful')
from dual;

select replace('Jack AND Jue', 'J', 'BL')
from dual; -- --replace('A', 'B', 'C')는 A에서 B를 C로 바꾼다.

--translate??

select round(12.345, 2), round(12.345, 0), round(12.345, -1)
from dual; --round(A, B)는 A를 소숫점 B째자리까지 반올림

select trunc(12.345, 2), round(12.345, 0), round(12.345, -1)
from dual; --trunc(A, B)는 A의 소숫점 B째자리까지 절삭

select mod(99, 4)
from dual; --mod(A, B)는 A를 B로 나눈 나머지를 산출

select ceil(12.345), floor(12.345)
from dual; --ceil()은 올림, floor()은 내림

select power(3, 2), power(5, 2)
from dual; --power(A, B)는 A의 B제곱을 산출


--사원번호중 홀수인 사원들만 출력
select ename, empno
from emp
where mod(empno, 2)=1;

```



- Date Function

```sql
select sessiontimezone from dual;
alter session set time_zone = '+3:00'; --timezone의 시간을 3시간 빠르게 설정
select sessiontimezone from dual;
select sysdate from dual;
select current_date from dual; --timezone기반 현재시간을 date타입으로 리턴
select current_timestamp from dual; --timezone기반 현재시간을 timestamp타입으로 리턴



add_months(date, n) --date에 n개월을 더해서 리턴
months_between(date, date) --날짜와 날짜 사이에 char가 더해져서 리턴
select add_months(sysdate, 6)
from dual;
select hiredate, add_months(hiredate, 6)
from emp;
select months_between(sysdate, hiredate)
from emp;



next_day(date, '요일명') --돌아오는 다음 '요일명'의 날짜를 리턴
select next_day(sysdate, '목')
from dual;



trunc, round
alter session set nls_date_format = 'RR/MM/DD';
select trunc(to_date('18/02/14'), 'MONTH'),
	   trunc(to_date('18/02/14'), 'YEAR')
	   from dual;
select round(to_date('18/02/16'), 'MONTH'),
	   round(to_date('18/07/16'), 'YEAR')
	   from dual; --월은 16일 기준으로 년은 7월 기준으로 반올림
	
    
    
last_day(date)
select last_day(to_date('14/02/14')), last_day(to_date('2000/02/14')),
	   last_day(to_date('2100/02/14'))
	   from dual; --해당 달의 마지막 날 리턴



--사원들의 입사 날짜로부터 6개월 후 날짜로부터 다음 금요일이 연봉 조정 날짜라 할 때, 사원들의 사번과 입사날짜, 연봉 조정 날짜를 출력하세요.
select empno, hiredate, next_day((add_months(hiredate, 6)), '금') as "연봉조정 날짜"
from emp;
```



- 변환함수: 변환 함수에 대해서는 oracle에서 to_OOO형태로 표현한다. ex) to_char, to_date,...

```sql
select to_char(123456.789, '$9,999,999.9999')
from dual; --number값과 뒤의 format형식이 일치하지 않더라도 형식에 맞춰서 변환해줌

select to_number('$1,234,567.999', '99,999,999,9999')
from dual; --error! 숫자의 문제가 아니고 앞에 $가 있어서 문제가 되는 것

select to_number('$1,234,567.999', '$99,999,999,999.9999')
from dual; --ok! 

select sysdate, to_char(sysdate, 'YYYY"년" MM"월" DD"일" DY')
from dual; 

alter session set nls_language=american;
select sysdate, to_char(sysdate, 'Year Month DDspth Day')
from dual;

alter session set nls_language=korean;
select '2019-05-30 5:43', to_date('2019-05-30 5:43', 'HH12:MI YYYY-MM-DD')
from dual; --error. to_date(A,B)에서 A,B의 형식이 같지 않음

select '2019-05-30 5:43', to_date('2019-05-30 5:43', 'YYYY-MM-DD HH12:MI')
from dual; --변환이 정상적으로 수행되면 세션 포맷형식으로 출력됨
```



- date 변환 함수의 경우 format은 ' '로 감싸고 그 안의 사용자 지정 문자열은 " "로 감싼다.
- RR날짜 형식에서 년도의 반올림 기준
  - 지정된 두 자리 연도가 0~49, 현재 연도의 두자리가 0~49인경우: 반환날짜는 현재 세기의 날짜
  - 지정된 두 자리 연도가 0~49, 현재 연도의 두자리가 50~99인경우: 반환날짜는 이전 세기의 날짜
  - 지정된 두 자리 연도가 50~99, 현재 연도의 두자리가 0~49인경우: 반환날짜는 이후 세기의 날짜
  - 지정된 두 자리 연도가 50~99, 현재 연도의 두자리가 50~99인경우: 반환날짜는 현재 세기의 날짜
- YY날짜 형식은 현재 세기 기준으로 반올림!

