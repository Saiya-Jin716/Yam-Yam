function loadPage(){
    window.location.href = "http://127.0.0.1:5000/welcome_page";
}

function calculate(){
    const input = document.getElementById("numbers").value;
    const numbers = input.split(",").map(Number);
    fetch("http://127.0.0.1:5000/calculate",{
        method: "POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({numbers:numbers})
    })
    .then(response => response.json())
    .then(data =>{
        document.getElementById("result").innerHTML = "Average: " + data.average;
    });
}

{
    document.addEventListener("DOMContentLoaded", function() {
        fetch("http://127.0.0.1:5000/api/fruits")
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById("fruitList");
            data.forEach(fruit => {
                list.innerHTML += "<li>" + fruit + "</li>";
            });
        });
    });
}

{
    document.addEventListener("DOMContentLoaded", function() {
        fetch("http://127.0.0.1:5000/api/profile")
        .then(response => response.json())
        .then(data => {
            document.getElementById("photo").src = data.photo;
            document.getElementById("name").textContent = data.name;
            document.getElementById("age").textContent = data.age;
            document.getElementById("course").textContent = data.course;
            document.getElementById("level").textContent = data.level;
            document.getElementById("department").textContent = data.department;
        });
    });
}
