// Typing Animation

const words = [
    "HTML",
    "CSS",
    "JS",
    "Frontend Developer",
    "Backend Developer",
    "Python Learner",
    "Django Learner",
];

let wordIndex = 0;
let charIndex = 0;
let deleting = false;
const typingElement = document.getElementById("typing");

function typeEffect() {

    if (!typingElement) return;

    const currentWord = words[wordIndex];

    if (!deleting) {

        typingElement.textContent = currentWord.substring(0, charIndex++);

        if (charIndex > currentWord.length) {

            deleting = true;

            setTimeout(typeEffect, 1200);

            return;

        }

    } else {

        typingElement.textContent = currentWord.substring(0, charIndex--);

        if (charIndex < 0) {

            deleting = false;

            wordIndex++;

            if (wordIndex >= words.length)
                wordIndex = 0;

        }

    }

    setTimeout(typeEffect, deleting ? 50 : 100);

}

typeEffect();
// Counter Animation

const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    const update = () => {

        const target = Number(counter.getAttribute("data-target"));

        const count = Number(counter.innerText);

        const increment = Math.ceil(target / 100);

        if (count < target) {

            counter.innerText = count + increment;

            setTimeout(update, 20);

        } else {

            counter.innerText = target;

        }

    };

    update();

});
window.addEventListener("scroll",function(){

    const navbar=document.querySelector(".custom-navbar");

    if(window.scrollY>50){

        navbar.style.background="#050b16";

        navbar.style.boxShadow="0 10px 25px rgba(0,0,0,.35)";

    }

    else{

        navbar.style.background="rgba(8,17,31,.65)";

        navbar.style.boxShadow="none";

    }

});
// ======================
// Dark / Light Theme
// ======================

const themeBtn = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");

// Load saved theme
if(localStorage.getItem("theme") === "light"){

    document.body.classList.add("light-theme");

    themeIcon.classList.remove("bi-moon-fill");
    themeIcon.classList.add("bi-sun-fill");

}

themeBtn.addEventListener("click",()=>{

    document.body.classList.toggle("light-theme");

    if(document.body.classList.contains("light-theme")){

        localStorage.setItem("theme","light");

        themeIcon.classList.remove("bi-moon-fill");
        themeIcon.classList.add("bi-sun-fill");

    }

    else{

        localStorage.setItem("theme","dark");

        themeIcon.classList.remove("bi-sun-fill");
        themeIcon.classList.add("bi-moon-fill");

    }

});
const toastElList = document.querySelectorAll('.toast');

toastElList.forEach(toastEl => {

    const toast = new bootstrap.Toast(toastEl, {
        delay: 3000
    });

    toast.show();

});
