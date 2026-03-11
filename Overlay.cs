using System.Numerics;

namespace Overlay
{
    public enum DeviceType { Joystick, Keyboard }
    public enum ButtonType { LP, MP, HP, LK, MK, HK }

    public class Button(Vector2 postition, int[] key, ButtonType type)
    {
        public int[] key = key;
        public Vector2 position = postition;
        public ButtonType type = type;
        public bool active = false;
    }

    public class Device
    {
        public DeviceType t_device = DeviceType.Keyboard;
        public List<Button> buttons = [];
        public Vector2 joystick = new();
    }

    public class Configs
    {
        public int Monitor = 0;
        public int Gamepad = 0;

        public Vector2 GamepadPosition = new(90, 90);
        public int GamepadRadius = 50;
        public int ButtonsRadius = 25;

        public Dictionary<ButtonType, Vector2> ButtonPositions = new() {
            { ButtonType.LP, new(210, 55) },
            { ButtonType.MP, new(265, 55) },
            { ButtonType.HP, new(320, 55) },
            { ButtonType.LK, new(210, 125) },
            { ButtonType.MK, new(265, 125) },
            { ButtonType.HK, new(320, 125) },
        };

        public int[] Directions = [87, 83, 65, 68];
        public int ChangeCast = 263;
        public List<int[]> Keys = [
            [73, 8], [79, 9], [80, 5],
            [74, 7], [75, 11],[76, 6]
        ];
    };
}