#include <iostream>
using namespace std;

// Square Pattern
void problem1(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

// Right Triangle Pattern
void problem2(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

// Increasing Number Triangle
void problem3(int n)
{
    for (int i = 1; i <= n; i++)
    {
        int count = 1;
        for (int j = 1; j <= i; j++)
        {
            cout << count++;
        }
        cout << endl;
    }
}

// Same Number Triangle
void problem4(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << i;
        }
        cout << endl;
    }
}

// Inverted Right Triangle
void problem5(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < n - i + 1; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

// Inverted Number Triangle
void problem6(int n)
{
    for (int i = 1; i <= n; i++)
    {
        int count = 1;
        for (int j = 1; j <= n - i + 1; j++)
        {
            cout << j;
        }
        cout << endl;
    }
}

// Centered Pyramid Pattern
void problem7(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i + 1; j++)
        {
            cout << " ";
        }

        for (int j = 0; j < 2 * i + 1; j++)
        {
            cout << "*";
        }

        for (int j = 0; j < n - i - 1; j++)
        {
            cout << " ";
        }
        cout << endl;
    }
}

// Inverted Centered Pyramid
void problem8(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }

        for (int j = 0; j < 2 * n - (2 * i + 1); j++)
        {
            cout << "*";
        }

        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }

        cout << endl;
    }
}

// Diamond Pattern
void problem9(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            cout << " ";
        }

        for (int j = 0; j < 2 * i + 1; j++)
        {
            cout << "*";
        }

        for (int j = 0; j < n - i - 1; j++)
        {
            cout << " ";
        }
        cout << endl;
    }

    for (int i = 1; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }

        for (int j = 0; j < 2 * n - (2 * i + 1); j++)
        {
            cout << "*";
        }

        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }

        cout << endl;
    }
}

// Symmetric Star Pattern
void problem10(int n)
{
    for (int i = 1; i <= 2 * n - 1; i++)
    {
        int stars = i;
        if (i > n)
            stars = 2 * n - i;
        for (int j = 1; j <= stars; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

// Binary Alternating Triangle
void problem11(int n)
{
    int start = 1;
    for (int i = 0; i < n; i++)
    {
        if (i % 2 == 0)
            start = 1;
        else
            start = 0;

        for (int j = 0; j <= i; j++)
        {
            cout << start;
            start = 1 - start;
        }
        cout << endl;
    }
}

// Mirrored Number Pattern
void problem12(int n)
{
    int space = 2 * (n - 1);
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << j;
        }

        for (int j = 1; j <= space; j++)
        {
            cout << " ";
        }

        for (int j = i; j >= 1; j--)
        {
            cout << j;
        }
        cout << endl;
        space -= 2;
    }
}

int main()
{
    // problem1(4);
    // problem2(4);
    // problem3(4);
    // problem4(4);
    // problem5(4);
    // problem6(4);
    // problem7(4);
    // problem8(5);
    // problem9(5);
    // problem10(5);
    // problem11(5);
    problem12(5);

    return 0;
}