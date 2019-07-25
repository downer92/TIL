# 190725_오픈API활용 & 자바 File IO

## 복습

#지도에  plot뿌리는데 마우스 오버하면 빨갛게 변하게하기

- map3.html

```html
<!DOCTYPE html>
<meta charset="utf-8">
<style>
svg circle {
  fill: orange;
  opacity: .5;
  stroke: white;
}
svg circle:hover {
  fill: red;
  stroke: #333;
}
svg text {
  pointer-events: none;
}
svg .municipality {
  fill: #efefef;
  stroke: #fff;
}
svg .municipality-label {
  fill: #bbb;
  font-size: 12px;
  font-weight: 300;
  text-anchor: middle;
}
svg #map text {
  color: #333;
  font-size: 10px;
  text-anchor: middle;
}
svg #places text {
  color: #777;
  font: 10px sans-serif;
  text-anchor: start;
}
</style>
<!-- 라이브러리 로드 -->
 <script src="http://d3js.org/d3.v3.min.js"></script>
 <script src="http://d3js.org/topojson.v1.min.js"></script>
  <script src="./js/map3.js"></script>
<body>
 <h3>서울 맛집</h3>
 <div id="chart"></div>
</body>
</html>
```



- map3.js

```javascript
window.addEventListener("load", function(){
	var width = 800;
	var height = 600;

	var svg = d3.select("#chart").append("svg")
		.attr("width", width)
		.attr("height", height);
	
	//1단계
	//svg안에 지도 레이어 map과 맛집 레이어 places를 만들기
	var map = svg.append("g").attr("id", "map");
	var places = svg.append("g").attr("id", "places");
	
	//2단계
	//메르카토르 투영법을 이용
	//map 레이어에 각 지역구에 대한 path와 지역명을 표시한 text요소를 생성했다.
	var projection = d3.geo.mercator()
		.center([126.9895, 37.5651])
		.scale(100000)
		.translate([width/2, height/2]); //어디에 표시할 것인지
	
	var path = d3.geo.path().projection(projection);
	
	d3.json("./datas/seoul_municipalities_topo_simple.json", function(error, data) { //에러가 발생하면 에러가 첫번째, 에러가 없으면 데이터를 읽어온다는 말
		var features = topojson.feature(data, data.objects.seoul_municipalities_geo).features;
		
		map.selectAll("path")
		   .data(features)
		   .enter().append("path")
		   .attr("class", function(d) {return "municipality c" + d.properties.code})
		   .attr("d", path); //d속성에 path를 넘겨주기
		
		
		//지도 레이어 안에 텍스트 추가
		map.selectAll("text")
		   .data(features)
		   .enter().append("text")
		   .attr("transform", function(d) { return "translate(" + path.centroid(d) + ")"; })
		   .attr("dy", ".35em")
		   .attr("class", "municipality-label")
		   .text(function(d) { return d.properties.name })   
	});
	
	
//	//3단계
//	//맛집 위,경도를 데이터 places.csv를 이용해 맛집을 지도에 출력
//	//places레이어에 circle과 text를 생성
	
	d3.csv("./datas/places.csv", function(data) {
		places.selectAll("circle")
			  .data(data)
			  .enter().append("circle")
			  .attr("cx", function(d) { return projection([d.lon, d.lat])[0];})
			  .attr("cy", function(d) { return projection([d.lon, d.lat])[1];})
			  .attr("r", 10);
		
		places.selectAll("text")
			  .data(data)
			  .enter().append("text")
			  .attr("cx", function(d) { return projection([d.lon, d.lat])[0];})
			  .attr("cy", function(d) { return projection([d.lon, d.lat])[1] + 8;})
			  .text(function(d) { return d.name });
	});
	
}); //addEventListener() end
```



-----------------

## Open API 활용

#네이버 오픈 API : 얼굴인식

- APIExamFace.java

