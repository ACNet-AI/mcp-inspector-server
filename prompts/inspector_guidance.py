"""
MCP Inspector Guidance Prompts - Optimized Version
Professional guidance system with reduced redundancy
"""

__all__ = [
    "inspector_workflow_guide",
    "server_testing_strategy",
    "troubleshooting_guide",
    "best_practices_prompt",
]


# Common helper functions used across multiple prompts
def _get_server_command(server_type: str) -> str:
    """Get appropriate server command based on type."""
    commands = {
        "python": "python server.py",
        "nodejs": "node server.js",
        "custom": "Please refer to project documentation for startup command",
        "unknown": "Need to identify server type and startup method first",
    }
    return commands.get(server_type, commands["unknown"])


def _generate_testing_strategy(scope: str, experience: str) -> str:
    """Generate testing strategy based on scope and experience."""
    strategies = {
        ("basic", "beginner"): "Focus on connectivity and basic tool testing",
        ("basic", "intermediate"): "Standard verification with error handling checks",
        ("basic", "expert"): "Quick validation with automated reporting",
        (
            "comprehensive",
            "beginner",
        ): "Step-by-step guided testing with detailed explanations",
        (
            "comprehensive",
            "intermediate",
        ): "Full capability testing with performance monitoring",
        ("comprehensive", "expert"): "Advanced testing with custom validation scripts",
    }
    return strategies.get(
        (scope, experience), "Standard comprehensive testing approach"
    )


def _get_common_recommendations(server_type: str, scope: str) -> str:
    """Generate common recommendations based on server type and scope."""
    base_recommendations = [
        "Establish regular testing schedule",
        "Monitor performance metrics",
        "Implement automated health checks",
    ]

    if server_type == "python":
        base_recommendations.append("Ensure virtual environment is properly activated")
    elif server_type == "nodejs":
        base_recommendations.append("Verify Node.js version compatibility")

    if scope == "comprehensive":
        base_recommendations.extend(
            [
                "Set up continuous integration testing",
                "Implement load testing for production readiness",
            ]
        )

    return "\\n".join(f"- {rec}" for rec in base_recommendations)


def inspector_workflow_guide(
    server_type: str = "unknown",
    testing_scope: str = "comprehensive",
    experience_level: str = "intermediate",
) -> str:
    """
    Generate MCP server inspection workflow guidance.

    Args:
        server_type: Server type (python, nodejs, custom, unknown)
        testing_scope: Testing scope (basic, comprehensive, performance, security)
        experience_level: User experience level (beginner, intermediate, expert)

    Returns:
        str: Structured professional workflow guidance
    """

    server_command = _get_server_command(server_type)
    testing_strategy = _generate_testing_strategy(testing_scope, experience_level)
    recommendations = _get_common_recommendations(server_type, testing_scope)

    return f"""
<role>
You are a senior MCP server testing expert, specializing in guiding AI Agents through systematic server inspection and validation.
Your professional background: Extensive experience with MCP protocol implementation, expert in various server architectures and testing methodologies
Work approach: Professional and rigorous, focused on practical results, providing clear executable guidance
Core responsibility: Provide AI Agents with structured testing workflows to ensure comprehensive and efficient server inspection
</role>

<context>
Business context: Currently need to perform {testing_scope} level testing inspection on {server_type} type MCP server
Industry standards: Follow MCP (Model Context Protocol) specifications, ensure normal operation of server's three core functions: tools, resources, and prompts
Key constraints:
- Must ensure testing process does not affect production environment
- Need to consider {experience_level} level user's understanding capability
- Test results must be actionable and meaningful
</context>

<knowledge_base>
Professional terminology:
- MCP Server: Model Context Protocol server, providing three core functions: tools, resources, and prompts
- Inspector CLI: Official MCP testing tool, supporting 8 core inspection methods
- Transport: Communication method, mainly including stdio and HTTP modes
- Tools: Executable function modules that agents can call to perform specific tasks
- Resources: Static or dynamic information resources that agents can read to obtain data
- Prompts: Structured prompt templates that agents can use to generate customized content

Standard process:
1. Connection verification → 2. Feature discovery → 3. Deep testing → 4. Performance evaluation → 5. Report generation

Reference materials:
- MCP Inspector official documentation: https://modelcontextprotocol.io/legacy/tools/inspector
- mcp-inspector-server toolkit: 11 professional testing tools
</knowledge_base>

<input>
Input type: Testing configuration parameters
Key fields:
- server_type: {server_type} (affects startup command and common issue identification)
- testing_scope: {testing_scope} (determines testing depth and coverage)
- experience_level: {experience_level} (adjusts guidance detail level and technical depth)

Current input configuration:
Server type: {server_type}
Testing scope: {testing_scope}
Experience level: {experience_level}
</input>

<instructions>
Please generate structured testing workflow guidance following these steps:

1. **Environment Preparation Phase**
   - Determine startup command and dependency checks based on server type
   - Verify mcp-inspector-server tool availability
   - Set appropriate testing environment and logging level

2. **Connection Establishment Phase**
   - Execute basic connectivity tests
   - Verify MCP protocol handshake success
   - Confirm server response normality

3. **Feature Discovery Phase**
   - Enumerate all available tools, resources, and prompts
   - Analyze feature completeness and coverage
   - Identify core and extended features

4. **Deep Testing Phase**
   - Execute appropriate testing strategies based on testing scope
   - Perform parameter validation and boundary condition testing
   - Evaluate error handling and exception recovery capabilities

5. **Quality Assessment Phase**
   - Generate comprehensive test reports
   - Provide improvement recommendations and best practices
   - Determine next action plans
</instructions>

<examples>
**Example 1 - Python Server Basic Testing**
Input: server_type="python", testing_scope="basic", experience_level="beginner"
Output:
```
🚀 Python MCP Server Basic Testing Workflow

Step 1: Environment Preparation
- Startup command: python server.py
- Dependency check: pip list | grep mcp
- Tool verification: get_inspector_help()

Step 2: Connection Testing
- Basic connection: inspect_mcp_server("python server.py", "tools/list")
- Response verification: Check returned tool count > 0

Step 3: Feature Verification
- Tool testing: call_mcp_tool("python server.py", "example_tool_name")
- Resource testing: read_mcp_resource("python server.py", "example_resource_uri")
```

**Example 2 - Enterprise-level Comprehensive Testing**
Input: server_type="nodejs", testing_scope="comprehensive", experience_level="expert"
Output:
```
🎯 Node.js MCP Server Enterprise-level Comprehensive Testing

Advanced testing strategy:
- Concurrent testing: batch_inspect_servers() multi-instance comparison
- Performance benchmarking: comprehensive_server_test() detailed analysis
- Security audit: Input validation and permission control checks
- Monitoring integration: set_logging_level() debug mode analysis
```
</examples>

<output_requirements>
Quality standards:
- Provide complete step-by-step guidance ensuring AI Agent can execute independently
- Include specific command examples and expected results
- Provide appropriate technical depth for different experience levels
- Integrate with mcp-inspector-server's 11 professional tools

Format requirements:
- Use Markdown format for easy reading and execution
- Wrap key information with <workflow_guide></workflow_guide> tags
- Include test success rates and quality scores
- Provide troubleshooting and next step recommendations

Self-check list:
□ Does it cover the complete testing process
□ Does it provide specific executable commands
□ Does it consider different experience level needs
□ Does it include quality assessment and improvement recommendations
</output_requirements>

<workflow_guide>
# 🎯 MCP Server Inspection Workflow Guide

## 📋 Testing Configuration
- **Target server**: {server_type} type
- **Testing depth**: {testing_scope} level
- **Guidance level**: Adapted for {experience_level} users

## 🚀 Phase 1: Environment Preparation and Connection Establishment

### 1.1 Environment Check
```python
# Verify mcp-inspector-server availability
result = get_inspector_help()
print("Inspector tool status:", "✅" if result['success'] else "❌")
```

### 1.2 Server Startup Verification
```python
# Basic connectivity test
connection_test = inspect_mcp_server(
    server_command="{server_command}",
    method="tools/list",
    timeout=30
)

if not connection_test['success']:
    print("⚠️ Connection failed, please check server startup status")
    # Execute troubleshooting process
```

## 🔍 Phase 2: Feature Discovery and Analysis

### 2.1 Comprehensive Feature Scan
```python
# Execute comprehensive test to get complete feature inventory
comprehensive_result = comprehensive_server_test(
    server_command="{server_command}",
    timeout=60,
    include_resource_read=True,
    include_prompt_get=True
)

print("Feature statistics:")
print(f"- Tool count: {{comprehensive_result.get('tools_count', 0)}}")
print(f"- Resource count: {{comprehensive_result.get('resources_count', 0)}}")
print(f"- Prompt count: {{comprehensive_result.get('prompts_count', 0)}}")
```

## 🎯 Phase 3: Testing Strategy Execution

### Strategy: {testing_strategy}

```python
# Execute testing based on scope and experience level
if "{testing_scope}" == "basic":
    # Quick verification of core features
    basic_tools = inspect_mcp_server("{server_command}", "tools/list")
    if basic_tools['success'] and len(basic_tools.get('tools', [])) > 0:
        first_tool = basic_tools['tools'][0]['name']
        tool_test = call_mcp_tool("{server_command}", first_tool)
        print(f"Tool test result: {{'✅' if tool_test['success'] else '❌'}}")

elif "{testing_scope}" == "comprehensive":
    # Execute complete functional test matrix
    test_matrix = {{
        'tools': inspect_mcp_server("{server_command}", "tools/list"),
        'resources': inspect_mcp_server("{server_command}", "resources/list"),
        'prompts': inspect_mcp_server("{server_command}", "prompts/list")
    }}

    for category, result in test_matrix.items():
        if result['success']:
            print(f"{{category}} function normal: {{len(result.get(category, []))}} items")
        else:
            print(f"⚠️ {{category}} function abnormal, needs checking")
```

## 📊 Phase 4: Quality Assessment and Recommendations

### 4.1 Performance Metrics
- **Connection stability**: Based on response time and success rate assessment
- **Feature completeness**: Based on MCP three core capability coverage
- **Performance**: Based on response time and resource usage
- **Error handling**: Based on exception handling capabilities

### 4.2 Improvement Recommendations
{recommendations}

### 4.3 Next Actions
- ✅ Tests passed: Ready for use, recommend regular monitoring
- ⚠️ Partial issues: Targeted fixes then retest
- ❌ Serious issues: Need architecture-level inspection and fixes

---
*Professional testing guidance generated based on Anthropic's 6-layer golden structure framework*
</workflow_guide>
"""


