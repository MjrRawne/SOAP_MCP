"""
Command-line interface for SOAPWeaver.
"""

import json
import click
from pathlib import Path
from typing import Optional
from .server import SOAPWeaver
import os


@click.group()
def main():
    """SOAPWeaver - Convert any SOAP API into an MCP server."""
    pass


@main.command()
@click.option("--name", default="SOAPWeaver", help="Server name")
@click.option("--config", type=click.Path(exists=True), help="API configuration file (JSON)")
@click.option("--transport", default="stdio", type=click.Choice(["stdio"]), help="Transport type")
def run(name: str, config: Optional[str], transport: str):
    """Run the SOAPWeaver server."""
    
    # Create server
    server = SOAPWeaver(name=name)
    
    # Load configuration if provided
    if config:
        config_path = Path(config)
        if config_path.exists():
            with open(config_path, 'r') as f:
                soap_config = json.load(f)
            
            # Register SOAP API from config file
            # This would need to be done through the MCP protocol
            # For now, we'll just start the server
            # click.echo(f"Loaded configuration from {config}")
    
    # Run server with appropriate transport
    if transport == "stdio":
        # click.echo(f"Starting {name} server on STDIO transport...")
        server.run()

if __name__ == "__main__":
    main()
