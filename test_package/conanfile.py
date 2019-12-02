from conans import (
    ConanFile,
    tools,
)
import os


class TestNormalizeCss(ConanFile):
    settings = "os_build"

    build_requires = "sassc/3.6.1@grisumbras/stable"

    def build(self):
        pass

    def test(self):
        cmd = "%s %s" % (
            os.path.join(self.source_folder, "test.sh"),
            os.path.join(self.source_folder, "style.scss"),
        )
        self.run(cmd)
