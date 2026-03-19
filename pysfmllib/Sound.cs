using SFML.Audio;

namespace pysfmllib
{
    public class Sound
    {
        private SFML.Audio.Sound sound;
        private SoundBuffer buffer;

        public Sound(string path)
        {
            buffer = new SoundBuffer(path);
            sound = new SFML.Audio.Sound(buffer);
        }

        public void Play() => sound.Play();
        public void Stop() => sound.Stop();
        public void Pause() => sound.Pause();
        public void SetLoop(bool IsLooping) => sound.IsLooping = IsLooping;
        public void SetVolume(float v) => sound.Volume = v;
    }
}