```java
package imageTest;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;

// 네이버 얼굴인식 API 예제
public class APIExamFace {

    public static void main(String[] args) {

        StringBuffer reqStr = new StringBuffer();
        String clientId = "ToWO7VaQ8vrvyMks6RQf";//애플리케이션 클라이언트 아이디값";
        String clientSecret = "mLnzcoejvF";//애플리케이션 클라이언트 시크릿값";

        try {
            String paramName = "image"; // 파라미터명은 image로 지정
            String imgFile = "C:/Users/student/Desktop/hajin1.jpg";
            File uploadFile = new File(imgFile);
            String apiURL = "https://openapi.naver.com/v1/vision/celebrity"; // 유명인 얼굴 인식
     //       String apiURL = "https://openapi.naver.com/v1/vision/face"; // 얼굴 감지
            URL url = new URL(apiURL);
            HttpURLConnection con = (HttpURLConnection)url.openConnection();
            con.setUseCaches(false);
            con.setDoOutput(true);
            con.setDoInput(true);
            // multipart request
            String boundary = "---" + System.currentTimeMillis() + "---";
            con.setRequestProperty("Content-Type", "multipart/form-data; boundary=" + boundary);
            con.setRequestProperty("X-Naver-Client-Id", clientId);
            con.setRequestProperty("X-Naver-Client-Secret", clientSecret);
            OutputStream outputStream = con.getOutputStream();
            PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, "UTF-8"), true);
            String LINE_FEED = "\r\n";
            // file 추가
            String fileName = uploadFile.getName();
            writer.append("--" + boundary).append(LINE_FEED);
            writer.append("Content-Disposition: form-data; name=\"" + paramName + "\"; filename=\"" + fileName + "\"").append(LINE_FEED);
            writer.append("Content-Type: "  + URLConnection.guessContentTypeFromName(fileName)).append(LINE_FEED);
            writer.append(LINE_FEED);
            writer.flush();
            FileInputStream inputStream = new FileInputStream(uploadFile);
            byte[] buffer = new byte[4096];
            int bytesRead = -1;
            while ((bytesRead = inputStream.read(buffer)) != -1) {
                outputStream.write(buffer, 0, bytesRead);
            }
            outputStream.flush();
            inputStream.close();
            writer.append(LINE_FEED).flush();
            writer.append("--" + boundary + "--").append(LINE_FEED);
            writer.close();
            BufferedReader br = null;
            int responseCode = con.getResponseCode();
            if(responseCode==200) { // 정상 호출
                br = new BufferedReader(new InputStreamReader(con.getInputStream()));
            } else {  // 에러 발생
                System.out.println("error!!!!!!! responseCode= " + responseCode);
                br = new BufferedReader(new InputStreamReader(con.getInputStream()));
            }
            String inputLine;
            if(br != null) {
                StringBuffer response = new StringBuffer();
                while ((inputLine = br.readLine()) != null) {
                    response.append(inputLine);
                }
                br.close();
                System.out.println(response.toString());
            } else {
                System.out.println("error !!!");
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```



#네이버 오픈 API : 번역기

- APIExamTranslate.java

```java
package imageTest;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
public class APIExamTranslate {

    public static void main(String[] args) {
        String clientId = "BPZjhIxF3WJ6TrlkVnTr";//애플리케이션 클라이언트 아이디값";
        String clientSecret = "J59ffolhfx";//애플리케이션 클라이언트 시크릿값";
        try {
            String text = URLEncoder.encode("분식", "UTF-8");
            String apiURL = "https://openapi.naver.com/v1/papago/n2mt";
            URL url = new URL(apiURL);
            HttpURLConnection con = (HttpURLConnection)url.openConnection();
            con.setRequestMethod("POST");
            con.setRequestProperty("X-Naver-Client-Id", clientId);
            con.setRequestProperty("X-Naver-Client-Secret", clientSecret);
            // post request
            String postParams = "source=ko&target=en&text=" + text;
            con.setDoOutput(true);
            DataOutputStream wr = new DataOutputStream(con.getOutputStream());
            wr.writeBytes(postParams);
            wr.flush();
            wr.close();
            int responseCode = con.getResponseCode();
            BufferedReader br;
            if(responseCode==200) { // 정상 호출
                br = new BufferedReader(new InputStreamReader(con.getInputStream()));
            } else {  // 에러 발생
                br = new BufferedReader(new InputStreamReader(con.getErrorStream()));
            }
            String inputLine;
            StringBuffer response = new StringBuffer();
            while ((inputLine = br.readLine()) != null) {
                response.append(inputLine);
            }
            br.close();
            System.out.println(response.toString());
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```



------------------------

## Java File IO

#내 하드디스크의 용량 확인하기

- FileTest1.java

```java
import java.io.File;
public class FileTest1 {
public static void main(String arg[]){        
       String drive;
       double totalSpace, usedSpace, freeSpace, usableSpace;        
       File[] roots = File.listRoots();    // 하드디스크의 루트 드라이버들을 배열로 반환한다
       for(File root : roots){            
	drive = root.getAbsolutePath();     // 루트 드라이버의 절대 경로       
	totalSpace = root.getTotalSpace() / Math.pow(1024, 3);   // 하드디스크 전체 용량
	usableSpace = root.getUsableSpace() / Math.pow(1024,3);   // 사용가능한 디스크 용량
            freeSpace = root.getFreeSpace() / Math.pow(1024,3);  // 여유 디스크 용량            
            usedSpace = totalSpace - usableSpace;         // 사용한 디스크 용량
            System.out.println("하드 디스크 드라이버 : " + drive);
            System.out.println("총 디스크 용량 : " + totalSpace + "GB");
            System.out.println("사용 가능한 디스크 용량 : " + usableSpace + "GB");
            System.out.println("여유 디스크 용량 : " + freeSpace + "GB");
            System.out.println("사용한 디스크 용량 : " + usedSpace+"GB");
            System.out.println();            
        }
    } 
}
```



