# 190618 javascript

## I. 자바스크립트 들어가기



**#자바스크립트의 특징**

1. 인터프리터 언어 
2. 동적 프로토타입 기반 객체지향언어 : 프로토타입을 상속을 받아서 그것을 기반으로 객체가 만들어짐
3. 동적 타입 언어 : 변수 앞에 타입을 선언하지 않고 저장되는 값에 따라서 그 변수의 값이 그 때 그 때 결정됨
4. 함수가 일급 객체이다 : 함수를 객체 취급한다!
5. 함수가 <u>클로저</u>를 정의한다 : 클로저를 정의하면 함수 내부에 있는 변수를 함수 밖으로 리턴받아서 사용할 수 있다.



**#저장할 때 주의할 사항**

1. 파일 이름 끝에 확장자를 붙인다 : OO.js
2. 파일의 문자 인코딩은 UTF-8로 설정한다. (유니코드 문자로 작성하는 언어이기 때문!)



```javascript
console.log("Hello, world!");
//Result: Hello, world! <.undefined

var n = 2 ; //var는 변수 선언
```



**#HTML문서에 자바스크립트 포함 위치**

```html
<head>
    <script>
    <!--1.자바스크립트 코드: 전역변수선언, 함수 선언 등-->
    <!--바디의 요소를 참조하거나 사용하는 자바스크립트 실행 문장은 오류가 발생할 가능성이 있다-->
    </script>
</head>
<body>
    <script>
    <!--2.자바스크립트 코드: 즉시 실행 문장과 관련된 코드--> 
    </script>
</body>
```



※but! HTML문서와 자바스크립트를 분리하는 것을 보통 권장한다. 그럴 경우는?

```html
<head>
    <script type="text/javascript" src="경로/파일.js">
        <!--이런식으로 별도의 자바스크립트 문서를 링크!-->
    </script>
</head>
<body>
</body>
```

-------------------------------------------



```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<script>
		window.alert("head 태그내에 포함된 javascript 실행");
	</script>
</head>
<body>
	<script>
		alert("body 태그내에 포함된 javascript 실행");
	</script>
</body>
</html>
```



**#외부 파일로 저장하기**

1) html내 자바스크립트 명령어를 통해 경로를 다른 자바스크립트 파일로 설정

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<script src="./first.js">
	</script>
</head>
<body>
  외부 javascript파일을 로딩해서 실행합니다.
</body>
</html>
```

2) 해당 경로에 자바스크립트 파일을 만들어서 명령어 지정

```javascript
window.alert("first.js파일에 저장된 javascript코드 실행")
```



#Console에 변수 정의하기 (오류의 예)

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
  #자바스크립트에서 변수 선언은 var 변수명; <br>
  var 변수명 = 초기값;
  자바 스크립트에서 문자열은 ""또는''로 감싸줘야 한다.	 
  <script>
  	var sum, a;
  	console.log("a=" + a + "<br>"); <!--콘솔에 출력하는 방법-->
  	document.write("sum=" + sum + "<br>"); 
  	//자바스크립트에서 선언만 한 변수는 아직까지 메모리엔 생성이 안된 것! 자바스크립트가 사용하는 브라우저 프로그램의 메모리에서 a변수와 sum변수로 저장된 값이 없으므로 undefined라고 나오는 것이다.
  	//document.write("x=" + x + "<br>"); 
  	//Error: x는 변수가 선언조차 안돼있어서 오류메시지가 뜬다
  </script>
</body>
</html>
```



**#전역객체**

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
    korea=3
  	document.write("korea=" + korea + "<br>"); //실행시에 전역객체(Global Object)는 window객체의 속성으로 추가된다. window객체는 어디서든 참조가 가능하다!
  </script>
