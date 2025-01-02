const http = require('http');
const url = require('url');

// Vulnérabilité : Eval
function executeCode(userInput) {
    eval(userInput); // Mauvaise pratique : exécution de code non sécurisé
}

// Vulnérabilité : Mauvaise configuration du serveur
const server = http.createServer((req, res) => {
    const queryObject = url.parse(req.url, true).query;

    if (queryObject.code) {
        executeCode(queryObject.code); // Exemple : accès avec ?code=console.log('Hello')
    }

    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Server is running');
});

server.listen(3000, () => {
    console.log('Server is listening on port 3000');
});
