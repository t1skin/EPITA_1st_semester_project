function updateClock() {
    const clock = document.getElementById("clock");
    const now = new Date();
    const timeString = now.toLocaleTimeString().slice(0, 5);
    clock.innerHTML = timeString;
}  

setInterval(updateClock, 1000);