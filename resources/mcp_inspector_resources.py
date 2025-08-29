"""
MCP Inspector Resources - Optimized Version
Essential documentation and repository information resources with reduced redundancy
"""

__all__ = [
    "get_inspector_documentation",
    "get_inspector_github_info",
    "get_inspector_usage_examples",
    "get_inspector_config_templates",
    "get_inspector_best_practices",
]


def get_inspector_documentation() -> str:
    """Get MCP Inspector official documentation content"""
    return """
# MCP Inspector - Official Documentation

## Overview
The MCP Inspector is the official testing and debugging tool for Model Context Protocol (MCP) servers. It provides comprehensive features for inspecting, testing, and validating MCP server implementations.

## Key Features
- **Server Inspection**: Discover tools, resources, and prompts
- **Interactive Testing**: Execute tools and access resources
- **Protocol Validation**: Verify MCP compliance
- **Performance Monitoring**: Measure response times

## Installation
```bash
# Install globally
npm install -g @modelcontextprotocol/inspector

# Or use directly
npx @modelcontextprotocol/inspector
```

## Usage Methods

### Interactive UI Mode
```bash
npx @modelcontextprotocol/inspector
# Access at http://localhost:5173
```

### Command Line Interface
```bash
npx @modelcontextprotocol/inspector --cli [server_command] --method [method]

# Examples:
npx @modelcontextprotocol/inspector --cli python server.py --method tools/list
npx @modelcontextprotocol/inspector --cli node server.js --method resources/list
```

## Supported Methods
1. **tools/list** - List all available tools
2. **tools/call** - Execute a specific tool
3. **resources/list** - List all available resources
4. **resources/read** - Read specific resource content
5. **resources/templates/list** - List resource templates
6. **prompts/list** - List all available prompts
7. **prompts/get** - Get specific prompt content
8. **logging/setLevel** - Set server logging level

## Method Parameters

### tools/call
```bash
--tool-name [tool_name]
--tool-arg key=value
```

### resources/read
```bash
--resource-uri [resource_uri]
```

### prompts/get
```bash
--prompt-name [prompt_name]
--prompt-arg key=value
```

### logging/setLevel
```bash
--level [debug|info|warn|error]
```

## Configuration
Supports STDIO and HTTP transports with configurable timeouts and environment variables.

## Best Practices
- Use inspector during development for validation
- Test all capabilities regularly
- Monitor performance characteristics
- Implement automated testing workflows

## Common Issues
- **Connection Problems**: Verify server is running
- **Tool Failures**: Validate parameters and implementation
- **Timeout Issues**: Increase timeout or optimize server
- **Resource Access**: Check URIs and permissions

For detailed information, visit the official repository and documentation.
"""


def get_inspector_github_info() -> str:
    """Get MCP Inspector GitHub repository information"""
    return """
# MCP Inspector - GitHub Repository

## Repository Details
- **URL**: https://github.com/modelcontextprotocol/inspector
- **License**: MIT License
- **Language**: TypeScript/JavaScript
- **Minimum Node.js**: 16.0.0

## Project Structure
```
inspector/
├── src/           # Source code
│   ├── cli/       # Command-line interface
│   ├── ui/        # Web-based UI
│   └── core/      # Core inspection logic
├── docs/          # Documentation
├── examples/      # Usage examples
└── tests/         # Test suites
```

## Installation Options
```bash
# Global installation
npm install -g @modelcontextprotocol/inspector

# Project-specific
npm install --save-dev @modelcontextprotocol/inspector

# Direct usage
npx @modelcontextprotocol/inspector
```

## Development Setup
```bash
git clone https://github.com/modelcontextprotocol/inspector.git
cd inspector
npm install
npm run dev
```

## API Reference

### CLI Commands
```bash
# Basic inspection
npx @modelcontextprotocol/inspector --cli [server_command] --method [method]

# Tool testing
npx @modelcontextprotocol/inspector --cli [server_command] --method tools/call --tool-name [name]

# Resource reading
npx @modelcontextprotocol/inspector --cli [server_command] --method resources/read --resource-uri [uri]
```

### Programmatic Usage
```javascript
const { Inspector } = require('@modelcontextprotocol/inspector');

const inspector = new Inspector();
const result = await inspector.inspect({
  command: 'python server.py',
  method: 'tools/list',
  timeout: 30000
});
```

## Contributing
- Fork repository and create feature branches
- Follow TypeScript and ESLint standards
- Include comprehensive tests
- Update documentation as needed

## Support
- GitHub Issues for bug reports
- Discussions for community questions
- Regular releases with semantic versioning

Visit the repository for current information, issues, and contributions.
"""


