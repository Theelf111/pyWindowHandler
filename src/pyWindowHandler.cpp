#include "pyWindowHandler.h"
#include <unordered_map>

extern "C" int test() { return 13; }

extern "C" int add2(int x, int y) { return x + y; }

struct WindowInfo
{
    int width;
    int height;
    bool resizable;
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

bool resizableHint = true;

extern "C"
void windowHint(int hint, int value)
{
    glfwWindowHint(hint, value);
    if (hint == GLFW_RESIZABLE)
        resizableHint = value;
}

void windowSizeCallback(GLFWwindow* window, int width, int height)
{
    if (windowsInfo[window].resizable)
    {
        windowsInfo[window].width = width;
        windowsInfo[window].height = height;
        GLFWwindow* currentContext = glfwGetCurrentContext();
        glfwMakeContextCurrent(window);
        glViewport(0, 0, width, height);
        glfwMakeContextCurrent(currentContext);
    }
    else
        glfwSetWindowSize(window, windowsInfo[window].width, windowsInfo[window].height);
}

extern "C"
GLFWwindow* createWindow(int width, int height)
{
    GLFWwindow* window = glfwCreateWindow(width, height, "window", NULL, NULL);
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

    windowsInfo[window] = WindowInfo {width, height, resizableHint};

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
void pollEvents()
{
    glfwPollEvents();
}

extern "C"
void swapBuffers(GLFWwindow* window)
{
    glfwSwapBuffers(window);
}
