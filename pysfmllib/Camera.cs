using SFML.Graphics;
using SFML.System;

namespace pysfmllib
{
    public class Camera
    {
        private View _view;

        public Camera(float x, float y, float width, float height)
        {
            _view = new View(new FloatRect(new Vector2f(x, y), new Vector2f(width, height)));
        }

        public void SetCenter(float x, float y) => _view.Center = new Vector2f(x, y);
        public void SetSize(float width, float height) => _view.Size = new Vector2f(width, height);
        public void SetRotation(float angle) => _view.Rotation = Angle.FromDegrees(angle);
        public float GetRotation() => _view.Rotation.Degrees;
        public void Move(float x, float y) => _view.Move(new Vector2f(x,y));
        public void Rotate(float angle) => _view.Rotate(angle);
        public void Zoom(float factor) => _view.Zoom(factor);
        public float GetX() => _view.Center.X;
        public float GetY() => _view.Center.Y;
        public View GetView() => _view;
    }
}