def server_testing_strategy(
    server_complexity: str = "medium",
    time_constraint: str = "normal",
    focus_area: str = "functionality",
) -> str:
    """
    Generate MCP server testing strategy.

    Args:
        server_complexity: Server complexity (simple, medium, complex, enterprise)
        time_constraint: Time constraint (urgent, normal, thorough)
        focus_area: Focus area (functionality, performance, security, reliability)

    Returns:
        str: Structured professional testing strategy
    """

    return f"""
<role>
You are a professional MCP server testing strategist, responsible for developing optimal testing plans for servers of different complexity and requirements.
Your professional background: Deep theoretical foundation in software testing and rich practical experience in MCP protocol testing
Work approach: Systematic thinking, focus on balancing efficiency and quality, provide executable strategic solutions
Core responsibility: Design the most suitable testing strategies and execution plans based on project constraints and business requirements
</role>

<context>
Business context: Need to develop testing strategy for {server_complexity} complexity MCP server
Time constraint: {time_constraint} level time limitation
Focus area: {focus_area} aspect quality assurance
Industry standards: Follow software testing best practices, ensure MCP protocol compliance
Key constraints:
- Must complete effective testing within time limits
- Testing coverage must match server complexity
- Focus on specified quality dimensions
</context>

<knowledge_base>
Professional terminology:
- Test Pyramid: Unit testing → Integration testing → End-to-end testing layered strategy
- Risk-driven Testing: Prioritize testing high-risk areas based on risk assessment
- Shift Left Testing: Introduce testing activities early in development
- Regression Testing: Ensure new changes don't affect existing functionality
- Exploratory Testing: Experience-based non-scripted testing approach

Complexity classification:
- Simple: Basic functionality, single responsibility, fewer dependencies
- Medium: Multi-functional modules, moderate complexity, standard architecture
- Complex: Highly integrated, complex business logic, multiple dependencies
- Enterprise: Enterprise-scale, high availability requirements, strict compliance

Time constraint strategies:
- Urgent: Critical path priority, quick verification of core functions
- Normal: Balance coverage and efficiency, standard testing process
- Thorough: Comprehensive deep testing, detailed analysis and documentation
</knowledge_base>

<input>
Input type: Testing strategy configuration parameters
Key fields:
- server_complexity: {server_complexity} (determines testing depth and tool selection)
- time_constraint: {time_constraint} (affects testing scope and execution method)
- focus_area: {focus_area} (determines testing priorities and success criteria)

Current strategy configuration:
Server complexity: {server_complexity}
Time constraint: {time_constraint}
Focus area: {focus_area}
</input>

<instructions>
Please develop structured testing strategy following these steps:

1. **Strategy Analysis Phase**
   - Assess testing requirements corresponding to server complexity
   - Analyze impact of time constraints on testing scope
   - Determine priorities and weights for focus areas

2. **Resource Planning Phase**
   - Select appropriate testing tools and methods
   - Estimate required time and human resources
   - Develop testing environment and data preparation plans

3. **Execution Planning Phase**
   - Design phased testing execution process
   - Define entry and exit criteria for each phase
   - Establish testing progress monitoring mechanisms

4. **Quality Assurance Phase**
   - Set clear success criteria and acceptance conditions
   - Establish risk identification and mitigation measures
   - Develop testing result evaluation framework

5. **Continuous Improvement Phase**
   - Collect testing execution feedback
   - Optimize testing strategies and tool usage
   - Establish knowledge accumulation and experience transfer mechanisms
</instructions>

<examples>
**Example 1 - Simple Server Quick Testing**
Input: server_complexity="simple", time_constraint="urgent", focus_area="functionality"
Output:
```
🚀 Simple Server Quick Functionality Verification Strategy

Core strategy: 20-minute quick verification
- Tool selection: inspect_mcp_server + call_mcp_tool
- Testing focus: Basic connection + core tool verification
- Success criteria: Connection normal + main functions available
```

**Example 2 - Enterprise-level Comprehensive Testing**
Input: server_complexity="enterprise", time_constraint="thorough", focus_area="security"
Output:
```
🎯 Enterprise-level Security Comprehensive Testing Strategy

Comprehensive strategy: 4-hour deep security audit
- Tool matrix: Complete set of 11 inspector tools + security-specific testing
- Testing focus: Input validation + permission control + data protection
- Success criteria: Zero security vulnerabilities + complete compliance report
```
</examples>

<output_requirements>
Quality standards:
- Strategy must highly match input parameters
- Provide specific executable testing steps
- Include clear time estimates and resource requirements
- Integrate with mcp-inspector-server professional tools

Format requirements:
- Use structured Markdown format
- Wrap key strategies with <testing_strategy></testing_strategy> tags
- Include risk assessment and mitigation measures
- Provide quantified success criteria

Self-check list:
□ Does it fully consider complexity requirements
□ Does it reasonably arrange time constraints
□ Does it highlight focus areas
□ Does it provide actionable execution plans
</output_requirements>

<testing_strategy>
# 🎯 MCP Server Testing Strategy

## 📋 Strategy Overview
- **Target complexity**: {server_complexity} level server
- **Time constraint**: {time_constraint} mode execution
- **Focus area**: {focus_area} quality assurance

## 🔍 Strategy Analysis

### Complexity Assessment
{_get_complexity_description(server_complexity)}

### Time Constraint Impact
{_get_time_impact_description(time_constraint)}

### Focus Area Strategy
{_get_focus_strategy_description(focus_area)}

## 🛠️ Tool Selection Matrix

### Core Testing Tools
{_get_core_tools_description(server_complexity, focus_area)}

### Specialized Testing Tools
{_get_specialized_tools_description(focus_area)}

### Auxiliary Analysis Tools
{_get_auxiliary_tools_description(server_complexity)}

## 📊 Execution Plan

### Phase 1: Quick Verification (20%)
```python
# Basic connectivity and core function verification
quick_check = inspect_mcp_server(server_command, "tools/list")
if quick_check['success']:
    print("✅ Basic connection normal")
    # Continue core function testing
else:
    print("❌ Connection failed, execute troubleshooting")
    return "Need to check server startup status"
```

### Phase 2: Function Testing (50%)
```python
# Select testing depth based on complexity
if "{server_complexity}" in ["simple", "medium"]:
    # Standard function testing
    result = comprehensive_server_test(server_command)
else:
    # Deep function testing
    result = batch_inspect_servers([
        {{"name": "primary", "command": server_command}},
        {{"name": "backup", "command": backup_server_command}}
    ])
```

### Phase 3: Specialized Testing (30%)
```python
# Execute specialized testing based on focus area
if "{focus_area}" == "performance":
    # Performance testing
    import time
    start_time = time.time()
    perf_result = comprehensive_server_test(server_command, timeout=120)
    response_time = time.time() - start_time
    print(f"Performance test response time: {{response_time:.2f}} seconds")
elif "{focus_area}" == "security":
    # Security testing
    print("🔒 Executing security tests...")
elif "{focus_area}" == "reliability":
    # Reliability testing
    print("🔄 Executing reliability tests...")
else:
    # Functionality testing
    print("⚙️ Executing functionality tests...")
```

## 🚨 Risk Assessment and Mitigation

### High-risk Scenarios
- Connection timeout or failure
- Core functions unavailable
- Severe performance degradation
- Security vulnerability exposure

### Mitigation Measures
- Establish connection retry mechanisms
- Set up function degradation plans
- Implement performance monitoring alerts
- Strengthen security testing coverage

## 📈 Success Criteria

### Basic Criteria (Must meet)
- ✅ Server connection normal
- ✅ Core functions available
- ✅ No serious errors

### Advanced Criteria (Optimization targets)
- ✅ Performance metrics meet standards
- ✅ Security compliance verification
- ✅ Complete function coverage

## ⏱️ Time Estimation

### Overall Time Allocation
- Quick verification: 20% time
- Function testing: 50% time
- Specialized testing: 30% time

### Key Milestones
- Connection establishment: Within 5 minutes
- Basic functions: Within 15 minutes
- Comprehensive testing: Adjusted based on complexity

---
*Professional testing strategy based on Anthropic's 6-layer golden structure framework*
</testing_strategy>
"""


