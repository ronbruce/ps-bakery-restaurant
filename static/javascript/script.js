document.addEventListener("DOMContentLoaded", () => {
    const searchIcon = document.querySelector('.search-icons');
    const searchForm = document.querySelector('.search-form');

    searchIcon.addEventListener('click', () => {
        searchForm.classList.add('active');
        cartItemsContainer.classList.remove('active');
    });

    const cartIcons = document.querySelector('.cart-icons');
    const cartItemsContainer = document.querySelector('.cart-items-container');

    cartIcons.addEventListener('click', () => {
        cartItemsContainer.classList.add('active');
        searchForm.classList.remove('active');
    });
  });