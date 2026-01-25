#include "pyWindowHandler.h"

extern "C" int test() { return 13; }

extern "C" int add2(int x, int y) { return x + y; }

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

extern "C"
void windowHint(int hint, int value)
{
    glfwWindowHint(hint, value);
    if (hint == GLFW_RESIZABLE)
        windowResizable = value;
}

GLFWwindow* window = nullptr;
int windowWidth = 0;
int windowHeight = 0;
bool windowResizable = true;

void windowSizeCallback(GLFWwindow* window, int width, int height)
{
    if (windowResizable)
    {
        windowWidth = width;
        windowHeight = height;
    }
    else
        glfwSetWindowSize(window, windowWidth, windowHeight);
    //cout << "RESIZE: " << width << ", " << height << endl;
}

extern "C"
int createWindow(int width, int height)
{
    windowWidth = width;
    windowHeight = height;
    window = glfwCreateWindow(width, height, "window", NULL, NULL);
    if (!window)
    {
        cout << "glfwCreateWindow() failed" << endl;
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);
    glViewport(0, 0, width, height);
    glfwSwapInterval(1);

    glfwSetWindowSizeCallback(window, windowSizeCallback);
    return 0;
}

extern "C"
int windowShouldClose()
{
    return glfwWindowShouldClose(window);
}

extern "C"
void pollEvents()
{
    glfwPollEvents();
}

extern "C"
void swapBuffers()
{
    glfwSwapBuffers(window);
}
