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

    /*$("#name").keyup(() =>{
        if($("#name").val().length < 0){
            $("#name-error").text("invalid name");
            $("#goto-page2").prop('disabled', true);
        }
        else{
            $("#name-error").text("valid name");
            $("#goto-page2").prop('disabled', false);
        }
    });

    $("#contactNo").keyup(() =>{
        if($.isNumeric($("#contactNo").val())){
            $("#contactNo-error").text("valid contact number");
            $("#goto-page2").prop('disabled', true);
        }
        else{
            $("#contactNo-error").text("invalid contact number");
            $("#goto-page2").prop('disabled', false);
        }
    });

    $("#email").keyup(() =>{
        if(validateEmail($(this).val())){
            $("#email-error").text("valid email");
            $("#goto-page2").prop('disabled', true);
        }
        else{
            $("#email-error").text("invalid email");
            $("#goto-page2").prop('disabled', false);
        }
    });*/

    function validatePage1(){
        var name = $("#name");
        var contactNo = $("#contactNo");
        var email = $("#email");
        var companyName = $("#companyName");
        var errors = {};

        if(name.val().trim() == "" || contactNo.val().trim() == "" || email.val().trim() == "" || companyName.val().trim() == ""){
            alert("Fields should not be empty");
            return false;
        }

        if(validateContactNo(contactNo.val())){
            $("#contactNo-error").text("");
        }
        else{
            $("#contactNo-error").text("invalid phone number");
            errors.push("contactNo");
        }

        if(validateEmail(email.val())){
            $("#email-error").text("");
        }
        else{
            $("#email-error").text("invalid email");
            errors.push("email");
        }

        if(errors.length() == 0){
            return true;
        }
        else{
            return false;
        }
    }

    function validateContactNo(contactNo){
        var phoneno = /^\d{11}$/;
        if(contactNo.value.match(phoneno)){
            return true;
        }
        else{
            return false;
        }
    }

    function validateEmail(email){
        var EmailRegex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
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

    $(".next-page").click(() => {
        currentPage++;
        updatePage(currentPage);
    })

    $(".previous-page").click(() => {
        currentPage--;
        updatePage(currentPage);
    });
});