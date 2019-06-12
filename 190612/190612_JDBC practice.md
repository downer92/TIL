# 190612_JDBC 유제

```sql
create table student ( --student테이블 생성
studentNo varchar2(5) constraint student_pk primary key,
studentName varchar2(15) not null,
c number(3) default 0,
linux number(3) default 0,
java number(3) default 0,
careerYears number(2),
internYn char(1) check (internYn in ('Y', 'N'))
);

alter table student add (average number(5, 2), pass char(1) check (pass in ('Y', 'N')));
alter table student modify(c number(3) default 0,
linux number(3) default 0,
java number(3) default 0);
desc student

insert into student values('10001', 'kim', 70, 70, 64, null, 'N', 65.4, 'N');
commit;
insert into student values('20002', 'kim', 90, 78, 85, null, 'Y', 88, 'Y');
commit;
```



## Student class

```java
package lab.jdbc.info;
public class Student {
	private String studentNo;
	private String studentName;
	private int c;
	private int linux;
	private int java;
	private int careerYears;
	private String internYn;
	private Double average;
	private String pass;
	public Student() {
		super();
	}	
	public Student(String studentNo, String studentName, int c, int linux, int java, 
			int careerYears, String internYn, Double average, String pass) {
		this.studentNo = studentNo;
		this.studentName = studentName;
		this.c = c;
		this.linux = linux;
		this.java = java;
		this.careerYears = careerYears;
		this.internYn = internYn;
		this.average = average;
		this.pass = pass;
	}
	public String getStudentNo() {
		return studentNo;
	}
	public void setStudentNo(String studentNo) {
		this.studentNo = studentNo;
	}
	public String getStudentName() {
		return studentName;
	}
	public void setStudentName(String studentName) {
		this.studentName = studentName;
	}
	public int getC() {
		return c;
	}
	public void setC(int c) {
		this.c = c;
	}
	public int getLinux() {
		return linux;
	}
	public void setLinux(int linux) {
		this.linux = linux;
	}
	public int getJava() {
		return java;
	}
	public void setJava(int java) {
		this.java = java;
	}
	public int getCareerYears() {
		return careerYears;
	}
	public void setCareerYears(int careerYears) {
		this.careerYears = careerYears;
	}
	public String getInternYn() {
		return internYn;
	}	
	public void setInternYn(String internYn) {
		this.internYn = internYn;
	}
	public void setAverage(Double average) {
		this.average = average;	
	}
	public void setPass(String pass) {
		this.pass = pass;
		
	}
	@Override
	public String toString() {
		return "Student [studentNo=" + studentNo + ", studentName=" + studentName + ", c=" + c + ", linux=" + linux
				+ ", java=" + java + ", careerYears=" + careerYears + ", internYn=" + internYn + ", average=" + average
				+ ", pass=" + pass + "]";
	}
}
```



## GradeManager Class