#해당 경로의 해당 파일 찾기

- FilenameFilterTest.java

```java
import java.io.File;
import java.io.FilenameFilter;
public class FilenameFilterTest {
  public static void main(String[] args) {      
	    File f = null;
	    File[] paths;      
	    try {        
	       // create new file
	       f = new File("c:/test");
	         
	       // create new filename filter
	       FilenameFilter fileNameFilter = new FilenameFilter() {   
	          @Override
	          public boolean accept(File dir, String name) {
	             if(name.lastIndexOf('.')>0) {
	               
	                // get last index for '.' char
	                int lastIndex = name.lastIndexOf('.');
	                
	                // get extension
	                String str = name.substring(lastIndex);
	                // match path name extension
	                if(str.equals(".pptx")) {
	                   return true;
	                }
	             }               
	             return false;
	           }
	       };
	         
	        // returns pathnames for files and directory
	       paths = f.listFiles(fileNameFilter);         
	       // for each pathname in pathname array
	       for(File path:paths) {         
           // prints file and directory paths
	          System.out.println(path);
	       }         
	    } catch(Exception e) {         
	       // if any error occurs
	       e.printStackTrace();
	    }
	 }
}
```



---------------

## 람다식

#Lambda Expressions : 익명함수를 생성하기 위한 식

- 자바 코드가 매우 간결해지고, 컬렉션의 요소를 필터링하거나 매핑해서 원하는 결과를 쉽게 집계할 수 있다.

- LambdaExamTest.java

```java
package Test;

public class LambdaExamTest {

	public static void main(String[] args) {
        new Thread( ()->{
            for(int i = 0; i < 10; i++){
                System.out.println("hello");
            }
        } ).start();
    }   
}
```



#Lambda Expression 활용

- 파라미터에 행위 전달 (Parameterized Behaviors)
  - 런타임에 행위를 전달 받아서 제어 흐름 수행 (cf. 전략 패턴)
  - 메소드 단위의 추상화가 가능
  - 함수형 언어의 고차 함수 (Higher-Order Function)

- 불변 변수 사용 (Immutable Free Variables)
  - 자바에서 익명 클래스 + 자유 변수 포획으로 클로저를 가능하게 하였다
  - 포획된 변수에는 명시적으로 final 지시자를 사용하도록 강제하였다. 
  - 람다식에서는 포획된 변수에 final 을 명시하지 않아도 되도록 변경되었지만 기존과 동일하게 포획된 변수는 변경할 수 없고, 변경하는 경우 컴파일 에러가 발생한다.

- 상태 없는 객체 (Stateless Object) : 바로바로 생성해서 쓰고 가비지컬렉션되니까
  - 클래스의 메소드(행위)에서 멤버 변수(상태)를 자유롭게 제어할 수 있다. 
  - 즉, 객체가 메소드를 호출하면 입력(Input)+상태(Properties)로부터 출력(Output)이 결정되기 때문에 Side-Effect가 발생할 수 있다. 
  - 함수 단위의 배타적 수행이 보장되지 않기 때문에 병렬 처리와 멀티 스레드 환경에서 여러 단점에 노출될 가능성이 있다.
  - 람다식으로 표현하게 되면, 오로지 입력(Input)과 출력(Output)에 종속되어 있기 때문에 Side-Effect 가 발생하지 않는 것을 최대한 보장할 수 있게 된다.  





#매개변수와 리턴값이 없는 람다식

- MyFunctionalInterface.java 인터페이스 생성

```java
@FunctionalInterface
public interface MyFunctionalInterface {
	public void method();
}
```



- MyFunctionalInterfaceExam.java 클래스 생성

```java
public class MyFunctionalInterfaceExam {

	public static void main(String[] args) {
		MyFunctionalInterface fi; 
        fi = () -> {    //인터페이스를 타켓 타입으로 갖는 람다식
            String str = "method call1";
            System.out.println(str);
        }; 
        fi.method();                 //람다식 호출
        fi = () -> {   
            System.out.println("method call2");
        };
        fi.method(); 
        fi = () -> System.out.println("method call3");
        fi.method(); //주로 2,3번으로 사용
	}
}
```





