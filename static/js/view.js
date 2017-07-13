$(document).ready(function() {
// creating a function that will build on DRY principals to make the AJAX call simpler and so I don't have to do it a ton of times.
/**
    function cardAssembly(zero, one, two, three, four, five, six) {
        $.ajax({
            type: 'GET',
            url: "/first_step",
            data: { get_param: 'value' },
            dataType: 'json',
            success: function (data) {
                if (data.suit.color === zero) {
                    $(one).remove();
                    $(two).addClass('playingCards').addClass('faceImages');
                    $(three).text('You drew a ' + data.face.name + ' of ' + data.suit.name);
                    $(four).addClass(data.face.style_rank).addClass(data.suit.style_name);
                    $(five).addClass('rank').text(data.face.symbol);
                    $(six).addClass('suit').html('&' + data.suit.style_name + ';');
                } else {
            alert("I'm sorry, your card was a " + data.face.name + ' of ' + data.suit.name);
                }
            }
        });
    }
    $("#red").on("click", function() {
        cardAssembly('red', '#back_card1', 'div#abe', 'div#readout1', 'div#first_card', 'span#span1', 'span#span2');
        $('#red').prop("disabled",true);
    });
    $("#black").on("click", function() {
        cardAssembly('black', '#back_card1', 'div#abe', 'div#readout1', 'div#first_card', 'span#span1', 'span#span2');
        $('#black').prop("disabled",true);
    });
    **/
    $('.btn-guess').on("click", function(e){
        e.preventDefault();
        var this_guess = $(this).val();
        $.ajax({
        method: "POST",
        url: "/test_route",
        data: { guess: this_guess }
    })
    .done(function( msg ) {
        alert( msg );
    });
    });

    $.ajax({
        method: "POST",
        url: "/first_step",
        data: { guess: "Black" }
    })
    .done(function( msg ) {
        alert( "Data Saved: " + msg );
    });
    $.ajax({
        method: "POST",
        url: "/second_step",
        data: { guess: "High" }
    })
    .done(function( msg ) {
        alert( "Data Saved: " + msg );
    });
    $.ajax({
        method: "POST",
        url: "/third_step",
        data: { guess: "Inside" }
    })
    .done(function( msg ) {
        alert( "Data Saved: " + msg );
    });
    $.ajax({
        method: "POST",
        url: "/final_step",
        data: { guess: "Spades" }
    })
    .done(function( msg ) {
        alert( "Data Saved: " + msg );
    });

});
