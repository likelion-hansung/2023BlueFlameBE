$(document).ready(function() {
    $("#likelion-page").show();
    $("#creator-page").hide();
});

function changeToCreator(){
    $("#likelion-page").hide();
    $("#creator-page").show();

    $("#nav2").css("color","#92AAFF");
    $("#nav2").css("border-bottom","2px solid #92AAFF");
    $("#nav1").css("color","#3A4DEE");
    $("#nav1").css("border-bottom","2px solid #3A4DEE");

}

function changeToLikelion(){
    $("#likelion-page").show();
    $("#creator-page").hide();

    $("#nav2").css("color","#3A4DEE");
    $("#nav2").css("border-bottom","2px solid #3A4DEE");
    $("#nav1").css("color","#92AAFF");
    $("#nav1").css("border-bottom","2px solid #92AAFF");
}