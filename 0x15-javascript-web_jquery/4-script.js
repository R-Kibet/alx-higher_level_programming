let elem = $('DIV#toggle_header');
elem.click(() => {
  $("header").toggleClass('red green');
});
