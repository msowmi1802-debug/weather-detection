// Live Clock
function updateClock() {
    const now = new Date();

    document.getElementById("clock").innerHTML =
        now.toLocaleTimeString();

    let greeting = "";

    if (now.getHours() < 12) {
        greeting = "☀️ Good Morning";
    }
    else if (now.getHours() < 18) {
        greeting = "🌤️ Good Afternoon";
    }
    else {
        greeting = "🌙 Good Evening";
    }

    document.getElementById("greeting").innerHTML = greeting;
}

setInterval(updateClock, 1000);
updateClock();


// Search Button Animation
const button = document.querySelector("button");

button.addEventListener("mouseover", () => {
    button.style.transform = "scale(1.08)";
});

button.addEventListener("mouseout", () => {
    button.style.transform = "scale(1)";
});


// Weather Card Fade In
window.addEventListener("load", () => {

    const card = document.querySelector(".weather-info");

    if (card) {
        card.style.opacity = "0";

        setTimeout(() => {
            card.style.transition = "1s";
            card.style.opacity = "1";
        }, 200);
    }
});