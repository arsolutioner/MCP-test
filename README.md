# MCP-Test Project: Port Scanner

## Overview
A simple Python port scanner that can scan a target host for open ports.

## Features
- Concurrent port scanning
- Customizable port range
- Supports hostname and IP address inputs

## Running the Application

### Local Python
```bash
# Basic usage (scans default target with default port range)
python app.py

# Scan a specific target
python app.py example.com

# Scan a specific target with custom port range
python app.py example.com 1 100
```

### Docker
```bash
# Build the Docker image
docker build -t mcp-test .

# Run the Docker container with default scan
docker run mcp-test

# Run with custom arguments (example)
docker run mcp-test python app.py scanme.nmap.org 1 500
```

## Usage Notes
- Default target: scanme.nmap.org
- Default port range: 1-1024
- Scan parameters: [target] [start_port] [end_port]

## Disclaimer
This tool is for educational purposes only. Always ensure you have permission 
before scanning networks or systems you do not own.
