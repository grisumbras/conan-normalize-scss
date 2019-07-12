from conans import ConanFile
import os


class TestNormalizeCss(ConanFile):
    exports_sources = "*.sh"

    def test(self):
        self.copy(os.path.join(self.source_folder, "test.sh"))
        self.copy(os.path.join(self.source_folder, "style.scss"))
        self.run("test.sh")
    #     env = {
    #         "PACKAGE_REFERENCE": str(self.requires["b2-helper"].ref),
    #         "PYTHONPATH": [os.path.join(self.source_folder, "modules")],
    #     }
    #     with tools.environment_append(env):
    #         for test_name in self._tests:
    #             self.run_test(test_name)
    #
