using SFML.Graphics;
using SFML.System;
using SFML.Window;

namespace pysfmllib
{
    public class Window
    {
        public RenderWindow window;
        private readonly Clock clock;

        public Window(uint width, uint height, string title)
        {
            ContextSettings settings = new();

            window = new RenderWindow(new VideoMode(new Vector2u(width, height)), title, Styles.Default, State.Windowed, settings);
            clock = new();

            window.Closed += (sender, e) =>
            {
                if (sender is RenderWindow win) win.Close();
            };
        }

        public void SetTitle(string title) => window.SetTitle(title);
        public void SetFramerateLimit(uint fps) => window.SetFramerateLimit(fps);
        public void SetVsync(bool enabled) => window.SetVerticalSyncEnabled(enabled);
        public void SetView(View camera) => window.SetView(camera);
        public void SetIcon(string path)
        {
            Image icon = new(path);
            Vector2u size = icon.Size;
            byte[] pixels = icon.Pixels;
            window.SetIcon(size, pixels);
        }
        public bool isOpen() => window != null && window.IsOpen;
        public void Clear(byte r, byte g, byte b) => window.Clear(new Color(r, g, b));
        public void Clear() => window.Clear();
        public void Display() => window.Display();

        public void DispatchEvents() => window.DispatchEvents();
        public void Close() => window.Close();

        public bool IsKeyPressed(Keyboard.Key key) => Keyboard.IsKeyPressed(key);
        public bool IsMouseButtonPressed(Mouse.Button btn) => Mouse.IsButtonPressed(btn);
        public Vector2u GetSize() => window.Size;
        public Vector2i GetMousePosition() => Mouse.GetPosition(window);
        public float GetDeltaTime() => clock.Restart().AsSeconds();

        public void Draw(RectangleShape rect)
        {
            if (rect != null) window.Draw(rect);
        }

        public RenderWindow GetRenderWindow() => window;
    }
}
