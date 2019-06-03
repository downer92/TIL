# 190603_Java Review

출처: 생활코딩



## I. 예외

:  실패하지 않는 법에 대한 수업. 낙법의 이치와 비슷하다. 덜 실패하는 법! 실패의 크기를 줄여주는 효과 뿐 아니라 실패에 대한 두려움을 억제해서 성공하는 법을 보다 적극적으로 시도할 수 있게 촉진한다는 점에서 중요한 부분!



**#예외란?**

: 프로그램을 만든 프로그래머가 상정한 정상적인 처리에서 벗어나는 경우에 이를 처리하기 위한 방법

```java
try {
    예외가 발생할 수 있는 문장; //이 사이에서 에러가 발생하면 그 순간 try안에서의 실행은 중지되고 catch키워드로 이동, catch{}안의 메서드가 실행됨.
} catch(예외클래스 인스턴스) {
    예외가 발생했을 때 실행되는 로직; //예외를 뒷수습하는 로직!
} 
```

그렇다면 어떻게 뒷수습을 할 수 있을 것인가?

```java
package lab.java.core;

public class ExceptionTest {
	
class Calculator {
	int left, right;
	public void setOprands(int left, int right) {
		this.left=left;
		this.right=right;
	}
	public void divide() {
		try {
			System.out.print("계산결과는 "); // 1
			System.out.print(this.left/this.right); //error => catch로 이동
			System.out.print(" 입니다.");
		} catch(Exception e) {
			System.out.println("\n\ne.getMessage()\n"+e.getMessage()); //2
			System.out.println("\n\ne.toString()\n"+e.toString()); //3
			System.out.println("\n\ne.printStackTrace()"); //4
			e.printStackTrace(); //5
		}
		System.out.println("Divdie End"); //catch안의 메소드가 다 실행이 되면 catch바깥으로 나와서 나머지 로직들이 계속해서 실행이 된다.
	}
}
```



**#여러개의 예외가 동시에 발생**한다면? **다중 catch 구문**을 사용한다! 단, 하위클래스 예외에서 상위클래스 예외의 순으로 처리해줘야 함.

```java
package lab.java.core;

class A {
		private int[] arr = new int[3];
		A() {
			arr[0] = 0;
			arr[10] = 10;
			arr[20] = 20;
		}
		public void z(int first, int second) {
			try {
				System.out.println(arr[first] / arr[second]); //ArrayIndexOutOfBoundsException Error
			} catch(ArithmeticException e) {
				System.out.println("ArithmeticException e");
			} catch(ArrayIndexOutOfBoundsException e) {
				System.out.println("ArrayIndexOutOfBoundsException e");
			} catch(Exception e) {
                System.out.println("Exception");
            } finally {
                System.out.println("finally");
            }
		}
	}
    
public class ExceptionDemo {
    public static void main(String[] args) {
        A a = new A();
        a.z(10, 0); //오류 발생
        a.z(1, 0); //오류 발생
        a.z(2, 1); //정상 동작
    }
}
}
```



#finally : try, catch와 무관하게 **언제나 실행되도록** 설계돼있는 로직!

- finally는 언제 사용할까?

  :  예외가 의심되는 로직이 예외가 발생했건 않았건 언제나 반드시 처리해야 될 일이 있다면 그 일을 fianlly 구간 안에 위치시키면 된다!

try~catch~finally의 과정은 API가 던진(throws) 예외를 강제로 처리하는 과정!



#책임의 전가 Throws : 넘기고 싶은 예외를 다음 사용자에게 넘기기 위해 사용하는 로직

```java
package lab.java.core;

public class ExceptionHandleTest {
	public void checkTall(double tall) throws AbnormalValueException{
		//중학생 키 범위를 140이상 180이하 여부를 체크해서 범위가 아니면 예외를 던진다.
		//키 값의 범위를 체크해서 예외가 발생하면 예외처리한다.
		if(tall<140) throw new AbnormalValueException("140보다 작습니다");
		if(tall>180) throw new AbnormalValueException("180보다 큽니다");
	}
	
	public static void main(String[] args) throws AbnormalValueException {
		double[] talls = new double[] { 155.5, 163.2, 170.4, 149.5, 
				128, 168, 189.5, 166, 172, 169, 158, 173 };
		//키 값의 범위를 체크해서 예외가 발생하면 예외처리한다.
		//=>작년도 키 평균값으로 보정한다.
		//올해의 중학생 평균 키 값을 출력
		ExceptionHandleTest test = new ExceptionHandleTest();
		for(int i=0; i<talls.length; i++) {
			try{
				test.checkTall(talls[i]); //예외처리문장
			} catch(AbnormalValueException e) {
				System.out.println(e.getMessage() + ", 작년도 키 값으로 보정합니다.");
				talls[i] = e.getOldTall();
			} 
		}
		double hap = 0.0;
		for(double tall : talls)
			hap +=tall; // 배열의 총합
		System.out.println("올해 중학생 평균 키는 " +(hap/talls.length)+"cm입니다.");
	
	} //main end
} //class end
```

