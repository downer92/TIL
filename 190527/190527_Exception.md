# 2019.05.27

# 1.예외처리

## 1) 에러의 종류

- Compile error - 문법적 문제, 언어 규칙에 맞지 않는 문제
- Runtime error - 실행시에 발생되는 오류 => 논리 오류, 로직 오류
- 자바의 runtime error - XXXError(프로그램적으로 수정할 수 없다. 무겁고 치명적)

RunTimeException의  하위Exception은 프로그램적으로 수정하면 정상적으로 프로그램 흐름을 유도 가능



## 2) 자바의 Exception

- **Checked Exception** : 실행 범위가 JRE를 넘어가는 경우의 코드에 대해서 
  - ex) IOException, Socket, ..... , SQLException
- **Unchecked Exception**:  실행 범위가 JRE를 벗어나지 않고, 사용자 부주의 또는 논리 오류에 의해서 발생될 수 있는 Exception 
  - ex) NullPointerException, ArrayIndexOutOfBoundsException, NumberFormatException



## 3) 예외처리 방식

- **Declare** 방식: throws를 메서드 선언부에 선언한다. 예외처리 대신에 메서드를 호출한 곳으로 예외처리를 떠넘긴다.
- **Handle** 방식: try~catch~finally

``` java
try {
    예외 발생될 가능성이 있는 문장;
    문장;
} catch(예외클래스타입 객체) {
    예외처리 문장;
} catch(예외클래스타입 객체) {
    예외처리 문장;
} finally {
    예외발생과 무관한 반드시 수행해야 할 코드 문장;
    ex) 사용했었던 자원 정리		.close() => checked exception
    try~catch 사용 가능
}
```



- catch를 여러개 정의할 경우 하위 Exception클래스부터 상위 Exception클래스 순으로 정의한다.

- 프로그램 구현시 의도적으로 예외를 발생시켜서 호출한 쪽(caller)에게 메시지를 전달해서 호출한쪽(caller)에서 흐름을 제어할 수 있도록 throw new 예외클래스(메시지)

- API에서 java.lang.Throwable - java.lang.Error/java.lang.Exception

- 사용자 정의 예외클래스

  AccessModifier class XXXException extends 구체적 Exception(API) {

​		// 속성

​		// 생성자

​		// 기능

​		}