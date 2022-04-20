window.addEventListener('load', (image) => {
    eel.get_user_image()(function(number){
        document.querySelector(".grid-item-image").innerHTML = number;
    })

    eel.get_user_info()(function(number){
        document.querySelector(".grid-item-info").innerHTML += number;
    })

    eel.user_top_artists()(function(number){
        document.querySelector(".display-artists").innerHTML += number;
    })

    var artist_div = document.querySelector(".top-artists-button");
    var user_div = document.querySelector(".user-button");
    var user_profile = document.querySelector(".display-user-info");
    var artists = document.querySelector(".display-artists");

    eel.display_user_info()(function(number){
        user_profile.innerHTML += number;
    })

    artist_div.addEventListener('click', function() {
        user_profile.style.display = 'none';

        if (artists.style.display === 'none') {
            artists.style.display = 'block';
        }
        else {
            artists.style.display = 'none';
        }
    })

    user_div.addEventListener('click', function() {
        artists.style.display = 'none';

        if (user_profile.style.display === 'none') {
            user_profile.style.display = 'block';
        }
        else {
            user_profile.style.display = 'none';
        }
    })




});


