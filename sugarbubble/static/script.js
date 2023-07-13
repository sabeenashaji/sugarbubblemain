const nav = document.getElementById("jav");
const bar = document.getElementById("menu");

bar.addEventListener("click",()=>{
    nav.classList.toggle("jav")
});

var icon = document.getElementById('mobilemenu')
var hiddenBox = document.getElementById('hidden-div')

icon.addEventListener('click',()=>{
    hiddenBox.classList.toggle('hidden')
})
var closeIcon = document.getElementById('mmm')
closeIcon.addEventListener('click',()=>{
    if(hiddenBox.classList.contains('hidden')){
        hiddenBox.classList.remove('hidden')
    }
})