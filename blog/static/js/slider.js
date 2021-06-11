
var btn_prev = document.querySelector(".btn-prev");
var btn_next = document.querySelector(".btn-next");
var image    = document.querySelectorAll(".slider-image img");
var slider   = document.querySelector(".slider");
var i = 0;

btn_next.onclick = function () {
    image[i].classList.remove('active');
    i++;
    if (i >= image.length) {
        i = 0;
    }
    image[i].classList.add('active');
};

btn_prev.onclick = function () {
    image[i].classList.remove('active');
    i--;
    if (i < 0) {
        i = image.length - 1;
    }
    image[i].classList.add('active');
};

function SlideNext() {
    image[i].classList.remove("active");
    i++;
    if (i >= image.length) {
        i = 0;
    }
    image[i].classList.add("active");
}
setInterval(SlideNext, 5000);

