let elem = $('DIV#add_item');
elem.click(() => {
  $("UL.my_list").append('<li>Item</li>');
});
