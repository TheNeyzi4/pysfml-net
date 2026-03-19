import os
import sys
import ctypes
import pythonnet
pythonnet.load("coreclr")
import clr
import System

_dll_dir = os.getcwd()

_lib_dir = os.path.join(os.path.dirname(__file__), "libs")

for _dir in (_lib_dir, _dll_dir):
    if os.path.exists(_dir):
        os.add_dll_directory(_dir)
        os.environ["PATH"] = _dir + os.pathsep + os.environ.get("PATH", "")
        if _dir not in sys.path:
            sys.path.insert(0, _dir)

try:
    clr.AddReference("SFML.System")
    clr.AddReference("SFML.Window")
    clr.AddReference("SFML.Graphics")
    clr.AddReference("SFML.Audio")
    _assembly = clr.AddReference("pysfmllib")
except Exception as e:
    raise ImportError(
        f"pysfml: failed to load SFML assemblies from '{_dll_dir}'.\n"
        f"Make sure csfml-*.dll and sfml-*-3.dll "
        f"are in the same folder as your script.\n"
        f"Original error: {e}"
    )

try:
    from SFML.Window import Keyboard, Mouse
    from SFML.Graphics import View
except Exception as e:
    raise ImportError(f"pysfml: could not import SFML.Window enums and from SFML.Graphics import View: {e}")

def _get(name: str):
    t = _assembly.GetType(name)
    if t is None:
        raise ImportError(
            f"pysfml: type '{name}' not found in pysfmllib.dll. "
        )
    return t

CsWindow = _get("pysfmllib.Window")
CsSprite = _get("pysfmllib.Sprite")
CsLabel  = _get("pysfmllib.Label")
CsSound  = _get("pysfmllib.Sound")
CsCamera = _get("pysfmllib.Camera")