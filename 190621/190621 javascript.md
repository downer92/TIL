# 190621 javascript



## Review

#location : 브라우저 객체중 문서의 URL을 관리하기 위해 사용

- location.href, assign(url), replace(url), reload



#navigator : 요청을 보낸 클라이언트의 브라우저 정보를 얻을 수 있는 객체.  html문서에 포함된 자바스크립		트는 클라이언트에 보내져서 클라이언트의 브라우저에서 자바스크립트가 실행되는 브라우저 정보 등을 처리

- geolocation, appName, onLine, platform



#screen : 화면의 크기와 색상정보를 관리하는 객체

- width, height, orientation, colorDepth, pixelDepth



#history : 웹페이지의 이력을 관리하는 객체

- length, back(), forward(), go(n|-n)





#이벤트 처리

- 이벤트소스객체.on이벤트 = function(){} //이벤트 핸들러 함수

- 이벤트소스객체.addEventListener("이벤트", 이벤트 핸들러 함수, 캡쳐링 여부);



#등록된 이벤트 제거

- 이벤트소스객체.on이벤트 = null;
- 이벤트소스객체.removeEventListener("이벤트", 이벤트 핸들러 함수)



#브라우저에서 처리해주는 기본 이벤트 취소

예) <a href=""></a>의 클릭이벤트

예) form태그의 submit 이벤트

1. 이벤트소스객체.on이벤트 = function() { //이벤트 핸들러 함수 override함수,

​																		....... return false; } 

2. event.preventDefault()



#이벤트 전파 방식

- 버블링 (대부분의 브라우저에서 기본으로 지원) : 자식객체 => 부모객체로 이벤트 전파
- 캡처링 :  부모객체=> 자식객체로 이벤트 전파
- 이벤트 버블링을 중단시키려면 : event.stopPropagation();



#뷰포트(윈도우 좌표계) : 웹 브라우저에서 문서의 내용을 표시하는 영역



#문서의 요소 객체는 박스모델이 적용되며, 왼쪽 X좌표는 left , 왼쪽 상단의 Y좌표는 top, 오른쪽 아래의 X좌		표는 right, 오른쪽 아래의 Y좌표는 bottom, 너비는 width, 높이는 height 속성으로 참조한다.



뷰포트의 너비 속성은 clientWidth, innerWidth (스크롤 막대 포함)

뷰포트의 높이 속성은 clientHeight, innerHeight (스크롤 막대 포함)



```html
문서의 요소 객체.innterHTML = "<strong>강조체</strong>";
문서의 요새 객체.textContent = "<strong>강조체</strong>"; 
------------------------------------------------------------------------
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
<script>
window.onload = function() {
	document.getElementById("d1").innerHTML = "<strong>강조체</strong>  <i>이탤릭</i>";

	document.getElementById("d2").textContent = "<strong>강조체</strong>  <i>이탤릭</i>";
	document.getElementById("d3").innerText = "<strong>강조체</strong>  <i>이탤릭</i>";

	console.log(document.getElementById("d4").innerHTML); //안에 들어있는 모든 내용
	console.log(document.getElementById("d4").textContent); //안에서 공백포함 텍스트만
	console.log(document.getElementById("d4").innerText); //안에서 공백제외 텍스트만
}
</script>
</head>
<body>
<div id="d1"></div>
<div id="d2"></div>
<div id="d3"></div>
<div id="d4">
	<div id="d5">
		내용
	</div>
</div>
</body>
</html>
```



-------------------------------------------



#File API : 웹 어플리케이션이 로컬 파일의 내용에 접근할 수 있도록 하는 API 

- File 인터페이스 : 파일 이름이나 크기 등의 기본적인 메타 데이터에 접근

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<script>
window.addEventListener("load", function(){
	var fileElement = document.getElementById("f1");
	fileElement.addEventListener("change", function() {
		var files = fileElement.files;
		var output = "";
		for(var i=0; i<files.length; i++) {
			var file=files[i];
			output += "파일 이름 : "+file.name+", 크기 : "+file.size+ ", 타입 : "+file.type+", URN : "+file.urn+"\n";
		}
		document.getElementById("result").innerHTML = output;
	}, false);
}, false);


</script>
<body>
	<input id="f1" type="file" multiple accept="image/*">
	<div id="result"></div>
