"use strict";

$(document).ready(function () {

    $('.arrow').on("click", function (event) {
        parrent = $(this).parent()


        if ($(parrent).find('.links').css("none")) {

            $(parrent).find('.links').show("slow");

        } else {

            $(parrent).find('.links').slideDown();
        }
    });
});
