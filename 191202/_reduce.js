// 배열의 총합을 구하세요
const numbers = [1, 2, 3, 4]

// before
// let total = 0
// for(let i = 0; i < numbers.length; i++) {
//     total += numbers[i]
// }

// using reduce
let sum = numbers.reduce(function(total, num) {
    return total += num
}, 0)  // 두번째 인자인 0은 첫 번째 인자인 total의 default값에 대한 설정이다.
console.log(sum)
console.log(numbers)

// 실습 1 : 평균을 구해보세요
const testResults = [90, 85, 70, 78, 58, 86, 99, 82]
let avg = testResults.reduce(function(total, num) {
    return total += num 
}, 0) / testResults.length

// 실습 2 : 배열에 담긴 이름의 중복을 확인해서 {이름: 중복횟수, 이름: 중복횟수} 형식의 Object로 반환

const names = ['pengsu', 'bboong', 'pororo', 'bbung', 'bungaeman', 'pengsu']

let nameResults = names.reduce(function(allNames, name) {
    if (name in allNames) {
        allNames[name] += 1
    } else {
        allNames[name] = 1
    }
    return allNames
}, {})                             