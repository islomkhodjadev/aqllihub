"use strict"

let mode = document.getElementById("mode_changer")

mode.addEventListener("click", function() {
    let navbar = document.getElementById("navbarmenu");
    if (navbar.getAttribute("data-bs-theme") == "dark") {
        navbar.setAttribute("data-bs-theme", "light")

    }else {
        navbar.setAttribute("data-bs-theme", "dark")
    }
    document.querySelectorAll(".card").forEach(function(card) {
        console.log(card)
        if (card.getAttribute("data-bs-theme") == "dark") {
            card.setAttribute("data-bs-theme", "light")
    
        }else {
            card.setAttribute("data-bs-theme", "dark")
        }
    })
    document.body.classList.toggle("dark")
    let pagination = document.getElementById("paginationnav");
    if (pagination.getAttribute("data-bs-theme") == "dark") {
        pagination.setAttribute("data-bs-theme", "light")

    }else {
        pagination.setAttribute("data-bs-theme", "dark")
    }
    
})