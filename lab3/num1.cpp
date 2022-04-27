#include <iostream>
#include <thread>
#include <queue>
#include <mutex>
#include <conio.h>
#include "windows.h"


std::queue <int> que;
std::mutex my_mutex;
std::mutex my_mutex2;

bool cunsomerGo = true;
bool manifGo = true;
bool allGo = true;

void popit1()
{
    while (allGo)
    {
        //std::lock_guard <std::mutex> guard(my_mutex);
        if (!que.empty() && allGo)
        {
            cunsomerGo = true;
        }
        while (cunsomerGo)
        {
            std::lock_guard <std::mutex> guard(my_mutex);
            if (!que.empty())
            {
                
                std::cout << "Потреблено --- " << que.front() << "---" << que.size() << '\n';
                que.pop();
                Sleep(300);
            }
            else
                cunsomerGo = false;

        }
    }
    if (!que.empty())
    {
        manifGo = false;
        do
        {
            std::lock_guard <std::mutex> guard(my_mutex);
            std::cout << "Потреблено --- " << que.front() << "---" << que.size() << std::endl;
            que.pop();
            Sleep(300);
        } while (!que.empty());
    }
}

void popit2()
{
    while (allGo)
    {
        //std::lock_guard <std::mutex> guard(my_mutex);
        if (!que.empty() && allGo)
        {
            cunsomerGo = true;
        }
        while (cunsomerGo)
        {
            std::lock_guard <std::mutex> guard(my_mutex);
            if (!que.empty())
            {

                std::cout << "Потреблено --- " << que.front() << "---" << que.size() << '\n';
                que.pop();
                Sleep(300);
            }
            else
                cunsomerGo = false;

        }
    }
    if (!que.empty())
    {
        manifGo = false;
        do
        {
            std::lock_guard <std::mutex> guard(my_mutex);
            std::cout << "Потреблено --- " << que.front() << "---" << que.size() << std::endl;
            que.pop();
            Sleep(300);
        } while (!que.empty());
    }
}

void pushit1()
{
    
    while (allGo)
    {
        //std::lock_guard <std::mutex> guard2(my_mutex); std::this_thread::get_id
        while (manifGo) 
        {
            std::lock_guard <std::mutex> guard2(my_mutex);
            if (que.size() <= 100)
            {
                
                que.push(rand()%100);
                std::cout << "Произведено -- "<<que.back() << "---" << que.size() <<std::endl;
                Sleep(250);
            }
            else 
            {
                manifGo = false;
            }
        }
        if ((que.size()<=80)&&(allGo))
        {
            manifGo = true;
        }
       
    }
}

void pushit2()
{

    while (allGo)
    {
        //std::lock_guard <std::mutex> guard2(my_mutex); std::this_thread::get_id
        while (manifGo)
        {
            std::lock_guard <std::mutex> guard2(my_mutex);
            if (que.size() <= 100)
            {

                que.push(rand() % 100);
                std::cout << "Произведено -- " << que.back() << "---" << que.size() << std::endl;
                Sleep(250);
            }
            else
            {
                manifGo = false;
            }
        }
        if ((que.size() <= 80) && (allGo))
        {
            manifGo = true;
        }

    }
}

void pushit3()
{

    while (allGo)
    {
        //std::lock_guard <std::mutex> guard2(my_mutex); std::this_thread::get_id
        while (manifGo)
        {
            std::lock_guard <std::mutex> guard2(my_mutex);
            if (que.size() <= 100)
            {

                que.push(rand() % 100);
                std::cout << "Произведено -- " << que.back() << "---" << que.size() << std::endl;
                Sleep(250);
            }
            else
            {
                manifGo = false;
            }
        }
        if ((que.size() <= 80) && (allGo))
        {
            manifGo = true;
        }

    }
}

void catchQ() 
{
    char ch = '\n';
    do {
        std::cin.get(ch);
    } while (ch != 'q');
    allGo = false;
    manifGo = false;
};

// std::lock_guard <std::mutex> guard(my_mutex);
int main()
{
    srand(10);
    setlocale(LC_ALL, "Russian");
    
 
   
    std::thread vvod(catchQ); // отслеживает ввод символа
    
    std::thread manifacturer1(pushit1);
    std::thread manifacturer2(pushit2);
    std::thread manifacturer3(pushit3);
    std::thread consumer2(popit2);
    std::thread consumer1(popit1);

    manifacturer1.join();
    manifacturer2.join();
    manifacturer3.join();
    consumer1.join();
    consumer2.join();
    vvod.join();

    std::cin.get();
    while (allGo);
 
    //Sleep(5000);
    return 0;
   
}
