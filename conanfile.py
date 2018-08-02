from conans import ConanFile, Meson

class videoConan(ConanFile):
    name = "timer"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "pkg_config"
    requires = "ffmpeg/4.0@bincrafters/stable"
    exports_sources = "src/*"

    def build(self):
        meson = Meson(self)
        meson.configure(source_folder="%s/src" % self.source_folder,
                        build_folder="%s/dist" % self.source_folder)
        meson.build()
