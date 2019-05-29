# 190528 Chapter 11



## I. Collections Framework 

: 데이터 군을 저장하는 클래스들을 표준화한 설계

- 배열: 생성시에 배열의 크기를 반드시 설정해야 하고 저장될 요소의 크기가 정적이다. (동적 변경 불가)
- Collection: 생성시에 저장될 요소의 크기를 설정하지 않아도 되고, 동적으로 요소가 저장될 크기는 변경된다.
  - List, Set

-----------------------------------------------------------------------------------------------------------------------------------------------------------

- **List Interface**: 순서가 있는 데이터의 집합. 데이터의 중복을 허용한다.

  => 저장한 순서 보장, 중복된 객체 저장

  => add(객체): 배열의 뒤에 추가할 때 / add(index, 객체): 배열의 중간에 추가할 때 / clear(), remove(객체), remove(index), removeAll()
  
  ​	size(), contains(), get(index), iterator()

  ``` - java
  Iterator<Book> - iterator()
  		while(iterator.hasNext()) {
  		Book b = iterator.next();
  		}
  
  // Enumeration - hasMoreElement(), nextElement()와 유사
  ```
  
  
  
  - **Vector**: 멀티스레드에서 여러사용자들에 의해 이용될 때 사용
    - **Stack**: 마지막에 저장한 데이터를 가장 먼저 꺼내게 되는 LIFO 구조 / push(객체), pop(), peek()
      =>웹브라우져도 지난 페이지가 계속 쌓이는 스택구조.
    - **Queue**: 처음에 저장한 데이터를 가장 먼저 꺼내게 되는 FIFO 구조 
  - 예제
  
  ```java
  package lab.java.core;
  import java.util.Vector;
  public class VectorTest {
  	public static void main(String[] args) {
  		Vector<String> vec = new Vector(); 
          // <>=generic class! 들어갈 때부터 타입 체크를 해주는 것
  		System.out.println("capacity: "+vec.capacity()); 
  		//capacity: 객체에 저장할 수 있는 용량, 능력
  		System.out.println("size: "+vec.size()); 
  		//size: 실제 저장된 개수
  		for(int i=1; i<12; i++)
  			vec.add("K"+i);
  		System.out.println("capacity: "+vec.capacity());
  		System.out.println("size: "+vec.size());
  		for(int i=12; i<23; i++)
  			vec.add("K"+i);
  		System.out.println("capacity: "+vec.capacity());
		System.out.println("size: "+vec.size());
  		for(int i=23; i<42; i++)
			vec.add("K"+i);
  		System.out.println("capacity: "+vec.capacity());
		System.out.println("size: "+vec.size());
  	}
  }
  /* <출력>
  capacity: 10
size: 0
  capacity: 20
  size: 11
  capacity: 40
  size: 22
  capacity: 80
  size: 41
  */
  ```
  
  
  
  - **ArrayList**: Vector를 개선한 것으로 싱글스레드에서 한명의 사용자에 의해 이용될 때 사용. 
  
    - Object배열을 이용해서 데이터를 순차적으로 저장한다.
    - 배열에 더이상 저장할 공간이 없으면 보다 큰 새로운 배열을 생성해 기존의 배열에 저장된 내용을 새로운 배열로 복사해서 저장된다.
    - 선언된 배열의 타입에 따라 저장할 수 있는 객체의 종류가 한정된다!
    - 예제
  
    ```java
    package lab.java.core;
    
    import java.util.ArrayList;
    import java.util.Collections;
    
    public class ArrayListEx1 {
    	public static void main(String[] args) {
    		ArrayList list1 = new ArrayList(10);
    		list1.add(new Integer(5));
    		list1.add(new Integer(4));
    		list1.add(new Integer(2));
    		list1.add(new Integer(0));
    		list1.add(new Integer(1));
    		list1.add(new Integer(3));
    
    		ArrayList list2 = new ArrayList(list1.subList(1, 4)); 
    		//list1의 1부터 4사이(즉 1,2,3)에 저장된 객체를 리턴한다.
    		print(list1, list2);
    		
    		Collections.sort(list1); // list1과 list2를 정렬한다.
    		Collections.sort(list2);
    		print(list1, list2);
    		
    		System.out.println("list1.containsAll(list2):" +list1.containsAll(list2));
    		
    		list2.add("B");
    		list2.add("C");
    		list2.add(3, "A");
    		print(list1, list2);
    		
    	// list1에서 list2와 겹치는 부분만 남기고 나머지는 삭제하기: retainAll()메서드 사용!
    		System.out.println("list1.retainAll(list2): "+list1.retainAll(list2));
    		print(list1, list2);
    		
    		// list2에서 list1와 공통된 객체들을 삭제하기
    		for(int i=list2.size()-1; i>=0; i--) { 
    			if(list1.contains(list2.get(i)))
    				list2.remove(i);
    		}//for end
      // 변수 i를 감소시켜가면서 삭제를 해야 자리이동이 발생해도 영향을 받지 않고 작업이 가능!
    		print(list1, list2);
    	}//main end
    
    	private static void print(ArrayList list1, ArrayList list2) {
    		System.out.println("list1: "+list1);
    		System.out.println("list2: "+list2);
    		System.out.println();	
    	} //print end
    }//class end
    
    /* <출력
    list1: [5, 4, 2, 0, 1, 3]
  list2: [4, 2, 0]  (list1의 1,2,3번)
    
  list1: [0, 1, 2, 3, 4, 5]
    list2: [0, 2, 4]  (Collections.sort로 정렬)
    
    list1.containsAll(list2):true
    list1: [0, 1, 2, 3, 4, 5]
    list2: [0, 2, 4, A, B, C]   
    
    list1.retainAll(list2): true
    list1: [0, 2, 4]
    list2: [0, 2, 4, A, B, C]  (list1에서 list2와 겹치는 부분 제외 제거)
    
    list1: [0, 2, 4]
    list2: [A, B, C]  (list2에서 list1과 공통된 객체 제거)
    
    */
    ```
  
    
  
  - **LinkedList**: 배열은 크기를 변경할 수 없고 비순차적인 데이터의 추가 또는 삭제에 시간이 많이 걸린다는 단점을 가지는데 이러한 배열의 단점을 보완해 고안된 클래스. but 순차적인 접근에 대해서는 ArrayList보다 느리다!



