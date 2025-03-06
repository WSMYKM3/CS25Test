document.addEventListener('DOMContentLoaded', function(){
    let form = document.querySelector('form');
    form.addEventListener('submit', function (event){
        let name = document.querySelector('#name').value;
        alert('this alert is created by greet function. Hello! ' + name 
        +"\nlet form = document.querySelector('form');\n"
            +'form.addEventListener("submit", greet)' 
        );
        event.preventDefault();
    });
})