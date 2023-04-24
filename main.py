from mkdocs_macros import MacrosPlugin
import re


def define_env(env: MacrosPlugin):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """


    @env.macro
    def escape_markdown(text: str):
        """
        Escape the markdown characters in a given string
        """
        return re.sub(r"([_\*])", r"\\\1", text)
        