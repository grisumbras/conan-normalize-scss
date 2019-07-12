# Copyright (c) 2019 Dmitry Arkhipov <grisumbras@gmail.com>
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE or copy at http://www.boost.org/LICENSE_1_0.txt)


from conans import (
    ConanFile,
    tools,
)


class NormalizeScssConan(ConanFile):
    name = "normalize-scss"
    version = "7.0.1"
    description = "Sass version of Normalize.css"
    homepage = "https://github.com/JohnAlbin/normalize-scss"
    url = "http://github.com/grisumbras/conan-normalize-scss"
    license = "MIT"

    def source(self):
        pass

    def build(self):
        pass

    def package(self):
        pass

    def package_info(self):
        self.info.header_only()
