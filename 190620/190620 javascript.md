# 190620 javascript

## Review

**#자바스크립트 함수를 정의하는 방법**

- 함수 선언문으로 정의

  - function square(x) { return x*x; }

- 함수 리터럴(익명 함수)로 정의

  - var square = function(x) { return x*x }

    square(5); //호출

- Function 생성자로 정의

  - var square = new Function("x", "return x*x");

- 화살표 함수 표현식(람다식)으로 정의

  - var square = x => x*x (return키워드 생략하고 바로 출력값 씀)

- 즉시 실행 함수 : 익명 함수를 정의하고 바로 실행하는 함수 
  - (function(x) { return x*x })(5)//   5는 넣고자 하는 인수
  - 한번 실행하기 때문에 초기화 작업을 할 때 많이 사용
  - 전역 유효 범위를 오염시키지 않는다.



#모든 함수의 인수는 <u>가변 길이</u>를 가진다.

- 선언된 인수보다 적으면  인수를 참조할 때 undefined 출력
- 선언된 인수보다 많으면 무시
- 모든 함수가 생성될 때 인수가 저장되는 함수의 property는 Arguments(타입) 객체의 arguments(프로퍼티명) 
  - arguments.length(인수가 몇개 넘어갔는지 확인)
  - arguments[index] (인수에서 특별한 순서에 해당하는 인수를 꺼내서 쓸 때)



#자바스크립트에서 <u>재귀함수</u>를 정의하고 사용할 수 있다.

```javascript
//ex)
function fact(n) {
    if(n<=1) return n;
    return n*fact(n-1);
}
fact(5);
```



#함수가 호출되어 실행되는 시점에 this값이 결정된다.

- 최상위 레벨의 코드에서 this는 Window객체의 참조변수 window
- 이벤트 핸들러 함수 내부에서 this는 이벤트 소스 객체

```javascript
window.onload = 이벤트핸들러 함수() {};
window.onload = function() {this.....//?
                           };
button.onclick = function() {
    this....//클릭이벤트가 발생한 버튼
};
```

- 생성자 함수 안에서 this는 생성자 함수로부터 생성되는 객체 자신
- 호출된 함수 내부에서 this는 window이다.

```javascript
console.log((function(x) {return x*x}) (5));
	console.log(this);
	console.log(this==window);
	function f() {console.log(this);} //전역 유효범위의 namespace에 추가되므로
		f(); //this는 window!
```



**#객체 정의 방법**

1. 객체 리터럴로 정의

   {속성:값, 속성:값, 속성:function(){},...}

2. 생성자 함수를 정의하고 생성자 함수로부터 객체를 생성할 수 있다.

```javascript
function Person(name, age) {
    var _name = name; //private성격의 속성을 가진 로컬변수 => 외부에서 참조될 수 없음. 
    var _age = age;
    return { //객체를 리턴하는 경우 {}로!
        getName : function() { return _name; },
        getAge : function() { return _age; },
    	setAge : function(n) { _age = n; }
    };
}

var p = new Person("kim", 30);
// console.log(p._name); // undefined
// console.log(p._age); // undefined
console.log(p.getName());
console.log(p.getAge());
```



**#클로저 함수**

```javascript
function makeCounter() {
		var count = 0;
		return g;
		function g() { //클로저 함수 : 원래는 외부 변수를 사용할 수 없는데 리턴을 통해 사용할 수 있게 해주는!
			return count++;
		}
	}
var counter = makeCounter(); //원래 함수 수행이 끝나면 garbage collection돼야 하는데 클로저 함수를 리턴하는 함수의 실행 Context는 Context 메모리에 계속 남아있다.
console.log(counter());
console.log(counter());
console.log(counter());
console.log(counter());
```



ex) 클로저 함수 예제

```javascript
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
<script>
//1.
        window.onload = function() {
		var buttons = document.getElementsByTagName("input");
		for(var i=0; i<buttons.length; i++) {
			let _i = i;
			buttons[_i].onclick = function() {
				console.log(_i);
			}
		} //for end
	}
	
//2.	
		window.onload = function() {
		var buttons = document.getElementsByTagName("input");
		for(var i=0; i<buttons.length; i++) (function(_i) {
			buttons[_i].onclick = function() {
				console.log(_i);
			}
		}) (i);
	};

</script>
</head>

<body>
<h3> 클로저 함수를 사용해야 하는 예제 </h3>
<input type="button" value="0">
<input type="button" value="1">
<input type="button" value="2">
</body>
</html>
```



