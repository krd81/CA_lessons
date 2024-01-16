var books = [
    {
      title: 'The Design of EveryDay Things',
      author: 'Don Norman',
      alreadyRead: false
    }, {
      title: 'The Most Human Human',
      author: 'Brian Christian',
      alreadyRead: true
    },
    {
      title: 'Pride & Prejudice',
      author: 'Jane Austen',
      alreadyRead: true
    },
    {
      title: 'The Time Traveler\'s Wife',
      author: 'Audrey Niffenegger',
      alreadyRead: true
    }
  ];

let ul = document.createElement("ul")
document.querySelector("body").append(ul)

for (let book of books){
    const newLi = document.createElement("li")
    newLi.textContent = `${book.title} by ${book.author}`
    ul.append(newLi)

    if (book.alreadyRead){
        console.log(book.title)
        newLi.style.backgroundColor = "rgba(52, 235, 152, 0.5)"
    }
}

