# Running the server

Install uv (if not already installed)

Windows:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Start the virtual environment:
```bash
.\.venv\Scripts\activate
```

Sync dependencies:
```bash
uv sync
```

Start the server:
```bash
fastapi dev main.py
```