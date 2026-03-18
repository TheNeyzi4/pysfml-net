import os
import sys
import ctypes
import pythonnet
pythonnet.load("coreclr")
import clr
import System

_dll_dir = os.getcwd()

if os.path.exists(_dll_dir):
    os.add_dll_directory(_dll_dir)
    os.environ["PATH"] = _dll_dir + os.pathsep + os.environ.get("PATH", "")

try:
    clr.AddReference("SFML.System")
    clr.AddReference("SFML.Window")
    clr.AddReference("SFML.Graphics")
    clr.AddReference("SFML.Audio")
    _assembly = clr.AddReference("pysfmllib")
except Exception as e:
    raise ImportError(
        f"pysfml: failed to load SFML assemblies from '{_dll_dir}'.\n"
        f"Make sure pysfmllib.dll, SFML.*.dll, csfml-*.dll and sfml-*-3.dll "
        f"are in the same folder as your script.\n"
        f"Original error: {e}"
    )

try:
    from SFML.Window import Keyboard, Mouse
except Exception as e:
    raise ImportError(f"pysfml: could not import SFML.Window enums: {e}")

def _get(name: str):
    t = _assembly.GetType(name)
    if t is None:
        raise ImportError(
            f"pysfml: type '{name}' not found in pysfmllib.dll. "
            f"Rebuild the C# project and replace pysfmllib.dll."
        )
    return t

CsWindow = _get("pysfmllib.Window")
CsSprite = _get("pysfmllib.Sprite")
CsLabel  = _get("pysfmllib.Label")
CsSound  = _get("pysfmllib.Sound")