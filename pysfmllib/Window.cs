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

        public bool isOpen() => window != null && window.IsOpen;
        public void Clear() => window?.Clear();
        public void Display() => window?.Display();

        public void DispatchEvents() => window?.DispatchEvents();
        public void Close() => window?.Close();

        public bool IsKeyPressed(Keyboard.Key key) => Keyboard.IsKeyPressed(key);

        public bool IsMouseButtonPressed(Mouse.Button btn) => Mouse.IsButtonPressed(btn);
        public Vector2i GetMousePosition() => Mouse.GetPosition(window);

        public float GetDeltaTime() => clock.Restart().AsSeconds();

        public void Draw(RectangleShape rect)
        {
            if (rect != null) window?.Draw(rect);
        }

        public RenderWindow GetRenderWindow() => window;
    }
}
