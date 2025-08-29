# Project Overview
MCP Inspector Server - A comprehensive MCP server testing and validation system that wraps the official MCP Inspector CLI functionality as MCP tools for programmatic inspection and debugging of other MCP servers.

This is an MCP (Model Context Protocol) server built with mcp-factory. It provides tools, resources, and prompts accessible via the MCP protocol.

## Server Configuration
**Claude Desktop Configuration (`claude_desktop_config.json`):**
```json
{
  "mcpServers": {
    "mcp-inspector-server": {
      "command": "uv",
      "args": ["run", "python", "server.py"],
      "cwd": "/path/to/mcp-inspector-server"
    }
  }
}
```

**Direct Connection:**
```bash
# Navigate to project directory first
cd /path/to/mcp-inspector-server
uv run python server.py
```

> **Note**: For alternative configuration methods (different environments, authentication, etc.), 
> see the [MCP Configuration Guide](https://github.com/modelcontextprotocol/docs) or consult 
> your MCP client documentation.

## Build and Test Commands
```bash
# Install dependencies
uv sync

# Run the server (always from mcp-factory root)
cd /path/to/mcp-factory
uv run python workspace/projects/mcp-inspector-server/server.py

# Test the server using mcp-inspector-server tools (self-testing)
# Call inspect_mcp_server with server_command parameter
# Call comprehensive_server_test for full validation
# Use call_mcp_tool to test individual inspection functions
```

## Code Style Guidelines
- Use `uv run ruff format .` to format code (from project directory)
- Run `uv run ruff check .` before committing
- Use type hints: functions return `dict[str, Any]` for tools
- Add docstrings to all functions (required for MCP registration)
- Use direct function parameters, not Pydantic models

## Testing Instructions
- Use mcp-inspector-server tools for all testing (including self-testing)
- Call `inspect_mcp_server` to verify server connectivity
- Use `comprehensive_server_test` for complete validation
- Test individual tools with `call_mcp_tool`
- Run `uv run ruff check .` to catch linting issues
- Always verify server starts from mcp-factory root directory

## Security Considerations
- Validate all input parameters in tools
- Be cautious with file system access in tools
- Don't expose sensitive data through resources
- Use appropriate error handling to avoid information leakage

## Component Management
This project supports dynamic component discovery and registration:

**Adding Components:**
- Tools: Create `.py` files in `tools/` directory with functions decorated with `@tool`
- Resources: Create `.py` files in `resources/` directory with functions decorated with `@resource`
- Prompts: Create `.py` files in `prompts/` directory with functions decorated with `@prompt`

**Component Discovery:**
- Components are automatically discovered and registered in `config.yaml`
- Use descriptive function names and comprehensive docstrings
- Ensure all parameters are JSON-serializable for MCP compatibility

## MCP Inspector Capabilities
This server provides programmatic access to MCP Inspector functionality:

**Core Inspection Tools:**
- `inspect_mcp_server`: Connect to and inspect any MCP server
- `call_mcp_tool`: Execute tools on target MCP servers with parameter validation
- `comprehensive_server_test`: Perform complete server validation and testing

**Testing and Validation:**
- JSON Schema validation for tool parameters
- Server connectivity and capability discovery
- Error handling and diagnostic reporting
- Performance and compatibility testing

**Integration Benefits:**
- Programmatic MCP server testing for AI agents
- Automated validation in development workflows
- Standardized testing protocols across MCP projects
- Integration with mcp-factory development lifecycle

## Development Notes
- **Path requirements**: Always run server from mcp-factory root directory
- **Schema requirements**: Use `dict[str, Any]` returns, ensure JSON-serializable parameters
- **Component discovery**: Components are automatically found and registered in `config.yaml`
- **MCP Inspector CLI**: Wraps `npx @modelcontextprotocol/inspector` functionality
- **Self-testing**: Can test itself using its own inspection tools
