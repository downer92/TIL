# 190610 

## I. View

- simple view  : 하나의 대상 테이블로부터 view 생성, not null 제약조건이 선언된 컬럼은 모두 포함, 컬럼표현식X, group by X, 그룹함수 X, rowid X, rownum 컬럼x
                  DML이 가능한 View (간접적 table access DML 수행됨)
- complex view  :  하나 이상의 테이블에 대한 select문으로 정의, 컬럼표현식 , group by  , 그룹함수  , 조인, rowid  , rownum 컬럼 등 포함된 경우
                  DML이 불가능한 View

- create view는 먼저 권한이 있어야 한다.

```sql
conn scott/oracle
select * from session_privs; ----user_sys_privs

conn sys/oracle as sysdba
grant create view to scott, hr; --권한부여

create view emp20_vu
as select empno, ename, deptno, job, sal*12 salary
   from emp
   where deptno = 20;

select text
from user_views
where view_name = 'EMP20_VU';
```



- create or replace view~~~~ => alter view 역할: 같은 이름의 뷰가 이미 존재할 경우에 현재 생성할 뷰로 대체해서 생성(선택)

```sql
create or replace force view dept_vu
as select *
from dept10; --error: base가 되는 dept10 테이블이 존재하지 않으므로

select object_name, object_type, valid
from user_objects
where object_name = 'DEPT_VU'; --dept_vu는 생성됐지만 유효하지 않음

create or replace view emp20_vu
as select empno, ename, deptno, job, sal
   from emp
   where deptno = 20;

insert into emp20_vu values (9005, 'Song', 20, 'SALESMAN', 2000); --행 삽입

select * from emp20_vu;

select empno, ename, deptno, job, sal
   from emp
   where deptno = 20;
   
   update emp20_vu set sal = 1900 where empno = 9005;
select * from emp20_vu;
select empno, ename, deptno, job, sal
   from emp
   where deptno = 20;

delete from emp20_vu where empno = 9005;
select * from emp20_vu;
select empno, ename, deptno, job, sal
   from emp
   where deptno = 20;

drop view emp20_vu;  --view객체 삭제, base 테이블에 영향을 주는지?
select * from emp20_vu;
select empno, ename, deptno, job, sal
   from emp
   where deptno = 20; 

view객체 삭제는 테이블에 영향을 주지 않고, 메타 정보만 data dictionary로부터 제거됩니다.


create or replace view emp20_vu
as select empno, ename, deptno, job, sal
   from emp
   where deptno = 20
   with check option;  --check제약조건을 설정

select constraint_name, constraint_type
from user_constraints
where table_name = 'EMP20_VU';

insert into emp20_vu values (9005, 'Song', 30, 'SALESMAN', 2000);  --error
select * from emp20_vu;
select empno, ename, deptno, job, sal
   from emp
   where deptno = 20;


create or replace view emp20_vu
as select empno, ename, deptno, job, sal
   from emp
   where deptno = 20
   with read only;  --제약조건 설정, select만 가능


select constraint_name, constraint_type
from user_constraints
where table_name = 'EMP20_VU';

insert into emp20_vu values (9005, 'Song', 20, 'SALESMAN', 2000);
delete from emp20_vu; 
```





## II. SEQUENCE

- 시퀀스 : 특정 규칙에 맞는 연속 숫자를 생성하는 객체. (번호표 발행기같은)

```sql
create sequence 시퀀스 이름 --아래 절 지정하지 않을 경우 1부터 시작해 1씩 계속 증가하는 시퀀스 생성
[increment by n] -- 시퀀스에서 생성할 번호의 증가값
[start with n] -- 시퀀스에서 생성할 번호의 시작값
[maxvalue n || nomaxvalue] -- 생성할 번호의 최댓값 지정 
[minvalue n || nominvalue] -- 생성할 번호의 최솟값 지정
[cycle || nocycle] -- 시퀀스에서 생성한 번호가 최댓값에 도달했을 경우 cycle이면 시작값에서 다시 시작, nocycle이면 번호 생성이 중단된다
[cache n || nocache] -- 시퀀스가 생성할 번호를 메모리에 미리 할당해 놓은 수를 지정, nocache는 미리 생성하지 않도록 설정, 옵션을 모두 생략하면 기본값은 20
```