</body>
</html>
```



#Drag and Drop

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script>
	var dropbox;
	window.addEventListener("load", function() {
		dropbox = document.getElementById("dropbox");
		//이벤트 핸들러 할당
		dropbox.addEventListener("drop", drop, false);
		dropbox.addEventListener("dragenter", dragEnter, false);
		dropbox.addEventListener("dragover", dragOver, false);
	}, false);

	function dragEnter(event) {
		event.stopPropagation();
		event.preventDefault();
	}

	function dragOver(event) {
		event.stopPropagation();
		event.preventDefault();
	}


	function drop(event) {
		event.stopPropagation();
		event.preventDefault();	

		var files = event.dataTransfer.files;
		var count = files.length;

		//오직 한 개 이상의 파일이 드랍된 경우에만 처리기를 호출한다.
		if (count>0) {
			var file = files[0];
			document.getElementById("droplabel").innerHTML
			= "Processing "+file.name;
			var reader = new FileReader();
			//파일 리더의 이벤트 핸들러 정의
			reader.onloadend = function(event) {
				var img = document.getElementById("preview");
				img.src = event.target.result; //event.target는 FileReader객체
			};
			reader.readAsDataURL(file);
		}
	}

</script>	
</head>
<body>
<h1>Drag and Drop Demo</h1>
	<div id="dropbox" style="width: 360px; height: 80px; border: 1px solid #aaa;">
		<span id="droplabel"> 이곳에 파일을 드랍해 주세요... </span>
	</div>
	<img id="preview" alt="[ preview will display here ]">

</body></html>
```



#FileReader API

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<title>Insert title here</title>
<script>
//1. new FileReader()
//2. onload, onloadend이벤트에 대한 핸들러 : result속성에 저장낸 내용을 textarea에..
//3. readAsText()사용  내용 읽기
  

  function readFile(){
  var file = document.getElementById("file").files[0];
  document.getElementById("fileName").innerHTML = file.name;
  document.getElementById("fileSize").innerHTML = file.size+"Bytes";

  var reader = new FileReader();
  reader.onloadened = function() {
    document.getElementById("content").innerHTML = reader.result;
  }
  var encoding List = document.getElementById("encoding");
  var encoding = 
  encodingList.options[encodingList.selectedIndex].value;
  reader.readAsText(file, encoding);
}
</script>
</head>
<body>
 <h1> FileReader Interface : readAsText()</h1>
       <input id="file" type="file">
       <select id="encoding">
           <option>UTF-8</option>
		   <option>euc-kr</option>
        </select>
        <button onclick="readFile()">읽기</button><br>
        <div>
            <span id="fileName">File Name</span>
            <span id="fileSize">File Size</span>
        </div>
        <textarea id="content" readonly="" style="width:600px; height:400px;"></textarea>

</body></html>
```



#Canvas

- toDataURL() : Canvas에 그린 이미지를 저장할 때 사용

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script>
window.addEventListener("load", function() {
	var img = document.getElementById("scream");
	var canvas1 = document.getElementById("drawCanvas");
	var ctx = canvas1.getContext("2d");
	ctx.drawImage(img, 10, 10);
}, false);

function fromImageData() {
	var canvas1 = document.getElementById("drawCanvas");
	var imgData = canvas1.toDataURL();
	var canvas2 = document.getElementById("copyCanvas");
	var ctx = canvas2.getContext("2d");
	var img = new Image();
	img.src = imgData;
	ctx.drawImage(img, 50, 50);
}
</script>
</head>
<body>
<h3>canvas API : Image Copy</h3>
<img id="scream" src="../jspractice4/red_dragon.jpeg" width="220" height="277" style="display:none;">
<canvas id="drawCanvas" width="200" height="200" style="position: relative; border: 1px solid #000;"></canvas>
<button onclick="fromImageData();">캔버스 복사=&gt;</button>                  
<canvas id="copyCanvas" width="300" height="300" style="position: relative; border: 1px solid #000;"></canvas>

</body></html>
```





#스타일 가이드 : 프로그램을 작성할 때 버그를 피하고 가독성을 높이기 위해 권장되는 코딩 규칙을 정리한 것



#예외처리 practice

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
<script>
function permutation(a) {
	if( !(a instanceof Array) ) {
	throw new Error(a+" is not an array");
	}
	return a;
} 
// permutation("ABC");
// x++;
//	if(a>0) {a++;}
	var a = ["a","b","c"];
	try {
		var p = permutation(a); // 정상적으로 수행
//		var p = permutation("ABC"); // 위에 주석치고 이 문장 실행하면 의도적으로 예외를 발생시킬 수 있다.
		p.forEach(function(v) {console.log(v)}); 
	} catch(e) {
		alert(e);
	}
</script>
</body>
</html>
```



#이터레이터 practice

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
<script>
function makeIterator(array) {
	var index = 0;
	return {
		next: function() {
			if(index<array.length) {
				return {value: array[index++], done: false};
			} else {
				return {value: undefined, done: true};
			}
		}
	};
}
var iter = makeIterator(["A", "B", "C"]);
console.log(iter.next()); // => Object {value: "A", done: false}
console.log(iter.next()); // => Object {value: "B", done: false}
console.log(iter.next()); // => Object {value: "C", done: false}
console.log(iter.next()); // => Object {value: undefined, done: true}
</script>
</body>
</html>
```



#제너레이터 

- 반복 가능한 이터레이터를 값으로 반환
- 작업에 대한 일시 정지와 재시작이 가능하며 자신의 상태를 관리한다.

- function*로 묶는다.



---------------



## jQuery

#jQuery 개요

- 모든 브라우저에서 동작하는 클라이언트 자바스크립트 라이브러리
- 무료로 사용가능한 오픈소스 라이브러리!



