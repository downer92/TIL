# 190619 javascript

## Review

**#자바스크립트?**

- 인터프리터 언어
- 동적 프로토타입 기반의 객체지향언어
- 동적 타입 언어
- 함수 기반 언어, 함수가 객체 => 함수형 프로그래밍 언어(함수를 변수에 저장, 함수의 인수로 함수를 전달, 함수 내부에 함수를 정의)
- 클로저 함수



**#자바스크립트 구성 기술 요소**

- ECMAScript Core
- 브라우저 제공 API(window, document, XMLHttpRequest,...)
- HTML5 API(Geolocation, WebWorks, Canvas, Video, Audio, DragnDrop,...)



**#자바스크립트 분류**

- 인코딩은 utf-8 권장
- 대소문자 구분
- .js파일로 저장
- 한 문장 단위로 ;으로 구분한다.()



**#자바스크립트에서 주석**

- 한줄 주석 : //
- 여러줄 주석 : /* */



**#변수** 

: 처리해야 할 값을 메모리에 저장하고 값을 참조하기 위해 사용하는 이름

- 변수 선언 : var 변수명
- 변수명 naming 규칙
  - _ , $ , 영문자로 시작
  - 두번째 문자부터는 숫자도 허용
  - 길이 제한 없음
  - 키워드X, 내장함수명X, 내장객체명 X



**#자바스크립트의 데이터 유형**

- primitive type : number, string, null, undefined, symbol, boolean
- reference type : function, object, interface, enum, ..... "배열(Array)는 객체인데 object유형이다!"



**#주의해야 할 경우**

- 선언되지 않은 변수를 참조하면 반환되는 값은? <u>ReferenceError</u>

- 선언만 된 변수, 초기값이 할당되지 않은 변수를 참조하면 반환되는 값은? <u>undefined</u>

- 객체를 메모리에서 검색을 했는데 검색되지 않으면 반환되는 값은? <u>null</u>



**#자바스크립트 출력방법**

- document.write(), document.writeln() : html문서의 body영역 출력

- console.log(), console.dir() : 브라우저 또는 node같은 자바스크립트의 실행환경에서 제공하는 콘솔창에 출력
- window.alert("메시지");



**#자바스크립트 입력방법**

- window.prompt("메시지", 기본값)  : 반환타입은 문자열
- window.confirm("메시지") : 반환타입은 boolean



**#자바스크립트 연산자**

- 산술연산자 : *, /, %, +, -
- 단항연산자 : ~(1의 보수), !, +, -, ++, --
- 비교연산자 : >, >=, <, <=, ==, !=, ===, !===(값과 타입까지 함께 비교)
- 비트연산자 : &, |, ^
- 논리연산자 : &&, ||
- shift 연산자 : <<, >>, >>>
- 삼항연산자 : 조건? 항1 : 항2 =>조건이 true일 때 항1 리턴, false일 때 항2 리턴
- 기타 연산자 : typeof, in, instanceof



**#switch문**

자바스크립트에서만 특이한 방식으로 쓸 수도 있는데

```javascript
switch(true) {
	case 조건1 : 문장; break;
	case 조건2 : 문장; break;
	case 조건3 : 문장; break;
	default : 문장;
}
```



**#반복문**

- 반복횟수를 알고 있을 때 : for(var count=0; count<조건; count증감식) {반복수행문장;}

- 조건에 따라 반복수행 여부를 결정해야 할 때 : while(조건) {반복수행문장;}

- 최초 1번은 무조건 수행후에 조건에 따라 반복수행 여부를 결정해야 할 때

  : do {반복수행문장;} while(조건);

- 배열의 요소 또는 객체의 속성을 순차적으로 꺼내올 때 사용할 수 있는 반복문

  : for( var 변수 in 배열or객체 ) {반복수행문장;}



**#hoisting**

```javascript
console.log(num); //정상 실행
var num = 10; //선언 문장은 hoisting됨. (소스코딩 구성상 앞으로 끌어올린다는 것!)
			  //global object인 window의 property로 추가됨
```



**#템플릿 리터럴과 placeholder** : 포맷형식 문자열에 실행시에 인수를 전달해서 

' 포맷형식 ${변수} 문자열 '



**#자바스크립트의 형변환** 

- 문자열로 형변환 : 값+" ", String()

- 정수나 실수로 형변환 : Number(), window.parseInt(), window.parseFloat()
- 논리형으로 변환 : !!값, Boolean()



-------------------------------------

