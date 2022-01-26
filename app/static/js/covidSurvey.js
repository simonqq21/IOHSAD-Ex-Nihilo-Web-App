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

    $(".next-page").click(() => {
        currentPage++;
        updatePage(currentPage);
    })

    $(".previous-page").click(() => {
        currentPage--;
        updatePage(currentPage);
    });
});