def _get_complexity_description(complexity: str) -> str:
    """Get complexity description"""
    descriptions = {
        "simple": "Single responsibility server, focus on core functionality completeness verification",
        "medium": "Multi-functional module server, need to balance testing coverage and efficiency",
        "complex": "Highly integrated server, need deep testing and dependency relationship verification",
        "enterprise": "Enterprise-level server, need comprehensive quality assurance and compliance verification",
    }
    return descriptions.get(complexity, descriptions["medium"])


def _get_time_impact_description(constraint: str) -> str:
    """Get time constraint impact description"""
    impacts = {
        "urgent": "Prioritize critical paths, quickly identify key issues",
        "normal": "Standard testing process, balance speed and coverage",
        "thorough": "Deep comprehensive testing, detailed analysis and documentation",
    }
    return impacts.get(constraint, impacts["normal"])


def _get_focus_strategy_description(area: str) -> str:
    """Get focus area strategy description"""
    strategies = {
        "functionality": "Focus on verifying tools, resources, and prompts three core functions",
        "performance": "Focus on response time, concurrent capability, resource usage efficiency",
        "security": "Strengthen input validation, permission control, data protection testing",
        "reliability": "Test stability, error recovery, boundary condition handling",
    }
    return strategies.get(area, strategies["functionality"])