- 시퀀스의 사용 : currval과 nextval을 사용해서 생성된 시퀀스를 사용할 수 있다

```sql
create sequence emp_seq;
select *
from user_sequences;
-- 시퀀스 객체를 생성하면 자동으로 시퀀스의 내장 컬럼 currval, nextval을 생성

select emp_seq.currval
from dual; --error: 시퀀스를 생성하면 최초값을 생성한 다음에 currval을 확인 가능. 즉, nextval을 먼저하고 currval을 해야한다는 것.
select emp_seq.nextval
from dual;
select emp_seq.currval
from dual;

insert into emp(empno, ename)
values(emp_seq.nextval, 'Kang');

select empno, ename
from emp;

update dept
set deptno = emp_seq.nextval
where deptno = 50;

select deptno, dname
from dept;
```



```sql
alter sequence 시퀀스명
increment by ~
maxvalue ~
minvalue ~
cycle ~
cache ~ ;

drop sequence 시퀀스명 ; --메타정보만 data dictionary로부터 삭제됨
```



## III. Synonym

: 동의어는 테이블, 뷰, 시퀀스 등 객체 이름 대신 사용할 수 있는 다른 이름을 부여하는 객체.

  역시 권한을 따로 부여해야 한다.

```sql
sqlplus system/oracle
grant create synonym to scott;
grant create public synonym to scott;
```

- 동의어 생성하기

  ```sql
  create synonym e
  for emp; -- emp에 다른 이름을 부여한 객체 생성
  select * from e;
  ```

- 동의어 삭제

  ```sql
  drop synonym e;
  ```



## IV. 사용자 관리

```sql
#dual -----소유자? 
select owner, table_name
from all_tables
where table_name='DUAL';   --sys

public으로 dual 테이블에 대한 select권한을 줌

desc dual  -- ?  dummy컬럼 존재
select * from dual;   ---? dummy컬럼값은 x

dual의 목적....from절이 필수이므로 단순 계산결과, 함수 결과를 확인할때
```

- 권한
  - 시스템 권한 : DB에서 특정 sql을 수행할 수 있는 권한, DBA
  - 객체 권한 : 예) table에는 insert, update, select, alter, delete 등을 수행, view에는 select, drop, insert, update, delete 등을 수행, sequence는 select, alter, drop 등을 수행. 객체의 소유자, DBA

```sql
conn kim/oracle
select * from scott.emp;

conn scott/oracle
grant select on emp to kim;

conn kim/oracle
select * from scott.emp;
grant select on scott.emp  to hr;  --error

conn scott/oracle
grant select on emp to kim with grant option;

conn kim/oracle
select * from scott.emp;
grant select on scott.emp  to hr;  ---?

conn hr/oracle
select * from scott.emp; ---?

conn scott/oracle
revoke select on emp from hr;  ---? error, 객체 권한은 직접 권한을 준 user가 회수 가능하다
revoke select on emp from kim; -- 권한 취소할 때에는 revoke 키워드 사용

conn kim/oracle
select * from scott.emp; ---?

conn hr/oracle
select * from scott.emp; ---? 객체권한은 cascade로 회수 됨
```



```sql
grant [시스템 권한] to [사용자 이름/롤(Role) 이름/PUBLIC]
--시스템 권한 : 한 번에 여러 종류의 권한은 쉼표(,)로 구분해 여러 개 명시 가능
--이후 권한을 부여하려는 대상을 지정해야 한다.
[WITH ADMIN OPTION]; --현재 grant문을 통해 부여받은 권한을 다른 사용자에게 부여할 수 있는 권한도 함께 부여받게 하는 옵션
```



**#ROLE**

