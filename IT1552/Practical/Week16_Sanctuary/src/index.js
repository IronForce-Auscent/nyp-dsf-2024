document.addEventListener('DOMContentLoaded', function () {
    let slideIndex = 1;
    showSlides(slideIndex);

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    function showSlides(n) {
        let i;
        let slides = document.getElementsByClassName("landing-slides");
        let dots = document.getElementsByClassName("dot");
        if (n > slides.length) {slideIndex = 1}
        if (n < 1) {slideIndex = slides.length}
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex-1].style.display = "block";
        dots[slideIndex-1].className += " active";
    }

    const dotElements = document.querySelectorAll(".dot");
    dotElements.forEach((dot, index) => {
        dot.addEventListener("click", () => currentSlide(index + 1));
    });

    const prevButton = document.querySelector(".prevbutton");
    const nextButton = document.querySelector(".nextbutton");

    prevButton.addEventListener("click", () => plusSlides(-1));
    nextButton.addEventListener("click", () => plusSlides(1));
});

