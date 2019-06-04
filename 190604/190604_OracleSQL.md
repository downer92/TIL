# 190604



## Review

그룹함수: 여러 행의 컬럼이 함수의 인수로 전달되고 함수의 결과는 한개

sum, avg, min, max, count, stddev, variance

날짜, 숫자, 문자 데이터 유형에 사용 가능 함수 : min, max, count



※그룹함수는 null을 연산에 포함시키지 않는다.

count(column) : null이 아닌 개수를 리턴

count(*) : 테이블의 전체 행수를 리턴, 내부적으로는 not null 또는 PK 제약조건이 선언된 컬럼을 기준으로



그룹함수(all | distinct 컬럼)



select ~	컬럼,  그룹함수(컬럼)  ------ 4

from ~					------- 1

[where 필터조건]  ------- 2

[group by 컬럼, ....]   -------- 3



※ 그룹함수를 적용한 컬럼과 그룹함수를 적용하지 않은 컬럼이 select 절에 선언될 경우, group by 절에 그룹함수를 적용하지 않은 컬럼을 반드시 선언해 줘야 한다.



※ 그룹함수의 조건은 having절에 선언한다.

select ~	컬럼,  그룹함수(컬럼)  ------ 5

from ~					------- 1

[where 필터조건]  ------- 2

[group by 컬럼, ....]   -------- 3

[having 그룹함수 조건] ------- 4

[order by 컬럼 정렬방식] -------- 6



검색방법 - projection, selection, join

join? 하나 이상의 테이블에서 동일한 속성의 컬럼값이 일치할 때 테이블의 row를 결합해서 결과집합으로 생성



inner join = equi join

non-equi join

self join : 하나의 테이블에 2개의 row가 join을 하는 것. 단, 자기 참조가 가능한 테이블에서만 수행될 수 있다. 

outer join : 일치하는 조인컬럼값이 없거나, 조인컬럼값이 null인 row를 조인결과로 생성할 때

cartesian product : 조인 조건을 생략하거나, 조인 조건을 논리적으로 잘못 정의하면 두 테이블의 모든 row가 한번씩 join되는 경우



오라클에서 초기 버젼부터 사용했었던 조인 구문

where 조인조건 --where절에서 선언했음



select e.ename, e.deptno, d.dname

from emp e, dept d;  ---- cartesian product





오라클에서 지원하는 sql1999 조인 구문

from tab1 a natural join tab2 b

from tab1 a join	   tab2  a   using  (조인컬럼명)



from tab1 a join   tab2  a   on  a.col = b.col2

from tab1 a join   tab2  a   on  a.col = b.col2  



select e.ename, e.deptno, d.dname

from e cross join dept d; ----



----------------------------------------------------------------------------------------------------------------------------------------------------------

## Subquery

:  select문 안쪽에 오는 또다른 select문을 subquery(=inner query=nested query)라 한다(main query = outer query라 함). 조건 값을 알 수 없어서 query를 2번 수행해야 하는 경우 subquery를 활용할 수 있다. 

- (   )로 감싸서 오고, where절에 가장 많이 온다. 이 외에도 select절, from절, having절, order by절에도 subquery가 올 수 있다. 
- where절과 having절의 query는 연산자 오른쪽 (  ) 안에 정의한다.



#subquery의 종류

- single row subquery :  단일 행을 리턴하는 subquery
- multiple row subquery : 복수 행을 리턴하는 subquery
- scalar subquery : 단일 행, 단일 컬럼 값을 리턴하는 subquery
- multiple column subquery : 두 개 이상의 컬럼 값을 리턴하는 subquery



