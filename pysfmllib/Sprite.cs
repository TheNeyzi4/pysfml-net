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
        public Vector2f GetSize() => rect.Size;
        public void SetOrigin(float x, float y) => rect.Origin = new Vector2f(x, y);
        public Vector2f GetOrigin() => rect.Origin;
        public float SetRotation(float angle) => rect.Rotation = angle;
        public float GetRotation() => rect.Rotation;
        public void SetScale(float x, float y) => rect.Scale = new Vector2f(x, y);
        public void FlipX()
        {
            Vector2f size = rect.Size;
            Vector2f origin = rect.Origin;

            if (rect.Scale.X > 0)
            {
                rect.Scale = new Vector2f(-1, rect.Scale.Y);
                rect.Origin = new Vector2f(size.X, origin.Y);
            } else
            {
                rect.Scale = new Vector2f(1, rect.Scale.Y);
                rect.Origin = new Vector2f(0, origin.Y);
            }
        }
        public void FlipY()
        {
            Vector2f size = rect.Size;
            Vector2f origin = rect.Origin;

            if (rect.Scale.Y > 0)
            {
                rect.Scale = new Vector2f(rect.Scale.X, -1);
                rect.Origin = new Vector2f(origin.X, size.Y);
            }
            else
            {
                rect.Scale = new Vector2f(rect.Scale.X, -1);
                rect.Origin = new Vector2f(origin.X, 0);
            }
        }
        public Vector2f SetPosition(float x, float y)
        {
            rect.Position = new Vector2f(x, y);

            return rect.Position;
        }
        public Vector2f GetPosition() => rect.Position; 
        public void SetFillColor(byte r, byte g, byte b, byte a) => rect.FillColor = new Color(r, g, b, a);
        public void Draw(RenderWindow win) => win.Draw(rect);
    }
}
