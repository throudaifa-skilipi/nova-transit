
from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>NOVA TRANSIT | Luxury Transportation</title>

<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    font-family: 'Montserrat', sans-serif;
    background: #090909;
    color: white;
}

header {
    height: 85px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 8%;
    background: #080808;
    border-bottom: 1px solid #252525;
}

.logo {
    font-size: 25px;
    font-weight: 800;
    color: #d6ad60;
    letter-spacing: 2px;
}

nav a {
    color: white;
    text-decoration: none;
    margin-left: 25px;
    font-size: 13px;
    transition: .3s;
}

nav a:hover {
    color: #d6ad60;
}

.hero {
    min-height: 650px;
    display: flex;
    align-items: center;
    padding: 80px 10%;
    background:
    linear-gradient(90deg, #080808 5%, rgba(0,0,0,.7), transparent),
    url('https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=1800') center/cover;
}

.hero-content {
    max-width: 650px;
}

.tag {
    color: #d6ad60;
    letter-spacing: 4px;
    font-size: 12px;
    font-weight: bold;
}

h1 {
    font-size: clamp(40px, 6vw, 70px);
    line-height: 1.15;
    margin: 25px 0;
}

h1 span {
    color: #d6ad60;
}

.hero p {
    color: #ccc;
    line-height: 1.9;
    max-width: 500px;
}

.btn {
    display: inline-block;
    margin-top: 30px;
    padding: 16px 30px;
    background: #d6ad60;
    color: black;
    text-decoration: none;
    font-weight: bold;
    border-radius: 3px;
    transition: .3s;
}

.btn:hover {
    background: white;
    transform: translateY(-3px);
}

section {
    padding: 90px 9%;
}

.section-title {
    text-align: center;
    margin-bottom: 55px;
}

.section-title h2 {
    font-size: 36px;
    margin-bottom: 15px;
}

.section-title span {
    color: #d6ad60;
}

.section-title p {
    color: #aaa;
    font-size: 14px;
}

.services {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 25px;
}

.card {
    background: #151515;
    border: 1px solid #292929;
    padding-bottom: 25px;
    transition: .3s;
}

.card:hover {
    transform: translateY(-8px);
    border-color: #d6ad60;
}

.card img {
    width: 100%;
    height: 190px;
    object-fit: cover;
}

.card h3 {
    padding: 20px 20px 10px;
    color: #d6ad60;
}

.card p {
    padding: 0 20px;
    color: #aaa;
    font-size: 13px;
    line-height: 1.8;
}

.about {
    background: #121212;
    text-align: center;
}

.about p {
    max-width: 750px;
    margin: auto;
    color: #bbb;
    line-height: 2;
}

.booking {
    background: #0d0d0d;
}

form {
    max-width: 650px;
    margin: auto;
    display: grid;
    gap: 18px;
}

input, select {
    padding: 17px;
    background: #1a1a1a;
    border: 1px solid #333;
    color: white;
    width: 100%;
    border-radius: 4px;
}

button {
    background: #d6ad60;
    border: none;
    padding: 17px;
    font-weight: bold;
    cursor: pointer;
}

footer {
    padding: 35px;
    text-align: center;
    background: black;
    color: #888;
    font-size: 12px;
}

footer span {
    color: #d6ad60;
}

@media(max-width: 700px) {
    header {
        height: auto;
        padding: 22px 5%;
        flex-direction: column;
        gap: 20px;
    }

    nav a {
        margin: 0 7px;
        font-size: 11px;
    }

    .hero {
        min-height: 550px;
        padding: 50px 7%;
    }

    section {
        padding: 65px 6%;
    }
}
</style>
</head>

<body>

<header>
    <div class="logo">NOVA TRANSIT</div>

    <nav>
        <a href="#home">Accueil</a>
        <a href="#services">Services</a>
        <a href="#about">À propos</a>
        <a href="#booking">Réservation</a>
    </nav>
</header>

<div class="hero" id="home">
    <div class="hero-content">

        <div class="tag">PREMIUM TRANSPORTATION</div>

        <h1>
            Travel Beyond<br>
            <span>Expectations.</span>
        </h1>

        <p>
            Découvrez une nouvelle expérience de transport.
            Confort, élégance et professionnalisme
            pour tous vos déplacements.
        </p>

        <a href="#booking" class="btn">
            RÉSERVER MAINTENANT →
        </a>

    </div>
</div>

<section id="services">

    <div class="section-title">
        <h2>Nos <span>Services</span></h2>
        <p>Des solutions de transport adaptées à vos besoins.</p>
    </div>

    <div class="services">

        <div class="card">
            <img src="https://images.unsplash.com/photo-1563720223185-11003d516935?w=800">
            <h3>Transport VIP</h3>
            <p>Voyagez dans des véhicules premium avec chauffeur professionnel.</p>
        </div>

        <div class="card">
            <img src="https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=800">
            <h3>Transport touristique</h3>
            <p>Découvrez les destinations avec confort et tranquillité.</p>
        </div>

        <div class="card">
            <img src="https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=800">
            <h3>Transfert aéroport</h3>
            <p>Des transferts fiables entre les aéroports et vos destinations.</p>
        </div>

        <div class="card">
            <img src="https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800">
            <h3>Transport privé</h3>
            <p>Des déplacements personnalisés pour particuliers et entreprises.</p>
        </div>

    </div>
</section>

<section class="about" id="about">

    <div class="section-title">
        <h2>Pourquoi choisir <span>NOVA TRANSIT ?</span></h2>
    </div>

    <p>
        NOVA TRANSIT est une marque de transport premium
        dédiée à offrir une expérience de voyage exceptionnelle.
        Notre vision repose sur la qualité, la ponctualité,
        la sécurité et le confort de nos passagers.
    </p>

</section>

<section class="booking" id="booking">

    <div class="section-title">
        <h2>Réservez votre <span>Voyage</span></h2>
        <p>Envoyez votre demande de réservation.</p>
    </div>

    <form onsubmit="sendBooking(event)">

        <input id="name" type="text"
        placeholder="Votre nom complet" required>

        <input id="email" type="email"
        placeholder="Votre adresse email" required>

        <input id="departure" type="text"
        placeholder="Ville de départ" required>

        <input id="destination" type="text"
        placeholder="Destination" required>

        <select id="service">
            <option>Transport VIP</option>
            <option>Transport touristique</option>
            <option>Transfert aéroport</option>
            <option>Transport privé</option>
        </select>

        <input id="date" type="date" required>

        <button type="submit">
            ENVOYER MA DEMANDE
        </button>

    </form>

</section>

<footer>
    © 2026 <span>NOVA TRANSIT</span>.
    Tous droits réservés.
    Premium Travel Experience.
</footer>

<script>
function sendBooking(event) {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const departure = document.getElementById("departure").value;
    const destination = document.getElementById("destination").value;
    const service = document.getElementById("service").value;
    const date = document.getElementById("date").value;

    const message =
    "Bonjour NOVA TRANSIT !%0A" +
    "Nom : " + encodeURIComponent(name) + "%0A" +
    "Départ : " + encodeURIComponent(departure) + "%0A" +
    "Destination : " + encodeURIComponent(destination) + "%0A" +
    "Service : " + encodeURIComponent(service) + "%0A" +
    "Date : " + encodeURIComponent(date);

    alert("Votre demande est prête. Le système de réservation WhatsApp doit encore être connecté.");
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
