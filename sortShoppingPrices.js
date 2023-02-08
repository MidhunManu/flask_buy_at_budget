const fs = require("fs")

fs.readFile("scrape.json", "utf-8", (err, data) => {
  if(err) {
    console.log(err);
    return;
  }

  const jsonData = JSON.parse(data);
  console.log("look here ....")

  jsonData.sort((a, b) => a.price - b.price);


  console.log(jsonData);

  fs.writeFileSync("scrape.json", JSON.stringify(jsonData));

})

