const $ = window.$;
$.get("https://fourtonfish.com/hellosalut/?lang=fr", (data, result) => {
  if (result === "success") {
    $("DIV#hello").text(data.hello);
  }
});
