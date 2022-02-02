$(document).ready(() => {
    var currentPage = 1;
    var page1 = $("#page-1");
    var page2 = $("#page-2");
    var page3 = $("#page-3");
    var page4 = $("#page-4");
    updatePage(currentPage);

    function updatePage(currentPage){
        switch(currentPage){
            case 1:
                page1.show();
                page2.hide();
                page3.hide();
                page4.hide();
                break;
            case 2:
                page1.hide();
                page2.show();
                page3.hide();
                page4.hide();
                break;
            case 3:
                page1.hide();
                page2.hide();
                page3.show();
                page4.hide();
                break;
            case 4:
                page1.hide();
                page2.hide();
                page3.hide();
                page4.show();
                break;
            default:
                page1.show();
                page2.hide();
                page3.hide();
                page4.hide();
        }
    }

    function validatePage1(){
        var username = $("#username");
        var contactNumber = $("#contactNumber");
        var email = $("#email");
        var companyName = $("#companyName");
        var errors = [];

        if(username.val().trim() == "" || contactNumber.val().trim() == "" || email.val().trim() == "" || companyName.val().trim() == ""){
            alert("Fields should not be empty");
            return false;
        }

        if($.isNumeric(contactNumber.val())){
            $("#contactNumber-error").text("");
        }
        else{
            $("#contactNumber-error").text("invalid phone number");
            errors.push("contactNumber");
        }

        if(validateEmail(email.val())){
            $("#email-error").text("");
        }
        else{
            $("#email-error").text("invalid email");
            errors.push("email");
        }

        if(errors.length == 0){
            return true;
        }
        else{
            return false;
        }
    }

    function validatePage2(){
        var distancingHardToImplementArea = $("#distancingHardToImplementArea");
        var errors = [];
        if(distancingHardToImplementArea.val().trim() == ""){
            $("#distancingHardToImplement-error").text("This answer is required and should not be blank");
            errors.push("distancingHardToImplement");
        }
        else{
            $("#distancingHardToImplement-error").text("");
        }

        if(errors.length == 0){
            return true;
        }
        else{
            return false;
        }
    }

    function validatePage3(){
        var actionTakenForCovid = $("#actionTakenForCOVID");
        var errors = [];
        if(actionTakenForCovid.val().trim() == ""){
            $("actionTakenForCovid-error").text("This answer is required and should not be blank");
            errors.push("actionTakenForCovid");
        }
        else{
            $("actionTakenForCovid-error").text("");
        }

        if(errors.length == 0){
            return true;
        }
        else{
            return false;
        }

    }

    function validateEmail(email){
        var EmailRegex = new RegExp('[a-z0-9]+@[a-z]+\.[a-z]{2,3}');
        return EmailRegex.test(email);
    }

    $("#goto-page2").click(() => {
        if(validatePage1()){
            currentPage++;
            updatePage(currentPage);
        }
        else{
            currentPage = 1;
            updatePage(currentPage);
        }
    });

    $("#goto-page3").click(() => {
        if(validatePage2()){
            currentPage++;
            updatePage(currentPage);
        }
        else{
            currentPage = 2;
            updatePage(currentPage);
        }
    });

    $("#goto-page4").click(() => {
        if(validatePage3()){
            currentPage++;
            updatePage(currentPage);
        }
        else{
            currentPage = 3;
            updatePage(currentPage);
        }
    });

    $(".previous-page").click(() => {
        currentPage--;
        updatePage(currentPage);
    });
});
