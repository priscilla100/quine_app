from abc import ABC, abstractmethod


class SelfReplicatingProgram:
    header = "from abc import ABC, abstractmethod\nfrom string import ascii_lowercase"

    @abstractmethod
    def print_source(self):
        ...


class Quine(SelfReplicatingProgram):
    def escape_newline(self, s):
        return s.replace('\n', '\\n')

    def print_source(self):
        header_lines = self.header.split('\n')
        code_lines = [self.escape_newline(line) for line in header_lines] + [
            "\n\nclass SelfReplicatingProgram:\n",
            f"    header = \"{self.escape_newline(self.header)}\"\n",
            "    @abstractmethod\n    def print_source(self):\n        ...\n\n\n",
            "class Quine(SelfReplicatingProgram):\n",
            "    def escape_newline(self, s):\n",
            "        return s.replace('\\n', '\\\\n')\n",
            "    def print_source(self):\n",
            "        header_lines = self.header.split('\\n')\n",
            "        code_lines = [self.escape_newline(line) for line in header_lines] + [\n",
            "            \"\\n\\nclass SelfReplicatingProgram:\\n\",\n",
            f"            \"    header = \\\"{self.escape_newline(self.header)}\\\"\\n\",\n",
            "            \"    @abstractmethod\\n    def print_source(self):\\n        ...\\n\\n\\n\",\n",
            "            \"class Quine(SelfReplicatingProgram):\\n\",\n",
            "            \"    def escape_newline(self, s):\\n\",\n",
            "            \"        return s.replace('\\\\n', '\\\\\\\\n')\\n\",\n",
            "            \"    def print_source(self):\\n\",\n",
            "            \"        header_lines = self.header.split('\\\\n')\\n\",\n",
            "            \"        code_lines = [self.escape_newline(line) for line in header_lines] + [\\n\",\n",
            "            \"            \"\",\n",
            "        ]\n",
            "        print('\\n'.join(code_lines))\n\n",
            "Quine().print_source()"
        ]
        print('\n'.join(code_lines))


Quine().print_source()