#매개변수가 있는 람다식

- MyFunctionalInterface2.java 인터페이스

```java
@FunctionalInterface
public interface MyFunctionalInterface2 {
	public void method(int x);
}
```



- MyFunctionalInterfaceExam.java 클래스

```java
public class MyFunctionalInterfaceExam2 {
    public static void main(String[] args) {
        MyFunctionalInterface2 fi;
        fi = (x) -> {
            int result = x * 5;
            System.out.println(result);
        };
        fi.method(2);
 
        fi = x -> System.out.println(x * 5);
        fi.method(2);
    }
}
```



#리턴값이 있는 람다식

- MyFunctionalInterface3.java 인터페이스

```java
@FunctionalInterface
public interface MyFunctionalInterface3 {
	public int method(int x, int y);
}
```



- MyFunctionalInterfaceExam3.java 클래스

```java
package Test;
public class MyFunctionalInterfaceExam3 {
	public static void main(String[] args) {
        MyFunctionalInterface3 fi;
        fi = (x, y) -> {
            int result = x + y; 
            return result;
        };
        System.out.println(fi.method(2, 5));
 
        fi = (x, y) -> {
            return x + y;
        };
        System.out.println(fi.method(2, 5));
        
        fi = (x, y) -> x + y;
        System.out.println(fi.method(2, 5));
 
        fi = (x, y) -> sum(x, y);
        System.out.println(fi.method(2, 5));
    }
 
    public static int sum(int x, int y) {
        return x + y;
    }
}
```





#클래스 멤버와 로컬변수 사용1

- UsingThis.java

```java
public class UsingThis {
    public int outterField = 10; 
    class Inner {
        int innerField = 20; 
        void method() {
            MyFunctionalInterface fi = () -> {
                System.out.println("Outter Field: " + outterField);
                System.out.println("Outter Field: " + UsingThis.this.outterField + "\n");
 
                System.out.println("Inner Field: " + innerField);
                System.out.println("Inner Field: " + this.innerField + "\n");
            };            
            fi.method();
        }
    }
}
```



- UsingThisExam.java

```java
public class UsingThisExam {
	public static void main(String[] args) {
        UsingThis usingThis = new UsingThis();
        UsingThis.Inner inner = usingThis.new Inner();
        inner.method();
	}
}
```





#클래스 멤버와 로컬변수 사용2

- 람다식에서 메소드의 매개 변수 또는 로컬 변수를 사용하면 이 두 변수는 final 특성을 가져야 합니다.

- 매개 변수 또는 로컬 변수를 람다식에서 읽는 것은 허용되지만, 람다식 내부 또는 외부에서 변경할 수 없습니다.



- UsingLocalVariable.java

```java
public class UsingLocalVariable {
    void method(int  arg) {
        int localVar = 40;
 
        // arg = 31; // final 특성 때문에 수정 불가
        // localVar = 41; // final 특성 때문에 수정 불가
 
        MyFunctionalInterface fi = () -> {
            System.out.println("arg: " + arg);
            System.out.println("localVar: " + localVar);
        };
 
        fi.method();
    }
}
```



- UsingLocalVariableExam.java

```java
public class UsingLocalVariableExam { 
    public static void main(String[] args) {
        UsingLocalVariable ulv = new UsingLocalVariable();
        ulv.method(20);
    } 
}
```





#Stream

- 자바 8부터 추가된 컬렉션(배열 포함)의 저장 요소를 하나씩 참조해서 람다식(functional-style)으로 처리할 수 있도록 해주는 반복자

- 컬렉션(java.util.Collection)의 stream() 메소드로 스트림 객체를 얻고 나서 stream.forEach (name -> System.out.println(name) ); 메소드를 통해 컬렉션의 요소를 하나씩 콘솔에 출력한다.

```java
public static void main(String[] args) {
    List<String> list = Arrays.asList("John", "Simons", "Andy");
    Stream<String> stream = list.stream(); 
    stream.forEach( name -> System.out.println(name) );
} 
```





#**메소드 참조**  

- 메소드를 참조해서 매개 변수의 정보 및 리턴 타입을 알아내어, 람다식에서 불필요한 매개 변수를 제거하는 것이 목적이다.

- 메소드 참조도 람다식과 마찬가지로 인터페이스의 익명 구현 객체로 생성되므로 타겟 타입인 인터페이스 추상 메소드가 어떤 매개 변수를 가지고, 리턴 타입이 무엇인가에 따라 달라진다.

- 메소드 참조는 정적 또는 인스턴스 메소드를 참조할 수 있고, 생성자 참조도 가능하다.