**#함수적 프로그래밍 특성**

- 변수에 함수를 저장할 수 있다.
- 배열의 요소로 함수를 저장할 수 있다.
- 함수 내부에 함수를 정의할 수 있다. (nested function : 내부함수)
- 함수에서 함수를 반환할 수 있다.
- 내부에 함수를 정의하거나 함수를 반환하는 함수를 '<u>고차 함수</u>'라고 한다.
- 함수의 인수로 함수를 전달할 수 있다. (인수로 전달할 수 있는 함수는 '<u>콜백함수</u>'라고 한다.)



**#자바스크립트 객체 분류**

- 내장 객체 : Object, String, Boolean, Number, Array
- 브라우저 객체
- ECMAScript 객체



**#객체**

- Window - close(), open(url, name, {...}), moveBy(), moveTo(), alert(), confirm(), prompt(), setTimeout(function(){}, time), setInterval(function(){}, time), clearInterval(id)

  Window객체의 속성 document는 Document로서 HTML요소관련 처리 객체

- Document - getElementById(""), getElementsByName(""), getElementsByTagName(""), getElementsByClassName(""), querySelector("css의 selector 형식"), querySelectorAll("css의 selector형식"), createElement(), createComment(), createDocumentFragement(), createAttribute(), createTextNode(), setAttribute(), getAttribute(), removeAttribute(), parentNode, childNode, body, appendChild()



--------------------------



**#스크롤 넣기 예제**

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<style>
	.box {
		display: inline-block;
		padding: 100px;
		margin: 100px;
		margin-left: 0;
		background-color: skyblue;
	}
</style>
<body>
	<div class="box" id="sec1"> #sec1 </div> <br>
	<div class="box" id="sec2"> #sec2 </div> <br>
	<div class="box" id="sec3"> #sec3 </div>

<script>
	function getScrollTop() {
		if(window.pageYOffset !== undefined) {
			return window.pageYOffset;
		} else {
			return document.documentElement.scrollTop || document.body.scrollTop;
		}
	}

	function getScrollLeft() {
		if(window.pageXOffset !== undefined) {
			return window.pageXOffset;
		} else {
			return document.documentElement.scrollLeft || document.body.scrollLeft;
		}
	}

	if ('scrollRestoration' in history) {
		history.scrollRestoration = 'manual';
	}
	var element = document.getElementById("sec3");
	var rect = element.getBoundingClientRect();
	scrollTo(rect.left+getScrollLeft(), rect.top+getScrollTop());
</script>
</body>
</html>
```



**#자바스크립트 이벤트**

- DOM Level 0 이벤트 모델 : on이벤트명 = function(){}=> 이벤트당 하나의 이벤트 핸들러만 연결
- DOM Level 2 이벤트 모델 : 이벤트소스(태그객체).addEventListener("이벤트명, function(){}, 이벤트캡쳐여부") - 이벤트캡쳐여부값은 기본이 false. 이벤트당 하나 이상의 이벤트 핸들러만 연결
- 이벤트에 대한 이벤트 핸들러가 한번만 수행 후 이벤트 핸들러 취소하려면 : 이벤트 소스.on이벤트속성 = null;
- 이벤트 핸들러  함수 내부에서 이벤트 객체의 속성들을 핸들링 할 때 이벤트 소스 객체 this를 참조한다.

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
<script>
/*	window.onload=function() {
		alert("load event handler1");
	}
	window.onload=function() {
		alert("load event handler2");
	}
	window.onload=function() {
		alert("load event handler3");
	}
*/
	

/*	window.addEventListener("load", 
		function(){alert("load event handler1")}, false);
	window.addEventListener("load", 
		function(){alert("load event handler2")}, false);
	window.addEventListener("load", 
		function(){alert("load event handler3")}, false);
*/
	window.addEventListener("load", function(){
		var h3=document.querySelector("#evt");
		h3.onclick = function() {
			alert("까꿍");
			this.onclick = null; //이벤트핸들러가 한번만 수행되도록!

		}
	});
</script>
</head>
<body>
	<h3 id="evt">이벤트 핸들러가 한번만 수행</h3>
</body>
</html>
```



