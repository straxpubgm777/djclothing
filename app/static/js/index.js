const searchInputDiv = document.querySelector(".search-input-div");
document.querySelector("#show-search-input").addEventListener("click", () => {
    if (searchInputDiv.style.display === "none" || searchInputDiv.style.display === "") {
        searchInputDiv.style.display = "flex";
        document.getElementById("show-search-input").style.display = "none"
    } 
});
document.getElementById("hide-search-input").addEventListener("click",()=>{
    searchInputDiv.style.display = "none";
    document.getElementById("show-search-input").style.display = "block"
})

document.querySelectorAll(".show-cart").forEach(element => {
    element.addEventListener("click", () => {
        document.querySelectorAll(".cart-right").forEach(x => {
            x.style.display = "flex";
        });
    });
});


document.querySelectorAll(".hide-cart").forEach(element => {
    element.addEventListener("click", () => {
        document.querySelectorAll(".cart-right").forEach(x => {
            x.style.display = "none";
        });
    });
});


$(document).ready(function () {
    $(".category-item").hover(
        function () {
            $(this).find(".subcategories").addClass("show");
        },
        function () {
            $(this).find(".subcategories").removeClass("show");
        }
    );
});