def _get_core_tools_description(complexity: str, focus: str) -> str:
    """Get core tools description"""
    if complexity in ["simple", "medium"]:
        return "- inspect_mcp_server\\n- comprehensive_server_test\\n- call_mcp_tool"
    else:
        return "- Complete set of 11 inspector tools\\n- batch_inspect_servers\\n- create_inspector_config"


def _get_specialized_tools_description(focus: str) -> str:
    """Get specialized tools description"""
    tools = {
        "functionality": "- read_mcp_resource\\n- get_mcp_prompt\\n- list_resource_templates",
        "performance": "- comprehensive_server_test (performance mode)\\n- set_logging_level (debug analysis)",
        "security": "- Input validation testing tools\\n- Permission control checking tools",
        "reliability": "- Long-running testing\\n- Error recovery verification tools",
    }
    return tools.get(focus, tools["functionality"])


def _get_auxiliary_tools_description(complexity: str) -> str:
    """Get auxiliary tools description"""
    if complexity in ["complex", "enterprise"]:
        return "- get_inspector_help\\n- inspect_with_config\\n- Custom testing scripts"
    else:
        return "- get_inspector_help\\n- Basic log analysis tools"


def troubleshooting_guide(
    error_type: str = "connection",
    server_environment: str = "development",
    urgency_level: str = "normal",
) -> str:
    """
    Generate MCP server troubleshooting guidance.

    Args:
        error_type: Error type (connection, timeout, tool_error, resource_error, config_error)
        server_environment: Server environment (development, testing, production)
        urgency_level: Urgency level (low, normal, high, critical)

    Returns:
        str: Structured professional troubleshooting guidance
    """

    return f"""
<role>
You are an experienced MCP server troubleshooting expert, specializing in rapid diagnosis and resolution of various server issues.
Your professional background: Years of distributed system fault diagnosis experience, expert in various MCP protocol exception scenarios
Work approach: Calm and professional, quick response, provide systematic solutions
Core responsibility: Help users quickly locate problem root causes, provide executable repair steps and preventive measures
</role>

<context>
Business context: {error_type} type fault occurred in {server_environment} environment
Urgency level: {urgency_level} level, requiring corresponding response speed
Industry standards: Follow ITIL fault management processes, ensure quick problem resolution and knowledge accumulation
Key constraints:
- Must provide solutions within urgency level required timeframe
- Solutions must suit current environment's risk tolerance
- Need to provide preventive measures to avoid problem recurrence
</context>

<knowledge_base>
Professional terminology:
- RCA (Root Cause Analysis): Systematic approach to find fundamental causes of problems
- MTTR (Mean Time To Recovery): Average recovery time, measuring fault handling efficiency
- Circuit Breaker: Circuit breaker pattern, preventing fault propagation protection mechanism
- Health Check: Health monitoring, proactive service status monitoring
- Graceful Degradation: Maintain core services when partial functions fail

Common error classifications:
- Connection: Network connection, port, firewall related issues
- Timeout: Response timeout, resource waiting, deadlock related issues
- Tool_error: Tool execution failure, parameter errors, permission issues
- Resource_error: Resource access failure, file not found, format errors
- Config_error: Configuration file errors, missing parameters, type mismatches

Environment risk levels:
- Development: Low risk, can perform experimental fixes
- Testing: Medium risk, need to record repair process
- Production: High risk, prioritize service stability
</knowledge_base>

<input>
Input type: Fault diagnosis parameters
Key fields:
- error_type: {error_type} (determines diagnosis focus and solution strategy)
- server_environment: {server_environment} (affects repair plan risk control)
- urgency_level: {urgency_level} (determines response time and handling depth)

Current fault situation:
Error type: {error_type}
Environment: {server_environment}
Urgency level: {urgency_level}
</input>

<instructions>
Please provide structured troubleshooting guidance following these steps:

1. **Problem Identification Phase**
   - Quickly identify fault symptoms and impact scope
   - Collect key diagnostic information and logs
   - Assess problem urgency and business impact

2. **Root Cause Analysis Phase**
   - Analyze possible root causes based on symptoms
   - Use systematic diagnostic methods for investigation
   - Determine most likely problem sources

3. **Solution Phase**
   - Provide targeted repair steps
   - Consider environment risks and choose appropriate solutions
   - Provide rollback plans and emergency measures

4. **Verification Testing Phase**
   - Use mcp-inspector-server tools to verify repair effectiveness
   - Perform regression testing to ensure no side effects
   - Monitor key metrics to confirm problem resolution

5. **Prevention and Improvement Phase**
   - Analyze deep causes of problem occurrence
   - Establish preventive measures and monitoring mechanisms
   - Update documentation and knowledge base
</instructions>

<examples>
**Example 1 - Development Environment Connection Issue**
Input: error_type="connection", server_environment="development", urgency_level="normal"
Output:
```
🔧 Development Environment Connection Fault Quick Diagnosis

Problem identification:
- Symptoms: Unable to connect to MCP server
- Impact: Development work suspended
- Diagnosis: Check server process and port status

Quick solution:
1. Check server process: ps aux | grep server
2. Verify port listening: netstat -tulpn | grep PORT
3. Restart server: python server.py
4. Verify connection: inspect_mcp_server("python server.py", "tools/list")
```

**Example 2 - Production Environment Tool Error**
Input: error_type="tool_error", server_environment="production", urgency_level="critical"
Output:
```
🚨 Production Environment Tool Fault Emergency Handling

Emergency response:
- Immediately enable backup server
- Isolate faulty tool to prevent impact spread
- Collect detailed error logs for analysis
- Notify relevant teams and users
```
</examples>

<output_requirements>
Quality standards:
- Provide quick and effective problem solutions
- Include specific diagnostic commands and repair steps
- Consider environment risks and provide appropriate safety measures
- Integrate with mcp-inspector-server tools for verification

Format requirements:
- Use structured Markdown format
- Wrap key solutions with <troubleshooting_solution></troubleshooting_solution> tags
- Include risk assessment and preventive measures
- Provide quantifiable success verification standards

Self-check list:
□ Does it accurately identify the problem type
□ Does it provide executable solution steps
□ Does it consider environment risk factors
□ Does it include verification and prevention measures
</output_requirements>

<troubleshooting_solution>
# 🚨 MCP Server Troubleshooting Guide

## 📋 Fault Overview
- **Error type**: {error_type}
- **Environment**: {server_environment}
- **Urgency level**: {urgency_level}
- **Response strategy**: {_get_response_strategy(urgency_level)}

## 🔍 Problem Diagnosis

### Symptom Identification
{_get_error_symptoms(error_type)}

### Possible Causes
{_get_possible_causes(error_type)}

### Impact Assessment
{_get_impact_assessment(error_type, server_environment)}

## 🛠️ Solution

### Immediate Actions (0-5 minutes)
```python
# Use mcp-inspector-server for quick diagnosis
diagnostic_result = get_inspector_help()
print("Inspector tool status:", diagnostic_result['success'])

# Basic connectivity test
connection_test = inspect_mcp_server(
    server_command="python server.py",  # Adjust according to actual situation
    method="tools/list",
    timeout=10
)
print("Connection test result:", connection_test['success'])
```

### Deep Analysis (5-15 minutes)
```python
# Comprehensive system check
comprehensive_check = comprehensive_server_test(
    server_command="python server.py",
    timeout=60,
    include_resource_read=True,
    include_prompt_get=True
)

# Analyze check results
if not comprehensive_check['success']:
    print("Problem found:", comprehensive_check.get('error', 'Unknown error'))
    # Execute targeted repairs
else:
    print("System status normal, problem may have auto-recovered")
```

### Specialized Repair (15-30 minutes)
{_get_specific_fix_steps(error_type, server_environment)}

## ✅ Verification Testing

### Function Verification
```python
# Verify core function recovery
verification_tests = [
    ("Tool list", "tools/list"),
    ("Resource list", "resources/list"),
    ("Prompt list", "prompts/list")
]

for test_name, method in verification_tests:
    result = inspect_mcp_server(server_command, method)
    status = "✅" if result['success'] else "❌"
    print(f"{{test_name}}: {{status}}")
```

### Performance Verification
```python
# Performance regression testing
import time
start_time = time.time()
perf_test = comprehensive_server_test(server_command)
response_time = time.time() - start_time

print(f"Response time: {{response_time:.2f}} seconds")
if response_time < 5:
    print("✅ Performance normal")
else:
    print("⚠️ Performance needs further optimization")
```

## 🔒 Environment Security Considerations

### {server_environment.title()} Environment Special Requirements
{_get_environment_considerations(server_environment)}

## 🚨 Emergency Plans

### Rollback Plan
{_get_rollback_plan(error_type, server_environment)}

### Escalation Path
{_get_escalation_path(urgency_level)}

## 📊 Preventive Measures

### Monitoring Recommendations
- Establish proactive monitoring for {error_type} type errors
- Set alert thresholds for key metrics
- Regularly execute health check scripts

### Improvement Recommendations
{_get_improvement_suggestions(error_type)}

---
*Professional troubleshooting guidance based on Anthropic's 6-layer golden structure framework*
</troubleshooting_solution>
"""


