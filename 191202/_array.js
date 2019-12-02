const numbers = [1, 2, 3, 4, 5, 6, 7]
// console.log(numbers[1])
// // console.log(numbers[-1]) // Error : 양의 정수만 index 가능
// console.log(numbers.length)
// console.log(numbers)
// console.log(numbers[0])

// push 후 배열 길이 리턴
numbers.push('peng') // return 값은 배열의 길이
console.log(numbers)
console.log(numbers.push('su'))

// pop (빼는 친구)
console.log(numbers.pop())
console.log(numbers)

// unshift : 배열의 가장 앞쪽에 요소를 추가 후 배열의 길이를 리턴
console.log(numbers.unshift("pengsu"))
console.log(numbers)

// shift : 배열의 가장 뒤쪽에 요소를 추가 후 배열의 길이를 리턴
console.log(numbers.shift())
console.log(numbers)