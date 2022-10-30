searchForm = document.querySelector('#search-form');


document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active');
}



$(window).on("load", function () {
    $(".loader-container").fadeOut("slow");
})



$(document).ready(function () {
    // book-slider

    $('#hero-slider').owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        items: 1,
        smartSpeed: 1000,
        dots: false,
        navText: ['<', '>'],
        autoplay:
        {
            delay: 4000,
            disableOnInteraction: false,
        },
        responsive: {
            0: {

            },
            600: {

            },
            1000: {

            }
        }
    })
});

var swiper = new Swiper(".featured-slider", {
    spaceBetween: 10,
    loop: true,
    centeredSlides: true,
    autoplay:
    {
        delay: 9500,
        disableOnInteraction: false,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints:
    {
        0:
        {
            slidesPerView: 1,
        },
        450:
        {
            slidesPerView: 2,
        },
        768:
        {
            slidesPerView: 3,
        },
        1024:
        {
            slidesPerView: 4,
        },
    },

});


var swiper = new Swiper(".arrivals-slider", {
    spaceBetween: 10,
    loop: true,
    centeredSlides: true,
    autoplay:
    {
        delay: 9500,
        disableOnInteraction: false,
    },
    breakpoints:
    {
        0:
        {
            slidesPerView: 1,
        },

        768:
        {
            slidesPerView: 2,
        },
        1024:
        {
            slidesPerView: 3,
        },
    },

});