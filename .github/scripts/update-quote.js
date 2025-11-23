const fs = require('fs');
const path = require('path');
const fetch = require('node-fetch'); // You need to use node-fetch or similar in your Action environment.

const endpoint = 'https://gist.githubusercontent.com/camperbot/5a022b72e96c4c9585c32bf6a75f62d9/raw/e3c6895ce42069f0ee7e991229064f167fe8ccdc/quotes.json';

async function generateQuoteBox() {
    try {
        const res = await fetch(endpoint);
        const data = await res.json();
        const quotes = data.quotes;
        
        const { quote, author } = quotes[Math.floor(Math.random() * quotes.length)];
        const formattedAuthor = author || 'Unknown';

        // Static HTML structure for the quote box
        const quoteHtml = `
<div align="center">
<blockquote style="max-width:700px; margin:30px auto; padding:40px; background:linear-gradient(135deg,#667eea,#764ba2); border-radius:16px; color:white; font-family:Georgia,serif; box-shadow:0 10px 30px rgba(0,0,0,0.3); position:relative;">
  <p style="font-size:1.8rem; margin:0 0 20px; line-height:1.5; font-style:italic; position:relative">
    <span style="font-size:5rem; opacity:0.15; position:absolute; left:-15px; top:-30px">“</span>
    ${quote}
  </p>
  <footer style="text-align:right; font-size:1.3rem; font-weight:bold">— ${formattedAuthor}</footer>
</blockquote>
</div>
`;
        return quoteHtml;

    } catch (e) {
        console.error("Failed to fetch quote:", e);
        // Return a default quote if fetching fails
        return `
<div align="center">
<blockquote style="max-width:700px; margin:30px auto; padding:40px; background:linear-gradient(135deg,#667eea,#764ba2); border-radius:16px; color:white; font-family:Georgia,serif; box-shadow:0 10px 30px rgba(0,0,0,0.3); position:relative;">
  <p style="font-size:1.8rem; margin:0 0 20px; line-height:1.5; font-style:italic; position:relative">
    <span style="font-size:5rem; opacity:0.15; position:absolute; left:-15px; top:-30px">“</span>
    The universe doesn't allow perfection.
  </p>
  <footer style="text-align:right; font-size:1.3rem; font-weight:bold">— Stephen Hawking</footer>
</blockquote>
</div>
`;
    }
}

async function updateReadme() {
    const readmePath = path.join(process.cwd(), 'README.md');
    let readmeContent = fs.readFileSync(readmePath, 'utf8');

    const quoteBox = await generateQuoteBox();

    // Regex to find and replace the content between the markers
    const regex = /[\s\S]*/;

    if (readmeContent.match(regex)) {
        readmeContent = readmeContent.replace(regex, quoteBox.trim());
        fs.writeFileSync(readmePath, readmeContent);
        console.log("README updated with a new quote!");
    } else {
        console.error("Could not find RANDOM_QUOTE_START/END markers in README.md");
    }
}

updateReadme();
