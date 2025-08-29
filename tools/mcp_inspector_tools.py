"""
MCP Inspector Tools - Fixed Version
Professional MCP server testing and inspection tools with direct parameters (mcp-factory compatible)
"""

import json
import subprocess
from pathlib import Path
from typing import Any

__all__ = [
    "inspect_mcp_server",
    "call_mcp_tool",
    "read_mcp_resource",
    "get_mcp_prompt",
    "list_resource_templates",
    "set_logging_level",
    "comprehensive_server_test",
    "get_inspector_help",
    "create_inspector_config",
    "batch_inspect_servers",
    "inspect_with_config",
]


def _run_inspector_command(
    server_command: str,
    method: str,
    server_args: str | None = None,
    tool_arguments: str | None = None,
    timeout: int = 30,
) -> dict[str, Any]:
    """
    Run MCP Inspector command and return parsed results

    Args:
        server_command: Command to start the MCP server
        method: Inspector method to call
        server_args: Additional server arguments
        tool_arguments: Tool-specific arguments
        timeout: Command timeout in seconds

    Returns:
        Parsed JSON result from inspector
    """
    try:
        # Build the inspector command
        cmd_parts = ["npx", "@modelcontextprotocol/inspector", "--cli", server_command]

        if server_args:
            cmd_parts.extend(server_args.split())

        cmd_parts.extend(["--method", method])

        if tool_arguments:
            cmd_parts.extend(["--arguments", tool_arguments])

        # Execute the command
        result = subprocess.run(
            cmd_parts, capture_output=True, text=True, timeout=timeout, check=False
        )

        if result.returncode == 0:
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError:
                return {
                    "success": True,
                    "raw_output": result.stdout,
                    "stderr": result.stderr,
                }
        else:
            return {
                "success": False,
                "error": f"Command failed with exit code {result.returncode}",
                "stdout": result.stdout,
                "stderr": result.stderr,
            }

    except subprocess.TimeoutExpired:
        return {"success": False, "error": f"Command timed out after {timeout} seconds"}
    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {str(e)}"}


def inspect_mcp_server(
    server_command: str, server_args: str = None, timeout: int = 30
) -> dict[str, Any]:
    """
    Inspect an MCP server to discover its capabilities

    Args:
        server_command: Command to start the MCP server (e.g., 'python server.py')
        server_args: Additional arguments for the server command (optional)
        timeout: Timeout in seconds for the inspection (default: 30)

    Returns:
        Comprehensive information about the server including tools, resources, and prompts
    """
    return _run_inspector_command(
        server_command=server_command,
        method="tools/list",
        server_args=server_args,
        timeout=timeout,
    )


def call_mcp_tool(
    server_command: str,
    tool_name: str,
    tool_arguments: str = None,
    server_args: str = None,
    timeout: int = 30,
) -> dict[str, Any]:
    """
    Call a specific tool on an MCP server

    Args:
        server_command: Command to start the MCP server
        tool_name: Name of the tool to call
        tool_arguments: JSON string of tool arguments (optional)
        server_args: Additional server arguments (optional)
        timeout: Timeout in seconds (default: 30)

    Returns:
        Tool execution result
    """
    method = f"tools/call/{tool_name}"
    return _run_inspector_command(
        server_command=server_command,
        method=method,
        server_args=server_args,
        tool_arguments=tool_arguments,
        timeout=timeout,
    )


def read_mcp_resource(
    server_command: str, resource_uri: str, server_args: str = None, timeout: int = 30
) -> dict[str, Any]:
    """
    Read a resource from an MCP server

    Args:
        server_command: Command to start the MCP server
        resource_uri: URI of the resource to read
        server_args: Additional server arguments (optional)
        timeout: Timeout in seconds (default: 30)

    Returns:
        Resource content
    """
    method = f"resources/read/{resource_uri}"
    return _run_inspector_command(
        server_command=server_command,
        method=method,
        server_args=server_args,
        timeout=timeout,
    )