</body>
</html>
```



※자바스크립트에서 같은 이름으로 선언된 변수는 모두 끌어올린 후에 하나의 영역에만 할당된다.



**#자바스크립트의 데이터 유형**

1. 정수와 실수는 구분하지 않고 number타입으로 통일
2. ""로 감싸도 ''로 감싸도 string타입으로 통일
3. 타입은 전부 소문자로! 대문자로 시작하는 String객체나 Number객체가 따로 있다는 것
4. **primitive type** : <u>string, number, boolean, undefined</u>(변수는 선언됐는데 값은 아직 선언되지 않은 경우 얘도 하나의 타입으로 봄), <u>null</u> / **reference type** : <u>function,  object</u>

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
	#자바스크립트의 데이터 유형 <br>
   <script>
   	var a = 1; 
   	document.write("a변수의 타입= "+ typeof(a) +"<br>");
   	var b = 0.5;
   	document.write("b변수의 타입= "+ typeof(b) +"<br>");
   	//정수와 실수 구분? A: 둘다 number라는 하나의 타입으로 통일돼 있다!
   	
   	a="javascript"; //동적타입언어! 
   	document.write("a변수의 타입= "+ typeof(a) +"<br>");
   	b='ECMAScript6';
	document.write("b변수의 타입= "+ typeof(b) +"<br>");
	//둘 다 string이라는 타입으로 통일!""든 ''든 string이다.
	
	a=function() {};
	document.write("a변수의 타입= "+ typeof(a) +"<br>");
	//타입은 function
	
	b=[]; //자바스크립트에서도 배열은 객체취급!
	document.write("b변수의 타입= "+ typeof(b) +"<br>");
	a={} //JSON(JavaScript Object Notation): 자바스크립트로 객체를 정의하는 표기법
	document.write("a변수의 타입= "+ typeof(a) +"<br>");
	b= new Object(); 
	document.write("b변수의 타입= "+ typeof(b) +"<br>");
	// 타입은 object

	a=true
	document.write("a변수의 타입= "+ typeof(a) +"<br>");
	// boolean 타입

   </script>
</body>
</html>

```



문자열의 ''나 ""안에서 특정 문자를 표기하고 싶을 때에는 이스케이프 시퀀스(\로 시작하는 것들)를 사용한다.



```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
	<script>
   	// a='"javascript"'
	// document.wirte(a+"<br>"); //"javascript"출력? X
	var c = [];
	document.write(c[0]+"<br>"); //없는 배열의 요소를 읽으면 출력? undefined
	a=function() {}; 
	document.write(a() + "<br>")//아무것도 반환하지 않는 함수가 반환하는 값은 출력? undefined
	a=function(d) {
		alert(d); // 함수를 호출했을 때 전달받지 못한 인수의 값은 뭐라고 찍힐까? undefined
	}
	a();
   </script>
</body>
</html>
```



--------------------------------------

## II. 연산자

※산술연산자에서 주의할 점

- 나누기의 경우 나눴을 때 자동으로 정수처리 되는 것이 아니라 실수값이 나올 수 있다는 것!
- 0/0 = NaN
- "one"+1 = NaN
- true + true = 2 (논리값의 타입을 숫자로 바꿔서 더함)
- 1 + null = 1 (null을 0으로 바꾸어 더함)
- 1+ undefined = NaN (undefined를 NaN으로 바꾸어 더함)



```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
   <script>
   실행할 때마다 주사위가 던져져서 값이 출력됩니다.
   <script>
   	var num = Math.round(Math.random()*5)+1;
   	document.write("주사위의 숫자 : "+num);
   </script>
</body>
</html>
```



JSON객체는  Object내장객체를 상속받는다.



**#문자열을 조작하는 메서드**

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
   <script>
	var msgObj = new String("Everything is practice");
   	document.write("msgObj.length :" + msgObj.length + "<br>");
   	document.write("msgObj.charAt(3) :" + msgObj.charAt(3) + "<br>");
   	document.write("msgObj[3] :" + msgObj[3] + "<br>");
   	document.write("msgObj.substring(7, 10) :" + msgObj.substring(7, 10) + "<br>");
   	document.write("msgObj.slice(7, 10) :" + msgObj.slice(7, 10) + "<br>");
   	document.write("msgObj.slice(-3) :" + msgObj.slice(-3) + "<br>");
   	document.write("msgObj.slice(-9, -6) :" + msgObj.slice(-9, -6) + "<br>");
   	document.write("msgObj.indexOf('t') :" + msgObj.indexOf('t', 10) + "<br>");
   	document.write("msgObj.indexOf('i', 10) :" + msgObj.indexOf('i', 10) + "<br>");
   	document.write("msgObj.split(' ') :" + msgObj.split(' ') + "<br>");
   	document.write("msgObj.replace('p', 'P') :" + msgObj.replace('p', 'P') + "<br>");
   	document.write("msgObj.includes('thing') :" + msgObj.includes('thing') + "<br>");
   	document.write("msgObj.charCodeAt(0) :" + msgObj.charCodeAt(0) + "<br>");
   	document.write("msgObj.codePointAt(0) :" + msgObj.codePointAt(0) + "<br>");
