using SFML.Graphics;
using SFML.System;

namespace pysfmllib
{
    public class Label
    {
        private Text text;
        private Font font;

        public Label(string fontPath, uint size)
        {
            font = new Font(fontPath);
            text = new Text(font, "", size);
        }

        public void SetText(string value) => text.DisplayedString = value;
        public void SetPosition(float x, float y) => text.Position = new Vector2f(x, y);
        public void Draw(RenderWindow win) => win.Draw(text);
    }
}
