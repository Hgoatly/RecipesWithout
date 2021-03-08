  $(document).ready(function(){
    
    // code copied from materialize
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('#method').val();
    $('select').formSelect();
    $('.slider').slider({full_width: true});
    $('.modal').modal();
    $('.collapsible').collapsible();
    // end of copied code
   
    //setTimout method removes flashed messages after 10 seconds.
    setTimeout(function() {
    $('.flash-messages').remove();
    }, 10000); 
    
    // code copied from CI 'Task Manager' mini project
    // custom code for Materialize select dropdown element
     validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
  });

// scroll to top button for all pages. To be found on 'base.html' template.

//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction();};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


document.getElementById("advanced-search-box").style.display = "none";
document.getElementById("show-advanced-search").addEventListener("click", function() {
document.getElementById("search-box").style.display = "none";
document.getElementById("show-advanced-search").style.display = "none";
document.getElementById("show-basic-search").style.display = "inline";
document.getElementById("advanced-search-box").style.display = "inline";

});  

document.getElementById("show-basic-search").style.display = "none";
document.getElementById("show-basic-search").addEventListener("click", function() {
document.getElementById("search-box").style.display = "inline";
document.getElementById("show-advanced-search").style.display = "inline";
document.getElementById("show-basic-search").style.display = "none";
document.getElementById("advanced-search-box").style.display = "none";

});