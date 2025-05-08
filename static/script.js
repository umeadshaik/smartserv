window.addEventListener("load", () => {
    const preloader = document.getElementById("preloader");
    preloader.style.opacity = "100%";
    preloader.style.transition = "opacity 1.0s ease-in-out";
    setTimeout(() => {
        preloader.style.display = "none";
    }, 1000); // matches transition time
});

// Handle "Book a Service" button click





document.addEventListener("DOMContentLoaded", function () {
    const bookButton = document.querySelector(".hero-buttons .btn-primary");
    if (bookButton) {
        bookButton.addEventListener("click", function () {
            window.location.href = "book_service.html";
        });
    }
});
document.addEventListener("DOMContentLoaded", function () {
    const learnmore = document.querySelector(".hero-buttons .btn-secondary");
    if (learnmore) {
        learnmore.addEventListener("click", function () {
            window.location.href = "learn_more.html";
        });
    }
});
