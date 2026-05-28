#include "pyWindowHandler.h"
#include <cstdlib>

extern "C" int test() { return 13; }

extern "C" int add2(int x, int y) { return x + y; }

struct WindowInfo
{
    int width;
    int height;
};

unordered_map<GLFWwindow*, WindowInfo> windowsInfo;

extern "C"
WindowInfo getWindowInfo(GLFWwindow* window)
{
    return windowsInfo[window];
}

extern "C"
int init()
{
    glfwInitHint(GLFW_WAYLAND_LIBDECOR, GLFW_WAYLAND_DISABLE_LIBDECOR);
    if (!glfwInit())
    {
        cout << "glfwInit() false" << endl;
        return -1;
    }

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    return 0;
}

extern "C"
void windowHint(int hint, int value)
{
    glfwWindowHint(hint, value);
}

struct Event
{
    void* window;
    int type = -1;
    int key = 0;
    int mods = 0;
};

vector<Event> events = {};

void windowSizeCallback(GLFWwindow* window, int width, int height)
{
    windowsInfo[window].width = width;
    windowsInfo[window].height = height;
    GLFWwindow* currentContext = glfwGetCurrentContext();
    glfwMakeContextCurrent(window);
    glViewport(0, 0, width, height);
    glfwMakeContextCurrent(currentContext);
}

void keyCallback(GLFWwindow* window, int key, int scancode, int action, int mods)
{
    switch (action)
    {
    case GLFW_PRESS:
        events.push_back(Event{window, EVENT_KEYDOWN, key, mods});
        break;
    case GLFW_RELEASE:
        events.push_back(Event{window, EVENT_KEYUP, key, mods});
        break;
    }
}

void mouseButtonCallback(GLFWwindow* window, int button, int action, int mods)
{
    switch (action)
    {
    case GLFW_PRESS:
        events.push_back(Event{window, EVENT_MOUSEBUTTONDOWN, button, mods});
        break;
    case GLFW_RELEASE:
        events.push_back(Event{window, EVENT_MOUSEBUTTONUP, button, mods});
        break;
    }
}

extern "C"
GLFWwindow* createWindow(int width, int height, char* title)
{
    GLFWwindow* window = glfwCreateWindow(width, height, title, NULL, NULL);
    if (!window)
    {
        cout << "glfwCreateWindow() failed" << endl;
        glfwTerminate();
        return 0;
    }

    glfwMakeContextCurrent(window);
    glViewport(0, 0, width, height);
    glfwSwapInterval(1);

    glfwSetWindowSizeCallback(window, windowSizeCallback);
    glfwSetKeyCallback(window, keyCallback);
    glfwSetMouseButtonCallback(window, mouseButtonCallback);

    windowsInfo[window] = WindowInfo {width, height};

    return window;
}

extern "C"
void selectWindow(GLFWwindow* window)
{
    glfwMakeContextCurrent(window);
}

extern "C"
int windowShouldClose(GLFWwindow* window)
{
    return glfwWindowShouldClose(window);
}

extern "C"
List pollEvents()
{
    events.clear();
    glfwPollEvents();
    return List{events.size(), events.data()};
}

extern "C"
void swapBuffers(GLFWwindow* window)
{
    glfwSwapBuffers(window);
}

extern "C"
Pos getCursorPos(GLFWwindow* window)
{
    double x, y;
    glfwGetCursorPos(window, &x, &y);
    return Pos{x, y};
}