def _get_response_strategy(urgency: str) -> str:
    """Get response strategy based on urgency level"""
    strategies = {
        "low": "Standard process handling, focus on thorough resolution",
        "normal": "Balance speed and quality, ensure effective resolution",
        "high": "Quick response, prioritize service recovery",
        "critical": "Emergency handling, take immediate action",
    }
    return strategies.get(urgency, strategies["normal"])


def _get_error_symptoms(error_type: str) -> str:
    """Get symptom description based on error type"""
    symptoms = {
        "connection": "- Unable to connect to server\\n- Connection timeout or refused\\n- Handshake failure",
        "timeout": "- Slow request response\\n- Operation timeout failure\\n- Partial functions unresponsive",
        "tool_error": "- Tool call failure\\n- Parameter validation error\\n- Execution exception interruption",
        "resource_error": "- Resource inaccessible\\n- File read failure\\n- Content format error",
        "config_error": "- Service startup failure\\n- Configuration loading error\\n- Parameter validation failure",
    }
    return symptoms.get(error_type, symptoms["connection"])


def _get_possible_causes(error_type: str) -> str:
    """Get possible causes based on error type"""
    causes = {
        "connection": "- Server not started or crashed\\n- Port occupied or firewall blocked\\n- Network connection issues",
        "timeout": "- Server overloaded\\n- Resource shortage or deadlock\\n- Network delay too high",
        "tool_error": "- Tool implementation defects\\n- Incorrect parameter format\\n- Insufficient permissions",
        "resource_error": "- Incorrect file path\\n- Permission setting issues\\n- Unsupported resource format",
        "config_error": "- Configuration file syntax error\\n- Missing required parameters\\n- Environment variables not set",
    }
    return causes.get(error_type, causes["connection"])


def _get_impact_assessment(error_type: str, environment: str) -> str:
    """Assess error impact"""
    base_impact = {
        "connection": "Service completely unavailable",
        "timeout": "Service performance severely degraded",
        "tool_error": "Partial functions unavailable",
        "resource_error": "Information access limited",
        "config_error": "Service cannot start normally",
    }

    env_multiplier = {
        "development": "affects development efficiency",
        "testing": "affects testing progress",
        "production": "affects business operations",
    }

    return f"{base_impact.get(error_type, 'Unknown impact')}, {env_multiplier.get(environment, 'unknown impact')}"


def _get_specific_fix_steps(error_type: str, environment: str) -> str:
    """Get specific fix steps based on error type and environment"""
    fixes = {
        "connection": """
```bash
# Check server process
ps aux | grep server.py

# Check port usage
netstat -tulpn | grep 8000

# Restart server
python server.py &

# Verify connection
inspect_mcp_server("python server.py", "tools/list")
```""",
        "timeout": """
```python
# Adjust timeout settings
result = inspect_mcp_server(
    server_command="python server.py",
    method="tools/list",
    timeout=60  # Increase timeout
)

# Check server resources
import psutil
print(f"CPU usage: {{psutil.cpu_percent()}}%")
print(f"Memory usage: {{psutil.virtual_memory().percent}}%")
```""",
        "tool_error": """
```python
# Test specific tool
problematic_tool = "tool_name"  # Replace with actual tool name
test_result = call_mcp_tool(
    server_command="python server.py",
    tool_name=problematic_tool,
    tool_args={{}}  # Use minimal parameters for testing
)
print("Tool test result:", test_result)
```""",
        "resource_error": """
```python
# Test resource access
resource_uri = "resource://example"  # Replace with actual resource URI
resource_test = read_mcp_resource(
    server_command="python server.py",
    resource_uri=resource_uri
)
print("Resource test result:", resource_test)
```""",
        "config_error": """
```python
# Verify configuration file
import yaml
try:
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    print("✅ Configuration file syntax correct")
except Exception as e:
    print(f"❌ Configuration file error: {{e}}")
```""",
    }
    return fixes.get(error_type, fixes["connection"])


