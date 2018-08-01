from conans import ConanFile, Meson

class TimerConan(ConanFile):
    name = "timer"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "pkg_config"
    requires = "Poco/1.9.0@pocoproject/stable"
    exports_sources = "src/*"

    def build(self):
        meson = Meson(self)
        meson.configure(source_folder="%s/src" % self.source_folder,
                        build_folder="build")
        meson.build()
