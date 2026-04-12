const fs = require("fs");
const path = require("path");

const args = process.argv.slice(2);

const showAll = args.includes("-a");
const onePerLine = args.includes("-1");

const paths = args.filter(arg => !arg.startsWith("-"));

const targetPath = paths[0] || ".";

fs.readdir(targetPath, (err, files) => {
  if (err) {
    console.error("Error:", err.message);
    process.exit(1);
  }

  let result = files;

  if (!showAll) {
    result = result.filter(file => !file.startsWith("."));
  }

  result.sort();

  if (onePerLine) {
    result.forEach(file => console.log(file));
  } else {
    console.log(result.join(" "));
  }
});