const PRODUCTS = [
    { name : 'cucumber', type : 'vegetable'},
    { name : 'banana', type : 'fruit'},
    { name : 'carrot', type : 'vegetable'},
    { name : 'apple', type : 'fruit'}
]

// before
var selectProducts = []
// for (var i = 0 ; i < PRODUCTS.length; i++) {
//     if(PRODUCTS[i].type === 'vegetable') {
//         selectProducts.push(PRODUCTS[i])
//     }
// }

let selectProducts = PRODUCTS.filter(function(prod) {
    return prod.type === 'vegetable'
})

console.log(selectProducts)
console.log(PRODUCTS)

// 실습 1 : 80점 이상인 결과만 따로 배열로 만들어 보자
const testResults = [90, 85, 70, 78, 58, 86, 99, 82]
let over80 = testResults.filter(function(jumsu) {
    return jumsu >= 80
})
console.log(over80)
console.log(testResults)