/* 리턴결과
msgObj.length :22
msgObj.charAt(3) :r
msgObj[3] :r
msgObj.substring(7, 10) :ing
msgObj.slice(7, 10) :ing
msgObj.slice(-3) :ice
msgObj.slice(-9, -6) : pr
msgObj.indexOf('t') :18
msgObj.indexOf('i', 10) :11
msgObj.split(' ') :Everything,is,practice
msgObj.replace('p', 'P') :Everything is Practice
msgObj.includes('thing') :true
msgObj.charCodeAt(0) :69
msgObj.codePointAt(0) :69
*/
    </script>
</body>
</html>
```



**#==연산자의 비교**

: ==은 값만 비교한다. 자바스크립트 엔진에서 자동으로 형변환이 수행된다.

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
   <script>
	document.write("null == undefined : " + (null == undefined) + "<br>");
   	document.write("1 == '1' : " + (1 == '1') + "<br>");
   	document.write("255 == '0xff' : " + (255 == '0xff') + "<br>");
   	document.write("true == 1 : " + (true == 1) + "<br>");
   	document.write("true == '1' : " + (true == '1') + "<br>");
   	document.write("new String('a') == 'a' : " + (new String('a') == 'a') + "<br>");
   	document.write("new Number(2) == 2 : " + (new Number(2) == 2) + "<br>");
   	//==은 값만 비교한다. 자바스크립트 엔진에서 자동 형변환이 수행됨.
/*리턴결과
null == undefined : true
1 == '1' : true
255 == '0xff' : true
true == 1 : true
true == '1' : true
new String('a') == 'a' : true
new Number(2) == 2 : true 
*/
</script>
</body>
</html>
```



**#===연산자의 비교**

: ===연산자는 값과 타입을 모두 비교해서 결과를 낸다.

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
   <script>
	document.write("null === undefined : " + (null === undefined) + "<br>");
   	document.write("1 === '1' : " + (1 === '1') + "<br>");
   	document.write("255 === '0xff' : " + (255 === '0xff') + "<br>");
   	document.write("true === 1 : " + (true === 1) + "<br>");
   	document.write("true === '1' : " + (true === '1') + "<br>");
   	document.write("new String('a') === 'a' : " + (new String('a') === 'a') + "<br>");
   	document.write("new Number(2) === 2 : " + (new Number(2) === 2) + "<br>");
    // =을 3개, 즉 ===를 쓰면 값만 비교하는 것이 아니라 값과 타입을 전부 비교한다.
/*리턴 결과
null === undefined : false
1 === '1' : false
255 === '0xff' : false
true === 1 : false
true === '1' : false
new String('a') === 'a' : false
new Number(2) === 2 : false */
</script>
</body>
</html>
```



**#eval, typeof, instanceof, in**

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
	<script>
	document.write("10>20>30 : " + (10>20>30)+ "<br>"); //false리턴 
	var a = "window.alert('eval은 문자열을 자바스크립트 코드로 실행한다.')";
	eval(a);
	var student = { "name":"kim", "ko":85, "en":90, "math":80};
	document.write("typeof(student): " + typeof(student)+"<br>");
	document.write("student instanceof Object: " + (student instanceof Object)+"<br>");
	document.write("ko in student : " + ('ko' in student) + "<br>");
/*리턴결과
10>20>30 : false
typeof(student): object
student instanceof Object: true
ko in student : true*/
    </script>
    </body>
</html>
```



**#형변환**

