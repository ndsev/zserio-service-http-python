package myservice;

struct Question { string text; };
struct Answer { string text; };

service MyService
{
    Answer ask(Question);
};
