menu_btn = document.getElementsByClassName('menu-btn')[0];
menu = document.getElementsByClassName('menu-container')[0];
menu_btn.addEventListener('click', function() {
    console.log('menu-btn clicked');
    menu.classList.toggle('hidden');
}
);
menu.addEventListener('click', function(e) {
    if (e.target.closest('.menu-body') === null) {
            menu.classList.add('hidden');
        } 
});