롤은 여러 종류의 권한을 묶어 놓은 그룹. 롤을 사용하면 여러 권한을 한번에 부여하고 해제할 수 있으므로 권한 관리의 효율을 높일 수 있다.

Role을 생성할 수 있는 권한은 DBA

```sql
1. create role 롤이름 ;
2. grant 시스템권한, 객체권한 to 롤이름;
3. grant 롤이름 to 사용자|롤이름|public;
```

롤 취소

```sql
revoke 롤이름 from 사용자|롤이름|public;
```

롤 삭제

```sql
drop role 롤이름
```

Role의 또 하나의 장점은 동적 권한 관리 가능!

- 사용자에 현재 부여된 권한과 롤을 확인하려면?

```SQL
select * from USER_SYS_PRIVS;
select * from  USER_ROLE_PRIVS;
```



-----------------------------------------------------------------------------------------------------------------------------------------------

# JDBC

먼저 C:\app\student\product\11.2.0\dbhome_1\jdbc\lib 경로의 ojdbc6.jar 파일을 

C:\Program Files\Java\jre1.8.0_211\lib\ext 경로에 넣어준다.

- connect하기

```java
package lab.java.core;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class DBTest {
	public static void main(String[] args) {
		Connection con = null; //DB 연결상태 세션 정보 저장
		Statement stat = null;
		ResultSet rs = null;
		String url = "jdbc:oracle:thin:@localhost:1521:orcl";
		String sql = "select * from dept";
		try {
			Class.forName("oracle.jdbc.OracleDriver");
//			System.out.println("driver loading 성공");
			con = DriverManager.getConnection(url, "scott", "oracle");
//			System.out.println("db connect 성공");
			stat = con.createStatement();
			stat.executeQuery(sql);
			rs = stat.executeQuery(sql);
			while(rs.next()) {
				System.out.print(rs.getInt("deptno") + " ");
				//System.out.print(rs.getInt(1));
				System.out.print(rs.getString("dname") + " ");
				//System.out.print(rs.getString(2));
				System.out.println(rs.getString("loc"));
				//System.out.println(rs.getString(3));
			}
		} catch(ClassNotFoundException e) {
			System.out.println("driver 없음");
		} catch(SQLException e) {
			System.out.println(e.getMessage());
			//db 연결 실패
		} finally {
			try {
			if(rs!=null) rs.close();
			if(stat!=null) stat.close();
			if(con!=null) con.close();
			} catch(Exception e) {
				e.printStackTrace();
			} 
		} //finally end
	} //main end
} //class end
```

- insert 하기

```java
package lab.java.core;
import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;
public class InsertTest {
	public static void main(String[] args) {
		Connection con = null; //DB 연결상태 세션 정보 저장
		PreparedStatement stat = null;
		String sql = "insert into dept values (?,?,?)";
		try {
			Properties prop = new Properties();
			prop.load(new FileInputStream("C:/workspace/day13/src/dbinfo.properties"));
			Class.forName(prop.getProperty("driver"));
			System.out.println("driver loading 성공");
			con = DriverManager.getConnection
			(prop.getProperty("url"), prop.getProperty("user"), prop.getProperty("pwd"));
			System.out.println("db connect 성공");
			
			stat = con.prepareStatement(sql);
			stat.setInt(1, 90);
			stat.setString(2, "BigData");
			stat.setString(3, "Seoul");
			int rows = stat.executeUpdate();
			if(rows>0) {
				System.out.println("insert 성공");
			}
		} catch(ClassNotFoundException e) {
			System.out.println("driver 없음");
		} catch(SQLException e) {
			System.out.println(e.getMessage());
			//db 연결 실패
		} catch(IOException e) {
			System.out.println(e.getMessage()); //properties 파일의 경로, 존재 오류
		} finally {
			try {
			if(stat!=null) stat.close();
			if(con!=null) con.close();
			} catch(Exception e) {
				e.printStackTrace();
			} 
		} //finally end
	} //main end
} //class end
```

