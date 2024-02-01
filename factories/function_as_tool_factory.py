
class FunctionAsToolFactory:
    """
    Function as Tool Factory for dynamically generating tools based on functions.
    This factory allows for dynamic function registration and instantiation as tools within the system.
    """

    def __init__(self):
        """
        Initializes the Function as Tool Factory with necessary configurations or states.
        """
        self.function_tools = {}

    def register_function_tool(self, function_name, function):
        """
        Registers a new function as a tool under a given function name.

        :param function_name: The name of the function to register as a tool.
        :param function: The function to register as a tool.
        """
        if function_name in self.function_tools:
            raise ValueError(f"Function tool {function_name} is already registered.")
        self.function_tools[function_name] = function

    def create_function_tool(self, function_name, *args, **kwargs):
        """
        Creates an instance of a function tool based on its name, with optional arguments.

        :param function_name: The name of the function tool to instantiate.
        :return: The result of the function tool execution.
        """
        if function_name not in self.function_tools:
            raise ValueError(f"Function tool {function_name} is not registered.")
        function = self.function_tools[function_name]
        result = function(*args, **kwargs)
        return result

# Example usage
# Assuming there's a function `greet` defined somewhere that takes a name argument
# function_as_tool_factory = FunctionAsToolFactory()
# function_as_tool_factory.register_function_tool("greet", greet)
# greeting = function_as_tool_factory.create_function_tool("greet", name="John")
# print(greeting)