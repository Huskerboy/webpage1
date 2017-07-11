$(document).ready(function() {
// creating a function that will build on DRY principals to make the AJAX call simpler and so I don't have to do it a ton of times.
    function cardAssembly(zero, one, two, three, four, five, six) {
        $.ajax({
            type: 'GET',
            url: "/_draw_card",
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

    /* This code here works
    $("#red").on("click", function() {
        $.ajax({
            type: 'GET',
            url: "/_draw_card",
            data: { get_param: 'value' },
            dataType: 'json',
            success: function (data) {
                if (data.suit.color === 'red') {
                    $('#back_card1').remove();
                    $('div#abe').addClass('playingCards').addClass('faceImages');
                    $('div#readout1').text('You drew a ' + data.face.name + ' of ' + data.suit.name);
                    $('div#first_card').addClass(data.face.style_rank).addClass(data.suit.style_name);
                    $('span#span1').addClass('rank').text(data.face.symbol);
                    $('span#span2').addClass('suit').html('&' + data.suit.style_name + ';');
                    $("#red, #black").prop("disabled",true);
                } else {
                    alert("I'm sorry, your card was a " + data.face.name + ' of ' + data.suit.name);
                }
            }
        });
    });
    */
    $("#draw2").on("click", function() {
        $.ajax({
            type: 'GET',
            url: "/_draw_card",
            data: { get_param: 'value' },
            dataType: 'json',
            success: function (data) {
                $('div#ben').addClass('playingCards').addClass('faceImages');
                $('div#readout2').text('You drew a ' + data.face.name + ' of ' + data.suit.name);
                $('div#second_card').addClass(data.face.style_rank).addClass(data.suit.style_name);
                $('span#span3').addClass('rank').text(data.face.symbol);
                $('span#span4').addClass('suit').html('&' + data.suit.style_name + ';');
                $("div#back_card2").hide();
            },
            error: function() {
            console.log('Houston we have a problem');
            }
        });
    });
    $("#draw3").on("click", function() {
        $.ajax({
            type: 'GET',
            url: "/_draw_card",
            data: { get_param: 'value' },
            dataType: 'json',
            success: function (data) {
                $('div#carl').addClass('playingCards').addClass('faceImages');
                $('div#readout3').text('You drew a ' + data.face.name + ' of ' + data.suit.name);
                $('div#third_card').addClass(data.face.style_rank).addClass(data.suit.style_name);
                $('span#span5').addClass('rank').text(data.face.symbol);
                $('span#span6').addClass('suit').html('&' + data.suit.style_name + ';');
                $("div#back_card3").hide();
            },
            error: function() {
            console.log('Houston we have a problem');
            }
        });
    });
    $("#draw4").on("click", function() {
        $.ajax({
            type: 'GET',
            url: "/_draw_card",
            data: { get_param: 'value' },
            dataType: 'json',
            success: function (data) {
                $('div#dane').addClass('playingCards').addClass('faceImages');
                $('div#readout4').text('You drew a ' + data.face.name + ' of ' + data.suit.name);
                $('div#fourth_card').addClass(data.face.style_rank).addClass(data.suit.style_name);
                $('span#span7').addClass('rank').text(data.face.symbol);
                $('span#span8').addClass('suit').html('&' + data.suit.style_name + ';');
                $("div#back_card4").hide();
            },
            error: function() {
            console.log('Houston we have a problem');
            }
        });
    });
});