## I.객체

**#자바 스크립트 객체 생성 방법**

1. 객체 리터럴 - JSON, 하나의 객체만 생성해서 사용하는 경우
2. 생성자 함수 정의 - new키워드 사용, 필요할 때마다 생성자함수로부터 객체 생성



#for in 반복문은 객체의 속성에 접근할 때 사용 가능

#객체에 대해서 사용하는 in키워드는 속성 존재 여부를 체크할 때 사용할 수 있다

```javascript
document.write("employee.ename=" + employee.ename+"<br>");
document.write("employee['job']=" + employee['job']+"<br>");
document.write("<br>");

for(var key in employee) {
	document.write(key + " : " + employee[key] +"<br>");
}
//key변수에는 객체의 property가 저장된다.

document.write("employee instanceof Object => "+ (employee instanceof Object) + "<br>"); //내장객체(Math, String, Number, ...) 중 최상위 Object객체 상속(자동으로 상속을 받는다는 것!)

console.dir(Object);
document.write(employee+ "<br>");

employee.toString = function() {
	var output = "";
	for(var key in this) {
		if(key != 'toString') {
			output+=key+" : "+this[key]+"\n";
		}
	} return output;
} 
document.write(employee+"<br>");
document.write(employee.toString()+"<br>");
delete(employee.adress);
document.write(employee+"<br>");
document.write("address in employee"+ ('address' in employee) + "<br>");
document.write("hiredate in employee"+ ('hiredate' in employee) + "<br>");
//해당 객체가 멤버인지 아닌지 확인하기 위해 in연산자 사용
```



#객체의 속성을 객체.속성 대신 속성명으로만 사용할 때 with(객체){} 사용한다.

```javascript
var student = {이름:'홍길동', 영어:88, 국어:90, 수학:77, 과학:75};
document.write(student.이름 +"의 총점 : " + (student.영어+student.국어+student.수학+student.과학) +"<br>");
//이렇게 번거로운 형태를 with를 사용해 아래와 같이 작성할 수 있다는 것.
with(student) {
	document.write(이름+"의 평균 : "+(영어+국어+수학+과학)/4 + "<br>");
}
```

#객체 리터럴 방식으로 정의되는 객체는 동적으로 속성, 메소드를 추가하거나 제거할 수 있다.



#var 변수 = function() {}; 익명(anonymous) 함수

#function 이름() {} named function, 선언적 함수

#사용자 정의 함수는 소스가 공개되지만, 내장함수 등의 소스는 native code로 공개하지 않는다.

#변수에 저장된 익명함수는 정의된 후에 호출이 가능하지만

#자바스크립트 엔진은 실행코드보다 먼저 선언적 함수를 읽는다.(hoisting)

#선언적 함수는 definition전에 호출을 하더라도 실행 순서상 문제가 되지 않는다.

```javascript
// func1(); //error
func2();  //선언적 함수(named function) 호출
var func1 = function(){
	var jum= Number(window.prompt("1~100사이의 수를 입력하세요"), 0);
	(jum%2==0)? alert("짝수") : alert("홀수");
}
function func2() {
	var jum= Number(window.prompt("1~100사이의 수를 입력하세요"), 0);
	(jum%2==0)? alert("짝수") : alert("홀수");
}
func1(); //변수에 저장된 함수 호출
```



**#자바스크립트 함수** 

- 모든 함수 가변인자를 가지는 함수로 정의할 수 있다.
- 함수가 실행될 때 실행 컨텍스트에서는 함수 내부에 arguments 배열과 유사한 타입의 속성이 생성된다. 
- arguments에 함수를 호출할 때 입력값인 인수가 저장된다. 
- 함수에 정의된 매개변수의 개수보다 많은 매개변수로 호출하면 실행시에 무시된다. 
- 함수에 정의된 매개변수의 개수보다 적은 매개변수를 호출하면 undefined로 전달된다.

