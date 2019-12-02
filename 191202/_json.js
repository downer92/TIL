let jsonStr = JSON.parse('{"name" : "pengsu", "age" : "10"}')
console.log(typeof jsonStr) // String 값인 Object를 JSON으로 변환

let obj = {
    name : 'pengsu',
    age : '10',
}
console.log(typeof obj)
let jsonObj = JSON.stringify(obj)
console.log(typeof jsonObj)
console.log(jsonObj)