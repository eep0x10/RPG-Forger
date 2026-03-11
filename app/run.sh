#!/bin/bash
# Inicia o servidor Flask de Feiticeiros & Maldições
cd "$(dirname "$0")"
echo "==================================================="
echo "  Feiticeiros & Maldições – Criador de Fichas"
echo "==================================================="
echo ""
echo "  Acesse: http://localhost:5000"
echo ""
echo "  Ctrl+C para parar o servidor"
echo "==================================================="
python3 app.py
