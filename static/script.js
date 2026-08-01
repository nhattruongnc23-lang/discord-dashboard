// ==========================
// Meow Meow UI
// ==========================

const menuBtn = document.getElementById("menu-toggle");
const sidebar = document.getElementById("sidebar");

if (menuBtn && sidebar) {

    menuBtn.addEventListener("click", () => {

        sidebar.classList.toggle("open");

    });

}

document.addEventListener("click", (e) => {

    if (
        window.innerWidth <= 768 &&
        sidebar &&
        sidebar.classList.contains("open") &&
        !sidebar.contains(e.target) &&
        !menuBtn.contains(e.target)
    ) {

        sidebar.classList.remove("open");

    }

});

