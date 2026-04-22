let ws;
let selected = null;
let correctAnswer = null;

// pega sala da URL
const params = new URLSearchParams(window.location.search);
let sala = params.get("sala");

function conectar(room_id) {
    const protocol = location.protocol === "https:" ? "wss" : "ws";

    ws = new WebSocket(`${protocol}://${location.host}/ws?sala=${room_id}`);

    ws.onopen = () => {
    console.log("Conectado na sala:", room_id);

    ws.send(JSON.stringify({
        action: "join"
    }));
};

    ws.onmessage = (e) => {
        const msg = JSON.parse(e.data);
        console.log(msg);

        if (msg.type === "waiting") {
            document.getElementById("question").innerText = ' Aguardando outro jogador...';
        }

        if (msg.type === "start" || msg.type === "next_question") {
            render(msg.state);
        }

        if (msg.type === "update_score") {
            document.getElementById("score").innerText =
                `Placar: ${msg.scores.p1} x ${msg.scores.p2}`;
        }

        if (msg.type === "winner") {
            showWinner(msg.winner, msg.scores);
        }
    };
}

// se NÃO tem sala → cria
if (!sala) {
    fetch("/api/create-room")
    .then(r => r.json())
    .then(data => {
        window.location.href = `/?sala=${data.room_id}`;
    });
} else {
    conectar(sala);
}