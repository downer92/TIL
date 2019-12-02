// before
var textbooks = ['Learning JS', 'Learning Django']
var comics = {
    DC : ['AquaMan', 'SuperMan'],
    Marvel : ['IronMan', 'AntMan']
}

var magazines = null;
// var bookStore = {
//     textbooks : textbooks,
//     comics : comics,
//     magazines : magazines
// }

let bookstore = {
    textbooks,
    comics,
    magazines,
} // 이름이랑 값이 똑같으면 이렇게만 넣어주면 됨!

console.log(bookstore)
console.log(typeof bookstore) // 타입 학인은 typeof로
console.log(bookstore.textbooks[0])