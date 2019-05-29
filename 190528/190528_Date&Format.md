# 190528_Chapter 10



## I. 날짜와 시간

Calendar는 추상클래스이기 때문에 직접 객체를 생성할 수 없고, 메서드를 통해서 완전히 구현된 클래스의 인스턴스를 얻어야 한다!

```java
Calendar cal = new Calendar(); // 에러! 추상클래스!
Calendar cal = Calendar.getInstance(); // OK! getInstance() 메서드를 이용한다.
```



캘린더 생성 방법

```java
java.util.Calendar

Calendar cal = Calendar.getInstance();
cal.get(Calendar.MONTH) //현재 월 
    
cal.set(2019, 5, 31) // 5월 31일 설정
cal.add(2019, 6, 1) // 6월 1일 추가

//날짜 데이터를 특정 형식으로 문자열화하기
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
Date d = new Date();
sdf.format(d);
```



- 예제1

```java
package lab.java.core;

import java.util.Calendar;

public class CalendarEx2 {
	
	
	public static void main(String[] args) {
		//요일은 1부터 시작하기 때문에 DAY_OF_WEEK[0]은 비워두는 것!
		final String [] DAY_OF_WEEK = {"", "일", "월", "화", "수", "목", "금", "토"};
		Calendar date1 = Calendar.getInstance();
		Calendar date2 = Calendar.getInstance();
		
		//month의 경우 0부터 시작하기 때문에 8월인 경우, 7로 지정해야 함!
		//date1.set(2015, Calendar.AUGUST, 15); 와 같이 할 수도 있다.
		date1.set(2015, 7, 15); //2015년 8월 15일로 날짜를 설정
		System.out.println("date1은 "+ toString(date1) + DAY_OF_WEEK[date1.get(Calendar.DAY_OF_WEEK) ] +
				"요일이고,");
		System.out.println("오늘(date2)은 " + toString(date2)+ DAY_OF_WEEK[date2.get(Calendar.DAY_OF_WEEK)] +
				"요일입니다.");
		
		//두 날짜간의 차이를 얻으려면, getTimeInMillis() 사용해서 천분의 일초 단위로 변환해야 한다.
		long difference = (date2.getTimeInMillis() - date1.getTimeInMillis()) / 1000;
		System.out.println("그 날(date1)부터 지금(date2)까지 "+difference+"초가 지났습니다.");
		System.out.println("일(day)로 계산하면 " + difference/(24*60*60) + "일입니다."); 
        //1일= (24*60*60)초	
	}
    
	public static String toString(Calendar date) {
		return date.get(Calendar.YEAR)+ "년 " + (date.get(Calendar.MONTH)+1) +"월 " +
	date.get(Calendar.DATE) + "일 ";
	}
}
```

- 예제2

```java
package lab.java.core;

import java.util.Calendar;

public class CalendarEx3 {

	public static void main(String[] args) {
		final int[] TIME_UNIT = {3600, 60, 1}; //큰 단위를 앞에 놓는다.
		final String[] TIME_UNIT_NAME = {"시간 ", "분 ", "초 "};
		
		Calendar time1 = Calendar.getInstance();
		Calendar time2 = Calendar.getInstance();
		
//		#time1을 10시 20분 30초로 설정
		time1.set(Calendar.HOUR_OF_DAY, 10);
		time1.set(Calendar.MINUTE, 20);
		time1.set(Calendar.SECOND, 30);
		
//		#time2를 20시 30분 10초로 설정
		time2.set(Calendar.HOUR_OF_DAY, 20);
		time2.set(Calendar.MINUTE, 30);
		time2.set(Calendar.SECOND, 10);
		
		System.out.println("time1 :" + time1.get(Calendar.HOUR_OF_DAY) + "시 " +
		time1.get(Calendar.MINUTE) +"분 " + time1.get(Calendar.SECOND)+"초" );
		System.out.println("time2 :" + time2.get(Calendar.HOUR_OF_DAY) + "시 " +
				time2.get(Calendar.MINUTE) +"분 " + time2.get(Calendar.SECOND)+"초" );
		
//		# time1과 time2의 시간차이
		long difference = Math.abs(time2.getTimeInMillis()-time1.getTimeInMillis())/1000;
		//getTimeInMillis()는 1/1000초 단위로 값을 반환하기 때문에 초 단위로 값을 반환하기 위해서는 		//1000으로 나누어 줘야 한다!
        System.out.println("time1과 time2의 차이는 " + difference + "초 입니다.");
		String tmp = "";
		
//		#시간차이를 시분초로 변환하기
		for(int i=0; i <TIME_UNIT.length; i++) {
			tmp +=difference/TIME_UNIT[i] +TIME_UNIT_NAME[i];
			difference %= TIME_UNIT[i];
		}//가장 큰 단위인 시간 단위(3600초)로 나누고 남은 나머지를 다시 분 단위(60초)로 나누면
		 // 그 나머지는 초 단위 값이 된다.
		System.out.println("시분초로 변환하면 " + tmp + "입니다.");
	}
}
```



