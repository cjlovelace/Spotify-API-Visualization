window.addEventListener('load', (image) => {
    eel.get_user_image()(function(number){
        document.querySelector(".grid-item-image").innerHTML = number;
    })

    eel.get_user_info()(function(number){
        document.querySelector(".grid-item-info").innerHTML += number;
    })
});