- **Set Interface**: 순서를 유지하지 않는 데이터의 집합. 데이터의 중복을 허용하지 않는다. Set 인터페이스를 구현한 클래스로는 HashSet, TreeSet 등이 있다. 정렬을 보장해준다는 장점

  - 예제1

  ```java
  package lab.java.core;
  
  import java.util.ArrayList;
  import java.util.HashSet;
  import java.util.Iterator;
  import java.util.List;
  import java.util.Set;
  import java.util.TreeSet;
  import java.util.Vector;
  
  public class SetTest {
  
  	public static void main(String[] args) {
  		String cars[] = {"k3", "sm6","k5", "k7", "k9", "sm3", "k3","sm5","sm6","sm7"};
  		Set<String> hSet = new HashSet();
  		Set<String> tSet = new TreeSet();
  		for (String car : cars) {
  			hSet.add(car); 
  			tSet.add(car);//
  		}
  		Iterator<String> iter = hSet.iterator();
  		System.out.print("HashSet :");
  		while(iter.hasNext()) {
  			System.out.print(iter.next() + ",");
  		}
  		System.out.println();
  		
          iter = tSet.iterator();
  		System.out.print("TreeSet :");
  		while(iter.hasNext()) {
  			System.out.print(iter.next() + ",");
  		}
  		System.out.println();	
  	}
  }
  /* <출력>
  HashSet :k3,sm3,k5,sm5,k7,sm7,sm6,k9,
  TreeSet :k3,k5,k7,k9,sm3,sm5,sm6,sm7,
  */
  ```

  

- **Map Interface**: 어떤 객체에 대해서 객체를 찾을 때 사용하는 키(key)와 값(value)의 쌍(pair)으로 이루어진 데이터의 집합. 키(key)의 핵심은 unique해야 한다는 것! 즉, 중복값과 null값을 허용하지 않는다. but, 값은 중복을 허용한다. Map인터페이스를 구현한 클래스로는 Hashtable, HashMap, LinkedHashMap, SortedMap, TreeMap 등이 있다.
  
  - Map.Entry 인터페이스: Map인터페이스의 내부 인터페이스. Map에 저장되는 key-value 쌍을 다루기 위해 내부적으로 Entry인터페이스를 정의해 놓은 것.
  - Map의 요소를 꺼내서 처리하려면
    1. 키집합을 리턴받고 - keySet() 메서드
    2. 키집합에 대한 Iterator 생성
    3. Iterator로 키를 하나하나 꺼내서 map에 저장된 Value객체를 꺼낸다 => get(Key)

```java
package lab.java.core;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class HashMapEx2 {

	public static void main(String[] args) {
		HashMap map = new HashMap();
		// .put을 이용해서 객체에 값을 저장
		map.put("김자바", new Integer(90));
		map.put("김자바", new Integer(100));
		map.put("이자바", new Integer(100));
		map.put("강자바", new Integer(80));
		map.put("안자바", new Integer(90));
		
		
		Set set = map.entrySet();
		Iterator it = set.iterator();
		
		while(it.hasNext()) { //hasNext() 메서드는 iteration이 요소를 더 가지고 있으면 true를 리턴
			Map.Entry e = (Map.Entry)it.next(); 
			//API에서 보면 Map에 Entry라는 객체가 있음. Entry는 키와 값의 결합!
			System.out.println("이름: "+e.getKey() + ", 점수 : "+e.getValue());
		}
		
		set = map.keySet();
		System.out.println("참가자 명단 : " + set);
		
		Collection values = map.values();
		it = values.iterator();
		
		int total = 0;
		
		while(it.hasNext()) {
			Integer i = (Integer)it.next();
			total += i.intValue();
		}
		System.out.println("총점 : " + total);
		System.out.println("평균 : " + (float)total/set.size());
		System.out.println("최고점수 : " + Collections.max(values));
		System.out.println("최저점수 : " + Collections.min(values));
	}
}

```





