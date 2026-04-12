const fs = require("fs");

const args = process.argv.slice(2);

const showLines = args.includes("-l");
const showWords = args.includes("-w");
const showBytes = args.includes("-c");

const files = args.filter(arg => !arg.startsWith("-"));

const noFlags = !showLines && !showWords && !showBytes;

function count(content) {
  const lines = content.split("\n").length - 1;
  const words = content.trim().split(/\s+/).filter(Boolean).length;
  const bytes = Buffer.byteLength(content, "utf8");

  return { lines, words, bytes };
}

let total = { lines: 0, words: 0, bytes: 0 };

files.forEach((file) => {
  try {
    const content = fs.readFileSync(file, "utf8");
    const { lines, words, bytes } = count(content);

    total.lines += lines;
    total.words += words;
    total.bytes += bytes;

    let output = "";

    if (noFlags || showLines) output += lines + " ";
    if (noFlags || showWords) output += words + " ";
    if (noFlags || showBytes) output += bytes + " ";

    console.log(output.trim(), file);
  } catch (err) {
    console.error(`wc: ${file}: ${err.message}`);
  }
});
if (files.length > 1) {
  let output = "";

  if (noFlags || showLines) output += total.lines + " ";
  if (noFlags || showWords) output += total.words + " ";
  if (noFlags || showBytes) output += total.bytes + " ";

  console.log(output.trim(), "total");
}