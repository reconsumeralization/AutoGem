
class AgentFactory:
    """
    Agent Factory for instantiating various types of agents with specific capabilities and behaviors.
    This factory is responsible for creating and managing different agents that can interact within the system,
    leveraging the capabilities of Googles Generative AI Models Gemini pro and gemini vision pro for multimodal capabilities.
    """

    def __init__(self):
        """
        Initializes the Agent Factory with necessary configurations or states.
        """
        self.agents = {}

    def register_agent(self, agent_name, agent_class):
        """
        Registers a new agent class under a given agent name.

        :param agent_name: The name of the agent to register.
        :param agent_class: The class of the agent to register.
        """
        if agent_name in self.agents:
            raise ValueError(f"Agent {agent_name} is already registered.")
        self.agents[agent_name] = agent_class

    def create_agent(self, agent_name, *args, **kwargs):
        """
        Creates an instance of an agent based on its name, with optional arguments.

        :param agent_name: The name of the agent to instantiate.
        :return: An instance of the requested agent.
        """
        if agent_name not in self.agents:
            raise ValueError(f"Agent {agent_name} is not registered.")
        agent_class = self.agents[agent_name]
        agent_instance = agent_class(*args, **kwargs)
        return agent_instance

    def list_agents(self):
        """
        Lists all registered agents.

        :return: A list of registered agent names.
        """
        return list(self.agents.keys())