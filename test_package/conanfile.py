from conans import (
    ConanFile,
    tools,
)
import os


class TestNormalizeCss(ConanFile):
    settings = "os_build"

    def system_requirements(self):
        sassc = "sassc"
        installer = tools.SystemPackageTool()
        installer.install(sassc)

    def build(self):
        pass

    def test(self):
        if self.settings.os_build == "Windows":
            return

        cmd = "%s %s" % (
            os.path.join(self.source_folder, "test.sh"),
            os.path.join(self.source_folder, "style.scss"),
        )
        self.run(cmd)
