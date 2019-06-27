# 190627_JSP Servlet

## Review

#Servlet : www웹서비스를 제공하는 웹 서버에서 실행되는 웹 컴포넌트를 구현하는 기술. 웹 요청을 처리, 처리 결과를 동적으로 응답 페이지(html) 생성해서 응답 보내기까지.

#WAS (Web Server + Application Server)  

- http listener, http daemon

- WebContainer(서버에서 실행되는 웹 컴포넌트의 실행환경을 제공, NamingContext 기능, Resource Pooling 기능)

#JSP (Java Server Page) : script





**#웹 컨텍스트 표준 구조**

웹 컨텍스트(http://ip주소:8080/폴더이름)

​	|------html, js, css, image, ... , jsp

​	|----WEB-INF (보안폴더)

​				|---classes (패키지형태로 class파일들 저장)

​				|---lib (jar파일 형태 - 외부 자바 library)	

​				|---web.xml (웹 컨텍스트의 환경설정파일 - 컨텍스트의 파라미터, 리스너, 필터, 전역세션timeout, 										전역에러 페이지, 서블릿, 리소스 참조, welcome-file-list, ...)

​				|---src (Optional)

​				|---tld, tags (Optional)



HttpServletRequest

HttpServletResponse

response.setContentType("text/html"; "charset=utf-8";)

PrintWriter

response.getWriter

@WebServlet("/요청URL") : 서블릿을 선언하기 위한 Annotation



메모리 로딩 => 객체 생성 => init() => service() => destroy()



[Servlet Spec]

1. 패키지 선언

2. public class로 선언

3. HttpServlet 상속받고

4. life cycle메서드 override

   service(), doGet(), doPost(), doPut(), ... 메서드는 요청 처리 및 응답을 위해 반드시 override해야 한다.

   service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException



[JSP Spec]

​	정적 페이지 선언 <%@ page ......%>



-------

- 실습1

```java
package lab.web.controller;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class HeaderInfo
 */
@WebServlet("/header")
public class HeaderInfo extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public HeaderInfo() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.print("<html>");
		out.print("<head><title>Request Header</title></head");
		out.print("<body>");
		out.print("<h3>Request Header정보</h3>");
		out.print("<ul>");
		Enumeration<String> headerName = request.getHeaderNames();
		while(headerName.hasMoreElements()) {
			String name = headerName.nextElement();
			out.print("<li> "+name+": ");
			Enumeration<String> values = request.getHeaders(name);
			while(values.hasMoreElements()) {
				out.print(values.nextElement()+", ");
			}
			out.print("/<li> ");
		}
		out.print("<li> 요청 메소드 : "+request.getMethod()+"</li>");
		out.print("<li> 요청한 client의 IP : "+ request.getRemoteAddr()+"</li>");
		out.print("<li> ContextPath : " +request.getContextPath() +"</li>" );
		out.print("<li> RequestURI : " +request.getRequestURI() +"</li>" );
		out.print("<li> RequestURL : " +request.getRequestURL() +"</li>" );
		out.print("<li> ServletPath : " +request.getServletPath() +"</li>" );
		out.print("</body>");
		out.print("</html>");
	}

}
```



- 실습2

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Insert title here</title>
</head>
<body>
<h3>회원가입 페이지</h3>
<form id="f1" action="join" method="post">
userid : <input type="text" name="userid"> <br>
password : <input type="password" name="userpwd"> <br>
관심사항 : <input type="checkbox" name="interest" value="영화"> 영화 
		 <input type="checkbox" name="interest" value="게임"> 게임 
		 <input type="checkbox" name="interest" value="독서"> 독서 
		 <input type="checkbox" name="interest" value="음악감상"> 음악감상 
		 <input type="checkbox" name="interest" value="춤"> 춤 <br>
<input type="hidden" name="address" value="seoul"> <br>
<input type="submit" value="회원가입"> <br>
</form>
</body>
</html>
```



```java
package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/join")
public class JoinServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
  
    public JoinServlet() {
        super();
    }

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8"); // 한글 깨지는 것 방지하기 위한 인코딩
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.print("<html>");
		out.print("<head><title>Request로 파라미터 처리</title></head");
		out.print("<body>");		
		out.print("<h3>Request로 파라미터 처리</h3>");
		out.print("<ul>");
		out.print("<li> userid : " + request.getParameter("userid")+"</li>");
		out.print("<li> password : " + request.getParameter("userpwd")+"</li>");
		out.print("<li> address : " + request.getParameter("address")+"</li>");
		String interest[] = request.getParameterValues("interest");
		out.print("<li> 관심사항: ");
		for(String inter : interest) {
			out.print(inter+", ");
		}
		out.println("</li>");
		out.println("</ul>");
		out.print("</body>");
		out.print("</html>");
	}
}
```



- 실습3

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>FileUpload 실습</title>
<style>
	input {margin : 2px;}
</style>
</head>
<body>
	<h2>FileUpload 실습</h2>
	<form method="post" action="/edu/upload" enctype="multipart/form-data">
		작성자<input type="text" name="theAuthor"> <br>
		나이<input type="text" name="theAge"> <br>
		파일<input type="file" name="theFile" multiple> <br>
		<input type="submit" value="업로드"> 
	</form>
</body>
</html>
```



```java
package lab.web.controller;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Collection;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

/**
 * Servlet implementation class UploadServlet
 */
@WebServlet("/upload")
@MultipartConfig (location = "c:/uploadtest", maxFileSize=1024*1024*5, maxRequestSize=1024*1024*5*5)
public class UploadServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
  
    public UploadServlet() {
        super();
    }

	public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		request.setCharacterEncoding("utf-8");
		String path = "C:/uploadtest";
		File isDir = new File(path);
		if (!isDir.isDirectory()) {
			isDir.mkdirs();
		}
		Collection<Part> parts = request.getParts();
		for (Part part : parts) {
			if (part.getContentType() != null) {
				String fileName = part.getSubmittedFileName();
				if(fileName != null) {
					part.write(fileName.substring(0,fileName.lastIndexOf(".")) + "_" + System.currentTimeMillis()+
							fileName.substring(fileName.lastIndexOf(".")));
					out.print("<br>업로드한 파일 이름: "+fileName);
					out.print("<br>크기: "+part.getSize());
				}
			} else {
				String partName = part.getName();
				String fieldValue = request.getParameter(partName);
				out.print("<br>" + partName + ": " + fieldValue);
			}
		}
		out.close();
	}
}
```

