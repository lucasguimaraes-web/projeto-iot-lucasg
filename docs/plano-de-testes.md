# Plano de testes — projeto-iot-lucasg

Cada caso registra como foi provocado, o resultado obtido e uma evidência
(print, log ou foto em [`evidencias/`](evidencias/)).

| # | Caso | Como provocar | Esperado | Resultado obtido | Evidência | OK? |
|---|------|---------------|----------|------------------|-----------|-----|
| 1 | Fluxo completo | Segurar o sensor por 1 min | Grafana muda em até ~10 s | | | ☐ |
| 2 | Umidade | Soprar perto do sensor | Umidade sobe | | | ☐ |
| 3 | Sensor desconectado | Soltar o fio de dados | Nada é publicado; "sem dados" em 30 s | | | ☐ |
| 4 | Wi-Fi cai | Desligar o roteador por 1 min | ESP reconecta sozinho | | | ☐ |
| 5 | Broker reiniciado | `docker compose restart` | ESP e coletor reconectam | | | ☐ |
| 6 | Acesso sem permissão | Sem usuário; publicar com `leitor-lucasg` | Recusado; publicação não chega | | | ☐ |
| 7 | Mensagem inválida | Publicar temperatura 900 | Coletor descarta com motivo | | | ☐ |
| 8 | VM reiniciada | Reiniciar a VM | Broker sobe sozinho; o resto volta | | | ☐ |
| 9 | Exatidão | Comparar com uma referência por 30 min | Diferença dentro do datasheet (±0,5 °C / ±2 %UR) | | | ☐ |

## Evidências por semana

| Semana | Prova pedida no manual | Evidência |
|--------|------------------------|-----------|
| 1 | Wi-Fi, MQTT, JSON periódico e Last Will provados separadamente; `mosquitto_sub` mostra o JSON a cada 10 s; fio solto não publica; ESP desligado gera `offline`; reinício do broker não exige mexer no ESP | |
| 2 | Conexão sem usuário recusada; `leitor-lucasg` não publica; mensagens inválidas descartadas com motivos diferentes; ESP e coletor voltam após `docker compose restart` | |
| 3 | `SELECT` das últimas leituras bate com o serial; inválidas não chegam ao banco; coletor sobrevive a reinício do MySQL | |
| 4 | `/docs` abre de outro computador; `horas=500` → 422; dispositivo inexistente → 404; `idade_s` cresce com o ESP desligado | |
| 5 | Grafana pede login e a senha padrão não funciona; mudança aparece em ~10 s; "sem dados" com ESP desligado; JSON importado num Grafana limpo aparece igual | |
