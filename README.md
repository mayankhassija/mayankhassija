## Hello, World! 🌒


<!-- Moon age: 0.3 days -->

![top](https://github.com/user-attachments/assets/c0ff87ae-14a3-4edd-a449-ee6e0e2f73f5)

<!-- quote-start -->
<div align="center">

> *before the throne of the almighty, man will be judged not by his acts but by his intentions. for god alone reads our hearts.*

</div>
<!-- quote-end -->


![bottom](https://github.com/user-attachments/assets/bf2cc040-2664-4cf3-8aaa-9d397c8a8f5c)

<!-- Random Quote Header -->

<div align="center">

<img src="https://raw.githubusercontent.com/mayhemantt/mayhemantt/main/Header.png" alt="Header" width="100%"/>

<br><br>

<blockquote id="quote-box" style="
    max-width: 700px;
    margin: 30px auto;
    padding: 30px 40px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 16px;
    color: white;
    font-family: 'Georgia', serif;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    transition: all 0.4s ease;
">
  <p id="text" style="
    font-size: 1.75rem;
    margin: 0 0 20px 0;
    line-height: 1.5;
    font-style: italic;
    position: relative;
  ">
    <span style="font-size: 4rem; opacity: 0.2; position: absolute; left: -20px; top: -20px;">“</span>
    Loading an inspiring quote...
  </p>
  <footer id="author" style="
    text-align: right;
    font-size: 1.3rem;
    font-weight: bold;
    margin-top: 15px;
  ">— freeCodeCamp style</footer>
</blockquote>

<button onclick="getQuote()" style="
    background: #fff;
    color: #667eea;
    border: none;
    padding: 12px 28px;
    font-size: 1rem;
    font-weight: bold;
    border-radius: 50px;
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    transition: all 0.3s;
">
  New Quote
</button>

<script>
// Quote API (same one used in freeCodeCamp's official example)
const quoteEndpoint = 'https://gist.githubusercontent.com/camperbot/5a022b72e96c4c9585c32bf6a75f62d9/raw/e3c6895ce42069f0ee7e991229064f167fe8ccdc/quotes.json';

let quotesData = [];

async function getQuote() {
  // Show loading state
  document.getElementById('text').innerHTML = 'Fetching wisdom...';
  document.getElementById('author').textContent = '';

  try {
    if (quotesData.length === 0) {
      const response = await fetch(quoteEndpoint);
      const data = await response.json();
      quotesData = data.quotes;
    }

    const randomIndex = Math.floor(Math.random() * quotesData.length);
    const { quote, author } = quotesData[randomIndex];

    // Beautiful fade-in effect
    const quoteBox = document.getElementById('quote-box');
    quoteBox.style.opacity = '0';
    
    setTimeout(() => {
      document.getElementById('text').innerHTML = 
        `<span style="font-size:4rem;opacity:0.2;position:absolute;left:-20px;top:-20px;">“</span>${quote}`;
      document.getElementById('author').textContent = `— ${author || 'Unknown'}`;
      quoteBox.style.opacity = '1';
    }, 300);

  } catch (err) {
    document.getElementById('text').textContent = 
      'The universe doesn\'t allow perfection.';
    document.getElementById('author').textContent = '— Stephen Hawking';
  }
}

// Load a quote immediately when the page loads
getQuote();
</script>

<br><br>

</div>