```javascript
function hap(a, b) {
		document.write("함수의 인수개수 : " + arguments.length+ "<br>");
		var sum = 0;
		for(var item in arguments) {
			document.write(arguments[item]+"<br>");
			sum+=arguments[item];
		}
		document.write("함수의 a, b : "+a+", "+b+"<br>");
		return sum;
	} 
	document.write("hap(3, 5) 호출 : " + hap(3, 5) + "<br>");
	// 인수개수에 맞게 함수 호출, hoisting돼서 위에 이미 끌어당겨짐
	document.write("<br>");
	document.write("hap(1, 3, 5, 7, 9) 호출 : " + hap(1, 3, 5, 7, 9) + "<br>"); 
	// 인수개수보다 많이 함수 호출
	document.write("<br>");
	document.write("hap(3) 호출 : " + hap(3) + "<br>"); 
	// 인수개수보다 적게 함수 호출
	var nums = [2,4,6,8,10];
	document.write("hap(nums) 호출 : "+hap(nums)+"<br>");
	// 배열을 인수로, 함수로 호출

/* 결과
함수의 인수개수 : 2
3
5
함수의 a, b : 3, 5
hap(3, 5) 호출 : 8

함수의 인수개수 : 5
1
3
5
7
9
함수의 a, b : 1, 3
hap(1, 3, 5, 7, 9) 호출 : 25

함수의 인수개수 : 1
3 
함수의 a, b : 3, undefined
hap(3) 호출 : 3
함수의 인수개수 : 1
2,4,6,8,10
함수의 a, b : 2,4,6,8,10, undefined
hap(nums) 호출 : 02,4,6,8,10
*/
```



**#자바스크립트에서 배열은 모든 타입을 요소로 저장할 수 있다.**

```javascript
var arrays = [1, 'hello', true, function(){}, {name: 'korea'}, [100, 200]]; //숫자, 문자열, boolean, 함수, 객체, 배열 전부!
	for (var index in arrays) {
		document.write(index+ ": " +arrays[index] +"<br>"); }
```



**#함수 내부에 함수를 정의할 수 있다.** => 외부함수와 충돌이 발생하는 경우, 함수를 사용하는 내부에 정의할 수 있으며, 내부함수는 내부함수가 정의된 함수 내부에서만 호출할 수 있다.

```javascript
function pythagoras(width, height) { //직각삼각형의 빗변의 길이
	function square(x) { //인수의 제곱을 반환
	return x*x;
}
	return Math.sqrt(square(width)+square(height));
}
document.write("밑변3, 높이4인 삼각형의 빗변의 길이 : " + pythagoras(3,4) +"<br>");
//삼각형이 직각인지 확인하는 함수
	function square(width, height, hypotenuse) {
		if (width*width + height*height == hypotenuse*hypotenuse) {
			return true;
		} else {
			return false;
		}
	}
```



#유효범위 : 변수에 접근할 수 있는 범위

```javascript
var globalVar = 'korea'; //전역변수
function test(name) {
	globalVar2 = name; //var키워드를 생략한 함수 내부에 선언된 변수는 함수호출 후에 전역변수로 Global 실행 컨텍스트에 생성된다. 함수 외부에서 참조가 가능해진다.
	var localVar = "Hello~"+name+"!!"; //로컬변수
	return function() {
		return(localVar);
	}
}
	document.write("전역변수 global Var : "+globalVar+"<br>");
//	document.write("전역변수 global Var2 : "+globalVar2+"<br>"); //error
	test('독도'); //함수 호출 후
	document.write("전역변수 global Var2 : "+globalVar2+"<br>");
//	document.write("지역변수 localVar : "+localVar+"<br>"); //error
	document.write("지역변수 localVar를 클로저 함수를 통해 참조 가능\t"+
	test('제주도')()+"<br>");
```



#let : 블록 유효 범위를 갖는 지역변수 선언

#const : 블록 유효 범위를 갖는 상수 선언// const문으로 선언한 상수 값은 수정할 수 없지만 상수 값이 객체이거나 배열일 경우에는 프로퍼티 또는 프로퍼티 값을 수정할 수 있다.

```javascript
	let x = "outer x";
	{
		let x = "inner x";
		let y = "inner y";
		document.write("블럭 내부에서 x : "+ x + "<br>");
		document.write("블럭 내부에서 y : "+ y + "<br>");
	}
	document.write("블럭 외부에서 x : "+ x + "<br>");
//	document.write("블럭 외부에서 y : "+ y + "<br>"); ReferenceError
	{
		const c = 3;
				document.write("블럭 내부에서 c : "+ c + "<br>");
//				c=5;
	}
```



동일한 속성을 가지는 객체를 하나 이상 생성해야 할 경우 객체 리턴 



생성자 함수로 생성되는 객체들의 기능은 모두 동일하므로 객체 생성시마다 메모리에 객체의 메서드가 생성되는 것 보다는 

생성자 함수는 function객체로 메모리에 생성될 때 프로토타입 속성객체가 자동으로 생성된다.

