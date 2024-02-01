
class PluginFactory:
    """
    Plugin Factory for handling the creation and management of plugins for extensibility.
    This factory is responsible for instantiating and managing different plugins
    that can be utilized across the application for extending its capabilities.
    """

    def __init__(self):
        """
        Initializes the Plugin Factory with necessary configurations or states.
        """
        self.plugins = {}

    def register_plugin(self, plugin_name, plugin_class):
        """
        Registers a new plugin class under a given plugin name.

        :param plugin_name: The name of the plugin to register.
        :param plugin_class: The class of the plugin to register.
        """
        if plugin_name in self.plugins:
            raise ValueError(f"Plugin {plugin_name} is already registered.")
        self.plugins[plugin_name] = plugin_class

    def create_plugin(self, plugin_name, *args, **kwargs):
        """
        Creates an instance of a plugin based on its name, with optional arguments.

        :param plugin_name: The name of the plugin to instantiate.
        :return: An instance of the requested plugin.
        """
        if plugin_name not in self.plugins:
            raise ValueError(f"Plugin {plugin_name} is not registered.")
        plugin_class = self.plugins[plugin_name]
        plugin_instance = plugin_class(*args, **kwargs)
        return plugin_instance

    def get_all_plugins(self):
        """
        Returns a list of all registered plugins.

        :return: A list of registered plugin names.
        """
        return list(self.plugins.keys())

# Example usage
# Assuming there's a class `LoggerPlugin` defined somewhere that takes no arguments for initialization
# plugin_factory = PluginFactory()
# plugin_factory.register_plugin("logger", LoggerPlugin)
# logger_plugin = plugin_factory.create_plugin("logger")