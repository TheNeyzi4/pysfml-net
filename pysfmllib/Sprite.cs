using SFML.Graphics;
using SFML.System;

namespace pysfmllib
{
    public class Sprite
    {
        private Texture texture = null!;
        public RectangleShape rect;

        public Sprite(float width, float height)
        {
            rect = new(new Vector2f(width, height))
            {
                FillColor = Color.White
            };
        }

        public void LoadTexture(string path)
        {
            if (!File.Exists(path)) throw new FileNotFoundException($"Texture not found: {path}");

            texture = new Texture(path);
            rect.Texture = texture;
        }

        public void SetTextureRect(int x, int y, int w, int h)
        {
            rect.TextureRect = new IntRect(new Vector2i(x, y), new Vector2i(w, h));
        }

        public void SetSize(float w, float h) => rect.Size = new Vector2f(w, h);

        public Vector2f SetPosition(float x, float y)
        {
            rect.Position = new Vector2f(x, y);

            return rect.Position;
        }

        public void SetFillColor(byte r, byte g, byte b, byte a) => rect.FillColor = new Color(r, g, b, a);

        public void Draw(RenderWindow win) => win.Draw(rect);
    }
}