프로토타입 속성객체에 생성자 함수로 생성되는 객체들의 기능을 추가하면, 전역 메서드처럼 사용 가능하다.

메모리 낭비를 줄이고.



``` javascript
var student = 
{이름:'홍길동', 영어:88, 국어:90, 수학:77, 과학:75, 
total:function(){ 
	return this.영어+this.국어+this.수학+this.과학; 
},
average: function(){
	return this.total()/4;
}
}
document.write(student.이름+"의 총점 : "+student.total()+"<br>");
document.write(student.이름+"의 평균 : "+student.average()+"<br>");


//but 객체가 여러개 있는 경우
function Student(name, ko, math, en, sci) {
	this.name = name;
	this.ko = ko;
	this.math = math;
	this.en = en;
	this.sci = sci;
}
	Student.prototype.total= function() {
		return this.en+this.math+this.ko+this.sci;
	};

	Student.prototype.average= function() {
		return this.total()/4;
	}

console.dir(Student);

//객체생성
var students = [ new Student('장기영',87, 82, 75, 82),
			     new Student('연하진',92, 98, 96, 98), 
 			     new Student('구지연',76, 96, 94, 90),
 			     new Student('나선주',98, 92, 96, 92),
 			     new Student('윤아린',95, 98, 98, 98),
 			     new Student('윤명월',64, 88, 92, 92),
 			     new Student('김미화',82, 86, 98, 88),
 			     new Student('김연화',88, 74, 78, 92),
 			     new Student('박아현',97, 92, 88, 98),
 			     new Student('서준서',45, 52, 72, 65) ];

 for (var idx in students) {
 	document.write(students[idx].name + "의 총점 : " + students[idx].total() + ", 평균 : " + students[idx].average() + "<br>");
 }
```



**#자바스크립트에서 배열은 서로 다른 타입의 요소를 저장할 수 있고 동적으로 요소를 추가하거나 삭제할 수 있다.**

```javascript
var array1 = new Array();
	var array2 = new Array(10); //요소 10개가 저장될 수 있는 배열 객체 생성
	var array3 = new Array(10, 20, 30, 40, 50);
	
	document.write("* array1.length :"+array1.length+"<br>");// 0
	document.write("* array2.length :"+array2.length+"<br>");// 10
	document.write("* array3.length :"+array3.length+"<br>");// 5
	array3[5] = 60;
	array3.push(70);
	for(var idx in array3)
	{
		document.write("* array3["+idx+"]="+ array3[idx]+"<br>");
	}
	document.write("<hr>");
	delete array3[1];
	for(var idx in array3)
	{
		document.write("* array3["+idx+"]="+ array3[idx]+"<br>");
	}
```





**#새 창열기**

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<script>
window.onload = function() {
	var btn = document.getElementById("newOpen");
	btn.onclick = function() {
		window.open("js12.html", "", "width=400 height=400");
	}
}
</script>
</head>
<body>
<h3>Window 객체 활용</h3>
<button id="newOpen"> 새창 열기</button> <br>
</body>
</html>
```





**#setInterval 함수**

```javascript
//setInterval(): 첫번째 인수에 지정된 함수가 두번째 인수로 지정된 시간마다 수행됨
		var cnt = 0;
		var intervalID = setInterval(function(){
			document.write(++cnt+"<br>");
		}, 1000);
		clearInterval(invervalID); 
```



**#setTimeout 함수**

```javascript
window.onload = function() {
			setTimeout
			(function(){window.close();}, 3000);
		}
```



**#window 함수들**

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<script>
	window.onload = function() {
	document.getElementById("up").onclick = function() {
		window.moveBy(0,-20); };
	document.getElementById("left").onclick = function() {
		window.moveBy(-20,0); };
	document.getElementById("right").onclick = function() {
		window.moveBy(20,0); };
	document.getElementById("down").onclick = function() {
		window.moveBy(0,20); };
}
</script>
</head>
<body>
<h3>js10.html</h3>
<input type="button" id="up" value="    UP   "   /> <br />
<input type="button" id="left" value="    LEFT   "   /> 
<input type="button" id="right" value="    RIGHT   "   /> <br />
<input type="button" id="down" value="    DOWN   "   /> 
</body>
</html>
```