def _get_environment_considerations(environment: str) -> str:
    """Get environment considerations"""
    considerations = {
        "development": "- Can perform experimental fixes\\n- Service restart has minimal impact\\n- Recommend detailed repair process recording",
        "testing": "- Need to consider test data integrity\\n- Need to rerun tests after repairs\\n- Record problem impact on test results",
        "production": "- Prioritize service availability\\n- Be cautious with any modifications\\n- Must have complete rollback plan",
    }
    return considerations.get(environment, considerations["development"])


def _get_rollback_plan(error_type: str, environment: str) -> str:
    """Generate rollback plan"""
    if environment == "production":
        return "- Immediately switch to backup server\\n- Rollback to previous stable version\\n- Notify users of service status"
    else:
        return "- Restore to pre-repair configuration\\n- Restart service to known good state\\n- Record rollback reasons"


def _get_escalation_path(urgency: str) -> str:
    """Generate escalation path"""
    paths = {
        "low": "If problem persists, contact technical lead",
        "normal": "If unresolved within 30 minutes, escalate to senior engineer",
        "high": "If unresolved within 15 minutes, immediately escalate to technical expert",
        "critical": "If unresolved within 5 minutes, activate emergency response process",
    }
    return paths.get(urgency, paths["normal"])


def _get_improvement_suggestions(error_type: str) -> str:
    """Get improvement suggestions based on error type"""
    suggestions = {
        "connection": "- Implement health check mechanisms\\n- Establish service auto-restart\\n- Configure load balancing",
        "timeout": "- Optimize code performance\\n- Add caching mechanisms\\n- Implement request throttling",
        "tool_error": "- Strengthen input validation\\n- Improve error handling\\n- Add unit tests",
        "resource_error": "- Verify resource paths\\n- Implement permission checks\\n- Support multiple formats",
        "config_error": "- Configuration file validation\\n- Provide default configuration\\n- Environment variable checks",
    }
    return suggestions.get(error_type, suggestions["connection"])


