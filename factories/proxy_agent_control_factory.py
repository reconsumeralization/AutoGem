
"""Proxy Agent Control Factory Module.

This module is responsible for creating and managing components for controlling proxy agents,
enabling communication and coordination among different parts of the system.
"""

class ProxyAgentControlFactory:
    def __init__(self):
        """Initialize the Proxy Agent Control Factory."""
        self.proxy_agents = {}

    def register_proxy_agent(self, agent_name, agent_class):
        """Register a new proxy agent class under a given agent name.

        Args:
            agent_name (str): The name of the proxy agent to register.
            agent_class (class): The class of the proxy agent to register.
        """
        if agent_name in self.proxy_agents:
            raise ValueError(f"Proxy Agent {agent_name} is already registered.")
        self.proxy_agents[agent_name] = agent_class

    def create_proxy_agent(self, agent_name, *args, **kwargs):
        """Create an instance of a proxy agent based on its name, with optional arguments.

        Args:
            agent_name (str): The name of the proxy agent to instantiate.

        Returns:
            An instance of the requested proxy agent, if found. Raises an error otherwise.
        """
        if agent_name not in self.proxy_agents:
            raise ValueError(f"Proxy Agent {agent_name} is not registered.")
        return self.proxy_agents[agent_name](*args, **kwargs)

    def get_proxy_agent(self, agent_name):
        """Retrieve a proxy agent by its name.

        Args:
            agent_name (str): The name of the proxy agent to retrieve.

        Returns:
            The class of the requested proxy agent, if found. None otherwise.
        """
        return self.proxy_agents.get(agent_name, None)