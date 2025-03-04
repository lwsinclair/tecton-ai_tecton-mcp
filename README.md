# Tecton MCP Server

This is a Mission Control Protocol (MCP) server from Anthropic for Tecton that provides a set of tools to interact with Tecton clusters, manage feature stores, and execute Tecton CLI commands.

## Features

The server provides the following MCP tools:

### CLI Tools
- `tecton_cli_help`: Get structured help information about available Tecton CLI commands
- `tecton_cli_execute`: Execute Tecton CLI commands

### Feature Store Management
- `list_workspaces`: List all workspaces in the connected Tecton cluster
- `list_feature_views`: List all feature views with their metadata
- `list_feature_services`: List all feature services with their metadata
- `list_transformations`: List all transformations with their metadata
- `list_data_sources`: List all data sources with their metadata
- `list_entities`: List all entities with their metadata

### Configuration Tools
- `get_feature_service_configuration`: Get detailed configuration of a feature service
- `get_feature_view_configuration`: Get detailed configuration of a feature view
- `get_feature_view_code`: Get the Python code definition of a feature view

## Setup

### Prerequisites
- Python >=3.10 or compatible version
- Tecton SDK installed and configured
- Mission Control Protocol (MCP) installed

### Installation

1. Install required Python packages:
```bash
pip install httpx click cloudpickle
```

2. Install Tecton SDK:
```bash
pip install tecton
```

3. Install MCP:
```bash
pip install mcp
```

### Configuration

Add the following to your MCP server configuration:

```json
{
    "mcpServers": {
        "tecton": {
            "command": "/path/to/python",
            "args": [
                "--directory",
                "/path/to/tecton",
                "run",
                "tecton.py"
            ],
            "env": {
                "PYENV_VERSION": "3.9.11"
            }
        }
    }
}
```

Replace `/path/to/python` and `/path/to/tecton` with your actual paths.

## Usage

### Starting the Server

1. First, ensure you have Tecton configured and logged in:
```bash
tecton login
```

2. Then run the server using:
```bash
python tecton.py
```

The server will start and listen for MCP commands.

### Using the Tools

All tools are available through the MCP interface. Here are some example uses:

1. List all workspaces:
```python
workspaces = await list_workspaces()
```

2. Get feature view configuration:
```python
config = await get_feature_view_configuration(name="my_feature_view", workspace="my_workspace")
```

3. Execute a Tecton CLI command:
```python
result = await tecton_cli_execute(command="workspace list")
```

## Error Handling

The server includes comprehensive error handling:
- All tools return empty lists or empty strings on failure
- Errors are logged using the `_err` function
- General operations are logged using the `_log` function

## Dependencies

- Core Python:
  - typing (built-in)
  - httpx
  - click
  - cloudpickle

- Tecton:
  - tecton
  - tecton._internals
  - tecton.cli.cli
  - tecton_core
  - tecton_proto

- MCP:
  - mcp.server.fastmcp

- Local:
  - utils (containing _err, _log, and run_command)

## Contributing

Feel free to submit issues and enhancement requests!