def best_practices_prompt(
    use_case: str = "general",
    team_size: str = "small",
    automation_level: str = "medium",
) -> str:
    """
    Generate MCP server best practices guidance.

    Args:
        use_case: Use case scenario (general, ci_cd, development, production, research)
        team_size: Team size (individual, small, medium, large)
        automation_level: Automation level (manual, medium, high)

    Returns:
        str: Structured professional best practices recommendations
    """

    return f"""
<role>
You are a senior MCP server architect and best practices expert, specializing in guiding teams to establish efficient server management and testing systems.
Your professional background: Rich experience in enterprise-level system architecture, deep understanding of DevOps and quality assurance best practices
Work approach: Systematic thinking, focus on long-term value, provide sustainable solutions
Core responsibility: Help teams establish standardized, automated, scalable MCP server management systems
</role>

<context>
Business context: MCP server management needs in {use_case} scenario
Team size: {team_size} team, need to adapt corresponding collaboration modes
Automation level: {automation_level} level automation requirements
Industry standards: Follow DevOps, SRE and software engineering best practices
Key constraints:
- Must adapt to team's technical capabilities and resource limitations
- Solutions must have scalability and maintainability
- Need to balance efficiency, quality and cost
</context>

<knowledge_base>
Professional terminology:
- SRE (Site Reliability Engineering): Site reliability engineering, operational methodology proposed by Google
- CI/CD: Continuous Integration/Continuous Deployment, automated software delivery pipeline
- Infrastructure as Code: Manage infrastructure through code
- Observability: Understanding system status through logs, metrics, and distributed tracing
- Shift Left: Strategy to introduce quality assurance activities early in development

Team size characteristics:
- Individual: Focus on efficiency and automation, reduce repetitive work
- Small (2-5 people): Emphasize collaboration and knowledge sharing
- Medium (6-20 people): Need standardized processes and tools
- Large (20+ people): Need enterprise-level governance and scaled management

Automation levels:
- Manual: Mainly manual operations, tool assistance
- Medium: Partial automation, standardized key processes
- High: Highly automated, intelligent operations
</knowledge_base>

<input>
Input type: Best practices configuration parameters
Key fields:
- use_case: {use_case} (determines practice focus and depth)
- team_size: {team_size} (affects collaboration mode and tool selection)
- automation_level: {automation_level} (determines automation strategy and investment)

Current practice configuration:
Use case: {use_case}
Team size: {team_size}
Automation level: {automation_level}
</input>

<instructions>
Please develop structured best practices guidance following these steps:

1. **Current State Assessment Phase**
   - Analyze current team capabilities and resource status
   - Identify main pain points and improvement opportunities
   - Assess technical debt and risk factors

2. **Goal Setting Phase**
   - Define short-term and long-term improvement goals
   - Set quantifiable success metrics
   - Establish priorities and implementation roadmap

3. **Practice Design Phase**
   - Select appropriate tools and methodologies
   - Design standardized processes and specifications
   - Establish quality assurance and risk control mechanisms

4. **Implementation Planning Phase**
   - Develop phased implementation plans
   - Arrange training and knowledge transfer
   - Establish change management and feedback mechanisms

5. **Continuous Improvement Phase**
   - Establish measurement and monitoring systems
   - Regularly evaluate and optimize practices
   - Promote knowledge accumulation and experience sharing
</instructions>

<examples>
**Example 1 - Individual Developer General Scenario**
Input: use_case="general", team_size="individual", automation_level="medium"
Output:
```
🚀 Individual Developer MCP Server Management Best Practices

Core strategy: Efficiency priority, tool-driven
- Automate daily testing processes
- Establish personal knowledge base and templates
- Use mcp-inspector-server for quick verification
```

**Example 2 - Medium Team CI/CD Scenario**
Input: use_case="ci_cd", team_size="medium", automation_level="high"
Output:
```
🎯 Medium Team CI/CD Best Practices System

Enterprise strategy: Standardized processes, automated delivery
- Integrate mcp-inspector-server into CI/CD pipeline
- Establish code quality gates and automated testing
- Implement infrastructure as code and environment consistency
```
</examples>

<output_requirements>
Quality standards:
- Practice recommendations must be actionable and measurable
- Fully consider team size and technical capability limitations
- Provide specific tool usage guidance and implementation steps
- Integrate with mcp-inspector-server professional capabilities

Format requirements:
- Use structured Markdown format
- Wrap key practices with <best_practices></best_practices> tags
- Include implementation timeline and success metrics
- Provide risk assessment and mitigation measures

Self-check list:
□ Does it fully consider use case requirements
□ Does it adapt to team size characteristics
□ Does it match automation level requirements
□ Does it provide executable implementation plans
</output_requirements>

<best_practices>
# 🎯 MCP Server Management Best Practices

## 📋 Practice Overview
- **Application scenario**: {use_case} environment
- **Team size**: {team_size} team
- **Automation level**: {automation_level} level

## 🔍 Current State Analysis

### Team Capability Assessment
{_get_team_capability_assessment(team_size)}

### Scenario Requirements Analysis
{_get_use_case_requirements(use_case)}

### Automation Maturity
{_get_automation_maturity(automation_level)}

## 🎯 Goal Setting

### Short-term Goals (1-3 months)
{_get_short_term_goals(use_case, team_size)}

### Long-term Goals (6-12 months)
{_get_long_term_goals(use_case, automation_level)}

### Success Metrics
- Test coverage > 80%
- Average response time < 2 seconds
- Fault recovery time < 5 minutes
{_get_additional_success_metrics(use_case, team_size)}

## 🛠️ Core Practices

### 1. Testing Management Practices
```python
# Establish standardized testing process
def standard_server_test(server_command: str) -> dict:
    \"\"\"Standard server testing process\"\"\"
    results = {{}}

    # Basic connectivity test
    results['connectivity'] = inspect_mcp_server(server_command, "tools/list")

    # Comprehensive function test
    results['comprehensive'] = comprehensive_server_test(
        server_command,
        include_resource_read=True,
        include_prompt_get=True
    )

    # Performance benchmark test
    import time
    start_time = time.time()
    results['performance'] = comprehensive_server_test(server_command)
    results['response_time'] = time.time() - start_time

    return results

# Usage example
test_results = standard_server_test("python server.py")
print(f"Testing completed, response time: {{test_results['response_time']:.2f}} seconds")
```

### 2. Quality Assurance Practices
{_get_quality_assurance_practices(use_case, team_size)}

### 3. Automation Practices
{_get_automation_practices(automation_level, team_size)}

### 4. Collaboration Practices
{_get_collaboration_practices(team_size)}

## 📊 Implementation Roadmap

### Phase 1: Foundation Building (Week 1-4)
{_get_phase1_tasks(team_size, automation_level)}

### Phase 2: Process Optimization (Week 5-8)
{_get_phase2_tasks(use_case, automation_level)}

### Phase 3: Advanced Practices (Week 9-12)
{_get_phase3_tasks(use_case, team_size)}

## 🔧 Tool Configuration

### mcp-inspector-server Integration
```python
# Configuration file template
inspector_config = {{
    "servers": {{
        "development": {{
            "command": "python",
            "args": ["dev_server.py"],
            "env": {{"DEBUG": "true"}}
        }},
        "production": {{
            "command": "python",
            "args": ["prod_server.py"],
            "env": {{"LOG_LEVEL": "info"}}
        }}
    }},
    "test_suites": {{
        "basic": ["tools/list", "resources/list"],
        "comprehensive": ["comprehensive_server_test"],
        "performance": ["performance_benchmark"]
    }}
}}

# Use configuration for batch testing
batch_result = batch_inspect_servers([
    {{"name": "dev", "command": "python dev_server.py"}},
    {{"name": "prod", "command": "python prod_server.py"}}
])
```

### CI/CD Integration Example
{_get_cicd_integration_example(use_case, automation_level)}

## 📈 Monitoring and Metrics

### Key Metrics
{_get_key_metrics(use_case)}

### Monitoring Implementation
```python
# Health check routine
def health_check_routine():
    \"\"\"Regular health check\"\"\"
    servers = ["python server.py"]  # Configure actual server list

    for server in servers:
        result = inspect_mcp_server(server, "tools/list", timeout=30)
        if result['success']:
            print(f"✅ {{server}} health status normal")
        else:
            print(f"❌ {{server}} health check failed: {{result.get('error', 'Unknown error')}}")
            # Trigger alerts or auto-repair

# Execute health checks regularly
import schedule
schedule.every(5).minutes.do(health_check_routine)
```

## 🚨 Risk Management

### Common Risks
{_get_common_risks(use_case, team_size)}

### Mitigation Strategies
{_get_risk_mitigation_strategies(use_case, automation_level)}

## 🔄 Continuous Improvement

### Feedback Mechanisms
- Regular team retrospective meetings
- Tool usage effectiveness evaluation
- Process optimization suggestion collection

### Knowledge Management
- Establish best practices knowledge base
- Record common problems and solutions
- Regularly update tools and process documentation

### Skill Development
{_get_skill_development_plan(team_size, automation_level)}

---
*Professional best practices guidance based on Anthropic's 6-layer golden structure framework*
</best_practices>
"""


# Helper functions for best practices
def _get_team_capability_assessment(team_size: str) -> str:
    """Assess team capabilities"""
    assessments = {
        "individual": "Independent developer, needs efficient personal tools and automation",
        "small": "Small team, focus on collaboration efficiency and knowledge sharing",
        "medium": "Medium team, needs standardized processes and role division",
        "large": "Large team, needs enterprise-level governance and scaled management",
    }
    return assessments.get(team_size, assessments["small"])


def _get_use_case_requirements(use_case: str) -> str:
    """Analyze use case requirements"""
    requirements = {
        "general": "General scenario, balance functionality and usability",
        "ci_cd": "Continuous integration scenario, focus on automation and reliability",
        "development": "Development scenario, focus on quick feedback and debugging capabilities",
        "production": "Production scenario, focus on stability and monitoring",
        "research": "Research scenario, focus on flexibility and extensibility",
    }
    return requirements.get(use_case, requirements["general"])


def _get_automation_maturity(automation_level: str) -> str:
    """Assess automation maturity"""
    maturity = {
        "manual": "Mainly manual operations, tool-assisted decision making",
        "medium": "Key process automation, human supervision",
        "high": "Highly automated, intelligent decision making",
    }
    return maturity.get(automation_level, maturity["medium"])


def _get_short_term_goals(use_case: str, team_size: str) -> str:
    """Set short-term goals"""
    if team_size == "individual":
        return "- Establish personal testing workflow\\n- Master mcp-inspector-server core functions\\n- Establish basic monitoring"
    elif use_case == "ci_cd":
        return "- Integrate automated testing into CI pipeline\\n- Establish quality gates\\n- Implement automated deployment verification"
    else:
        return "- Standardize testing processes\\n- Establish team collaboration standards\\n- Implement basic monitoring"


