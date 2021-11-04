// hamburger menu

const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelectorAll('.nav__link')

navToggle.addEventListener('click', () => {
    document.body.classList.toggle('nav-open');
});

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        document.body.classList.remove('nav-open');
    })
})

// bottom nav bar

function makeActive() {
    let element = document.querySelector(".nav-bottom__link");
    element.classList.add("nav-bottom__link--active")
}