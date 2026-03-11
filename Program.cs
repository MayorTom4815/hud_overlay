using System.Text.Json;
using System.Numerics;

using SharpHook.Data;
using SharpHook;

using Raylib_cs;
using Overlay;

internal static class Program
{
    const int WindowHeight = 175;
    const int WindowWidth = 375;

    static readonly string DefaultPath = Environment.GetEnvironmentVariable("HOME") ?? ".";
    static readonly EventLoopGlobalHook hook = new();
    static readonly HashSet<KeyCode> lastkeys = [];
    static readonly Device device = new();
    static Configs configs = new();

    static void SaveConfig(Configs config) => File.WriteAllText($"{DefaultPath}/HUDOveray.json", JsonSerializer.Serialize(config));
    static Configs ReadConfig()
    {
        if (!File.Exists($"{DefaultPath}/HUDOveray.json")) SaveConfig(new Configs());
        return JsonSerializer.Deserialize<Configs>(File.ReadAllText($"{DefaultPath}/HUDOveray.json")) ?? throw new Exception("Can't parse the file");
    }

    public static void InitOverlay()
    {   
        configs = ReadConfig();
        device.t_device = Raylib.IsGamepadAvailable(0) ? DeviceType.Joystick : DeviceType.Keyboard;

        int current_button = 0;
        foreach(ButtonType b_type in Enum.GetValues(typeof(ButtonType))) {
            device.buttons.Add(new(
                configs.ButtonPositions[b_type],
                configs.Keys[current_button],
                b_type
            ));

            current_button++;
        }
    }

    public static void UpdateOverlay()
    {
        if(device.t_device is DeviceType.Joystick)
        {
            device.joystick = new(
                Raylib.GetGamepadAxisMovement(0, GamepadAxis.RightX),
                Raylib.GetGamepadAxisMovement(0, GamepadAxis.RightY)
            );

            foreach (var btn in device.buttons)
            {
                if (Raylib.IsGamepadButtonDown(0, (GamepadButton)btn.key[1]))
                {
                    btn.active = true;
                    continue;
                }
                btn.active = false;
            }
        } 

        else
        {
            device.joystick = Vector2.Zero;
            if(lastkeys.Contains((KeyCode)configs.Directions[0])) 
                device.joystick.Y = -1;

            if(lastkeys.Contains((KeyCode)configs.Directions[1]))
                device.joystick.Y = 1;

            if(lastkeys.Contains((KeyCode)configs.Directions[2]))
                device.joystick.X = -1;

            if(lastkeys.Contains((KeyCode)configs.Directions[3]))
                device.joystick.X = 1;

            foreach (Button btn in device.buttons)
            {
                if (lastkeys.Contains((KeyCode)btn.key[0]))
                {
                    btn.active = true;
                    continue;
                }
                btn.active = false;
            }
        }
    }

    public static void DrawOverlay()
    {
        Vector2 end_v = new(
            configs.GamepadPosition.X + device.joystick.X * configs.GamepadRadius, 
            configs.GamepadPosition.Y + device.joystick.Y * configs.GamepadRadius);

        Raylib.BeginDrawing();

        Raylib.ClearBackground(Color.Blank);
        Raylib.DrawCircleLinesV(configs.GamepadPosition, configs.GamepadRadius, Color.DarkBlue);
        Raylib.DrawCircleV(end_v, configs.GamepadRadius / 2 , Color.SkyBlue);
        foreach(var btn in device.buttons)
        {   
            var colors = btn.active ? (Color.DarkGreen, Color.Green) : (Color.DarkBrown, Color.Red);
            int m_label = Raylib.MeasureText($"{btn.type}", 20);
            Raylib.DrawCircleV(btn.position, configs.ButtonsRadius, colors.Item1);
            Raylib.DrawCircleV(btn.position, configs.ButtonsRadius - 5, colors.Item2);
            Raylib.DrawText(
                $"{btn.type}", 
                (int)btn.position.X - m_label / 2, 
                (int)btn.position.Y - m_label / 2, 
                20, Color.White
            );
        }

        Raylib.EndDrawing();
    }

    [STAThread]
    public static void Main()
    {
        Raylib.SetConfigFlags(ConfigFlags.TransparentWindow | ConfigFlags.UndecoratedWindow | ConfigFlags.TopmostWindow);
        Raylib.InitWindow(WindowWidth, WindowHeight, "HUDOverlay");
        Raylib.SetTargetFPS(60);

        Raylib.SetWindowPosition(Raylib.GetMonitorWidth(0) - WindowWidth, Raylib.GetMonitorHeight(0) - WindowHeight);
        hook.KeyReleased += (s, e) => lastkeys.Remove(e.Data.KeyCode);
        hook.KeyPressed += (s, e) => lastkeys.Add(e.Data.KeyCode);
        hook.RunAsync();

        InitOverlay();
        while (!Raylib.WindowShouldClose())
        {
            UpdateOverlay();
            DrawOverlay();
        }

        Raylib.CloseWindow();
        hook.Dispose();
    }
}