- StringTokenizer: StringTokenizer는 내부에 포인터를 가지고 있고 구분자를 기준으로 포인터를  이동하면서 hasNextTokens( ) 메서드는 Token이 있으면 true를 리턴하고 없으면 false를 리턴한다. 포인터가 가리키는 Token을 반환받으려면 nextToken( )메서드를 사용하며 이 과정을 반복문에서 수행한다.

```java
String s = "월, 화, 수, 목, 금, 토, 일";
StringTokenizer sToken = new StringTokenizer(s, ",");
```



## II. 형식화 클래스

**#DecimalFormat**

: 숫자를 형식화 하는데 사용. 숫자 데이터를 정수, 부동소수점, 금액 등의 다양한 형식으로 표현할 수 있으며, 반대로 일정한 형식의 텍스트 데이터를 숫자로 쉽게 변환하는 것도 가능하다. 패턴을 정의하는 것이 중요!

cf) 특정 형식으로 문자열화된 데이터를 숫자로 변환하려면 df.parse( ) 사용!



- 예제1

```java
package lab.java.core;

import java.text.DecimalFormat;

public class DecimalFormatTest {

	public static void main(String[] args) {
		double number = 1234567.89;
//		1.원하는 출력형식의 패턴 작성
		String[] pattern = { 
				"0",				//1234568: 정수부까지 반올림
				"#",				//1234568: 정수부까지 반올림
				"0.0",				//1234567.9: 소숫점 첫째자리까지 반올림
				"#.#",				//1234567.9: 소숫점 첫째자리까지 반올림
				"0000000000.0000",	//0001234567.8900: 무의미한 0표시 
				"##########.####",	//1234567.89: 무의미한 0 표시 안함
				"#.#-",				//1234567.9-
				"-#.#",				//-1234567.9
				"#,###.##",			//1,234,567.78
				"#,####.##",		//123,4567.89
				"#E0",				//.1E7
				"0E0",				//1E6
				"##E0",				//1.2E6
				"00E0",				//12E5
				"####E0",			//123.5E4
				"0000E0",			//1235E3
				"#.#E0",			//1.2E6
				"0.0E0",			//1.2E6
				"0.000000000E0",	//1.234567890E6
				"00.00000000E0",	//12.34567890E5
				"000.0000000E0",	//123.4567890E4
				"#.#########E0",	//1.23456789E6
				"##.########E0",	//1.23456789E6
				"###.#######E0",	//1.23456789E6
				"#,###.##+;#,###.##-",	//1,234,567.89+
				"#.#%",				//123456789%
				"#.#\u2030",		//1234567890\u2030
				"\00A4 #,###",		//\ 1,234,568: 화폐
				"'#'#,###",			//#1,234,568
				"''#,###"			//'1,234,568
				
		};
		
		for (int i=0; i<pattern.length; i++) {
//			2.DecimalFormat인스턴스를 생성
			DecimalFormat df = new DecimalFormat(pattern[i]);
//			3.출력하고자 하는 문자열을 for문을 통해 호출
			System.out.printf("%19s : %s\n", pattern[i], df.format(number));
		} // for end
	} //main end
}//class end
```



