$(document).ready(function(){
    if($(this).is(":checked")){
        $(".unionHeadDetails").show()
    }
    else{
        $(".unionHeadDetails").hide()
    }
    $("#unionPresence").click(function(){
        if($(this).is(":checked")){
            $(".unionHeadDetails").show()
        }
        else{
            $(".unionHeadDetails").hide()
        }
    });
});