#!/bin/bash

echo "================================"
echo "Growth Hacking Manager - Web App"
echo "================================"
echo ""
echo "Installing dependencies..."
pip3 install -q -r requirements.txt

echo ""
echo "Starting web server..."
echo ""
echo "🌐 Open your browser and go to:"
echo ""
echo "   http://localhost:5000"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

python3 web_app.py
