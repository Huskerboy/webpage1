$(document).ready(function() {
// creating a function that will build on DRY principals to make the AJAX call simpler and so I don't have to do it a ton of times.

    $('.btn-guess-hl').on("click", function(e){
        e.preventDefault();
        var this_guess = $(this).val();
        $.ajax({
            method: "POST",
            url: "/test_route",
            contentType:"application/json; charset=utf-8",
            data: JSON.stringify({"guess_color": this_guess}),
        }).done(function( msg ) {
            alert( msg );
        });
    });
    $('.btn-guess').on("click", function(e){
        e.preventDefault();
        var this_guess = $(this).val();
        var this_route = $(this).data('route');
        $.ajax({
            method: "POST",
            url: this_route,
            contentType:"application/json; charset=utf-8",
            data: JSON.stringify({"guess": this_guess}),
        }).done(function( score_card ) {
            // console.log( score_card )
            if (score_card["value"] === 'True') {
                assemble('div#back_card1', score_card['card']);
            } else {
                alert ('False');
            }
        });
    });
    function assemble (card_element, card) {
        $(card_element).remove();
        $('div#abe').addClass('playingCards').addClass('faceImages');
        $('div#first_card').addClass(card.face.style_rank).addClass(card.suit.style_name);
        $('span#span1').addClass('rank').text(card.face.symbol);
        $('span#span2').addClass('suit').html('&' + style_name + ';');
    }
});
    /**
    $('.btn-guess-hl').on("click", function(e){
        e.preventDefault();
        var this_guess = $(this).val();
        $.ajax({
            method: "POST",
            url: "/test_route",
            contentType:"application/json; charset=utf-8",
            data: JSON.stringify({"guess_hl": this_guess}),
        }).done(function( msg ) {
            alert( msg );
        });
    });
    **/
    //this is a comment

