from ffmpegio import plugins, path
import ffmpegio_plugin_static_ffmpeg
from static_ffmpeg import run


def test_plugin():
    assert ffmpegio_plugin_static_ffmpeg in plugins.pm.get_plugins()


def test_operation():
    ffmpeg_bin, ffprobe_bin = run.get_or_fetch_platform_executables_else_raise()
    path.find()
    assert path.get_ffmpeg() == ffmpeg_bin
    assert path.get_ffmpeg(True) == ffprobe_bin


if __name__ == "__main__":
    test_plugin()
    test_operation

    print(path.FFMPEG_BIN)
    print(path.FFPROBE_BIN)