```sql
--ADAMS보다 급여를 많이 받는 사원
select ename, sal
from emp
where sal > (ADAMS의 급여)

select ename, sal
from emp
where sal > (select sal
             from emp
             where ename = 'ADAMS');

-- 사원번호 7839번과 동일한 직무를 담당하는 사원정보 검색
select ename, sal, job
from emp
where job = (select job
             from emp
             where empno = 7839);
     
-- emp 테이블에서 최소 월급을 받는 사원 정보 검색
select *
from emp
where sal = (사원들의 최소 급여)

select *
from emp
where sal = (select min(sal)
             from emp);

-- emp테이블에서 전체 사원 평균 월급보다 급여를 적게 받는 사원 정보 검색
select *
from emp
where sal < (select avg(sal)
             from emp);

-- emp 테이블에서 사원번호가 7521인 사원과 업무가 같고 급여가 7934인 사원보다 많은 사원의 사원번호, 이름, 담당업무, 입사일자, 월급
select *
from emp
where job = (7521인 사원의 업무)
and sal > (7934인 사원의 급여);

select *
from emp
where job = (select job
             from emp
             where empno = 7521)
and sal > (select sal
           from emp
           where empno = 7934);
       
--emp테이블에서 부서별 최소 급여가 20번 부서의 최소 급여보다 많은 부서번호와 부서의 최소급여를 조회
select deptno, min(sal)
from emp
group by deptno
having min(sal) > (20번 부서의 최소급여);
--조건이 group by절에 대한 조건이니까 having절에 subquery가 들어와야 한다
select deptno, min(sal)
from emp
group by deptno
having min(sal) > (select min(sal)
                   from emp
                   where deptno = 20); 

--10번 부서 사원의 월급과 동일한 월급을 받는 다른 부서의 사원을 검색하라.
select *
from emp
where sal in (select sal
              from emp
              where deptno = 10)
and deptno <> 10;
--multiple row subquery의 값을 and, or로 비교하려면 in 연산자를 사용한다.


--부서별로 가장 급여를 많이 받는 사원의 사원번호, 이름, 급여, 부서번호를 조회하라
select empno, ename, sal, deptno
from emp
where (deptno, sal) in (select deptno, max(sal)
                        from emp
                        group by deptno);
--multiple column subquery, pair-wise비교


--업무가 SALESMAN인 최소 한명 이상의 사원보다 급여를 많이 받는 사원의 이름, 급여, 업무를 조회하라
select ename, sal, job
from emp
where sal >any (select sal
                from emp
                where job = 'SALESMAN')
and job <> 'SALESMAN';


--업무가 SALESMAN인 모든 사원이 받는 급여보다 많은 급여를 받는 사원의 이름, 급여, 업무를 조회하라
select ename, sal, job
from emp
where sal >ALL (select sal
                from emp
                where job = 'SALESMAN')
and job <> 'SALESMAN';


--직무별 평균 급여중에서 직무별 평균급여가 가장 작은 직무를 조회하시오(직무, 평균월급)
select job, avg(sal)
from emp
group by job
having avg(sal)= (select min(avg(sal))
                  from emp
                  group by job);             



--부서번호 80번 사원들 중에서 월급이 높은 세 사람을 조회하시오(employees-employee_id, department_id, last_name, salary)
select rownum, employee_id, department_id, last_name, salary
from (select employee_id, department_id, last_name, salary
      from employees
      where department_id=80
      order by salary desc)
where rownum <4;


--subquery를 사용해서 관리자인 사원들만 검색
select empno
from emp
where empno in (select mgr from emp);

--반대로 관리자가 아닌 사원들만 검색
select empno
from emp
where empno not in (select mgr from emp); --error
--subquery의 모든 값을 비교해야 하는 연산에서는 null이 포함되어 있는지의 여부를 먼저 체크해서 null을 처리하거나 제외시켜야 한다.
select empno
from emp
where empno not in (select mgr 
                	from emp
               		where mgr is not null);

--각 부서별로 평균 급여보다 급여를 많이 받는 사원 검색(이름, 부서, 급여) correlated subquery, join
select a.ename, a.deptno, a.sal
from emp a, (select deptno, avg(sal) avgsal
             from emp
             group by deptno) b
where a.deptno = b.deptno
and a.sal > b.avgsal; --1.join 사용

               
select a.ename, a.deptno, a.sal
from emp a
where a.sal > (select avg(sal)
               from emp 
               where a.deptno = deptno); --2.correlated subquery
               

--사원들 중에서 2번 이상 부서 또는 직무를 변경한 이력이 있는 사원의 사번, 이름(last_name)을 출력하라 (desc job_history : 과거 근무했었던 부서, 직무, 기간 / desc employees : 현재 근무부서와 직무)
select a.employee_id, a.last_name
from employees a, (select employee_id, count(employee_id) as cnt
                   from job_history
                   group by employee_id) b
where a.employee_id = b.employee_id
and b.cnt >= 2; --join 사용

select a.employee_id, a.last_name
from employees a
where 2 <= (select count(employee_id)
            from job_history
            where a.employee_id = employee_id); --correlated subquery 사용
```



