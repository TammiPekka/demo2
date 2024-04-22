
class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
    #muokattu formatointia
    def _stringify_dependencies(self, dependencies):
        if dependencies:
            return "\n".join(f"- {key}" for key in dependencies.keys())
        return "-"
    
    def _stringify_list(self, items):
        return "\n".join(f"- {item}" for item in items)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.license}"
            f"\n"
            f"\nAuthors:\n{self._stringify_list(self.authors)}"
            f"\n"
            f"\nDependencies:\n{self._stringify_dependencies(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:\n{self._stringify_dependencies(self.dev_dependencies)}"
        )