- 문자열로 형변환 : 값+"" 또는 String(값)
- 숫자로 형변환 : window.parseInt("123a") 또는 window.parseFloat("0.123b") 또는 Number("123a")
- 논리값으로 형변환 : !!값 또는 Boolean(값); 123

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
<h3> 자바스크립트 형변환 </h3>
#문자열로 형변환 : 값+"" 또는 String(값)<br>
#숫자로 형변환 : window.parseInt("123a") 또는 window.parseFloat("0.123b") 또는 Number("123a") <br>
#논리값으로 형변환 : !!값 또는 Boolean(값);
   
   <script>
   	document.write(window.parseInt("123a")+"<br>");
   	document.write(window.parseFloat("0.123b")+"<br>");
   	document.write(Number("123a") + "<br>");
   	document.write(!!" "+ "<br>");
   	document.write(!!""+ "<br>");
   	document.write(!!null + "<br>");
   	document.write(!!undefined + "<br>");
   	document.write(!!null + "<br>");
/*리턴결과
0.123
NaN
true
false
false
false
false
*/
   </script>
</body>
</html>
```



**#입력자**

- prompt : 숫자를 입력받을 때 사용
- confirm : boolean값을 입력받을 때 사용

```html
ex)	var input1 = window.prompt("점수를 입력하세요", 0); 
	//prompt는 숫자를 입력받을 때 사용
	document.write(input1+typeof(input1)+"<br>");

	var input2 = window.confirm("종료하시겠습니까?");
	//boolean값을 입력할 때는 confirm을 사용
	document.write(input2+typeof(input2)+"<br>");
```



**#조건문 연습문제**

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
<script>
	//문제1) if문을 이용해서 사용자로부터 입력받은 정수가 짝수인지 홀수인지 출력
	 var input = window.prompt("정수를 입력하세요", 0);
	 var num = parseInt(input);
	 if(num%2==0) {
	 	document.write("짝수입니다." + "<br>");
	 } else if(num%2==1) {
	 	document.write("홀수입니다." + "<br>");
	 }

	//문제2) 삼항연산자를 이용해서 위 문제 풀기

	var input = window.prompt("정수를 입력하세요", 0);
	var num = parseInt(input);
    //var num = Number(window.prompt("OOOOO",0));로 해도 됨!
	s=(num%2==0)?'짝수입니다.':'홀수입니다.';
	document.write(s);

	//문제3) &&,|| 등의 논리연산자를 이용해서 위 문제 풀기
	var input = window.prompt("정수를 입력하세요", 0);
	var num = parseInt(input);
    (num%2==0) || document.write("홀수입니다." + "<br>"); 
    //||의 경우 조건식1이 true이면 조건식2 수행하지 않고 false이면 수행한다.
    (num%2==0) && document.write("짝수입니다." + "<br>");
    //&&의 경우 조건식1이 true이면 조건식2 수행하고 false이면 수행하지 않는다.


	//문제4) switch문을 사용해서 사용자로부터 입력받은 점수에 대한
	//A(>=90), B(>=80), C(>=70), D(>=60), F(<60) 등급을 판별하는 웹 어플 구현
	var input = window.prompt("점수를 입력하세요", 0);
	var num = parseInt(input);
	// switch(Math.floor(num/10)) {
	// 	case 9 : document.write("A"); break;
	// 	case 8 : document.write("B"); break;
	// 	case 7 : document.write("C"); break;
	// 	case 6 : document.write("D"); break;
	// 	default: document.write("F"); break;
	// } 
	switch(true) {
		case num>89 : document.write("A"); break;
		case num>79 : document.write("B"); break;
		case num>69 : document.write("C"); break;
		case num>59 : document.write("D"); break;
		default : document.write("F"); break;
	}
    
    var nums = [1,2,3,4,5,6,7,8,9,10];
	for(var n in nums) {
		if(n%2==1) {
			document.write(n+"<br>");
		}
	}
//------------------------------------------------------	
	for(var i=0; i<10; i++) {
		if (i%2==1) {
			document.write(i+"<br>");
		}
	}
//------------------------------------------------------
	var i=0;
	while(i<10) {
		++i;
		if(i%2==1) {
			document.write(i+"<br>");
		}
	}
//------------------------------------------------------
	i=0;
	do{
		if(i%2==1)
			document.write(i+"<br>");
	} while(++i<10);
//-------------------------------------------------------
	for(var su=1; su<10; su++) {
		for(var dan=2; dan<10; dan++) {
			document.write(dan+'X'+su+'='+dan*su+'\t');
		}
		document.write("<br>");
	}
</script>
</body>
</html>
```













