function findUserxx(users, usr, pwd) {
   for (let index in users){
    // let user = []    
    let user = users[index]
    for (let item in user){
        if(user[item] == usr){
            if(user.password == pwd) {
            console.log(`${item}: ${user[item]}`)
            return users[index]
        }
    }
    }
   }
   console.log(`${usr} not found`)
   return false
  }
  

  function findUser(users, usr, pwd) {
    for (let user of users){
        if(user.username === usr && user.password === pwd){
            console.log(user)
            return user
        }
    }
        return false    
  }


  let users = [
    {
      username: "John",
      password: "password123",
      role: "public",
    },
    {
      username: "xXxSn1p3rK1lLaxXx",
      password: "newbDestroyer",
      role: "public",
    },
    {
      username: "admin",
      password: "admin",
      role: "admin",
    },
  ];

// findUser(users, "John", "password123")
//   findUser(users, "xXxSn1p3rK1lLaxXx", "newbDestroyer")
//   findUser(users, "xXxSnip3rK1lLaxXx", "foobar")
//   findUser(users, "foobar", "newbDestroyer")
  findUser(users, "admin", "admin")