- subquery에 그룹함수를 사용할 수 있다.
- subquery의 select구문에는 order by 절을 제외한 모든 구문을 쓸 수 있다.
- where절의 조건마다 subquery로 적용 가능하다.
- multiple column subquery, pair-wise 비교
- where 절에 single row subquery를 사용할 경우 반드시 single row operator(>, >=, <, <=, =, <>)와 함께 사용
- where 절에 multiple row subquery를 사용할 경우 반드시 multiple row operator(in, any, all)와 함께 사용
  - ">ANY" : 여러개의 값 중에서 어떤 하나의 값(하나 이상의 값)보다 크면 대상 row가 될 때 사용
  - ">ALL" : 여러개의 값 중에서 모든 값보다 크면 대상 row가 될 때 사용
- from절의 subquery를 inline view라고 부른다.
- rownum은 하나씩 가져올 때마다 row번호를 출력

- where exists (co-related subquery) : exists 연산자는 서브퀘리에 결과 값이 하나 이상 존재하면 조건식이 모두 true, 존재하지 않으면 모두 false가 되는 연산자이다.

```sql
--where exists (co-related subquery) 활용

--subquery를 사용해서 관리자인 사원들만 검색
select empno
from emp
where empno in (select mgr from emp);

select empno
from emp a
where exists (select '1'
              from emp
              where a.empno = mgr);
              
--반대로 관리자가 아닌 사원들만 검색
select empno
from emp
where empno not in (select mgr 
                	from emp
               		where mgr is not null);
               		
select empno
from emp a
where not exists(select '1'
                 from emp
                 where a.empno = mgr);
```



- from절에 사용하는 서브쿼리와 with절

```sql
with
dept_sum as (select department_id, sum(salary) sum_sal
             from employees
             group by department_id),
emp_avg as (select avg(sum_sal) total_avg
              from dept_sum)  
select a.department_id, a.sum_sal
from dept_sum a, emp_avg b
where a.sum_sal > b.total_avg;
```



- 교집합 : 중복체크, SORT

- 합집합 : union(중복되는 것이 없으면 사용), unionAll(중복되는 것이 있으면 사용)

```sql
--hr2
--20명 사원의 현재와 과거의 모든 부서, 직무 이력을 출력(동일한 직무와 부서, 근무 이력은 중복 데이터로 출력합니다.) 
select employee_id, job_id, department_id
from employees
union all
select employee_id, job_id, department_id
from job_history;


--20명 사원의 현재와 과거의 모든 부서, 직무 이력을 출력 (동일한 직무와 부서 근무 이력은 한번만 결과 데이터로 출력합니다.)
select employee_id, job_id, department_id
from employees
union  
select employee_id,  job_id, department_id
from job_history;   


--20명 사원중 의 현재 직무와 부서를 과거에 동일한 부서와 직무를 담당한 사원 조회 (사원번호, 직무, 부서번호)
select employee_id, job_id, department_id
from employees
intersect 
select employee_id,  job_id, department_id
from job_history;


--입사한 이후에 한번도 직무나 부서를 변경한 적이 없는 사원번호 출력
select employee_id 
from employees
minus
select employee_id 
from job_history;


--scott
--전체 사원들의 급여 평균과 부서별 사원들의 급여 평균과 부서와 직무별 사원들의 급여 평균을 단일 결과 집합으로 출력하라.
select to_number(null), to_char(null), avg(sal)
from emp
union all
select deptno, to_char(null), avg(sal)
from emp
group by deptno
union all
select deptno, job, avg(sal)
from emp
group by rollup (deptno, job);


--전체 사원들의 급여 평균과 부서별 사원들의 급여 평균과 직무별 사원들의 급여 평균과 부서와 직무별 사원들의 급여 평균을 단일 결과 집합으로 출력하라.
select deptno, job, avg(sal)
from emp
group by cube (deptno, job)

```

- group by rollup (A, B, C)

  => group by (A, B, C)

  => group by (A, B)

  => group by (A)

  => group by (  )

- group by cube (A,B,C)

  => group by (A,B,C)

  => group by(A,B), (B,C), (A,C)

  => group by (A), (B), (C)

  => group by (  )















