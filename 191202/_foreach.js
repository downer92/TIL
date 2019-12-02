// 예전 방식
var colors = ['red', 'orange', 'yellow']
for (var i = 0; i < colors.length; i++) {
    console.log(colors[i])
}

// forEach 방식
const COLORS = ['red', 'orange', 'yellow']
COLORS.forEach(function(color) {
    console.log(color)
})

let result = COLORS.forEach(color => console.log(color))
console.log(result)

// 실습1
function handlePosts() {
    const posts = [{
        id : 23,
        title : "오늘의 뉴스"
    },
    {
        id : 34,
        title : "세상에나 마상에나"
    },
    {
        id : 78,
        title : "오늘의 연예"
    }]
    
    // for(let i = 0 ; i < posts.length(); i++) {
    //     console.log(posts[i])
    //     console.log(post[i].id)
    //     console.log(post[i].title)
    // }
    
    posts.forEach(function(post) {
        console.log(post)
    })
}

// 실습 2
// 이미지 배열 안에 있는 정보를 가지고 넓이를 구하고 그 값을 areas에 저장해보자
const IMAGES = [
    { height : 10, width : 30},
    { height : 22, width : 68},
    { height : 35, width : 15}
]

// let areas = []
// IMAGES.forEach(function(image) {
//     areas.push(image.height*image.width)
// })
// console.log(areas)

IMAGES.forEach(image => areas.push(image.height * image.width))
console.log(areas)