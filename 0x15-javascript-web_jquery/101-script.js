$('document').ready(function() {
    $("DIV#add_item").click(function() {
	$('UL.my_list').append($("<li></li>").text("Item"));
    });
    $("DIV#remove_item").click(function() {
	$('UL.my_list li:last').remove();
    });
    $("DIV#clear_list").click(function() {
	$('UL.my_list').empty();
    });
});