def get_mcp_prompt(
    server_command: str,
    prompt_name: str,
    prompt_arguments: str = None,
    server_args: str = None,
    timeout: int = 30,
) -> dict[str, Any]:
    """
    Get a prompt from an MCP server

    Args:
        server_command: Command to start the MCP server
        prompt_name: Name of the prompt to get
        prompt_arguments: JSON string of prompt arguments (optional)
        server_args: Additional server arguments (optional)
        timeout: Timeout in seconds (default: 30)

    Returns:
        Prompt content
    """
    method = f"prompts/get/{prompt_name}"
    return _run_inspector_command(
        server_command=server_command,
        method=method,
        server_args=server_args,
        tool_arguments=prompt_arguments,
        timeout=timeout,
    )


def list_resource_templates(
    server_command: str, server_args: str = None, timeout: int = 30
) -> dict[str, Any]:
    """
    List resource templates from an MCP server

    Args:
        server_command: Command to start the MCP server
        server_args: Additional server arguments (optional)
        timeout: Timeout in seconds (default: 30)

    Returns:
        Available resource templates and their schemas
    """
    return _run_inspector_command(
        server_command=server_command,
        method="resource_templates/list",
        server_args=server_args,
        timeout=timeout,
    )


def set_logging_level(level: str) -> dict[str, Any]:
    """
    Set logging level for inspector operations

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR)

    Returns:
        Operation result
    """
    import logging

    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
    }

    if level.upper() in level_map:
        logging.getLogger().setLevel(level_map[level.upper()])
        return {"success": True, "message": f"Logging level set to {level.upper()}"}
    else:
        return {
            "success": False,
            "error": f"Invalid logging level: {level}. Use DEBUG, INFO, WARNING, or ERROR",
        }


def comprehensive_server_test(
    server_command: str, server_args: str = None, timeout: int = 60
) -> dict[str, Any]:
    """
    Perform comprehensive testing of an MCP server

    Args:
        server_command: Command to start the MCP server
        server_args: Additional server arguments (optional)
        timeout: Timeout in seconds for comprehensive testing (default: 60)

    Returns:
        Detailed test results and summary
    """
    results = {"server_command": server_command, "test_results": {}, "summary": {}}

    try:
        # Test tools listing
        tools_result = _run_inspector_command(
            server_command, "tools/list", server_args, timeout=timeout
        )
        results["test_results"]["tools_list"] = tools_result

        # Test resources listing
        resources_result = _run_inspector_command(
            server_command, "resources/list", server_args, timeout=timeout
        )
        results["test_results"]["resources_list"] = resources_result

        # Test prompts listing
        prompts_result = _run_inspector_command(
            server_command, "prompts/list", server_args, timeout=timeout
        )
        results["test_results"]["prompts_list"] = prompts_result

        # Generate summary
        results["summary"] = {
            "tools_available": len(tools_result.get("tools", []))
            if tools_result.get("success")
            else 0,
            "resources_available": len(resources_result.get("resources", []))
            if resources_result.get("success")
            else 0,
            "prompts_available": len(prompts_result.get("prompts", []))
            if prompts_result.get("success")
            else 0,
            "overall_status": "healthy"
            if all(
                r.get("success")
                for r in [tools_result, resources_result, prompts_result]
            )
            else "issues_detected",
        }

        return results

    except Exception as e:
        results["error"] = f"Comprehensive test failed: {str(e)}"
        return results


def get_inspector_help(topic: str = None) -> dict[str, Any]:
    """
    Get help information about MCP Inspector usage

    Args:
        topic: Specific help topic (optional)

    Returns:
        Documentation and usage examples
    """
    help_content = {
        "mcp_inspector": {
            "description": "MCP Inspector is a tool for testing and debugging MCP servers",
            "basic_usage": "npx @modelcontextprotocol/inspector --cli <server_command> --method <method>",
            "common_methods": [
                "tools/list - List all available tools",
                "resources/list - List all available resources",
                "prompts/list - List all available prompts",
                "tools/call/<tool_name> - Call a specific tool",
                "resources/read/<resource_uri> - Read a specific resource",
                "prompts/get/<prompt_name> - Get a specific prompt",
            ],
        },
        "server_commands": {
            "description": "Examples of server commands to inspect",
            "examples": [
                "python server.py",
                "node server.js",
                "uv run python server.py",
                "npm start",
            ],
        },
        "troubleshooting": {
            "common_issues": [
                "Server not starting - Check server command and dependencies",
                "Connection timeout - Increase timeout or check server startup time",
                "Invalid method - Verify method name and server capabilities",
            ]
        },
    }

    if topic:
        topic_lower = topic.lower()
        if topic_lower in help_content:
            return {
                "success": True,
                "topic": topic,
                "content": help_content[topic_lower],
            }
        else:
            return {
                "success": False,
                "error": f"Help topic '{topic}' not found",
                "available_topics": list(help_content.keys()),
            }
    else:
        return {"success": True, "content": help_content}


