addUserApi = "http://127.0.0.1:5000/register"
loginApi = "http://127.0.0.1:5000/login"
homeApi = "http://127.0.0.1:5000/"

function loadHome(){
  window.location.href="/";
}

function registerFormSubmit(event){
  event.preventDefault();
  var username = document.querySelector('input[name="username"]').value
  var phonenumber = document.querySelector('input[name="phonenumber"]').value
  var password = document.querySelector('input[name="password"]').value
  var password_confirm = document.querySelector('input[name="password-confirm"]').value
  if (username == "" || phonenumber == "" || password == "" || password_confirm == ""){
    document.getElementById("messageError").innerHTML = "Vui lòng điền đầy đủ thông tin";
  }
  else if (password != password_confirm){
    document.getElementById("messageError").innerHTML = "Mật khẩu xác nhận không khớp";
  }
  else{
    data = {
      username: username,
      password: password,
      phonenumber: phonenumber
    }
    createNewUser(data,loadHome)
  }
}
function loginFormSubmit(event){
  var username = document.querySelector('input[name="username"]').value
  var password = document.querySelector('input[name="password"]').value
  console.log(username)
  console.log(password)
  if (username == "" || password == ""){
    document.getElementById("messageError").innerHTML = "Vui lòng điền đầy đủ thông tin";
    event.preventDefault();
  }
  else{
    data = {
      username: username,
      password: password
    }
    checkLogin(data,loadHome)
  }
}

function checkLogin(data,callback){
  console.log(JSON.stringify(data));
  var options = {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
          "Content-Type": "application/json"
      }
  }
  fetch(loginApi, options)
      .then(function(response){
        console.log(response.json());
      })
      .then(callback)
      .catch(function(error){
          console.log(error);
      })
}
function createNewUser(data,callback){
  console.log(JSON.stringify(data));
  var options = {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
          "Content-Type": "application/json"
      }
  }
  fetch(addUserApi, options)
      .then(function(response){
        console.log(response.json());
      })
      .then(callback)
      .catch(function(error){
          console.log(error);
      })
}