**#강제 이벤트 발생방법**

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>이벤트</title>
<script>
		window.addEventListener("load", function(){
		document.querySelector("#btn1").onclick = function() {
		var span1= document.querySelector("#count1");
			span1.innerHTML=Number(span1.innerHTML)+1;
		};

		document.querySelector("#btn2").onclick = function() {
			var span2 = document.querySelector("#count2");
			span2.innerHTML=Number(span2.innerHTML)+1;
			document.querySelector("#btn1").onclick(); //강제 이벤트 발생
		};
	}, false);
</script>
</head>
<body>
 <h3> 자바스크립트 이벤트 </h3>
# 강제 이벤트 발생  방법 : 이벤트소스객체.on이벤트();<br>
<button id="btn1">Button 1</button>
<button id="btn2">Button 2</button><br>
<h3>Button 1 Click Count : <span id="count1">0</span></h3>
<h3>Button 2 Click Count : <span id="count2">0</span></h3>

</body></html>
```





**#버블링과 캡쳐링**

- 버블링 : html문서 내에서 자식 태그객체에서 발생된 이벤트가 부모 태그 객체로 이벤트 전파되는 것
- 캡쳐링 : html문서 내에서 부모 태그객체에서 발생된 이벤트가 자식 태그 객체로 이벤트 전파되는 것
- 이벤트 전파를 막으려면? 

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>이벤트</title>
<style>
div, h1, p { border:2px solid black;
             padding : 10px;
             margin : 10px; }
</style>
<script>
 window.addEventListener("load", function(evt){
	document.getElementById("outerDiv").onclick= function(){
		var event = evt || window.event;
		event.cancelBubble = true; //IE의 이벤트 전파를 취소
		if(event.stopPropagation) {
			event.stopPropagation(); //W3C 표준 이벤트 전파 취소 함수
		}	
		this.style.backgroundColor='gray';
	}
	document.getElementById("innerDiv").onclick= function(evt){
		var event = evt || window.event;
		event.cancelBubble = true; //IE의 이벤트 전파를 취소
		if(event.stopPropagation) {
			event.stopPropagation(); //W3C 표준 이벤트 전파 취소 함수
		}	
		this.style.backgroundColor='cyan';
	}
	document.getElementById("header1").onclick= function(evt){
		var event = evt || window.event;
		event.cancelBubble = true; //IE의 이벤트 전파를 취소
		if(event.stopPropagation) {
			event.stopPropagation(); //W3C 표준 이벤트 전파 취소 함수
		}	
		this.style.backgroundColor='magenta';
	}
	document.getElementById("p1").onclick= function(evt){
		var event = evt || window.event;
		event.cancelBubble = true; //IE의 이벤트 전파를 취소
		if(event.stopPropagation) {
			event.stopPropagation(); //W3C 표준 이벤트 전파 취소 함수
		}		 
		this.style.backgroundColor='orange';
	}
}, false);
</script>
</head>
<body>
 <h3> 자바스크립트 버블링과 캡처링 </h3>
자바스크립트 버블링 : html문서내에서 자식 태그객체에서 발생된 이벤트가 부모 태그 객체로 이벤트 전파되는 것 <br>
자바스크립트 캡처링 : html문서내에서 부모 태그객체에서 발생된 이벤트가 자식 태그 객체로 이벤트 전파되는 것 <br>
<div id="outerDiv">
  <div id="innerDiv">
    <h1 id="header1">
       <p id="p1">이벤트 전파</p>
    </h1>
  </div>
</div>
</body>
</html>
```



#브라우저에 정의된 기본 이벤트 취소 : 브라우저에서 자동으로 처리해주는 기본 이벤트 핸들러를 취소하려면 이벤트 핸들러 함수를  override해서 false를 리턴한다.

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
<title>이벤트</title>
<script>
window.addEventListener("load", function(){
//브라우저 기본 이벤트 핸들러 취소
	document.getElementById("searchForm").onsubmit = function() {
		return false;
	}	
	document.getElementById("link1").onclick = function() {
		// return false; 이렇게 해도 되고!
		event.preventDefault();
	}
}, false);
</script>
</head>
<body>
 <h3> 브라우저에 정의된 기본 이벤트 취소 </h3>
 브라우저에서 자동으로 처리해주는 기본 이벤트 핸들러를 취소하려면 이벤트 핸들러 함수를  override해서 false를 리턴합니다.<br>