**#SimpleDateFormat**

: Date와 Calendar만으로 날짜 데이터를 원하는 형태로 출력하는 것은 불편하고 복잡하지만 SimpleDateFormat을 사용해서 이를 간단하게 해결할 수 있다.

- 예제1

```java
package lab.java.core;

import java.text.SimpleDateFormat;
import java.util.Date;

public class DateFormatEx1 {

	public static void main(String[] args) {
//		1.Date 객체 생성
		Date today = new Date();
		
		SimpleDateFormat sdf1, sdf2, sdf3, sdf4;
		SimpleDateFormat sdf5, sdf6, sdf7, sdf8, sdf9;
		
//		2.원하는 출력형식의 패턴을 작성해 SimpleDateFormat인스턴스를 생성
		sdf1 = new SimpleDateFormat("yyyy-MM-dd"); 
        // y: 년도, M: 월(1~12 또는 1월~12월), d: 월의 몇 번째 일(1~31)
		sdf2 = new SimpleDateFormat("''yy년 MMM dd일 E요일"); 
        // E: 요일
		sdf3 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS"); 
        //s: 초(0~59), S: 천분의 일초(0~999)
		sdf4 = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss a"); 
        //a: 오전/오후(AM, PM)
		sdf5 = new SimpleDateFormat("오늘은 올 해의 D번째 날입니다."); 
        // D: 년의 몇 번째 일(1~366)
		sdf6 = new SimpleDateFormat("오늘은 이 달의 d번째 날입니다."); 
		sdf7 = new SimpleDateFormat("오늘은 올 해의 w번째 주입니다."); 
        // w: 년의 몇 번째 주(1~53)
		sdf8 = new SimpleDateFormat("오늘은 이 달의 W번째 날입니다."); 
        // W: 월의 몇 번째 주(1~5)
		sdf9 = new SimpleDateFormat("오늘은 이 달의 F번째 E요일입니다."); 
        // F: 월의 몇 번째 요일(1~5), E: 요일
		
		
//		3.출력하고자 하는 Date인스턴스를 가지고 format(Date d)를 호출
		System.out.println(sdf1.format(today));
		System.out.println(sdf2.format(today));
		System.out.println(sdf3.format(today));
		System.out.println(sdf4.format(today));
		System.out.println();
		System.out.println(sdf5.format(today));
		System.out.println(sdf6.format(today));
		System.out.println(sdf7.format(today));
		System.out.println(sdf8.format(today));
		System.out.println(sdf9.format(today));
	}
}

/* <출력>
2019-05-28
'19년 5월 28일 화요일
2019-05-28 16:24:18.797
2019-05-28 04:24:18 오후

오늘은 올 해의 148번째 날입니다.
오늘은 이 달의 28번째 날입니다.
오늘은 올 해의 22번째 주입니다.
오늘은 이 달의 5번째 날입니다.
오늘은 이 달의 4번째 화요일입니다.
*/
```

- 예제2

```java
package lab.java.core;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class DateFormatEx2 {
	public static void main(String[] args) {
		Calendar cal = Calendar.getInstance();
		cal.set(2005, 9, 3); 
		Date day = cal.getTime(); 
        // Calendar를 Date로 변환하는 방법
        
		SimpleDateFormat sdf1, sdf2, sdf3, sdf4;
		sdf1 = new SimpleDateFormat("yyyy-MM-dd");
		sdf2 = new SimpleDateFormat("yy-MM-dd E요일");
		sdf3 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
		sdf4 = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss a");
		
        // Date인스턴스만 format메서드에 사용될 수 있기 때문에 
        // 위에서 Calendar인스턴스를 Date인스턴스로 변환한 것이다.
		System.out.println(sdf1.format(day));
		System.out.println(sdf2.format(day));
		System.out.println(sdf3.format(day));
		System.out.println(sdf4.format(day));
	}
}
```

**#java.time패키지**

```java
LocalDate today = LocalDate.now()
//get()으로 Month값 반환받을 때 1~12값 반환
LocalTime = LocalTime.now()
```

