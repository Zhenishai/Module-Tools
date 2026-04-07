const fs = require("fs");//fs is a toolbox from node

const args = process.argv.slice(2);

const showNumbers = args.includes("-n");
const showNonEmptyNumbers = args.includes("-b");

const files = args.filter(arg => arg !== "-n" && arg !== "-b");

files.forEach(file => {
  const content = fs.readFileSync(file, "utf-8");
  const lines = content.split("\n");

  let count = 1;

  lines.forEach((line, index) => {
    if (showNonEmptyNumbers) {
      if (line.trim() !== "") {
        console.log(`${count++} ${line}`);
      } else {
        console.log(line);
      }
    } else if (showNumbers) {
      console.log(`${index + 1} ${line}`);
    } else {
      console.log(line);
    }
  });
});