<a id="link1" href="http://www.google.com/">구글</a><br>
<form id="searchForm" action="http://70.12.50.130:9000/js3/data.jsp" method="GET">
찾기 <input type="search">
<input type="submit" value="검색">
</form>
</body>
</html>
```



#location

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
<script>
	window.addEventListener("load", function(){
	setTimeout(function() {
		location.href=("http://www.w3schools.com"); //이동1
		location.assign("http://www.naver.com"); //이동2
		location.replace("http://www.daum.net"); //이동3
		
		location.reload(); //리로드1
		location.href=location.href //리로드2
		}, 3000);
		}, false);

</script>
</head>

<body>
<!--<h3> 이 페이지는 3초 후에 www.w3schools.com으로 이동합니다.</h3>-->
	<h3> 이 페이지는 3초 후에 reload됩니다.</h3>
	<div id="panel">
	</div>
</body>
```



#이미지 움직이기

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title></title>
	<style>
		body{
			font-size:9pt;		
		}
		
		#panel{
			width:600px;
			height:300px;
			border:1px solid #999;
			position:relative;
		}
		
		#bar{
			position:absolute;
			left:50px;
			top:190px;
			width:500px;
			height:20px;
			
			background:#F30;
		}
		
		#img1{
			position:absolute;
			left:50px;
			top:120px;		
		}
		
		#nav{
			text-align:center;
			width:600px;
		}
	</style>
	
	<script>
		var nEndX;
		var nCurrentX;
		var nStartX;
		var nTimerID;
		var nStep;
		var objIMG;
	
		window.onload=function(){
			var objBar = document.getElementById("bar");
			
			// 시작위치 구하기.
			this.nStartX = objBar.offsetLeft;
	
			// 마지막 위치.(시작위치 + bar의 넓이 - 이미지 넓이)
			this.nEndX = objBar.clientWidth;
			//clientWidth : 실제로 보여지고 있는 콘텐츠가 차지하는 넓이 확인
			this.nEndX += this.nStartX;		
			this.nEndX -= 128;
	
			// 이미지의 현재 위치를 시작위치로 설정.
			this.nCurrentX = this.nStartX;
			this.nStep = 2;
			this.nTimerID = 0;
			
			// 계속해서 사용하게 될 이미지 엘리먼트를 변수에 저장.
			this.objIMG = document.getElementById("img1");
		 
			// 시작버튼 이벤트 리스너 등록.
			document.getElementById("btn_start").addEventListener("click",function(){
				start();
			},false);
			
			// 정지버튼 이벤트 리스너 등록.
			document.getElementById("btn_stop").addEventListener("click",function(){
				stopMove();
			},false);
		}
		 
		
		// 타이머 실행.
		function start(){
			if(this.nTimerID==0)
				this.nTimerID = setInterval(this.startMove,20);
		}
		
		// 이미지 움직이기.
		function startMove(){
			// nStep만큼 이동합니다.
			this.nCurrentX += this.nStep;
			//  위치값이 마지막 위치값을 넘어가는 순간, 
			//  시작 위치<--- 마지막 위치로 이동될수 있도록 방향을 바꿔준다.
			if(this.nCurrentX>this.nEndX){
				this.nCurrentX=this.nEndX;
				this.nStep=-2;
			}
			// 위치값이 시작위치값을 넘어가는 순간,
			// 시작위치 ---->마지막 위치로 이동될수 있도록 방향을 바꿔준다.
			if(this.nCurrentX<this.nStartX){
				this.nCurrentX=this.nStartX;
				this.nStep=2;
			}
			
			// 최종적으로 조절된 위치값을 left에 적용시켜 준다.
			this.objIMG.style.left=this.nCurrentX+"px";		
		}
		
		// 타이머 정지시키기.
		function stopMove(){
			if(this.nTimerID!=0){
				clearInterval(this.nTimerID);
				this.nTimerID=0;
			}
		}
	</script>
</head>

	<body><div> 
		<h4>#img1을 #bar의 영역에서 계속 좌우로 움직이도록 만들어주세요.</h4>
		<div id="panel">
			<div id="bar"> </div>
			<div id="img1" style="left: 248px;">
				<img src="./js15-solution_files/fish.png">
			</div>
		</div>
		<div id="nav">
			<button id="btn_start">시작</button>
			<button id="btn_stop">멈춤</button>
		</div>
	</div>       
</body></html>
```

