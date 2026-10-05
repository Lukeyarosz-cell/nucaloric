# Local development
No build step is needed for this static website.

```bash
cd /home/luke/Projects/nucaloric-site
python3 -m http.server 3000 --bind 127.0.0.1
```

Open http://127.0.0.1:3000/. In VS Code use Ctrl+Shift+P → Live Preview: Show Preview (Internal Browser). Microsoft Live Preview (`ms-vscode.live-server`) and GitHub Pull Requests (`github.vscode-pull-request-github`) are installed.

```bash
node --check app.js
```

Saved browser evidence is in `Evidence/`; the audit runner uses Playwright and Brave and expects port 3000. Its selectors need correction before claiming comprehensive interaction passes.

The current session cannot bind the server socket or launch Brave/Obsidian. Run the preview in a normal desktop terminal. The project was sent to the VS Code CLI, but visible UI state cannot be verified here.
