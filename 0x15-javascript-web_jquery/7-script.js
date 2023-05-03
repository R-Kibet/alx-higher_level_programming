$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", (data, result) => {
  if (result === "success") {
    $("DIV#character").text(data.name);
  }
  });
