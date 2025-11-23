## Hello, World! 🌒


<!-- Moon age: 0.3 days -->

![top](https://github.com/user-attachments/assets/c0ff87ae-14a3-4edd-a449-ee6e0e2f73f5)

<!-- quote-start -->
<div align="center">

> *before the throne of the almighty, man will be judged not by his acts but by his intentions. for god alone reads our hearts.*

</div>
<!-- quote-end -->


![bottom](https://github.com/user-attachments/assets/bf2cc040-2664-4cf3-8aaa-9d397c8a8f5c)

<div align="center">

<!-- Optional banner (remove or replace if you don’t want one) -->
<img src="https://raw.githubusercontent.com/mayhemantt/mayhemantt/main/Header.png" alt="Header" width="100%"/>

<br><br>

<!-- Random Quote Box -->
<blockquote id="quote-box" style="max-width:700px; margin:30px auto; padding:40px; background:linear-gradient(135deg,#667eea,#764ba2); border-radius:16px; color:white; font-family:Georgia,serif; box-shadow:0 10px 30px rgba(0,0,0,0.3); position:relative; transition:opacity .4s">
  <p id="text" style="font-size:1.8rem; margin:0 0 20px; line-height:1.5; font-style:italic; position:relative">
    <span style="font-size:5rem; opacity:0.15; position:absolute; left:-15px; top:-30px">“</span>
    Loading an inspiring quote...
  </p>
  <footer id="author" style="text-align:right; font-size:1.3rem; font-weight:bold">— freeCodeCamp style</footer>
</blockquote>

<button onclick="getQuote()" style="background:#fff; color:#667eea; border:none; padding:12px 30px; font-size:1rem; font-weight:bold; border-radius:50px; cursor:pointer; box-shadow:0 5px 15px rgba(0,0,0,0.2); transition:.3s">
  ✨ New Quote
</button>

<script>
// Same quote source freeCodeCamp uses in their official Random Quote Machine example
const endpoint = 'https://gist.githubusercontent.com/camperbot/5a022b72e96c4c9585c32bf6a75f62d9/raw/e3c6895ce42069f0ee7e991229064f167fe8ccdc/quotes.json';
let quotes = [];

async function getQuote() {
  document.getElementById('text').innerHTML = '<span style="font-size:5rem;opacity:0.15;position:absolute;left:-15px;top:-30px">“</span>Fetching wisdom...';
  document.getElementById('author').textContent = '';

  try {
    if (quotes.length === 0) {
      const res = await fetch(endpoint);
      const data = await res.json();
      quotes = data.quotes;
    }
    const { quote, author } = quotes[Math.floor(Math.random() * quotes.length)];

    const box = document.getElementById('quote-box');
    box.style.opacity = '0';
    setTimeout(() => {
      document.getElementById('text').innerHTML = `<span style="font-size:5rem;opacity:0.15;position:absolute;left:-15px;top:-30px">“</span>${quote}`;
      document.getElementById('author').textContent = `— ${author || 'Unknown'}`;
      box.style.opacity = '1';
    }, 350);

  } catch (e) {
    document.getElementById('text').innerHTML = '<span style="font-size:5rem;opacity:0.15;position:absolute;left:-15px;top:-30px">“</span>The universe doesn\'t allow perfection.';
    document.getElementById('author').textContent = '— Stephen Hawking';
  }
}

// Load quote as soon as the page renders
getQuote();
</script>

<br><br>
</div>
