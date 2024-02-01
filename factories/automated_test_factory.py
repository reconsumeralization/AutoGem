
class AutomatedTestFactory:
    """
    Automated Test Factory for generating tools and structures for automated testing of various components within the system.
    This factory is responsible for creating and managing different testing tools that can be utilized across the application
    to ensure the reliability and robustness of the system.
    """

    def __init__(self):
        """
        Initializes the Automated Test Factory with necessary configurations or states.
        """
        self.test_tools = {}

    def register_test_tool(self, tool_name, tool_class):
        """
        Registers a new test tool class under a given tool name.

        :param tool_name: The name of the test tool to register.
        :param tool_class: The class of the test tool to register.
        """
        if tool_name in self.test_tools:
            raise ValueError(f"Test tool {tool_name} is already registered.")
        self.test_tools[tool_name] = tool_class

    def create_test_tool(self, tool_name, *args, **kwargs):
        """
        Creates an instance of a test tool based on its name, with optional arguments.

        :param tool_name: The name of the test tool to instantiate.
        :return: An instance of the requested test tool.
        """
        if tool_name not in self.test_tools:
            raise ValueError(f"Test tool {tool_name} is not registered.")
        tool_class = self.test_tools[tool_name]
        tool_instance = tool_class(*args, **kwargs)
        return tool_instance

    def list_registered_tools(self):
        """
        Lists all registered test tools.

        :return: A list of registered test tool names.
        """
        return list(self.test_tools.keys())