const URL = 'https://www.fourtonfish.com/hellosalut/hello/';

function Hello (lang) {
  $.get(`${URL}?lang=${lang}`, (data, result) => {
    if (result === 'success' && lang) {
      $('DIV#hello').text(data.hello);
    }
  });
}

$(document).ready(function () {
  $('#btn_translate').click(() => {
    const lang = $('#language_code').val();
    Hello(lang);
  });
});