```java
package lab.jdbc.biz;
import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Properties;
import lab.jdbc.info.Student;

public class GradeManager {
	
    public Connection dbCon() {
		Connection con = null;
		try {
			Properties prop = new Properties();
			prop.load(new FileInputStream("C:/workspace/day14/src/dbinfo.properties"));
			Class.forName(prop.getProperty("driver"));
			// System.out.println("driver loading 성공");
			con = DriverManager.getConnection
			(prop.getProperty("url"), prop.getProperty("user"), prop.getProperty("pwd"));
			// System.out.println("db connect 성공");
		} catch(Exception e) {
			e.printStackTrace();
		}
		return con;
	}
	
	public void dbClose(Connection con, Statement stat, ResultSet rs) {
		try {
			if(rs!=null) rs.close();
			if(stat!=null) stat.close();
			if(con!=null) con.close();
			} catch(Exception e) {
				e.printStackTrace();
			} 
	}
	
	//전체학생목록 추출
	public void getAllStudent() {
		Connection con = null;
		Statement stat = null;
		String sql = "select * from Student";
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.createStatement();
			rs = stat.executeQuery(sql);
			while(rs.next()) {
				Student student = new Student();
				student.setStudentNo(rs.getString("studentNo"));
				student.setStudentName(rs.getString("studentName"));
				student.setC(rs.getInt("c"));
				student.setLinux(rs.getInt("linux"));
				student.setJava(rs.getInt("java"));
				student.setCareerYears(rs.getInt("careerYears"));
				student.setInternYn(rs.getString("internYn"));
				student.setPass(rs.getString("pass"));
				student.setAverage(rs.getDouble("average"));
				System.out.println(student);
			} //while end
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);
			} 
		}
	
	//합격학생 추출
	public void getPassStudent() {
		Connection con = null;
		Statement stat = null;
		String sql = "select * from Student";
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.createStatement();
			rs = stat.executeQuery(sql);
		
			while(rs.next()) {
				Student student = new Student();
				double avg = (rs.getInt("c")+rs.getInt("java")+rs.getInt("linux"))/3;
				if (rs.getString("studentNo").startsWith("1") && avg>=70 ||
						rs.getString("studentNo").startsWith("2") && avg>=80) {
				student.setStudentNo(rs.getString("studentNo"));
				student.setStudentName(rs.getString("studentName"));
				student.setC(rs.getInt("c"));
				student.setLinux(rs.getInt("linux"));
				student.setJava(rs.getInt("java"));
				student.setCareerYears(rs.getInt("careerYears"));
				student.setInternYn(rs.getString("internYn"));
				student.setPass(rs.getString("pass"));
				student.setAverage(rs.getDouble("average"));
				System.out.println(student);
				}
			} //while end
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);
			} 
		
	}
	
	//불합격학생 추출
	public void getFailStudent() {
		Connection con = null;
		Statement stat = null;
		String sql = "select * from Student";
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.createStatement();
			rs = stat.executeQuery(sql);
		
			while(rs.next()) {
				Student student = new Student();
				double avg = (rs.getInt("c")+rs.getInt("java")+rs.getInt("linux"))/3;
				if (rs.getString("studentNo").startsWith("1") && avg<70 ||
						rs.getString("studentNo").startsWith("2") && avg <80) {
				student.setStudentNo(rs.getString("studentNo"));
				student.setStudentName(rs.getString("studentName"));
				student.setC(rs.getInt("c"));
				student.setLinux(rs.getInt("linux"));
				student.setJava(rs.getInt("java"));
				student.setCareerYears(rs.getInt("careerYears"));
				student.setInternYn(rs.getString("internYn"));
				student.setPass(rs.getString("pass"));
				student.setAverage(rs.getDouble("average"));
				System.out.println(student);
				}
			} //while end
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);
			} 
	}
	
    //학생정보 추가
	public int insertStudent(Student s){
		int rows = 0;
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "insert into student (studentno, studentname, c, java, linux, careeryears, internyn, average, pass) values (?,?,?,?,?,?,?, ?, ?)";
		try {
			con = dbCon();
			stat = con.prepareStatement(sql);
			stat.setString(1, s.getStudentNo());
			stat.setString(2, s.getStudentName());
			stat.setInt(3, s.getC());
			stat.setInt(4, s.getJava());
			stat.setInt(5, s.getLinux());			
			if(s.getStudentNo().startsWith("1")) {
				stat.setString(7, s.getInternYn());
				stat.setInt(6, 0);
			}else {
				stat.setInt(6, s.getCareerYears());
				stat.setString(7, "N");
			}
			double avg = (s.getC()+s.getJava()+s.getLinux())/3.0;			 
			stat.setDouble(8, Double.parseDouble( String.format("%.2f", avg)));
			if(s.getStudentNo().startsWith("1") && avg>=70) {
				stat.setString(9, "Y");
			}else if(s.getStudentNo().startsWith("2") && avg>=80) {
				stat.setString(9, "Y");
			}else {
				stat.setString(9, "N");
			}			
			rows = stat.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, null);
		}
		return rows;
	}


//학생정보 수정(과목 점수, 경력, 인턴여부 변경)
	public int updateStudent(Student s){
		int rows = 0;
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "update student set c=?, java=?, linux=?, careeryears=?, internyn=? where studentno=?  ";
		try {
			con = dbCon();
			con.setAutoCommit(false);
			stat = con.prepareStatement(sql);
			stat.setString(6, s.getStudentNo());			
			stat.setInt(1, s.getC());
			stat.setInt(2, s.getJava());
			stat.setInt(3, s.getLinux());
			stat.setInt(4, s.getCareerYears());
			stat.setString(5, s.getInternYn());
			rows = stat.executeUpdate();			
			sql = "update student set average=?, pass=? where studentno=?  ";
			double avg = (s.getC()+s.getJava()+s.getLinux())/3.0;
			stat = con.prepareStatement(sql);
			stat.setDouble(1, Double.parseDouble( String.format("%.2f", avg)));
			if(s.getStudentNo().startsWith("1") && avg>=70) {
				stat.setString(2, "Y");
			}else if(s.getStudentNo().startsWith("2") && avg>=80) {
				stat.setString(2, "Y");
			}else {
				stat.setString(2, "N");
			}		
			stat.setString(3, s.getStudentNo());
			rows += stat.executeUpdate();
			con.commit();
		} catch (Exception e) {			 
			e.printStackTrace();			
		} finally {
			dbClose(con, stat, null);
		}
		return rows;
	}

	
	//학번으로 레코드 삭제
	public int deleteStudent(String sno) {
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "delete from student where studentno=?";
		int rows = 0;
		try {
			con = dbCon();
			stat = con.prepareStatement(sql);
			stat.setString(1, sno);
			rows = stat.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, null);
		}
		return rows;
	}
	
	//학번으로 학생 검색
	public ArrayList<Student> searchStudents(String sno) {
		ArrayList<Student> searchStudents = new ArrayList();
		Connection con = null;
		PreparedStatement stat = null;
		String sql = "select * from	student where studentno=?";
		ResultSet rs = null;
		try {
			con = dbCon();
			stat = con.prepareStatement(sql);
			stat.setString(1, sno); // 1은 첫번째 물음표의 위치
			rs = stat.executeQuery();
			while(rs.next()) {
				Student st = new Student();
				st.setStudentNo(rs.getString("studentno"));
				st.setStudentName(rs.getString("studentname"));
				st.setC(rs.getInt("c"));
				st.setLinux(rs.getInt("linux"));
				st.setJava(rs.getInt("java"));
				st.setAverage(rs.getDouble("average"));
				st.setPass(rs.getString("pass"));
				if(rs.getString("studentno").startsWith("1")) {
					st.setInternYn(rs.getString("internYn"));
				} else {
					st.setCareerYears(rs.getInt("careeryears"));
				}
				searchStudents.add(st);
			} //while end
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			dbClose(con, stat, rs);
		} return searchStudents;
	}
}
```



