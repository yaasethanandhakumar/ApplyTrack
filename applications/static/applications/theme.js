
const themeToggle = document.getElementById("themeToggle");

// Apply the selected theme
function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);

    themeToggle.textContent =
        theme === "dark" ? "Light Mode" : "Dark Mode";
}

// Load the previously saved theme
const savedTheme = localStorage.getItem("applytrack-theme") || "light";

applyTheme(savedTheme);

// Switch theme when the button is clicked
themeToggle.addEventListener("click", function () {
    const currentTheme =
        document.documentElement.getAttribute("data-theme");

    const newTheme = currentTheme === "dark" ? "light" : "dark";

    applyTheme(newTheme);

    localStorage.setItem("applytrack-theme", newTheme);
});
