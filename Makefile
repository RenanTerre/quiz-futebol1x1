.PHONY: setup run tunnel tunnel-lhr tunnel-serveo dev dev-lhr dev-serveo stop help

# Alvo para configurar o ambiente (Criar venv e instalar dependências)
setup:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

# Inicia o servidor usando a venv
run:
	./venv/bin/python3 main.py

# Tunel via localhost.run (URL aleatória gerada automaticamente)
tunnel-lhr:
	ssh -R 80:localhost:8888 nokey@localhost.run -o StrictHostKeyChecking=no

# Tunel via serveo.net (subdomínio fixo: https://velhia.serveo.net)
tunnel-serveo:
	ssh -R velhia:80:localhost:8888 serveo.net -o StrictHostKeyChecking=no

# Atalho padrão → serveo (subdomínio fixo)
tunnel: tunnel-serveo

# Servidor + serveo.net (padrão)
dev: dev-serveo

# Servidor + localhost.run
dev-lhr:
	$(MAKE) run &
	$(MAKE) tunnel-lhr

# Servidor + serveo.net
dev-serveo:
	$(MAKE) run &
	$(MAKE) tunnel-serveo

# Encerra processos do servidor e túneis
stop:
	@lsof -ti :8888 | xargs kill -9 2>/dev/null && echo "Servidor encerrado." || echo "Nenhum servidor rodando."
	@pkill -f "ssh.*serveo.net" 2>/dev/null && echo "Túnel serveo.net encerrado." || echo "Nenhum túnel serveo.net ativo."
	@pkill -f "ssh.*localhost.run" 2>/dev/null && echo "Túnel localhost.run encerrado." || echo "Nenhum túnel localhost.run ativo."

# Lista os comandos disponíveis
help:
	@echo ""
	@echo "  Comandos:"
	@echo "  make setup         - Configura ambiente virtual"
	@echo "  make run           - Inicia servidor"
	@echo "  make tunnel-lhr    - Tunel via localhost.run (URL aleatória)"
	@echo "  make tunnel-serveo - Tunel via serveo.net (https://velhia.serveo.net)"
	@echo "  make tunnel        - Atalho para tunnel-serveo"
	@echo "  make dev-lhr       - Servidor + localhost.run"
	@echo "  make dev-serveo    - Servidor + serveo.net"
	@echo "  make dev           - Atalho para dev-serveo"
	@echo "  make stop          - Encerra tudo"
	@echo ""