#기본 태그 연습

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title> jQuery 기본 </title>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<script>
/*		jQuery(document).ready(function(){alert("ready event handler1")})
		$(document).ready(function(){alert("ready event handler2")}) //이 방식을 더 많이 씀!
		$(function(){alert("즉시 실행될 함수");});				*/

	$(document).ready(function() {
//1.	$("h3").css("color", "blue").css("backgroundColor", "orange"); });
//2.	$("*").css("color", "blue").css("backgroundColor", "orange"); }); //전체에 적용할 때에는 * 사용
//3.	$("div, p").css("color", "blue").css("backgroundColor", "orange"); }); //여러 태그에 적용하려면 콤마(,)로 연결
//4.	$("#simple").css("color", "blue").css("backgroundColor", "orange"); }); //ID는 #붙여서
//5.	$(".todo").css("color", "blue").css("backgroundColor", "orange"); }); //class는 .붙여서
		$("body>p").css("backgroundColor", "orange");
		$("input[type='text']").val("Hello, jQuery~"); }); //body태그 안의 p태그만
		$("input:password").css("backgroundColor", "cyan");
		$("input:focus").css("backgroundColor", "lightgray");
	</script>
</head>
<body>
<h3> JQuery </h3>
<h3 id="simple"> JQuery는 JavaScript보다 코드가 간결해서 코드량을 평균 1/3으로 줄여준다. </h3>
<h3> JQuery 효과를 조합하면 멋진 효과를 만들 수 있다.</h3>
<div class="todo"> <p>1. 푹 쉬기</p></div>
<p>2. 많이 먹기</p>
<article class="todo"> 3.많이 공부하기 </article>
<ul>
	<li> 4.사회관계망 튼튼하게 하기</li>
	<li> 5.긍정적 마인드 컨트롤하기..</li>
</ul>
text: <input type="text"><br>
password: <input type="password"><br>
email: <input type="email"><br>
search: <input type="search" autofocus="autofocus"><br>
tel: <input type="tel"><br>
url: <input type="url"><br>

</body>
</html>
```



#실습2

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title> jQuery 기본 </title>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<script>
		$(document).ready(function() {
			setTimeout(function() {
				var to = $('select > option:selected').val();
				alert(to);
			}, 5000);
		});
	</script>
<body>
	<select>
		<option>Apple</option>
		<option>Bag</option>
		<option>Cat</option>
		<option>Dog</option>
		<option>Elephant</option>
	</select>
</body>
</html>
```



#실습3

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title> jQuery 기본 </title>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
	$(document).ready(function() {
		$('tr:odd').css('background', '#F9F9F9');
		$('tr:even').css('background', '#9F9F9F');
		$('tr:first').css('background', '#000000').css('color', '#FFFFFF');
	});
</script>

<body>
     <table>
        <tbody><tr><th>이름</th><th>혈액형</th><th>지역</th></tr>
        <tr><td>강민수</td><td>AB형</td><td>서울특별시 송파구</td></tr>
        <tr><td>구지연</td><td>B형</td><td>미국 캘리포니아</td></tr>
        <tr><td>김미화</td><td>AB형</td><td>미국 메사추세츠</td></tr>
        <tr><td>김선화</td><td>O형</td><td>서울 강서구</td></tr>
        <tr><td>남기주</td><td>A형</td><td>서울 노량진구</td></tr>
        <tr><td>윤하린</td><td>B형</td><td>서울 용산구</td></tr>
    </tbody></table>
</body>
</html>
```



​	#실습4

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title> jQuery 기본 </title>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
    $(document).ready(function() {
    $('tr:eq(0)').css('background','#000000').css('color','white');
    $('td:nth-child(3n+1)').css('background','#565656');
    $('td:nth-child(3n+2)').css('background','#A9A9A9');
    $('td:nth-child(3n)').css('background','#F9F9F9');
    });
</script>
<body>
    <table>
        <tbody><tr><th>이름</th><th>혈액형</th><th>지역</th><th>이름</th><th>혈액형</th><th>지역</th></tr>
        <tr><td>강민수</td><td>AB형</td><td>서울특별시 송파구</td><td>강민수</td><td>AB형</td><td>서울특별시 송파구</td></tr>
        <tr><td>구지연</td><td>B형</td><td>미국 캘리포니아</td>
        <td>구지연</td><td>B형</td><td>미국 캘리포니아</td></tr>
        <tr><td>김미화</td><td>AB형</td><td>미국 메사추세츠</td>
        <td>김미화</td><td>AB형</td><td>미국 메사추세츠</td></tr>
        <tr><td>김선화</td><td>O형</td><td>서울 강서구</td>
        <td>김선화</td><td>O형</td><td>서울 강서구</td></tr>
        <tr><td>남기주</td><td>A형</td><td>서울 노량진구</td><td>남기주</td><td>A형</td><td>서울 노량진구</td></tr>
        <tr><td>윤하린</td><td>B형</td><td>서울 용산구</td>
        <td>윤하린</td><td>B형</td><td>서울 용산구</td></tr>
    </tbody></table>
</body>
</html>
```

