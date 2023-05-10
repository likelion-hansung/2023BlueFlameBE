function day1(){
    window.location.href = "/2023BlueFlame/pages/booth(Day1).html";
}

function day2(){
    window.location.href = "/2023BlueFlame/pages/booth(Day2).html";
}

function day3(){
    window.location.href = "/2023BlueFlame/pages/booth(Day3).html";
}

function first1(){
    $('#day1-wrap').show();

    $('#loc1-wrap').show();
    $('#loc2-wrap').hide();
    $('#loc3-wrap').hide();

    $('#first-time').css("color", "#92AAFF");
    $('#day1-info').css("color", "#92AAFF");

    $('#second-time').css("color", "#3A4DEE");
    $('#day2-info').css("color", "#3A4DEE");
    $('#third-time').css("color", "#3A4DEE");
    $('#day3-info').css("color", "#3A4DEE");

    $('#location1').css("background","#92AAFF");
    $('#location2').css("background","rgba(58, 77, 238, 0.2)");
    $('#location3').css("background","rgba(58, 77, 238, 0.2)");

    $('#location1-text').css("color"," #090B26");
    $('#location2-text').css("color"," #3A4DEE");
    $('#location3-text').css("color"," #3A4DEE");

    $('#first-tap1').css("border-bottom", "1px solid #92AAFF");
    $('#first-tap2').css("border-bottom", "1px solid #3A4DEE");
    $('#first-tap3').css("border-bottom", "1px solid #3A4DEE");
}

function first2(){
    $('#loc1-wrap').hide();
    $('#loc2-wrap').show();
    $('#loc3-wrap').hide();

    $('#location1').css("background","rgba(58, 77, 238, 0.2)");
    $('#location2').css("background","#92AAFF");
    $('#location3').css("background","rgba(58, 77, 238, 0.2)");

    $('#location1-text').css("color"," #3A4DEE");
    $('#location2-text').css("color"," #090B26");
    $('#location3-text').css("color"," #3A4DEE");
}

function first3(){
    $('#loc3-wrap').show();
    $('#loc1-wrap').hide();
    $('#loc2-wrap').hide();

    $('#location1').css("background","rgba(58, 77, 238, 0.2)");
    $('#location2').css("background","rgba(58, 77, 238, 0.2)");
    $('#location3').css("background","#92AAFF");

    $('#location1-text').css("color"," #3A4DEE");
    $('#location2-text').css("color"," #3A4DEE");
    $('#location3-text').css("color"," #090B26");
}

function second1(){
    $('#day2-wrap').show();
    $('#loc4-wrap').show();
    $('#loc5-wrap').hide();
    $('#loc6-wrap').hide();

    $('#first-time').css("color", "#3A4DEE");
    $('#day1-info').css("color", "#3A4DEE");
    $('#third-time').css("color", "#3A4DEE");
    $('#day3-info').css("color", "#3A4DEE");

    $('#second-time').css("color", "#92AAFF");
    $('#day2-info').css("color", "#92AAFF");

    $('#location4').css("background","#92AAFF");
    $('#location5').css("background","rgba(58, 77, 238, 0.2)");
    $('#location6').css("background","rgba(58, 77, 238, 0.2)");

    $('#location4-text').css("color"," #090B26");
    $('#location5-text').css("color"," #3A4DEE");
    $('#location6-text').css("color"," #3A4DEE");

    $('#first-tap2').css("border-bottom", "1px solid #92AAFF");
    $('#first-tap1').css("border-bottom", "1px solid #3A4DEE");
}

function second2(){
    $('#loc5-wrap').show();
    $('#loc4-wrap').hide();
    $('#loc6-wrap').hide();

    $('#location4').css("background","rgba(58, 77, 238, 0.2)");
    $('#location5').css("background","#92AAFF");
    $('#location6').css("background","rgba(58, 77, 238, 0.2)");

    $('#location4-text').css("color"," #3A4DEE");
    $('#location5-text').css("color"," #090B26");
    $('#location6-text').css("color"," #3A4DEE");
}

function second3(){
    $('#loc6-wrap').show();
    $('#loc4-wrap').hide();
    $('#loc5-wrap').hide();

    $('#location4').css("background","rgba(58, 77, 238, 0.2)");
    $('#location5').css("background","rgba(58, 77, 238, 0.2)");
    $('#location6').css("background","#92AAFF");

    $('#location4-text').css("color"," #3A4DEE");
    $('#location5-text').css("color"," #3A4DEE");
    $('#location6-text').css("color"," #090B26");
}

function third1(){
    $('#day3-wrap').show();
    $('#day1-wrap').hide();
    $('#day2-wrap').hide();
    $('#loc7-wrap').show();
    $('#loc8-wrap').hide();
    $('#loc9-wrap').hide();

    $('#first-time').css("color", "#3A4DEE");
    $('#day1-info').css("color", "#3A4DEE");

    $('#second-time').css("color", "#3A4DEE");
    $('#day2-info').css("color", "#3A4DEE");

    $('#third-time').css("color", "#92AAFF");
    $('#day3-info').css("color", "#92AAFF");

    $('#location7').css("background","#92AAFF");
    $('#location8').css("background","rgba(58, 77, 238, 0.2)");
    $('#location9').css("background","rgba(58, 77, 238, 0.2)");

    $('#location7-text').css("color"," #090B26");
    $('#location8-text').css("color"," #3A4DEE");
    $('#location9-text').css("color"," #3A4DEE");

    $('#first-tap3').css("border-bottom", "1px solid #92AAFF");
    $('#first-tap1').css("border-bottom", "1px solid #3A4DEE");
    $('#first-tap2').css("border-bottom", "1px solid #3A4DEE");
}

function third2(){
    $('#loc8-wrap').show();
    $('#loc7-wrap').hide();
    $('#loc9-wrap').hide();

    $('#location7').css("background","rgba(58, 77, 238, 0.2)");
    $('#location8').css("background","#92AAFF");
    $('#location9').css("background","rgba(58, 77, 238, 0.2)");

    $('#location7-text').css("color"," #3A4DEE");
    $('#location8-text').css("color"," #090B26");
    $('#location9-text').css("color"," #3A4DEE");
}

function third3(){
    $('#loc9-wrap').show();
    $('#loc8-wrap').hide();
    $('#loc7-wrap').hide();

    $('#location7').css("background","rgba(58, 77, 238, 0.2)");
    $('#location8').css("background","rgba(58, 77, 238, 0.2)");
    $('#location9').css("background","#92AAFF");

    $('#location7-text').css("color"," #3A4DEE");
    $('#location8-text').css("color"," #3A4DEE");
    $('#location9-text').css("color"," #090B26");
}