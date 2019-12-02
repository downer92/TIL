// // 실습
// // => 화살표 함수로 변환시켜 보자.
// let square = function(num) {
//     return num ** 2
// }

// // 1. function 이름 제거
// let square = (num) => {
//     return num ** 2
// }

// // 2. 인자가 1개인 경우 () 삭제
// let square = num => {
//     return num ** 2 // **2는 제곱
// }

// // 3. body 부분이 1개로 되어 있을 때
// let square = num => num ** 2

// // 인자가 없다면
// let noArgs = function() {
//     return 'no Args'
// }
// let noArgs = () => 'no Args'
// let noArgs = _ => 'no Args' 

// // object 형식으로 반환된다면?
// let returnObj = () => {
//     return {key:'value'}
// }

// let returnObj = () => ({key:'value'})
// console.log(returnObj())

// let sayHi = function(name="pengsu") {
//     return `hi ${name}`
// }

// let sayHi = (name="pengsu") => `hi ${name}`
// console.log(sayHi())


// 즉시 실행 함수
// 기명함수 즉시 실행
const cube = function(num) {
    return num ** 3
}
console.log(cube(2))

// 익명함수 즉시 실행
console.log(function(num){return num ** 3}(2))