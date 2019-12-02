// 배열의 모든 요소에 2를 곱하여 새로운 배열로 만들기

// before
// var numbers = [1, 2, 3]
// var doubleNumber = []

// for (var i = 0; i < numbers.length; i++) {
//     doubleNumber.push(numbers[i]*2)
// }

// map 사용하기
let numbers = [2, 4, 6]

let doubleNum = numbers.map(function(num){
    return num*2
})
console.log(numbers) // 기존의 값을 유지. map은 원본 데이터를 유지시켜주고 새롭게 배열을 만들어 줌을 확인할 수 있다.
console.log(doubleNum)

let doubleNum = numbers.map(num => num*2)


// 실습 1 : 숫자가 담긴 배열을 받아서 각 숫자들의 제곱근이 들어있는 새 배열로 만들어 보자
const newNums = [9, 4, 16]
let roots = newNumbs.map(newnum => newnum.sqrt(2))

// 실습 2 : images 배열 안에 object 들의 height만 저장되어 있는 배열을 만들어 보자
const IMAGES = [
    {height: "34px", width: "39px"},
    {height: "42px", width: "15px"},
    {height: "31px", width: "4px"}
]

let heights = IMAGES.map(function(img) {
    return img.height
})
console.log(heights)

// 실습 3 : { name : brand, movie : 영화 }가 되는 object를 만들어 보자.
const brands = ["Marvel", "DC"]
const movies = ["Avengers", "Darknight"]

// const Heroes = brands.map(function (brand, idx) {
//     return {name: brand, movie: movies[idx]}
// })
const Heroes = brands.map((brand, idx) => ({name:brand, movie:movies[idx]}))
console.log(Heroes)