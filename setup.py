import sublime
import os


def plugin_loaded():
    init_default_settings("mtx_npg")
    init_default_settings("mtx_scs")


def init_default_settings(scope):
    """
    There are some setting, which are essensial to make G-Code files
    work correctly on a CNC later. If no language specific settings
    file exists, create one with those settings.
    """
    file_name = scope + ".sublime-settings"
    file_path = os.path.join(sublime.packages_path(), "User", file_name)
    if not os.path.exists(file_path):

        settings = sublime.load_settings(file_name)

        # UTF8 encoding not supported
        settings.set("default_encoding", "Western (Windows 1252)")
        settings.set("fallback_encoding", "Western (Windows 1252)")

        # avoid tab stops end ensure newline at eof
        settings.set("ensure_newline_at_eof_on_save", True)
        settings.set("translate_tabs_to_spaces", True)
        settings.set("use_tab_stops", False)

        # Define the format of binary numbers for the Hex-Bin-System plugin
        # Binaries look like 0b101110
        settings.set("convert_src_bin", "0b([01]+)")
        settings.set("convert_dst_bin", "0b{0:b}")

        # Define the format of hexadecimal numbers for the Hex-Bin-System plugin
        # Hexadecimals look like 0h12FA
        settings.set("convert_src_hex", "0h[0-9A-F]+)")
        settings.set("convert_dst_hex", "0h{0:X}")

        # Define the format of exponential numbers for the Hex-Bin-System plugin
        # The pattern must match the base as group 1 and exponent as group 2.
        # Exponential numbers look like 3.14e-4
        settings.set("convert_src_exp", "\\b([1-9]\\.\\d+)e([-+]?\\d+)\\b")
        settings.set("convert_dst_exp", "e")

        sublime.save_settings(file_name)