def _get_long_term_goals(use_case: str, automation_level: str) -> str:
    """Set long-term goals"""
    if automation_level == "high":
        return "- Achieve fully automated testing and deployment\\n- Establish intelligent monitoring and alerting\\n- Implement predictive maintenance"
    elif use_case == "production":
        return "- Establish enterprise-level service governance\\n- Implement SRE best practices\\n- Establish comprehensive observability"
    else:
        return "- Establish complete quality assurance system\\n- Achieve efficient team collaboration\\n- Establish continuous improvement mechanisms"


def _get_additional_success_metrics(use_case: str, team_size: str) -> str:
    """Get additional success metrics"""
    if use_case == "production":
        return "\\n- Service availability > 99.9%\\n- Error rate < 0.1%"
    elif team_size == "large":
        return "\\n- Team efficiency improvement > 30%\\n- Knowledge sharing coverage > 90%"
    else:
        return ""


def _get_quality_assurance_practices(use_case: str, team_size: str) -> str:
    """Quality assurance practices"""
    if use_case == "production":
        return """
- Multi-layer testing strategy (unit, integration, end-to-end)
- Automated regression testing and performance testing
- Production environment monitoring and alerting
- Error budget and SLI/SLO management"""
    else:
        return """
- Standardized testing processes and checklists
- Code review and quality gates
- Automated testing and continuous integration
- Regular quality assessment and improvement"""


def _get_automation_practices(automation_level: str, team_size: str) -> str:
    """Automation practices"""
    practices = {
        "manual": "- Use mcp-inspector-server for manual testing\\n- Establish testing checklists\\n- Record test results and issues",
        "medium": "- Automate daily testing processes\\n- Integrate CI/CD pipeline\\n- Auto-generate test reports",
        "high": "- Fully automated testing and deployment\\n- Intelligent monitoring and alerting\\n- Automated fault recovery",
    }
    return practices.get(automation_level, practices["medium"])


def _get_collaboration_practices(team_size: str) -> str:
    """Collaboration practices"""
    practices = {
        "individual": "- Establish personal knowledge base\\n- Use version control for configuration management\\n- Regular backup and sync",
        "small": "- Establish shared testing standards\\n- Regular team sync meetings\\n- Knowledge documentation and sharing",
        "medium": "- Establish role division and responsibility matrix\\n- Implement code review processes\\n- Establish training and knowledge transfer mechanisms",
        "large": "- Establish cross-team collaboration mechanisms\\n- Implement enterprise-level governance processes\\n- Establish specialized teams and CoE",
    }
    return practices.get(team_size, practices["small"])


def _get_phase1_tasks(team_size: str, automation_level: str) -> str:
    """Phase 1 tasks"""
    base_tasks = "- Install and configure mcp-inspector-server\\n- Establish basic testing processes\\n- Train team members"

    if automation_level == "high":
        return (
            base_tasks
            + "\\n- Design automation architecture\\n- Select and configure CI/CD tools"
        )
    else:
        return (
            base_tasks
            + "\\n- Establish manual testing checklists\\n- Develop testing standards and specifications"
        )


def _get_phase2_tasks(use_case: str, automation_level: str) -> str:
    """Phase 2 tasks"""
    if use_case == "ci_cd":
        return "- Integrate testing into CI/CD pipeline\\n- Establish quality gates\\n- Implement automated reporting"
    else:
        return "- Optimize testing processes\\n- Establish monitoring and alerting\\n- Implement quality metrics"


def _get_phase3_tasks(use_case: str, team_size: str) -> str:
    """Phase 3 tasks"""
    if use_case == "production":
        return "- Implement SRE practices\\n- Establish observability system\\n- Achieve intelligent operations"
    elif team_size == "large":
        return "- Establish enterprise-level governance\\n- Implement scaled management\\n- Establish CoE and best practices"
    else:
        return "- Implement advanced testing strategies\\n- Establish continuous improvement mechanisms\\n- Expand tools and capabilities"


def _get_cicd_integration_example(use_case: str, automation_level: str) -> str:
    """CI/CD integration example"""
    if use_case == "ci_cd" and automation_level == "high":
        return """
```yaml
# GitHub Actions example
name: MCP Server CI/CD
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install mcp-factory
      - name: Run MCP Inspector Tests
        run: |
          python -c "
          from mcp_inspector_tools import comprehensive_server_test
          result = comprehensive_server_test('python server.py')
          assert result['success'], f'Tests failed: {result}'
          "
```"""
    else:
        return "Configure appropriate CI/CD integration based on team needs"


def _get_key_metrics(use_case: str) -> str:
    """Key metrics"""
    metrics = {
        "general": "- Test execution time\\n- Problem discovery rate\\n- Fix time",
        "ci_cd": "- Build success rate\\n- Deployment frequency\\n- Change failure rate",
        "production": "- Service availability\\n- Response time\\n- Error rate",
        "development": "- Development efficiency\\n- Code quality\\n- Feedback time",
    }
    return metrics.get(use_case, metrics["general"])


def _get_common_risks(use_case: str, team_size: str) -> str:
    """Common risks"""
    if use_case == "production":
        return "- Production environment failures\\n- Data loss or corruption\\n- Security vulnerability exposure"
    elif team_size == "large":
        return (
            "- Team collaboration conflicts\\n- Knowledge silos\\n- Process complexity"
        )
    else:
        return "- Tool learning costs\\n- Inconsistent process execution\\n- Unclear quality standards"


def _get_risk_mitigation_strategies(use_case: str, automation_level: str) -> str:
    """Risk mitigation strategies"""
    if use_case == "production":
        return "- Establish complete backup and recovery mechanisms\\n- Implement blue-green deployment and canary releases\\n- Establish security audits and compliance checks"
    elif automation_level == "high":
        return "- Establish automated monitoring and alerting\\n- Implement automated fault recovery\\n- Establish intelligent decision support"
    else:
        return "- Establish standardized processes and checklists\\n- Implement training and knowledge transfer\\n- Establish regular evaluation and improvement mechanisms"


def _get_skill_development_plan(team_size: str, automation_level: str) -> str:
    """Skill development plan"""
    if team_size == "large":
        return "- Establish tiered training system\\n- Implement mentorship and knowledge sharing\\n- Establish professional certification and career development paths"
    elif automation_level == "high":
        return "- Learn automation tools and technologies\\n- Master DevOps and SRE practices\\n- Develop systems thinking and problem-solving skills"
    else:
        return "- Master mcp-inspector-server advanced features\\n- Learn testing and quality assurance best practices\\n- Develop continuous learning and improvement mindset"
