import os

from conans import ConanFile, tools
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain

class LeanVTKConan(ConanFile):
    name = "LeanVTK"
    version = "1.0"
    description = "A minimal VTK file writer for triangle, quad, hex and tet meshes in 2D and 3D. Only C++ standard lib as dependencies"
    topics = ("conan", "vtk")
    license = "MIT"
    homepage = "https://github.com/mmorse1217/lean-vtk"
    url = "https://github.com/jellespijker/lean-vtk"
    settings = "os", "compiler", "build_type", "arch"
    exports = "LICENSE*"
    options = {
        "build_testing": [True, False],
        "shared": [True, False],
        "fPIC": [True, False]
    }
    default_options = {
        "build_testing": False,
        "shared": True,
        "fPIC": False
    }
    scm = {
        "type": "git",
        "subfolder": ".",
        "url": "auto",
        "revision": "auto"
    }

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["BUILD_TESTING"] = self.options.build_testing
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*", src = os.path.join(self.build_folder, "package"), dst = ".")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