## CommonUtil Class

```java
package lab.jdbc.util;

import java.util.Scanner;

public class CommonUtil {
	public static String getUerInput() {
		   Scanner input = new Scanner(System.in);
		   return input.nextLine();
	   }
	   public static void printHead() {
		   System.out.println("=======================================================================================");
		   System.out.println("사번      이름   신입/경력  인턴여부  경력년수  C   Linux   Java   총점   평균   합격여부");;
		   System.out.println("=======================================================================================");
	   }  
	   public static void printTail() {
		   System.out.println("=======================================================================================");
	   }
}
```



## GradeTest Class

```java
package lab.jdbc.test;
import java.util.ArrayList;
import java.util.Scanner;
import lab.jdbc.biz.GradeManager;
import lab.jdbc.info.Student;
import lab.jdbc.util.CommonUtil;

public class GradeTest {

	public static void main(String[] args) {
		Student student = new Student();
		GradeManager test = new GradeManager();
		ArrayList<Student> students = null;
		
			while(true) {
				printMenu();
				System.out.print("##메뉴 입력: ");
				Scanner sc = new Scanner(System.in);
				int menu = sc.nextInt();
				if(menu == 8) {
					System.out.println("## 성적 관리 시스템을 종료합니다!!"); break;
				} 
				switch(menu) {
				case 1 : 
					test.getAllStudent(); break;
				case 2 :
					test.getPassStudent(); break;
				case 3 :
					test.getFailStudent(); break;
				case 4:	
					System.out.print("> 사번 입력하세요:");
					student.setStudentNo(CommonUtil.getUerInput());
					System.out.print("> 이름을 입력하세요:");
					student.setStudentName(CommonUtil.getUerInput());
					System.out.print("> C 점수를 입력하세요:");
					student.setC(Integer.parseInt(CommonUtil.getUerInput())); 
					System.out.print("> JAVA 점수를 입력하세요:");
					student.setJava(Integer.parseInt(CommonUtil.getUerInput()));
					System.out.print("> Linux 점수를 입력하세요:");
					student.setLinux(Integer.parseInt(CommonUtil.getUerInput()));
					if(student.getStudentNo().startsWith("1")) {
						System.out.print("> 인턴여부(Y/N)을 입력하세요:");
						student.setInternYn(CommonUtil.getUerInput());
					}else {
						System.out.print("> 경력년수을 입력하세요:");
						student.setCareerYears(Integer.parseInt(CommonUtil.getUerInput()));
					}
					if(test.insertStudent(student)>0) {
						System.out.println("수강생 정보 추가하였습니다.");
					}
					break; 
					 
				case 5:
					System.out.print("> 변경할 사번 입력하세요:");
					student.setStudentNo(CommonUtil.getUerInput());
		
					System.out.print("> C 점수를 입력하세요:");
					student.setC(Integer.parseInt(CommonUtil.getUerInput())); 
					System.out.print("> JAVA 점수를 입력하세요:");
					student.setJava(Integer.parseInt(CommonUtil.getUerInput()));
					System.out.print("> Linux 점수를 입력하세요:");
					student.setLinux(Integer.parseInt(CommonUtil.getUerInput()));
					if(student.getStudentNo().startsWith("1")) {
						System.out.print("> 인턴여부(Y/N)을 입력하세요:");
						student.setInternYn(CommonUtil.getUerInput());
					}else {
						System.out.print("> 경력년수을 입력하세요:");
						student.setCareerYears(Integer.parseInt(CommonUtil.getUerInput()));
					}
					if(test.updateStudent(student)>0) {
						System.out.println("수강생 정보 수정하였습니다.");
					}
					break; 
					
				case 6:
					System.out.print("> 삭제할 사번 입력하세요:");
					String sno;
					sno = CommonUtil.getUerInput();
					if(test.deleteStudent(sno)>0) {
						System.out.println("수강생 정보 삭제하였습니다.");
					}  
					break;
				
				case 7:
					System.out.print("> 검색할 사번 입력하세요:");
					sno = CommonUtil.getUerInput();
					students = test.searchStudents(sno);
					if(students!=null) {
						CommonUtil.printHead();					 
						System.out.println(students);				 
						CommonUtil.printTail();  
					}  
					break;			 
				}// switch end
			} // while end
		}
	
	public static void printMenu() {
		System.out.println("== <<성적 관리 시스템 메뉴>> ==");
		System.out.println("1. 전체 수강생 출력");
		System.out.println("2. 합격 수강생 출력");
		System.out.println("3. 불합격 수강생 출력");
		System.out.println("4. 수강생 정보 추가");
		System.out.println("5. 수강생 정보 수정(과목 점수, 경력, 인턴여부)");
		System.out.println("6. 학번으로 레코드 삭제");
		System.out.println("7. 학번으로 수강생 검색");
		System.out.println("8. 종료");
		System.out.println("============================");
	}
}
```

