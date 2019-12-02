let heroes = [
    { name : 'Tony Stark', age : 45},
    { name : 'Captain', age : 82},
    { name : 'Thor', age : 1500},
    { name : 'Tony Stark', age : 25}
]

// before
// var hero = {}
// for (var i = 0; i < heroes.length; i++) {
//     if(heroes[i].name === "Tony Stark") {
//         hero = heroes[i]
//         break;
//     }
// }

let hero = heroes.find(function(man) {
    return man === 'Tony Stark'
})
console.log(hero)

// 실습 1 : 잔액이 2만원 이상인 사람의 이름을 출력
const ACCOUNTS = [
    {name : "pengsu", money : 1200},
    {name : "bbung", money : 24000},
    {name : "pororo", money : 50000}
]

let person = ACCOUNTS.find(function(amount) {
    return amount.money >= 20000
})