def create_inspector_config(
    server_command: str, config_name: str, server_args: str = None
) -> dict[str, Any]:
    """
    Create a configuration file for repeated inspections

    Args:
        server_command: Command to start the MCP server
        config_name: Name for the configuration
        server_args: Additional server arguments (optional)

    Returns:
        Configuration creation result
    """
    config = {
        "name": config_name,
        "server_command": server_command,
        "server_args": server_args,
        "created_at": str(
            Path(__file__).parent.parent / "inspector_configs" / f"{config_name}.json"
        ),
    }

    try:
        config_dir = Path(__file__).parent.parent / "inspector_configs"
        config_dir.mkdir(exist_ok=True)

        config_file = config_dir / f"{config_name}.json"
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

        return {
            "success": True,
            "message": f"Configuration saved to {config_file}",
            "config": config,
        }

    except Exception as e:
        return {"success": False, "error": f"Failed to save configuration: {str(e)}"}


def batch_inspect_servers(server_configs: str, timeout: int = 30) -> dict[str, Any]:
    """
    Inspect multiple MCP servers in batch

    Args:
        server_configs: JSON string containing array of server configurations
        timeout: Timeout per server in seconds (default: 30)

    Returns:
        Aggregated results from multiple servers
    """
    try:
        configs = json.loads(server_configs)
        results = {
            "batch_results": [],
            "summary": {"total_servers": len(configs), "successful": 0, "failed": 0},
        }

        for i, config in enumerate(configs):
            server_command = config.get("command")
            server_args = config.get("args")

            if not server_command:
                result = {
                    "index": i,
                    "config": config,
                    "success": False,
                    "error": "Missing server command",
                }
            else:
                result = {
                    "index": i,
                    "config": config,
                    **_run_inspector_command(
                        server_command=server_command,
                        method="tools/list",
                        server_args=server_args,
                        timeout=timeout,
                    ),
                }

            results["batch_results"].append(result)

            if result.get("success"):
                results["summary"]["successful"] += 1
            else:
                results["summary"]["failed"] += 1

        return results

    except json.JSONDecodeError:
        return {"success": False, "error": "Invalid JSON in server_configs parameter"}
    except Exception as e:
        return {"success": False, "error": f"Batch inspection failed: {str(e)}"}


def inspect_with_config(config_file: str, timeout: int = 30) -> dict[str, Any]:
    """
    Inspect a server using a saved configuration file

    Args:
        config_file: Path to the configuration file
        timeout: Timeout in seconds (default: 30)

    Returns:
        Inspection result using saved configuration
    """
    try:
        config_path = Path(config_file)
        if not config_path.exists():
            return {
                "success": False,
                "error": f"Configuration file not found: {config_file}",
            }

        with open(config_path, encoding="utf-8") as f:
            config = json.load(f)

        server_command = config.get("server_command")
        server_args = config.get("server_args")

        if not server_command:
            return {
                "success": False,
                "error": "Configuration file missing server_command",
            }

        result = _run_inspector_command(
            server_command=server_command,
            method="tools/list",
            server_args=server_args,
            timeout=timeout,
        )

        result["config_used"] = config
        return result

    except json.JSONDecodeError:
        return {"success": False, "error": "Invalid JSON in configuration file"}
    except Exception as e:
        return {"success": False, "error": f"Failed to inspect with config: {str(e)}"}
