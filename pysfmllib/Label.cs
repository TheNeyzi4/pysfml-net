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
        public void SetColor(byte red, byte green, byte blue, byte a) => text.FillColor = new Color(red, green, blue, a);
        public void SetPosition(float x, float y) => text.Position = new Vector2f(x, y);
        public void SetOutline(byte r, byte g, byte b, byte a, float thickness)
        {
            text.OutlineColor = new Color(r, g, b, a);
            text.OutlineThickness = thickness;
        }
        public void SetCharacterSize(uint size) => text.CharacterSize = size;
        public void SetLetterSpacing(uint size) => text.LetterSpacing = size;
        public void SetLineSpacing(uint size) => text.LineSpacing = size;
        public FloatRect GetBounds() => text.GetGlobalBounds();

        public void Draw(RenderWindow win) => win.Draw(text);
    }
}
