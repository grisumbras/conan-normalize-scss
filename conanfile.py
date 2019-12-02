# Copyright (c) 2019 Dmitry Arkhipov <grisumbras@gmail.com>
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE or copy at http://www.boost.org/LICENSE_1_0.txt)


from conans import (
    ConanFile,
    tools,
)
import io
import os
import re


class NormalizeSassConan(ConanFile):
    name = "normalize-sass"
    description = "Sass version of normalize.css"
    homepage = "https://github.com/necolas/normalize.css"
    url = "http://github.com/grisumbras/normalize-sass"
    license = "MIT"

    exports_sources = "LICENSE", "sass/*.scss"

    def source(self):
        tools.get(
            "https://github.com/necolas/normalize.css/archive/{version}.{ext}"
            .format(version=self.version, ext=self._os_ext)
        )

        _src_subfolder = "normalize.css-%s" % self.version
        os.rename(
            os.path.join(_src_subfolder, "normalize.css"), "normalize.css"
        )
        os.rename(os.path.join(_src_subfolder, "LICENSE.md"), "LICENSE.md")
        tools.rmdir(_src_subfolder)

    def build(self):
        in_comment = False
        tools.mkdir("sass/normalize")
        with open("sass/normalize/mixin.scss", "w") as dst:
            dst.write("@mixin normalize() {\n")
            src = os.path.join(self.source_folder, "normalize.css")
            with open(src, "r") as src:
                for line in src:
                    if in_comment:
                        line = "// " + line
                    else:
                        line, in_comment = re.subn(r"/\*+", "//", line)
                    if in_comment:
                        line, in_comment = re.subn(r"\*/", "", line)
                        in_comment = not in_comment
                    dst.write(line)
            dst.write("}\n")

    def package(self):
        self.copy("*.scss", dst="share")
        self.copy("LICENSE", dst="share/normalize-sass")
        self.copy("LICENSE.md", dst="share/normalize.css")

    def package_info(self):
        self.env_info.SASS_PATH = [
            os.path.join(self.package_folder, "share", "sass")
        ]

    def package_id(self):
        self.info.header_only()

    @property
    def _os_ext(self):
        return "zip" if tools.os_info.is_windows else "tar.gz"
