# Copyright (c) 2019 Dmitry Arkhipov <grisumbras@gmail.com>
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE or copy at http://www.boost.org/LICENSE_1_0.txt)


from conans import (
    ConanFile,
    tools,
)
import os


class NormalizeScssConan(ConanFile):
    name = "normalize-scss"
    version = "7.0.1"
    description = "Sass version of Normalize.css"
    homepage = "https://github.com/JohnAlbin/normalize-scss"
    url = "http://github.com/grisumbras/conan-normalize-scss"
    license = "MIT"

    def source(self):
        tools.get(
            "https://github.com/JohnAlbin/normalize-scss/archive/7.0.1.tar.gz",
            sha256="9292360981046536bf5320238117061df3078e11f71df3d19f93af9adadca334",
        )

    def build(self):
        pass

    def package(self):
        self.copy(
            "*.scss",
            src=os.path.join(self._src_subfolder, "sass"),
            dst=os.path.join("share", "%s" % self.name),
        )

    def package_info(self):
        self.env_info.SASS_PATH = [
            os.path.join(self.package_folder, "share", self.name),
        ]

    def package_id(self):
        self.info.header_only()

    @property
    def _src_subfolder(self):
        return "%s-%s" % (self.name, self.version)
