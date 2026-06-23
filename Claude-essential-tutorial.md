#### Example of Coding Agent
- Anthropic Claude Code
- OpenAI Codex
- Amazon Kiro
- OpenCode

#### Code Harness
- Code Harness or Agent Harness: surrounding program or infrastructure that turns an LLM
	into a coding agent including engineered prompts, tools, sandboxes and more
	
	- Example of Code Harnesses (agentic coding tool)
		- Claude Code
		- Cursor
		- OpenAI Codex
		- AutoGPT
		- LnagChain
		- Sweep
		- Cline
		- Continue
		- Aider

	- Claude Code (Use case):
		- Automate the work you keep putting off
		- Build features and fix bugs
		- Create commits / PR 
		- Connect your tool with MCP
		- Customize with instructions, skills, and hooks
		- Run agent teams and build custom agents
		- Pipe script and automate with CLI
		- Work from any where

	- Agentic Loop
		- prompt - (model) - Invoke claude code ask them to do something, that is going to start the loop
		- You can interrupt, steer or add context to correct agent
		- loop through 3 steps till it achieve its goal;
			- Gather context
			- Take action
			- Verify results

		- Agentic Loop - Tool Calls: Tools are *Code function* that agent is aware of and invoke to complete thier tasks
		- Agentic Loop - Models: 
				- default
				- sonnet: daily coding task; well balanced
				- sonnet[1m]: long session 1 million token
				- opus: complex reasoning; really slow; really smart
				- opusplan: Use opus during plan mode then switch to sonnet for execution
				- haiku: Use for simple tasks; really fast; really dumb

		- Claude Modes:
			- Normal mode: claude code will execute only stop to ask permission; might give sum info but won't generate large plan
			- Plan mode: claude code will create a plan; generate document to review; you can chose to accept and execute it or keep asking it to revisions

		- Resources:
			- https://anthropic.skilljar.com
			- htpps://claude.ai

		- Installing Claude code - Linux | Mac
			- $ curl -fsSL https://claude.ai/install.sh | bash
			- $ irm https://claude.ai/install.ps1 | iex

		- Commands
			- $ claude auth login (not recommanded)
			- $ /login (launch claude)
			- $ doctor
			- $ claude auth status
			- $ claude (launch from project folder)
			- $ claude doctor
			- $ claude --help (check for system env path variable if not working)

	