**#Document 객체를 이용한 문서구조변경**

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<script>
		window.onload=function(){
		var h1 = document.createElement("h1");
		var text1 = document.createTextNode("새 요소 추가");
		h1.appendChild(text1);
		document.body.appendChild(h1);
		

		var img1 = document.createElement("img");
		img1.src="../jspractice2/dog.jpg";
		img1.width = 300;
		img1.height = 300;
		document.body.appendChild(img1);
		

		var img2 = document.createElement("img");
		img2.setAttribute('src', "../jspractice2/cat.jpg");
		img2.setAttribute('width', 300);
		img2.setAttribute('height', 300);
		console.log(img2.getAttribute("src"));
		document.body.appendChild(img2);


		console.log(document.getElementById("j1").innerHTML);
		var nodelist = document.getElementsByName("j2");
		console.log(nodelist.length);
		console.log(nodelist[0].innerHTML+","+nodelist[1].innerHTML);
		nodelist = document.getElementsByTagName("p");
		console.log(nodelist.length);
		var p1 = document.getElementById("j1");
		p1.style.border = "2px solid blue";
		p1.style.color = "orange";
		p1.style.fontSize="20";
		console.log(document.getElementById("j1").parentNode.nodeName);

		// document.body.removeChild(p1);
		}
	</script>
</head>
<body>
<h3>Document 객체를 이용한 문서 구조 변경</h3>
<p id="j1"> JavaScript </p>
<p id="j1"> JavaWorld </p>
<p id="j1"> JavaLife </p>
<p name="j2"> jQuery </p>
<p name="j2"> SencaTouch </p>
</body>
</html>
```





**#querySelector**

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Query Selector Demo</title>
  <style type="text/css">
    td {
      border-style: solid;
      border-width: 1px;
      font-size: 300%;
    }

    td:hover {
      background-color: cyan;
    }

    #hoverResult {
      color: green;
      font-size: 200%;
    }
  </style>

  <script>
  	window.onload = function() {
  		document.getElementById("findHover").onclick = function() {
  			var hovered = document.querySelector("td:hover");
  			if(hovered) {
  				document.getElementById("hoverResult").innerHTML= hovered.innerHTML; 
  			}
  		}
  	}
   </script>
</head>

<body>
<h3> document.querySelector() </h3>
  <section>
    <!-- create a table with a 3 by 3 cell display -->
    <table>
      <tbody><tr>
        <td>A1</td> <td>A2</td> <td>A3</td>
      </tr>
      <tr>
        <td>B1</td> <td>B2</td> <td>B3</td>
      </tr>
      <tr>
        <td>C1</td> <td>C2</td> <td>C3</td>
      </tr>
    </tbody></table>

    <div>Focus the button, hover over the table cells, and hit Enter to identify them using querySelector('td:hover').</div>
    <button type="button" id="findHover" autofocus="">Find 'td:hover' target</button>
    <div id="hoverResult"></div>
  </section>
</body>
</html>
```





**#querySelectorAll**

```html
<!DOCTYPE html>
<!-- saved from url=(0038)http://70.12.50.130:9000/js2/js17.html -->
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  
  <title>Query Selector All Demo</title>

  <style type="text/css">
    td {
      border-style: solid;
      border-width: 1px;
      font-size: 200%;
    }

    #checkedResult {
      color: green;
      font-size: 200%;
    }
  </style>

  <script>
    window.onload = function() {
      document.getElementById("findChecked").onclick = function() {
        var selected = document.querySelectorAll("*:checked");
        var result = "Selected boxes are: ";
        for (var i=0; i<selected.length; i++) {
          result +=(selected[i].name + " ");
         }
         document.getElementById("checkedResult").innerHTML= result; 
      }
    }
   </script>

</head>

<body>

  <section>

    <table>
      <tbody><tr>
        <td><input type="checkbox" name="A1">A1</td>
        <td><input type="checkbox" name="A2">A2</td>
        <td><input type="checkbox" name="A3">A3</td>
      </tr>

      <tr>
        <td><input type="checkbox" name="B1">B1</td>
        <td><input type="checkbox" checked="" name="B2">B2</td>
        <td><input type="checkbox" name="B3">B3</td>
      </tr>

      <tr>
        <td><input type="checkbox" name="C1">C1</td>
        <td><input type="checkbox" name="C2">C2</td>
        <td><input type="checkbox" name="C3">C3</td>
      </tr>
    </tbody></table>
    <div>Select various checkboxes, then hit the button to identify them using querySelectorAll("*:checked").</div>
    <button type="button" id="findChecked" autofocus="">Find checked boxes</button>
    <div id="checkedResult"></div> 
  </section>
</body></html>
```

