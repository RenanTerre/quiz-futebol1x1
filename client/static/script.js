let ws;

fetch("/api/create-room")
.then(r => r.json())
.then(data => {

    ws = new WebSocket(`ws://${window.location.host}/ws?sala=${data.room_id}`);

    ws.onopen = () => {
        console.log(" Conectado:", data.room_id);
        ws.send(JSON.stringify({ action: "next" }));
    };

    ws.onmessage = (e) => {
        const msg = JSON.parse(e.data);

        if (msg.type === "update") {
            renderizarPergunta(msg.state);
        }
        
        if (msg.type === "result") {
            console.log("Pontuação:", msg.total_score);
        }

        if (msg.type === "winner" || msg.type === "game_over") {
            console.log("Fim do jogo!");
            mostrarFim(msg.result || { acertos: msg.total });
        }
    };

    ws.onerror = () => {
        document.getElementById("question").innerText = "Erro na conexão 😬";
    };

    // troca tela
    document.getElementById("start-screen")?.classList.add("hidden");
    document.getElementById("game-screen")?.classList.remove("hidden");

});