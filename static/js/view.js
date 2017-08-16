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
        var this_parent = $(this).parent();;
        // var prev_card = window.game.prev_card || null;
        $.ajax({
            method: "POST",
            url: this_route,
            contentType:"application/json; charset=utf-8",
            data: JSON.stringify({"guess": this_guess}),
        }).done(function( score_card ) {
            // console.log( score_card )
            // window.game.prev_card = score_card;
            if (score_card["value"] === 'True') {
                assemble(this_parent, score_card['card']);
            } else {
                alert ('False');
            }
        });
    });

    function assemble (this_parent, score_card) {
        this_parent.children('div.back_card').remove();
        this_parent.children('div.card_front').addClass('playingCards').addClass('faceImages');
        this_parent.find('div.display').addClass(score_card['face']['style_rank']).addClass(score_card['suit']['style_name']);
        this_parent.find('span.rank').text(score_card['face']['symbol']);
        this_parent.find('span.suit').html('&' + score_card.suit.style_name + ';');
    }
});
    /**
        function assemble (first_section) {
        $(back_card).remove();
        $('div#abe').addClass('playingCards').addClass('faceImages');
        $('div#first_card').addClass(card.face.style_rank).addClass(card.suit.style_name);
        $('span#span1').addClass('rank').text(card.face.symbol);
        $('span#span2').addClass('suit').html('&' + style_name + ';');
    }
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