def get_inspector_usage_examples() -> str:
    """Get MCP Inspector usage examples"""
    return """
# MCP Inspector - Usage Examples

## Basic Usage

### Server Discovery
```bash
# List tools
npx @modelcontextprotocol/inspector --cli python server.py --method tools/list

# List resources
npx @modelcontextprotocol/inspector --cli python server.py --method resources/list

# List prompts
npx @modelcontextprotocol/inspector --cli python server.py --method prompts/list
```

### Tool Testing
```bash
# Simple tool call
npx @modelcontextprotocol/inspector --cli python server.py --method tools/call --tool-name calculate --tool-arg expression="2+2"

# Complex parameters
npx @modelcontextprotocol/inspector --cli python server.py --method tools/call \\
  --tool-name search_database \\
  --tool-arg query="user data" \\
  --tool-arg limit=10
```

### Resource Access
```bash
# Read resource
npx @modelcontextprotocol/inspector --cli python server.py --method resources/read \\
  --resource-uri "file://config.json"

# List templates
npx @modelcontextprotocol/inspector --cli python server.py --method resources/templates/list
```

### Prompt Testing
```bash
# Get prompt
npx @modelcontextprotocol/inspector --cli python server.py --method prompts/get \\
  --prompt-name code_review \\
  --prompt-arg code="def hello(): print('world')"
```

## Advanced Scenarios

### Automated Testing Script
```bash
#!/bin/bash
SERVER_CMD="python server.py"
INSPECTOR="npx @modelcontextprotocol/inspector --cli"

echo "Testing server capabilities..."

# Test connectivity
$INSPECTOR $SERVER_CMD --method tools/list > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Server connectivity: OK"
else
    echo "❌ Server connectivity: FAILED"
    exit 1
fi

# Count capabilities
TOOLS=$($INSPECTOR $SERVER_CMD --method tools/list | jq '.tools | length')
RESOURCES=$($INSPECTOR $SERVER_CMD --method resources/list | jq '.resources | length')
PROMPTS=$($INSPECTOR $SERVER_CMD --method prompts/list | jq '.prompts | length')

echo "📊 Capabilities: Tools=$TOOLS, Resources=$RESOURCES, Prompts=$PROMPTS"
```

### CI/CD Integration
```yaml
name: MCP Server Testing
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - name: Install Inspector
        run: npm install -g @modelcontextprotocol/inspector
      - name: Test Server
        run: |
          python server.py &
          sleep 5
          npx @modelcontextprotocol/inspector --cli python server.py --method tools/list
```

## Error Handling

### Debug Mode
```bash
# Enable debug logging
npx @modelcontextprotocol/inspector --cli python server.py --method logging/setLevel --level debug

# Capture output
npx @modelcontextprotocol/inspector --cli python server.py --method tools/list > output.json 2> errors.log
```

### Common Issues
- **Connection timeout**: Increase timeout or check server status
- **Invalid parameters**: Verify tool/resource/prompt arguments
- **Permission errors**: Check file access and server permissions

These examples cover the essential usage patterns for effective MCP server testing and validation.
"""


def get_inspector_config_templates() -> str:
    """Get MCP Inspector configuration templates"""
    return """
# MCP Inspector - Configuration Templates

## Basic Server Configuration
```json
{
  "name": "basic-server",
  "server": {
    "command": "python",
    "args": ["server.py"],
    "env": {"DEBUG": "false"},
    "timeout": 30
  },
  "tests": {
    "basic": ["tools/list", "resources/list", "prompts/list"],
    "comprehensive": ["tools/list", "resources/list", "prompts/list", "resources/templates/list"]
  }
}
```

## Multi-Environment Configuration
```json
{
  "name": "multi-environment",
  "servers": {
    "development": {
      "command": "python",
      "args": ["dev_server.py"],
      "env": {"ENV": "dev", "DEBUG": "true"}
    },
    "production": {
      "command": "python",
      "args": ["prod_server.py"],
      "env": {"ENV": "production", "DEBUG": "false"}
    }
  },
  "test_matrix": {
    "health": ["tools/list", "resources/list"],
    "full": ["tools/list", "resources/list", "prompts/list"]
  }
}
```

## CI/CD Integration
```yaml
# GitHub Actions
name: MCP Testing
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - name: Install Inspector
        run: npm install -g @modelcontextprotocol/inspector
      - name: Test Server
        run: |
          python server.py &
          sleep 5
          npx @modelcontextprotocol/inspector --cli python server.py --method tools/list
```

## Load Testing Configuration
```json
{
  "name": "load-testing",
  "server": {"command": "python", "args": ["server.py"]},
  "load_tests": {
    "light": {"concurrent_requests": 5, "duration": 60},
    "heavy": {"concurrent_requests": 20, "duration": 300}
  },
  "thresholds": {
    "max_response_time": 5.0,
    "min_success_rate": 0.95
  }
}
```

## Monitoring Configuration
```json
{
  "name": "monitoring",
  "server": {"command": "python", "args": ["server.py"]},
  "monitoring": {
    "check_interval": 60,
    "health_checks": [
      {"name": "connectivity", "method": "tools/list", "critical": true},
      {"name": "resources", "method": "resources/list", "critical": false}
    ]
  },
  "alerting": {
    "email": ["admin@example.com"],
    "conditions": ["connectivity_failed", "response_time > 5.0"]
  }
}
```

These templates provide structured approaches for different testing scenarios and can be customized based on specific requirements.
"""


