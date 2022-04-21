#include <iostream>
#include <thread>
#include <queue>
#include <mutex>
//#include <stdio.h>
#include <conio.h>
#include "windows.h"


std::queue <int> que;
std::mutex my_mutex;
std::mutex my_mutex2;

bool cunsomerGo = true;
bool manifGo = true;
bool allGo = true;

void popit()
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

void pushit()
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
    
    std::thread manifacturer[3];
    std::thread consumer[2];
    std::thread vvod(catchQ); // отслеживает ввод символа
    

    for (int i = 0; i < 3; i++) {
        manifacturer[i] = std::thread(pushit);
    };

    for (int i = 0; i < 2; i++) {
        consumer[i] = std::thread(popit);
    }
    manifacturer[0].join();
    manifacturer[1].join();
    manifacturer[2].join();
    consumer[0].join();
    consumer[1].join();
    vvod.join();

    std::cin.get();
    while (allGo);
 
    //Sleep(5000);
    return 0;
   
}
