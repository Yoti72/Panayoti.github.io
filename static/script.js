window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
    var pageWrapper = document.querySelector('.page-wrapper');
    var pageWrapperBottom = pageWrapper.getBoundingClientRect().bottom;

    if (window.scrollY > pageWrapperBottom) {
        navbar.classList.add('fixed-bottom');
    } else {
        navbar.classList.remove('fixed-bottom');
    }
});