def get_inspector_best_practices() -> str:
    """Get MCP Inspector best practices guide"""
    return """
# MCP Inspector - Best Practices

## Development Workflow

### Daily Development Routine
```bash
# Morning check
npx @modelcontextprotocol/inspector --cli python server.py --method tools/list

# After changes
npx @modelcontextprotocol/inspector --cli python server.py --method tools/list
npx @modelcontextprotocol/inspector --cli python server.py --method resources/list

# Pre-commit validation
npx @modelcontextprotocol/inspector --cli python server.py --method tools/call --tool-name new_tool
```

### Code Integration
```python
import subprocess

def validate_server():
    try:
        result = subprocess.run([
            'npx', '@modelcontextprotocol/inspector',
            '--cli', 'python', 'server.py',
            '--method', 'tools/list'
        ], capture_output=True, timeout=30)
        return result.returncode == 0
    except Exception:
        return False

# Use before starting development
if not validate_server():
    print("❌ Server validation failed")
    exit(1)
```

## Testing Strategy

### Test Pyramid
- **E2E Tests**: Inspector integration testing
- **Integration Tests**: Tool/resource functionality
- **Unit Tests**: Individual component testing

### Comprehensive Checklist
- [ ] Connectivity testing
- [ ] Capability discovery
- [ ] Functionality validation
- [ ] Error handling verification
- [ ] Performance benchmarking
- [ ] Security validation

## Production Practices

### Health Monitoring
```python
import time
import logging

def monitor_server(server_cmd, interval=60):
    while True:
        try:
            result = subprocess.run([
                'npx', '@modelcontextprotocol/inspector',
                '--cli', *server_cmd.split(),
                '--method', 'tools/list'
            ], capture_output=True, timeout=30)

            if result.returncode == 0:
                logging.info("✅ Server healthy")
            else:
                logging.error("❌ Server unhealthy")

        except Exception as e:
            logging.error(f"Monitor error: {e}")

        time.sleep(interval)

monitor_server("python server.py")
```

### Performance Testing
```python
import statistics
import time

def performance_test(server_cmd, method, iterations=10):
    times = []
    for _ in range(iterations):
        start = time.time()
        result = subprocess.run([
            'npx', '@modelcontextprotocol/inspector',
            '--cli', *server_cmd.split(),
            '--method', method
        ], capture_output=True, timeout=30)

        if result.returncode == 0:
            times.append(time.time() - start)

    if times:
        return {
            'avg': statistics.mean(times),
            'min': min(times),
            'max': max(times)
        }

results = performance_test("python server.py", "tools/list")
print(f"Performance: avg={results['avg']:.3f}s")
```

## CI/CD Integration

### Quality Gates
```python
def check_quality_gate(test_results):
    checks = [
        test_results.get('success_rate', 0) >= 0.95,
        test_results.get('avg_response_time', 0) <= 2.0,
        test_results.get('tool_count', 0) >= 1
    ]

    if all(checks):
        print("🎉 Quality gate PASSED")
        return True
    else:
        print("❌ Quality gate FAILED")
        return False
```

### Automated Pipeline
```yaml
jobs:
  test:
    steps:
      - name: Install Inspector
        run: npm install -g @modelcontextprotocol/inspector
      - name: Test Server
        run: |
          python server.py &
          sleep 5
          npx @modelcontextprotocol/inspector --cli python server.py --method tools/list
```

## Security Practices

### Input Validation Testing
```python
def test_security():
    malicious_inputs = [
        "'; DROP TABLE users; --",
        "<script>alert('xss')</script>",
        "../../../etc/passwd"
    ]

    for payload in malicious_inputs:
        result = subprocess.run([
            'npx', '@modelcontextprotocol/inspector',
            '--cli', 'python', 'server.py',
            '--method', 'tools/call',
            '--tool-name', 'echo',
            '--tool-arg', f'message={payload}'
        ], capture_output=True)

        # Check if payload was properly handled
        if payload not in result.stdout:
            print(f"✅ Security test passed for: {payload[:20]}...")
```

## Maintenance

### Regular Tasks
- **Weekly**: Update Inspector, review test trends
- **Monthly**: Performance baseline review, security testing
- **Quarterly**: Test automation improvement, documentation updates

### Maintenance Script
```bash
#!/bin/bash
echo "🔧 MCP Inspector maintenance..."

# Update Inspector
npm update -g @modelcontextprotocol/inspector

# Clean old results
find . -name "*_results.json" -mtime +30 -delete

# Health check
npx @modelcontextprotocol/inspector --cli python server.py --method tools/list

echo "✅ Maintenance complete"
```

Following these practices ensures reliable, secure, and maintainable MCP server testing workflows.
"""
