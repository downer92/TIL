# 인터페이스

## 1. 인터페이스의 용도

- 사용자(User)와 제공자(Provider) 사이에서 매개체(연결) 역할
- 설계시에 서로 다른 시스템을 통합할 때 표준화를 위해서 활용한다.



## 2. 구성요소

- public static final 상수속성
- abstract method(구현 body 없음)
- static method
- default method

ex) public interface 인터페이스이름 [extends 인터페이스1, 인터페이스2, ...];



## 3. 주의해야 할 특징

- 인터페이스는 **이원화**된 구조이다. 따라서 인터페이스(선언)는 반드시 **인터페이스 구현 클래스**가 있어야만 선언한 서비스 제공이 가능하다.
- 인터페이스 타입은 참조변수의 타입(객체명)으로는 선언할 수 있지만 **객체생성은 불가능**하다.
  - 따라서 인터페이스를 구현한 클래스로 객체 생성이 가능하다! (다형성 객체)
- 인터페이스는 인터페이스만 상속 가능(클래스 상속 불가능)하며 다중 상속도 가능하다.



## 인터페이스 예제1

- 건반악기, 관악기, 현악기로 구성된 심포니 연주해보기.

- 건반악기: 피아노 / 관악기: 플룻, 트럼본/ 현악기: 바이올린, 비올라

- Class Diagram

  - Instrument(<<interface>>>): +playStart(), +playStop()

  - Gunban: +playStart(), +playStop(), toString: String

  - Kwan: +playStart(), +playStop(), toString: String

  - Hyeon: +playStart(), +playStop(), toString: String

  - Piano, Flute, Trumbon, Violin, Viola: toString: String

    

```java
package exercise.overall.symphony; 

public interface Instrument {  //1.인터페이스 선언
	public abstract void playStart(); 
	public abstract void playStop();
} //abstract method는 일반적으로 모든 자식클래스의 공통 기능을 선언하는 부모 클래스에 정의



public class Gunban implements Instrument { //2-1.건반악기 클래스 선언
    // implements로 건반클래스가 Instrument 인터페이스를 상속
	@Override
	public String toString() {return "건반악기";}
	@Override
	public void playStart() {System.out.println(this.toString()+ " 연주 시작");}
	@Override
	public void playStop() {System.out.println(this.toString()+ " 연주 종료");}
}


public class Kwan implements Instrument { //2-2.관악기 클래스 선언
	@Override
	public String toString() {return "관악기";}
	@Override
	public void playStart() {System.out.println(this.toString()+ " 연주 시작");}
    @Override
	public void playStop() {System.out.println(this.toString()+ " 연주 종료");}
}


public class Hyeon implements Instrument { //2-3.현악기 클래스 선언
	@Override
	public String toString() {return "현악기";}
	@Override
	public void playStart() {System.out.println(this.toString()+ " 연주 시작");}
	@Override
	public void playStop() {System.out.println(this.toString()+ " 연주 종료");}
}


public class Piano extends Gunban { //3-1.건반악기 클래스를 상속하는 피아노 클래스 선언
	@Override
	public String toString() {return super.toString() + " : 피아노";}
}

public class Flute extends Kwan { //3-2.관악기 클래스를 상속하는 플룻 클래스 선언
	@Override
	public String toString() {return super.toString() + " : 플룻";}
}

public class Trumbon extends Kwan { //3-3.관악기 클래스를 상속하는 트럼본 클래스 선언
	@Override
	public String toString() {return super.toString() + " : 트럼본";}
}

public class Violin extends Hyeon { //3-4.현악기 클래스를 상속하는 바이올린 클래스 선언
	@Override
	public String toString() {return super.toString() + " : 바이올린";}
}

public class Viola extends Hyeon { //3-5.현악기 클래스를 상속하는 비올라 클래스 선언
	@Override
	public String toString() {return super.toString() + " : 비올라";}
}


public class MusicTest { //4.Method 테스트 클래스 선언
	
    public static void main(String[] args) {
		Instrument[] e = new Instrument[] {new Piano(), new Flute(), new Timpani(),
			new Drum(),new Trumpet()}; 
//e[0] ~ e[4] 모든 객체는 자동으로 Upcasting돼서 선언이 되고 생성은 자식클래스로 생성된 다형성 객체
		playAll(e); 
		summary(e);
	} //Instrument 배열 건수만큼 For Loop 반복해서 playStart()와 playStop() 호출
	
    private static void playAll(Instrument[] e) { 
//Instrument 인터페이스의 구현 클래스들은 인자로 전달할 경우 자동으로 Upcasting이 되고, Downcasting할 수 있다.
		System.out.println("=============연주 시작=============");
		for(Instrument instrument : e) {instrument.playStart();}
		System.out.println();
		System.out.println("=============연주 종료=============");
		for(Instrument instrument : e) {instrument.playStop();}
		System.out.println();}
	
    private static void summary(Instrument[] e) {
		int gunban = 0, kwan = 0, hyeon = 0;
		System.out.println("=============연주 악기 목록=============");
		for(Instrument instrument : e) { 
            System.out.println(instrument);
			if(instrument instanceof Gunban) {
				gunban +=1;
			} else if(instrument instanceof Kwan) {
				kwan +=1;
			} else if(instrument instanceof Hyeon) {
				hyeon +=1;
            }
		}//for end
		System.out.println();
		System.out.println("=============연주 악기 수=============");
		System.out.println("##건반악기 수: " + gunban);
		System.out.println("##관악기 수: " + kwan);
		System.out.println("##현악기 수: " + hyeon);
		System.out.println("====================================");
	}
} 

```

