from fasthtml.common import *

# Define global style to center content and style the progress bar
style = Style("""
body {
    min-height: 100vh;
    margin: 0;
    background-color: #1A1A1E;
    display: grid;
    place-items: center; /* Center everything */
    font-family: Arial, sans-serif;
    color: white;
    text-align: center;
}

.progress-bar {
    height: 20px;
    background-color: #444;
    margin-top: 20px;
    width: 100%;
    position: relative;
}

.progress {
    height: 100%;
    background-color: #00ff00;
    width: 0%;
    transition: width 0.9s linear; /* Smooth transition for the bar */
}

.quote {
    font-size: 1rem;
    margin-bottom: 20px;
}

""")

# Headers to include Tailwind (if needed) or additional stylesheets
hdrs = (
    Script(src="https://cdn.tailwindcss.com"),
    style
)

# Initialize the FastHTML app
app, rt = fast_app(hdrs=(hdrs,))


# Home route
@rt('/')
def get():
    return Div(
        Div(id="quote-box", cls="quote"),
        Div(
            Div(cls="progress", id="progress-bar"),
            cls="progress-bar"
        ),
        Script("""
        let quotes = [
                        "Reduza, reutilize e recicle: pequenos hábitos fazem grande diferença.",
                        "Plante árvores para ajudar a combater as mudanças climáticas.",
                        "Use transporte público, ande de bicicleta ou caminhe sempre que possível.",
                        "Economize água: feche a torneira enquanto escova os dentes.",
                        "Evite o desperdício de alimentos: planeje suas refeições com antecedência.",
                        "Use sacolas reutilizáveis em vez de plásticas descartáveis.",
                        "Escolha produtos de limpeza ecológicos e biodegradáveis.",
                        "Descarte o lixo eletrônico corretamente, levando-o a pontos de coleta especializados.",
                        "Desligue aparelhos eletrônicos quando não estiverem em uso para economizar energia.",
                        "Apoie empresas e marcas que adotam práticas sustentáveis."
                    ];


        let currentIndex = 0;
        let progress = 0;

        function updateQuote() {
            // Update the quote text
            const quoteBox = document.getElementById('quote-box');
            quoteBox.textContent = quotes[currentIndex];
            currentIndex = (currentIndex + 1) % quotes.length;

            // Reset progress
            progress = 0;
        }

        function updateProgressBar() {
            const progressBar = document.getElementById('progress-bar');
            progress += 10; // Increment progress by 10% (1 second = 10%)
            progressBar.style.width = progress + '%';

            // If progress reaches 100%, update the quote
            if (progress >= 100) {
                updateQuote();
                progress = 0;
            }
        }

        // Initialize the quote and start updating
        updateQuote();
        setInterval(updateProgressBar, 1000); // Update progress bar every second
        """)
    )

# Run the server
serve()
